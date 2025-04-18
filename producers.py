# this is messy and bad, need to fix by more clearly separating functions and files...
from setup import set_good_events, add_triggers_and_FS_to_good_events
from file_functions import load_process_from_file, load_and_store_NWEvents
from branch_functions import set_branches
from plotting_functions import set_vars_to_plot
from utility_functions import log_print
from file_map_dictionary import set_dataset_info
from file_functions import load_process_from_file
from cut_and_study_functions import apply_AR_cut
import numpy as np
import gc



def set_AR_region(final_state_mode, era, temp_version):
  common_selection = set_good_events(final_state_mode, era, non_SR_region=True, temp_version=temp_version)
  common_selection = add_triggers_and_FS_to_good_events(common_selection, final_state_mode, era)
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

