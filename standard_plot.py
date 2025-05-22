# Authored by Braden Allmond, Sep 11, 2023
DEBUG = False

# libraries
import numpy as np
import sys
import matplotlib.pyplot as plt
import gc
import copy
import correctionlib

# explicitly import used functions from user files, grouped roughly by call order and relatedness
# import statements for setup
from setup               import setup_handler, set_good_events
from branch_functions    import set_branches
from plotting_functions  import set_vars_to_plot
from file_map_dictionary import set_dataset_info

# import statements for data loading and processing
from file_functions          import load_process_from_file, append_to_combined_processes, sort_combined_processes
from FF_functions            import set_JetFakes_process, FF_control_flow
from cut_and_study_functions import apply_HTT_FS_cuts_to_process
from cut_and_study_functions import apply_cut, set_protected_branches

# plotting
from luminosity_dictionary import luminosities_with_normtag as luminosities
from plotting_functions    import get_midpoints, make_eta_phi_plot
from plotting_functions    import get_binned_data, get_binned_backgrounds, get_binned_signals, get_summed_backgrounds
from plotting_functions    import setup_ratio_plot, make_ratio_plot, spruce_up_plot, spruce_up_legend
from plotting_functions    import spruce_up_single_plot, add_text
from plotting_functions    import plot_data, plot_MC, plot_signal, make_bins, make_pie_chart, make_two_dimensional_plot
from plotting_functions    import make_two_dimensional_ratio_plot
from plotting_functions    import setup_unrolled_plot, spruce_up_unrolled_plot
from binning_dictionary    import label_dictionary

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info, log_print, print_processing_info

from make_fitter_shapes    import save_fitter_shapes, make_masks_per_bin

def add_HpT_correction(process, cut_events):
  # add H_pT correction to all samples
  # for signal, use ggH or VBF as necessary. For others, average the correction.
  recoHpT = cut_events["HTT_H_pt"]
  nCleanJet = cut_events["nCleanJet"]
  correctionJetMode = np.array([0 if nJet == 0 else 1 for nJet in nCleanJet])
  if ("_TauTau" in process):
    if ("ggH" in process):
      val = cevalHpT["recoHpTFactor"].evaluate(recoHpT, correctionJetMode, correctionEra, "ggH")
    else: # VBF or VH or ttH
      val = cevalHpT["recoHpTFactor"].evaluate(recoHpT, correctionJetMode, correctionEra, "VBF")
  else:
    val1 = cevalHpT["recoHpTFactor"].evaluate(recoHpT, correctionJetMode, correctionEra, "ggH")
    val2 = cevalHpT["recoHpTFactor"].evaluate(recoHpT, correctionJetMode, correctionEra, "VBF")
    val = (val1+val2)/2
  cut_events["HTT_H_pt_corr"] = recoHpT*val
  return cut_events

