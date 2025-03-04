# Authored by Braden Allmond, Sep 11, 2023

# libraries
import numpy as np
import sys
import matplotlib.pyplot as plt
import gc
import copy
from iminuit import Minuit
from iminuit.cost import LeastSquares

# explicitly import used functions from user files, grouped roughly by call order and relatedness
# import statements for setup
from setup import setup_handler, set_good_events
from branch_functions import set_branches
from plotting_functions import set_vars_to_plot
from file_map_dictionary import set_dataset_info

# import statements for data loading and processing
from file_functions        import load_process_from_file, append_to_combined_processes, sort_combined_processes
#from FF_functions          import * # will lead to recursive import
from FF_functions          import set_JetFakes_process
from cut_and_study_functions import apply_HTT_FS_cuts_to_process
from cut_and_study_functions import apply_cut, apply_jet_cut, set_protected_branches

# plotting
from luminosity_dictionary import luminosities_with_normtag as luminosities
from plotting_functions    import get_midpoints, make_eta_phi_plot
from plotting_functions    import get_binned_data, get_binned_backgrounds, get_binned_signals, get_summed_backgrounds
from plotting_functions    import setup_ratio_plot, make_ratio_plot, spruce_up_plot, spruce_up_legend
from plotting_functions    import setup_single_plot, spruce_up_single_plot
from plotting_functions    import plot_data, plot_MC, plot_signal, make_bins, make_pie_chart, plot_raw

from binning_dictionary import label_dictionary

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info, log_print

from cut_ditau_functions import make_ditau_cut
from cut_mutau_functions import make_mutau_cut

