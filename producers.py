# this is messy and bad, need to fix by more clearly separating functions and files...
from setup import set_good_events
from file_functions import load_process_from_file, customize_DY, load_and_store_NWEvents
from branch_functions import set_branches
from plotting_functions import set_vars_to_plot
from utility_functions import log_print
from file_map_dictionary import set_dataset_info
from file_functions import load_process_from_file
from cut_and_study_functions import apply_AR_cut
import numpy as np
import gc


def set_AR_region(final_state_mode, era, temp_version):
  # TODO: need to abstract the handling in setup and then copy it over here
  common_selection = set_good_events(final_state_mode, era, non_SR_region=True, temp_version=temp_version)
  if final_state_mode == "ditau":
    triggersV1 = "(HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1\
               | HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60\
               | HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75\
               | HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1\
               | HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1)" # HLepV1
    triggersV2 = "((Trigger_ditau) | (Trigger_ditauplusjet) | (Trigger_VBFditau) | (Trigger_VBFsingleTau))" # HLepV2

    triggers = triggersV1 if temp_version == "V1" else triggersV2
    common_selection += " & (abs(HTT_pdgId)==15*15) & " + triggers

  elif final_state_mode == "mutau":
    good_eventsV1 = " & (abs(HTT_pdgId)==13*15) & (Trigger_mutau)" # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==13*15) & ((Trigger_mutau) | (Trigger_SingleMuon))" # HLepV2
    common_selection += good_eventsV1 if temp_version == "V1" else good_eventsV2

  elif final_state_mode == "etau":
    good_eventsV1 = " & (abs(HTT_pdgId)==11*15) & (Trigger_etau)" # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==11*15) & ((Trigger_etau) | (Trigger_SingleElectron))" # HLepV2
    common_selection += good_eventsV1 if temp_version == "V1" else good_eventsV2

  elif final_state_mode == "emu":
    good_eventsV1 = " & (abs(HTT_pdgId)==11*13) & (Trigger_emu) " # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==11*13) & ((Trigger_emu) | (Trigger_mue))" # HLepV2
    common_selection += good_eventsV1 if temp_version == "V1" else good_eventsV2

  return common_selection


def produce_FF_weight(setup, fakesLabel, jet_mode, semilep_mode):
    # kinda weird, but okay
    testing, final_state_mode, _, era, lumi, tau_pt_cut = setup.state_info # don't reset jet_mode
    using_directory, _, log_file, _, file_map, one_file_at_a_time, temp_version = setup.file_info
    _, _, DeepTau_version, _, _, _, _ = setup.misc_info
    if one_file_at_a_time: import glob

    jet_mode = jet_mode.removesuffix("_testing")
    dataset, _ = set_dataset_info(final_state_mode)
    AR_region    = set_AR_region(final_state_mode, era, temp_version) # same role as "set_good_events"
    vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode)
    branches     = set_branches(final_state_mode, era, DeepTau_version, process=dataset, temp_version=temp_version)

    FF_dictionary = {}
    FF_dictionary[fakesLabel] = {}
    FF_dictionary[fakesLabel]["PlotEvents"] = {}
 
    log_print(f"Processing {final_state_mode} AR region!", log_file, time=True)
    if not one_file_at_a_time:
      # One single entry per process, probably containing wildcard symbol, as defined in file_map_dictionary.py
      input_files = [file_map[dataset]]
    else:
      # Multiple entries per process, results from wildcard search
      input_files = glob.glob( using_directory + "/" + file_map[dataset] + ".root")
      input_files = sorted([f.replace(using_directory+"/","")[:-5] for f in input_files])
    for input_file in input_files:
      this_file_map = {dataset: input_file} # Make a temporary filemap just for this loop
      AR_process_dictionary = load_process_from_file(dataset, using_directory, this_file_map, log_file,
                                              branches, AR_region, final_state_mode,
                                              data=True, testing=testing)
      AR_events = AR_process_dictionary[dataset]["info"]
      cut_events_AR = apply_AR_cut(era, dataset, AR_events, final_state_mode, jet_mode, semilep_mode, DeepTau_version, tau_pt_cut)
      if "FF_weight" not in FF_dictionary[fakesLabel]: # First file, or not doing one at a time
        FF_dictionary[fakesLabel]["FF_weight"]  = cut_events_AR["FF_weight"]
        for var in vars_to_plot:
          if ("flav" in var) or ("Generator_weight" in var): continue
          FF_dictionary[fakesLabel]["PlotEvents"][var] = cut_events_AR[var]
      else:
        FF_dictionary[fakesLabel]["FF_weight"]  = np.append(FF_dictionary[fakesLabel]["FF_weight"], cut_events_AR["FF_weight"])
        for var in vars_to_plot:
          if ("flav" in var): continue
          FF_dictionary[fakesLabel]["PlotEvents"][var] = np.append(FF_dictionary[fakesLabel]["PlotEvents"][var], cut_events_AR[var])
      del AR_process_dictionary
      del AR_events
      del cut_events_AR
      gc.collect()

    return FF_dictionary