if __name__ == "__main__":
  '''
  Just read the code, it speaks for itself.
  Kidding.

  This is the main block, which calls a bunch of other functions from other files
  and uses local variables and short algorithms to, by final state
  1) load data from files
  2) apply bespoke cuts to reject events
  3) explicitly remove large objects after use
  4) create a lovely plot

  Ideally, if one wants to use this library to make another type of plot, they
  would look at this script and use its format as a template.

  This code sometimes loads very large files, and then makes very large arrays from the data.
  Because of this, I do a bit of memory management, which is atypical of python programs.
  This handling reduces the program burden on lxplus nodes, and subsequently leads to faster results.
  Usually, calling the garbage collector manually like this reduces code efficiency, and if the program
  runs very slowly in the future the memory consumption would be the first thing to check.
  In the main loop below, gc.collect() tells python to remove unused objects and free up resources,
  and del(large_object) in related functions lets python know we no longer need an object, and its resources can be
  reacquired at the next gc.collect() call
  '''
  # do setup
  setup = setup_handler()
  testing, final_state_mode, jet_mode, era, lumi, tau_pt_cut = setup.state_info
  using_directory, plot_dir, log_file, use_NLO, file_map, one_file_at_a_time, temp_version = setup.file_info
  hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, _, presentation_mode = setup.misc_info
  if one_file_at_a_time: import glob

  print_setup_info(setup)
  # used for printing, might be different from what is called per process
  good_events  = set_good_events(final_state_mode, era, non_SR_region=False, temp_version=temp_version)
  branches     = set_branches(final_state_mode, era, DeepTau_version, "ggH_TauTau", temp_version=temp_version)
  vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)
  print_processing_info(good_events, branches, vars_to_plot, log_file)

  _, reject_datasets = set_dataset_info(final_state_mode)

  # make and apply cuts to any loaded events, store in new dictionaries for plotting
  combined_process_dictionary = {}
  # load corrections to apply
  cevalHpT = correctionlib.CorrectionSet.from_file("HpT_Gen_Reco_corr.json")

  eraConversionMap = {
   "2022 CD"  : "2022preEE",
   "2022 EFG" : "2022postEE",
   "2023 C"   : "2023preBPix",
   "2023 D"   : "2023postBPix",
  }
  correctionEra = eraConversionMap[era]

  for process in file_map: 

    # being reset each run, but they're literally strings so who cares
    branches     = set_branches(final_state_mode, era, DeepTau_version, process, temp_version=temp_version)

    # This line skips Muon_Run* when processing the ditau final state, for example 
    if (process in reject_datasets): continue

    # This line skips WJ backgrounds if the semilep_mode is set to indicate it is already considered in JetFakes
    if ("WJ" in process) and (("WJ" in semilep_mode) or ("Full" in semilep_mode)): continue

    if not one_file_at_a_time:
      # One single entry per process, probably containing wildcard symbol, as defined in file_map_dictionary.py
      input_files = [file_map[process]]
    else:
      # Multiple entries per process, results from wildcard search
      input_files = glob.glob( using_directory + "/" + file_map[process] + ".root")
      input_files = sorted([f.replace(using_directory+"/","")[:-5] for f in input_files])

    for input_file in input_files:
      this_file_map = {process: input_file} # Make a temporary filemap just for this loop
      new_process_dictionary = load_process_from_file(process, using_directory, this_file_map, log_file,
                                                branches, good_events, final_state_mode,
                                                data=("Data" in process), testing=testing)
      if new_process_dictionary == None: continue # skip process if empty

      cut_events = apply_HTT_FS_cuts_to_process(era, process, new_process_dictionary, log_file, final_state_mode, jet_mode,
                                                DeepTau_version, tau_pt_cut)

      if cut_events == None: continue

      cut_events = add_HpT_correction(process, cut_events)

      if ("DY" in process) and (final_state_mode != "dimuon"):
        # def split_DY_by_gen, return combined_process_dictionary
        event_flavor_arr = cut_events["event_flavor"]
        pass_gen_flav, pass_lep_flav, pass_jet_flav = [], [], []
        for i, event_flavor in enumerate(event_flavor_arr):
          if event_flavor == "G": pass_gen_flav.append(i)
          if event_flavor == "L": pass_lep_flav.append(i)
          if event_flavor == "J": pass_jet_flav.append(i)
    
        protected_branches = set_protected_branches(final_state_mode="none", jet_mode="Inclusive")
        background_gen_deepcopy = copy.deepcopy(cut_events)
        background_gen_deepcopy["pass_flavor_cut"] = np.array(pass_gen_flav)
        background_gen_deepcopy = apply_cut(background_gen_deepcopy, "pass_flavor_cut", protected_branches)
        if background_gen_deepcopy == None: continue

        background_lep_deepcopy = copy.deepcopy(cut_events)
        background_lep_deepcopy["pass_flavor_cut"] = np.array(pass_lep_flav)
        background_lep_deepcopy = apply_cut(background_lep_deepcopy, "pass_flavor_cut", protected_branches)
        if background_lep_deepcopy == None: continue

        background_jet_deepcopy = copy.deepcopy(cut_events)
        background_jet_deepcopy["pass_flavor_cut"] = np.array(pass_jet_flav)
        background_jet_deepcopy = apply_cut(background_jet_deepcopy, "pass_flavor_cut", protected_branches)
        if background_jet_deepcopy == None: continue

        combined_process_dictionary = append_to_combined_processes(process+"DYGen", background_gen_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
        combined_process_dictionary = append_to_combined_processes(process+"DYLep", background_lep_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
        combined_process_dictionary = append_to_combined_processes(process+"DYJet", background_jet_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
        del background_gen_deepcopy
        del background_lep_deepcopy
        del background_jet_deepcopy
      else:
        combined_process_dictionary = append_to_combined_processes(process, cut_events, vars_to_plot, 
                                                                   combined_process_dictionary, one_file_at_a_time)
      del new_process_dictionary
      del cut_events
      gc.collect()

  # after loop, sort big dictionary into three smaller ones
  data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

  fakesLabel = "JetFakes"

  # uncomment for original behavior
  # set_JetFakes_process runs a single loop on Data, and makes FFweights using
  # information from FF_dictionary, FF_functions, and producers
  #FF_dictionary = set_JetFakes_process(setup, fakesLabel, semilep_mode) # original
  #if (final_state_mode != "dimuon") and (do_JetFakes == True):
  #  background_dictionary[fakesLabel] = FF_dictionary[fakesLabel] # manually include QCD as background

  # Interesting to include at some point..
  # for mutau and etau the possible scenarios are
  # full JetFakes QCD and WJ (ideally split)
  # JetFakes QCD with WJ from MC
  # no JetFakes with WJ from MC - for debug

  # lazily including the whole updated FF method here because I couldn't figure out the proper
  # way to include it in a separate file
  region = "AR_star" # AR_star for DiTau (which is ARPF + ARFP + ARFF), and AR for mutau/etau
  if (final_state_mode == "mutau") or (final_state_mode == "etau"): region = "AR"
  non_SR_region = ("AR" in region) or ("DR" in region) or ("aiso" in region) or ("combined" in region)
  good_events  = set_good_events(final_state_mode, era, non_SR_region)

  # make and apply cuts to any loaded events, store in new dictionaries for plotting
  combined_process_dictionaryFakes = {}
  for process in file_map: 

    branches     = set_branches(final_state_mode, era, DeepTau_version, process, temp_version=temp_version)

    if (process in reject_datasets): continue
    if ("WJ" in process) and (("WJ" in semilep_mode) or ("Full" in semilep_mode)): continue

    if not one_file_at_a_time:
      input_files = [file_map[process]]
    else:
      input_files = glob.glob( using_directory + "/" + file_map[process] + ".root")
      input_files = sorted([f.replace(using_directory+"/","")[:-5] for f in input_files])

    for input_file in input_files:
      this_file_map = {process: input_file}
      new_process_dictionary = load_process_from_file(process, using_directory, this_file_map, log_file,
                                            branches, good_events, final_state_mode,
                                            data=("Data" in process), testing=testing)
      event_dictionary = new_process_dictionary[process]["info"]
      if (event_dictionary == None): continue

      protected_branches = ["None"]
      from cut_and_study_functions import append_lepton_indices, append_flavor_indices
      event_dictionary = append_lepton_indices(event_dictionary)
      if ("Data" not in process):
        protected_branches = ["FS_t1_flav", "FS_t2_flav", "pass_gen_cuts", "event_flavor"]
        from file_functions import load_and_store_NWEvents
        load_and_store_NWEvents(process, event_dictionary)
        # Remove fakes from MC if they come from TT or WJ samples.
        # We do this because we assume their jetFakes are not well-modeled
        # and so we replace them with the JetFakes estimate from Data.
        # For other MC, we use the fakes from MC, meaning those should be subtracted from Data
        # during the estimate.
        keep_fakes = False if (("TT" in process) or ("WJ" in process)) else True
        event_dictionary = append_flavor_indices(event_dictionary, final_state_mode, keep_fakes=keep_fakes)
        event_dictionary = apply_cut(event_dictionary, "pass_gen_cuts", protected_branches)
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      event_dictionary = FF_control_flow(final_state_mode, semilep_mode, region, event_dictionary, DeepTau_version)
      event_dictionary = apply_cut(event_dictionary, "pass_"+region+"_cuts", protected_branches)

      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      from cut_and_study_functions import apply_jet_cut
      event_dictionary   = apply_jet_cut(event_dictionary, jet_mode)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      skip_DeepTau = True
      if (final_state_mode == "ditau"):
        from cut_ditau_functions import make_ditau_cut
        event_dictionary   = make_ditau_cut(era, event_dictionary, DeepTau_version, skip_DeepTau, tau_pt_cut)
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      if (final_state_mode == "mutau"):
        from cut_mutau_functions import make_mutau_cut
        event_dictionary   = make_mutau_cut(era, event_dictionary, DeepTau_version)
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      if (final_state_mode == "etau"):
        from cut_etau_functions import make_etau_cut
        event_dictionary   = make_etau_cut(era, event_dictionary, DeepTau_version)
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      protected_branches = set_protected_branches(final_state_mode=final_state_mode, jet_mode="none")
      event_dictionary   = apply_cut(event_dictionary, "pass_cuts", protected_branches)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      # then skip DY splitting stuff because we subtract MC from Data later where the MC is all combined anyways

      event_dictionary = add_HpT_correction(process, event_dictionary)

      combined_process_dictionaryFakes = append_to_combined_processes(process, event_dictionary, vars_to_plot, 
                                                             combined_process_dictionaryFakes, one_file_at_a_time)

      del new_process_dictionary
      del event_dictionary
      gc.collect()

  # after loop, sort big dictionary into three smaller ones
  data_dictionaryFakes, background_dictionaryFakes, signal_dictionaryFakes = sort_combined_processes(combined_process_dictionaryFakes, fakes=True)
    
  fakesLabel = "JetFakes"
  # TODO: if mutau or etau give handling for two binned processes, JetFakes_QCD and JetFakes_WJ

  binned_JetFakes_var_dictionary = {}
  for var in vars_to_plot:
    log_print(f"Plotting {var}", log_file, time=True)
    xbins = make_bins(var, final_state_mode)

    h_data               = get_binned_data(final_state_mode, testing, data_dictionaryFakes, var, xbins, lumi)
    h_backgrounds        = get_binned_backgrounds(final_state_mode, testing, background_dictionaryFakes, var, xbins, lumi)
    h_summed_backgrounds = get_summed_backgrounds(h_backgrounds)
    h_signals            = get_binned_signals(final_state_mode, testing, signal_dictionaryFakes, var, xbins, lumi) 

    # FF background = h_data(already mult. by FF) - h_summed_backgrounds(ditto) - h_signals(ditto)
    if testing:
      jetFakes_background = h_data["Data"]["BinnedEvents"] - \
                            h_summed_backgrounds["Bkgd"]["BinnedEvents"] - \
                            (h_signals["VBF_TauTauFakes"]["BinnedEvents"]/100)
    else:
      jetFakes_background = h_data["Data"]["BinnedEvents"] - \
                            h_summed_backgrounds["Bkgd"]["BinnedEvents"] - \
                            (h_signals["ggH_TauTauFakes"]["BinnedEvents"]/100) - \
                            (h_signals["VBF_TauTauFakes"]["BinnedEvents"]/100) - \
                            (h_signals["WmH_TauTauFakes"]["BinnedEvents"]/100) - \
                            (h_signals["WpH_TauTauFakes"]["BinnedEvents"]/100) - \
                            (h_signals["ZH_TauTauFakes"]["BinnedEvents"]/100)

    binned_JetFakes_var_dictionary[var] = {}
    binned_JetFakes_var_dictionary[var]["BinnedEvents"] = jetFakes_background
    binned_JetFakes_var_dictionary[var]["BinnedErrors"] = {}

  log_print("Processing finished!", log_file, time=True)

  ## end processing loop, begin plotting

  dataset, _ = set_dataset_info(final_state_mode)
  eta_phi_plot = False
  if (eta_phi_plot == True): make_eta_phi_plot(data_dictionary, dataset, final_state_mode, jet_mode, "Data")

  # reversed dictionary search for era name based on lumi 
  title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
  title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"

  # idea: give plot_MC an optional argument, which contains a histogram that gets put on the bottom of the stack
 
  vars_to_plot = [var for var in vars_to_plot if "flav" not in var]
  vars_to_plot.append("HTT_H_pt_corr")
  CUSTOM_VARS = False
  if (presentation_mode == True): CUSTOM_VARS = False # always overwrite, you'll want all the plots in this mode
  if CUSTOM_VARS == True:
    if (final_state_mode == "ditau"):
      vars_to_plot = ["HTT_m_vis", "FS_trig_idx",
                    "FS_t1_pt", "FS_t1_eta", "FS_t1_phi", "FS_t1_DM", "FS_t1_mass",
                    "FS_t2_pt", "FS_t2_eta", "FS_t2_phi", "FS_t2_DM", "FS_t2_mass",
                    "FS_dphi_t1t2", "FS_deta_t1t2",
                    "PuppiMET_pt", "HTT_H_pt", "HTT_H_pt_corr",
                    "nCleanJetGT30"]
    if (final_state_mode == "mutau"):
      vars_to_plot = ["HTT_m_vis", 
                    "FS_tau_pt", "FS_tau_eta", "FS_tau_phi", "FS_tau_mass", "FS_tau_DM",
                    "FS_mu_pt", "FS_mu_eta", "FS_mu_phi", 
                    "FS_dphi_mutau", "FS_deta_mutau",
                    "PuppiMET_pt", "HTT_H_pt", "HTT_H_pt_corr",
                    "FS_mt", "nCleanJetGT30"]
  plots_unrolled = False
  #if (presentation_mode == True): plots_unrolled = True
  if (plots_unrolled == True):
    #rolled_vars = ["FastMTT_mass"]
    #rolled_vars = ["FS_t1_mass", "FS_t2_mass"]
    #rolled_vars = ["FS_tau_mass"]
    #rolled_vars = ["FS_t1_eta"]
    rolled_vars  = ["HTT_m_vis"]
    unrolled_vars = {
      "HTT_pT_l1l2" : [0, 25, 50, 100],
      #"HTT_H_pt"      : [0, 45, 80, 120, 200, 350, 450],
      #"nCleanJetGT30" : [0, 1, 2, 3, 4],
      #"FS_t1_DM" : [0, 1, 2, 3], # quirky encoding: 0: 0, 1: 1, 2: 10, 3: 11
      #"FS_t2_DM" : [0, 1, 2, 3],
      #"FS_tau_DM" : [0, 1, 2, 3]
    }
    if ("1j" in jet_mode):
      unrolled_vars["CleanJetGT30_pt_1"] = [30, 60, 120, 200, 350]

    for unrolled_var, unrolled_bins in unrolled_vars.items():
      unrolled_bins_data       = make_masks_per_bin(data_dictionary, unrolled_var, unrolled_bins)
      unrolled_bins_background = make_masks_per_bin(background_dictionary, unrolled_var, unrolled_bins)
      unrolled_bins_signal     = make_masks_per_bin(signal_dictionary, unrolled_var, unrolled_bins)
  
      for rolled_var in rolled_vars:
        xbins = make_bins(rolled_var, final_state_mode)
        fig_unroll, stack_n_ax, ratio_n_ax = setup_unrolled_plot(len(unrolled_bins))
  
        for ith_bin in range(len(unrolled_bins)):
          print(unrolled_bins_data)
          h_data_ur = get_binned_data(final_state_mode, testing, data_dictionary, rolled_var, xbins, lumi,
                                        mask=unrolled_bins_data, mask_n=ith_bin)
          h_backgrounds_ur = get_binned_backgrounds(final_state_mode, testing, background_dictionary, rolled_var, xbins, lumi,
                                        mask=unrolled_bins_background, mask_n=ith_bin)
          h_summed_backgrounds_ur = get_summed_backgrounds(h_backgrounds_ur)
          # ADD THE MANUAL FF WEIGHTS!
          h_signals_ur = get_binned_signals(final_state_mode, testing, signal_dictionary, rolled_var, xbins, lumi,
                                        mask=unrolled_bins_signal, mask_n=ith_bin)
          blind, blind_range = False, []
          # remove yields for these plots by setting presentation_mode to True below
          plot_data(   stack_n_ax[ith_bin], xbins, h_data_ur,        lumi, True, blind, blind_range)
          # FFweights not setup yet for unrolled plots, because you need to rederive/rebin with the masks...
          # implies the need for a binning function for the FFweights quanitities that can be called when it's needed
          #extra_hist = binned_JetFakes_var_dictionary[var]["BinnedEvents"]
          #plot_MC(     stack_n_ax[ith_bin], xbins, h_backgrounds_ur, lumi, extra_hist, True)
          plot_MC(     stack_n_ax[ith_bin], xbins, h_backgrounds_ur, lumi, True)
          plot_signal( stack_n_ax[ith_bin], xbins, h_signals_ur,     lumi, True)

          make_ratio_plot(ratio_n_ax[ith_bin], xbins, 
                          h_data_ur["Data"]["BinnedEvents"], "Data", np.ones(np.shape(h_data_ur)),
                          h_summed_backgrounds_ur["Bkgd"]["BinnedEvents"], "Data", np.ones(np.shape(h_summed_backgrounds_ur)))

          spruce_up_unrolled_plot(fig_unroll, stack_n_ax, ratio_n_ax, label_dictionary[rolled_var], title+" Unrolled", 
                                  final_state_mode, jet_mode, tau_pt_cut, set_x_log=False, set_y_log=False) # True 
          text = ""
          if (unrolled_var == "HTT_H_pt") or (unrolled_var == "HTT_H_pt_corr"):
            try:               text = f"{unrolled_bins[ith_bin]} ≤ H_pT < {unrolled_bins[ith_bin+1]}"
            except IndexError: text = f"H_pT > {unrolled_bins[ith_bin]}"
          elif (unrolled_var == "nCleanJetGT30"):
            nJet = f"{unrolled_bins[ith_bin]}"
            text = f"nJet = {nJet}" if ith_bin != (len(unrolled_bins)-1) else f"nJet ≥ {nJet}"
          elif (unrolled_var == "CleanJetGT30_pt_1"):
            try:               
              text = f"{unrolled_bins[ith_bin]} ≤ j1_pT < {unrolled_bins[ith_bin+1]}"
              if (ith_bin == 0): text = f"0j category"
            except IndexError: text = f"j1_pT > {unrolled_bins[ith_bin]}"
          elif (unrolled_var == "FS_t1_DM"):
            decay_mode_mapping = [0, 1, 10, 11]
            text = f"Leading Tau Decay Mode: {decay_mode_mapping[ith_bin]}"
          elif (unrolled_var == "FS_t2_DM"):
            decay_mode_mapping = [0, 1, 10, 11]
            text = f"Subleading Tau Decay Mode: {decay_mode_mapping[ith_bin]}"
          else:
            print("haven't styled that variable yet, no text added")
          add_text(stack_n_ax[ith_bin], text, loc=[0.05, 0.90])

        plt.savefig(plot_dir + "/" + "unrolled_TauPtCategory_" + tau_pt_cut + "_" + str(rolled_var) + "-"
                    + str(unrolled_var) + ".png", dpi=200)
 

  for var in vars_to_plot:
    if DEBUG: log_print(f"Plotting {var}", log_file, time=True)

    xbins = make_bins(var, final_state_mode)
    hist_ax, hist_ratio = setup_ratio_plot()

    h_data = get_binned_data(final_state_mode, testing, data_dictionary, var, xbins, lumi)
    h_backgrounds = get_binned_backgrounds(final_state_mode, testing, background_dictionary, var, xbins, lumi,
                                           presentation_mode)
    h_summed_backgrounds = get_summed_backgrounds(h_backgrounds)
    extra_hist = binned_JetFakes_var_dictionary[var]["BinnedEvents"]
    h_summed_backgrounds["Bkgd"]["BinnedEvents"] += extra_hist # adding JetFakes
    h_signals = get_binned_signals(final_state_mode, testing, signal_dictionary, var, xbins, lumi) 

    # plot everything :)
    plot_data(   hist_ax, xbins, h_data,        lumi, presentation_mode)
    plot_MC(     hist_ax, xbins, h_backgrounds, lumi, extra_hist, presentation_mode)
    #plot_MC(     hist_ax, xbins, h_backgrounds, lumi, presentation_mode) # old mode
    plot_signal( hist_ax, xbins, h_signals,     lumi, presentation_mode)

    make_ratio_plot(hist_ratio, xbins, 
                    h_data["Data"]["BinnedEvents"], "Data", np.ones(np.shape(h_data)),
                    h_summed_backgrounds["Bkgd"]["BinnedEvents"], "Data", np.ones(np.shape(h_summed_backgrounds)))
   
    if ("dxy" in var) or ("dz" in var):  hist_ax.set_yscale('log')
    spruce_up_plot(hist_ax, hist_ratio, label_dictionary[var], title, final_state_mode, jet_mode)
    spruce_up_legend(hist_ax, final_state_mode)

    plt.savefig(plot_dir + "/" + str(var) + ".png", dpi=200)
 
  plots_2D = False
  if (plots_2D == True):
    varY = "FS_t1_mass"
    if (jet_mode == "Inclusive"):
      list_varX = ["FS_t1_pt", "nCleanJetGT30", "HTT_H_pt"]
      list_binX = [np.linspace(0, 200, 20+1), np.linspace(0, 8, 8+1), np.linspace(0, 500, 20+1)]
      list_varX = "FS_t2_mass"
      list_binX = binning_dictionary[final_state_mode][list_varX[0]] 
    elif (jet_mode == "1j"):
      list_varX = ["FS_t1_pt", "nCleanJetGT30", "HTT_H_pt", "CleanJetGT30_pt_1"]
      list_binX = [np.linspace(0, 200, 20+1), np.linspace(0, 8, 8+1), np.linspace(0, 500, 20+1), np.linspace(0, 600, 12+1)]
    list_of_processes = ["DataTau", "ggH", "VBF", "JetFakes"]
    for varX, binX in zip(list_varX, list_binX):
      for single_process in list_of_processes:
        secondary_dict = signal_dictionary if ("ggH" in single_process) or ("VBF" in single_process) else background_dictionary
        use_dict = data_dictionary if "Data" in single_process else secondary_dict
        make_two_dimensional_plot(use_dict[single_process]["PlotEvents"], final_state_mode,
                                  varX, varY, add_to_title=single_process)
                                  #alt_x_bins=binX, alt_y_bins=np.linspace(0, 140, 14+1))
        plt.savefig("ditau_2D_plot/" + process + "_" + varX + "_" + varY + ".png", dpi=200)
  
    for varX, binX in zip(list_varX, list_binX):
      make_two_dimensional_ratio_plot(signal_dictionary, data_dictionary,
                                      #final_state_mode, varX, varY, add_to_title="Expected Higgs / Obs.",
                                      final_state_mode, varX, varY, add_to_title="Expected Higgs / √Obs.",
                                      alt_x_bins=binX, alt_y_bins=np.linspace(0, 140, 14+1))
                                      #alt_x_bins=binX, alt_y_bins=np.linspace(0, 140, 7+1))
      plt.savefig("ditau_2D_plot/ratio_" + varX + "_" + varY + ".png", dpi=200)

  print(f"Plots are in {plot_dir}")
  if hide_plots: pass
  else: plt.show()

  print("Making fitter shapes!")
  save_fitter_shapes(plot_dir, era, final_state_mode, vars_to_plot, combined_process_dictionary, combined_process_dictionaryFakes, fakesLabel, testing, lumi)
  _, f_ax = plt.subplots()
  f_ax.text(x=0.5, y=0.5, s="Finished!", fontsize=20, ha="center", va="center")
  plt.show()