if __name__ == "__main__":
  '''
  '''

  # do setup
  setup = setup_handler()
  testing, final_state_mode, jet_mode, era, lumi, tau_pt_cut = setup.state_info
  using_directory, plot_dir, log_file, use_NLO, file_map, one_file_at_a_time, temp_version = setup.file_info
  hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, _, _ = setup.misc_info

  print_setup_info(setup)

  if (jet_mode == "Inclusive"): 
    print("This script is not meant to work with Inclusive jet_mode.")
    print("You can set your jet_mode by adding --jet_mode 0j to your command. Exiting...")
    sys.exit()

  do_QCD = do_JetFakes
  _, reject_datasets = set_dataset_info(final_state_mode)

  dataset_dictionary = {"ditau" : "DataTau", "mutau" : "DataMuon", "etau" : "DataElectron", "emu" : "DataEMu"}
  dataset = dataset_dictionary[final_state_mode]

  store_region_data_dictionary = {}
  store_region_bkgd_dictionary = {}
  store_region_sgnl_dictionary = {}
  semilep_mode = "QCD" #"QCD" or "WJ"
  # this is treated like data in your plots (i.e. it's the black dots)
  pseudo_SR = "DRsr" # need the data from here to compare to
  # this is treated like MC in your plots (i.e. it's multiplied by the FF to make the pink bars)
  pseudo_AR = "AR" # need the events from here to make the QCD estimate
  # DRsr DRar is closure check 
  for region in [pseudo_SR, pseudo_AR]:
    non_SR_region = ("AR" in region) or ("DR" in region) or ("aiso" in region)
    good_events  = set_good_events(final_state_mode, era, non_SR_region)

    vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)

    # make and apply cuts to any loaded events, store in new dictionaries for plotting
    combined_process_dictionary = {}

    for process in file_map: 

      gc.collect()
      if (process in reject_datasets): continue

      branches     = set_branches(final_state_mode, era, DeepTau_version, process)
      new_process_dictionary = load_process_from_file(process, using_directory, file_map, log_file,
                                              branches, good_events, final_state_mode,
                                              data=("Data" in process), testing=testing)
      event_dictionary = new_process_dictionary[process]["info"]
      if (event_dictionary == None): continue

      protected_branches = ["None"]
      from cut_and_study_functions import append_lepton_indices, append_flavor_indices
      event_dictionary = append_lepton_indices(event_dictionary)
      if ("Data" not in process):
        from file_functions import load_and_store_NWEvents
        load_and_store_NWEvents(process, event_dictionary)
        event_dictionary = append_flavor_indices(event_dictionary, final_state_mode, keep_fakes=True)

      from FF_functions import FF_control_flow
      event_dictionary = FF_control_flow(final_state_mode, semilep_mode, region, event_dictionary, DeepTau_version)
      event_dictionary = apply_cut(event_dictionary, "pass_"+region+"_cuts", protected_branches)

      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      event_dictionary   = apply_jet_cut(event_dictionary, jet_mode)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      if (final_state_mode == "ditau"):
        event_dictionary   = make_ditau_cut(era, event_dictionary, DeepTau_version) # no DeepTau or Charge requirements
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      if (final_state_mode == "mutau"):
        event_dictionary   = make_mutau_cut(era, event_dictionary, DeepTau_version) # no DeepTau or Charge requirements
        if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      protected_branches = set_protected_branches(final_state_mode=final_state_mode, jet_mode="none")
      event_dictionary   = apply_cut(event_dictionary, "pass_cuts", protected_branches)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      from FF_functions import add_FF_weights
      if ("Data" in process):
        event_dictionary   = add_FF_weights(event_dictionary, final_state_mode, jet_mode, semilep_mode, closure=True)

      # TODO : extendable to jet cuts (something I've meant to do for some time)
      '''
      if "DY" in process:
        event_flavor_arr = event_dictionary["event_flavor"]
        pass_gen_flav, pass_lep_flav, pass_jet_flav = [], [], []
        for i, event_flavor in enumerate(event_flavor_arr):
          if event_flavor == "G":
            pass_gen_flav.append(i)
          if event_flavor == "L":
            pass_lep_flav.append(i)
          if event_flavor == "J":
            pass_jet_flav.append(i)
      
        from cut_and_study_functions import apply_cut, set_protected_branches
        protected_branches = set_protected_branches(final_state_mode="none", jet_mode="Inclusive")
        background_gen_deepcopy = copy.deepcopy(event_dictionary)
        background_gen_deepcopy["pass_flavor_cut"] = np.array(pass_gen_flav)
        background_gen_deepcopy = apply_cut(background_gen_deepcopy, "pass_flavor_cut", protected_branches)
        if background_gen_deepcopy == None: continue

        background_lep_deepcopy = copy.deepcopy(event_dictionary)
        background_lep_deepcopy["pass_flavor_cut"] = np.array(pass_lep_flav)
        background_lep_deepcopy = apply_cut(background_lep_deepcopy, "pass_flavor_cut", protected_branches)
        if background_lep_deepcopy == None: continue

        background_jet_deepcopy = copy.deepcopy(event_dictionary)
        background_jet_deepcopy["pass_flavor_cut"] = np.array(pass_jet_flav)
        background_jet_deepcopy = apply_cut(background_jet_deepcopy, "pass_flavor_cut", protected_branches)
        if background_jet_deepcopy == None: continue

        combined_process_dictionary = append_to_combined_processes("DYGen", background_gen_deepcopy, vars_to_plot, 
                                                                   combined_process_dictionary)
        combined_process_dictionary = append_to_combined_processes("DYLep", background_lep_deepcopy, vars_to_plot, 
                                                                   combined_process_dictionary)
        combined_process_dictionary = append_to_combined_processes("DYJet", background_jet_deepcopy, vars_to_plot, 
                                                                   combined_process_dictionary)
        
      else:
        combined_process_dictionary = append_to_combined_processes(process, event_dictionary, vars_to_plot, 
                                                                   combined_process_dictionary)
      '''
      combined_process_dictionary = append_to_combined_processes(process, event_dictionary, vars_to_plot, 
                                                                 combined_process_dictionary, one_file_at_a_time)

    # after loop, sort big dictionary into three smaller ones
    data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

    # store dictionaries
    store_region_data_dictionary[region] = data_dictionary
    store_region_bkgd_dictionary[region] = background_dictionary
    store_region_sgnl_dictionary[region] = signal_dictionary

  pseudo_SR_data = store_region_data_dictionary[pseudo_SR] # this has FF weights
  pseudo_SR_bkgd = store_region_bkgd_dictionary[pseudo_SR]
  pseudo_SR_sgnl = store_region_sgnl_dictionary[pseudo_SR]
  pseudo_AR_data = store_region_data_dictionary[pseudo_AR] # this also has FF weights
  pseudo_AR_bkgd = store_region_bkgd_dictionary[pseudo_AR]
  pseudo_AR_sgnl = store_region_sgnl_dictionary[pseudo_AR]

  fakesLabel = "JetFakes" # all used to be "myQCD"
  QCD_dictionary = {}
  QCD_dictionary[fakesLabel] = {}
  QCD_dictionary[fakesLabel]["PlotEvents"] = {}
  QCD_dictionary[fakesLabel]["FF_weight"]  = pseudo_AR_data[dataset]["FF_weight"]
  for var in vars_to_plot:
    if ("flav" in var) or ("Generator_weight" in var): continue
    QCD_dictionary[fakesLabel]["PlotEvents"][var] = pseudo_AR_data[dataset]["PlotEvents"][var]

  log_print("Processing finished!", log_file, time=True)
  ## end processing loop, begin plotting

  vars_to_plot = [var for var in vars_to_plot if "flav" not in var]
  if (final_state_mode == "ditau"):
    vars_to_plot = ["HTT_m_vis", 
                  "FS_t1_pt", "FS_t1_eta", "FS_t1_phi", "FS_t1_DM", "FS_t1_mass",
                  "FS_t2_pt", "FS_t2_eta", "FS_t2_phi", "FS_t2_DM", "FS_t2_mass",
                  "PuppiMET_pt"]
  if (final_state_mode == "mutau"):
    vars_to_plot = ["HTT_m_vis", 
                  "FS_tau_pt", "FS_tau_eta", "FS_tau_phi", "FS_tau_DM", "FS_tau_mass",
                  "FS_mu_pt", "FS_mu_eta", "FS_mu_phi", "PuppiMET_pt", "FS_mt"]
  # and add back variables unique to the jet mode
  if (jet_mode == "1j") or (jet_mode == "GTE2j"): vars_to_plot.append("CleanJetGT30_pt_1")
  if (jet_mode == "GTE2j"): vars_to_plot.append("CleanJetGT30_pt_2")
  for var in vars_to_plot:
    log_print(f"Plotting {var}", log_file, time=True)

    xbins = make_bins(var, final_state_mode)

    ax_hist, ax_ratio = setup_ratio_plot()

    h_pseudo_SR_data = get_binned_data(final_state_mode, testing, pseudo_SR_data, var, xbins, lumi)
    h_pseudo_AR_data = get_binned_data(final_state_mode, testing, pseudo_AR_data, var, xbins, lumi)
    h_pseudo_SR_backgrounds        = get_binned_backgrounds(final_state_mode, testing, pseudo_SR_bkgd, var, xbins, lumi)
    h_pseudo_SR_summed_backgrounds = get_summed_backgrounds(h_pseudo_SR_backgrounds)
    h_pseudo_AR_backgrounds        = get_binned_backgrounds(final_state_mode, testing, pseudo_AR_bkgd, var, xbins, lumi)
    h_pseudo_AR_summed_backgrounds = get_summed_backgrounds(h_pseudo_AR_backgrounds)

    h_QCD           = get_binned_backgrounds(final_state_mode, testing, QCD_dictionary, var, xbins, 1)
    h_QCD_for_ratio = get_summed_backgrounds(h_QCD)

    h_pseudo_SR_data_m_MC = {}
    h_pseudo_SR_data_m_MC["Data"] = {}
    h_pseudo_SR_data_m_MC["Data"]["BinnedEvents"] = h_pseudo_SR_data["Data"]["BinnedEvents"] - \
                                                    h_pseudo_SR_summed_backgrounds["Bkgd"]["BinnedEvents"]
    # TODO: ADD ERRORS TO THIS IN A CORRECT WAY
    h_pseudo_SR_data_m_MC["Data"]["BinnedErrors"] = h_pseudo_SR_data["Data"]["BinnedErrors"] 
                                                    
    # add back the WJ MC if testing WJ agreement
    if (semilep_mode == "WJ"):
      h_pseudo_SR_data_m_MC["Data"]["BinnedEvents"] += h_pseudo_SR_backgrounds[semilep_mode]["BinnedEvents"]
    
    
    # set negative values to zero
    # ratio[np.isnan(ratio)] = 0
    #h_pseudo_SR_data_m_MC[np.where(h_pseudo_SR_data_m_MC["Data"]["BinnedEvents"] < 0)] = 0
    #h_pseudo_AR_weight = (h_pseudo_AR_data - h_pseudo_AR_summed_backgrounds) / h_pseudo_AR_data # not used.

    # reversed dictionary search for era name based on lumi 
    title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
    title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"

    # plot everything :)
    plot_data(ax_hist, xbins, h_pseudo_SR_data_m_MC, lumi, color="black", label=f"{pseudo_SR} : Data-MC")
    plot_MC(ax_hist, xbins, h_QCD, lumi) # weight = h_pseudo_AR_weight

    ratio_out, ratio_err = make_ratio_plot(ax_ratio, xbins, 
                    #h_pseudo_SR_data_m_MC["Data"]["BinnedEvents"], "Data", np.ones(np.shape(h_pseudo_SR_data_m_MC)),
                    #h_QCD_for_ratio["Bkgd"]["BinnedEvents"], "Data", np.ones(np.shape(h_QCD_for_ratio)))
                    h_QCD_for_ratio["Bkgd"]["BinnedEvents"], "Data", np.ones(np.shape(h_QCD_for_ratio)), # inverted, switch back
                    h_pseudo_SR_data_m_MC["Data"]["BinnedEvents"], "Data", np.ones(np.shape(h_pseudo_SR_data_m_MC)))

    if ("vis" in var):
      print("PRINTING JANKY MVIS SS-OS CORRECTION!")
      print("MAKE SURE THE RATIO FUNC IS INVERTED SO YOU GET THE RIGHT VALUES")
      print(f"RAW RATIO OF {pseudo_SR} / ({pseudo_AR}*FF)")
      print(ratio_out)
      print("RAW ERROR")
      print(ratio_err)

    spruce_up_plot(ax_hist, ax_ratio, label_dictionary[var], title, final_state_mode, jet_mode)
    spruce_up_legend(ax_hist, final_state_mode)

    plt.savefig(plot_dir + "/" + str(var) + ".png")

    # do extra stuff for second lepton leg
    #if var in ["FS_t2_pt", "FS_mu_pt", "FS_ele_pt"]:
      #fit the ratio plot, and print the fit
      #put it in an additional plot, a la FF_plot_set_1p5 (i guess you could merge those, huh?)

  print(f"Plots are in {plot_dir}")
  if hide_plots: pass
  else: plt.show()
  log_print(f"Finished plots for FF region!", log_file, time=True)

