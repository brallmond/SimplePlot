# Authored by Braden Allmond, Sep 11, 2023
DEBUG = False

# libraries
import numpy as np
import sys
import matplotlib.pyplot as plt
import gc
import copy

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
from plotting_functions    import plot_raw, plot_data, plot_MC, plot_signal, make_bins, make_pie_chart, make_two_dimensional_plot
from plotting_functions    import make_two_dimensional_ratio_plot
from plotting_functions    import setup_unrolled_plot, spruce_up_unrolled_plot
from binning_dictionary    import label_dictionary

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info, log_print, print_processing_info

from make_fitter_shapes    import save_fitter_shapes

def make_masks_per_bin(input_dictionary, var, binning):
  passing_var_bins_dict = {}
  for process in input_dictionary.keys():
    passing_var_bins = []
    input_array = input_dictionary[process]["PlotEvents"][var]
    for i in range(len(binning)):
      if (i != len(binning) - 1):
        premask1 = input_array >= binning[i]
        premask2 = input_array < binning[i+1]
        mask = np.logical_and(premask1, premask2)
      else:
        mask = input_array >= binning[i]
      passing_var_bins.append(mask)
    passing_var_bins_dict[process] = passing_var_bins
  return passing_var_bins_dict # dictionary of list of masks


if __name__ == "__main__":
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
  from branch_functions import add_signal_branches
  vars_to_plot = add_signal_branches(vars_to_plot)
  print_processing_info(good_events, branches, vars_to_plot, log_file)

  _, reject_datasets = set_dataset_info(final_state_mode)

  signal_processes = ["ggH_TauTau", "VBF_TauTau"]

  # make and apply cuts to any loaded events, store in new dictionaries for plotting
  combined_process_dictionary = {}
  for process in file_map: 

    if (process not in signal_processes): continue

    # being reset each run, but they're literally strings so who cares
    branches     = set_branches(final_state_mode, era, DeepTau_version, process, temp_version=temp_version)

    # This line skips Muon_Run* when processing the ditau final state, for example 
    if (process in reject_datasets): continue

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

        if ("NLO" in process): process += "temp"
        combined_process_dictionary = append_to_combined_processes(process.replace("temp","DYGen"), background_gen_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
        combined_process_dictionary = append_to_combined_processes(process.replace("temp","DYLep"), background_lep_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
        combined_process_dictionary = append_to_combined_processes(process.replace("temp","DYJet"), background_jet_deepcopy, 
                                             vars_to_plot, combined_process_dictionary, one_file_at_a_time)
      else:
        combined_process_dictionary = append_to_combined_processes(process, cut_events, vars_to_plot, 
                                                                   combined_process_dictionary, one_file_at_a_time)
      del new_process_dictionary
      del cut_events
      gc.collect()

  # after loop, sort big dictionary into three smaller ones
  data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

  # reversed dictionary search for era name based on lumi 
  title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
  title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"

  #varY, varX  = "Gen_H_pT", "HTT_H_pt"
  #make_two_dimensional_plot(signal_dictionary[process]["PlotEvents"], final_state_mode,
  #                          varX, varY, add_to_title=process)
  
  _, diff_ax = plt.subplots()
  _, diff_ax2 = plt.subplots()
  process_colors = {"ggH_TauTau" : "blue", "VBF_TauTau" : "red"}
  process_labels = {"ggH_TauTau" : "ggH", "VBF_TauTau" : "qqH"}
  for process in signal_processes: 
    # 1D plot 
    xbins = make_bins("HTT_H_pt", final_state_mode)
    h_signal_reco = get_binned_signals(final_state_mode, testing, signal_dictionary, "HTT_H_pt", xbins, lumi) 
    h_signal_gen  = get_binned_signals(final_state_mode, testing, signal_dictionary, "Gen_H_pT", xbins, lumi) 
    reco = h_signal_reco[process]["BinnedEvents"]
    gen  = h_signal_gen[process]["BinnedEvents"]
    #plot_raw(diff_ax, xbins, reco, 
    #                  color=process_colors[process], label=f"{process_labels[process]} Reco", marker="v")
    #plot_raw(diff_ax, xbins, gen, 
    #                  color=process_colors[process], label=f"{process_labels[process]} Gen", fillstyle="none")
    #plot_raw(diff_ax, xbins, reco/gen, 
    #                  color=process_colors[process], label=f"{process_labels[process]} Gen Ratio", fillstyle="none")
    plot_raw(diff_ax, xbins, 1/(reco/gen), 
                      color=process_colors[process], label=f"{process_labels[process]} Gen Ratio", fillstyle="none")

    spruce_up_single_plot(diff_ax, "H_pT", "Events", title, final_state_mode, jet_mode)

    raw_gen  = signal_dictionary[process]["PlotEvents"]["Gen_H_pT"]
    raw_reco = signal_dictionary[process]["PlotEvents"]["HTT_H_pt"]
    #raw_reco = raw_reco[raw_gen > 200]
    #raw_gen  = raw_gen[raw_gen > 200]
    temp_bins = np.linspace(-1, 1, 60)
    vals = (raw_reco-raw_gen)/raw_gen # make this 2D with H_pT
    temp_hist, _ = np.histogram(vals, temp_bins)
    temp_hist = temp_hist/np.max(temp_hist) # normed
    from scipy import stats
    print(process)
    print(stats.describe(vals))

    mean = np.average(vals)
    std  = np.std(vals)
    print(mean, std)

    #new_hist, _ = np.histogram(vals+mean, temp_bins)
    #new_hist, _ = np.histogram(vals*mean/std, temp_bins)
    new_hist, _ = np.histogram(vals*mean, temp_bins)

    fig, axis = plt.subplots(figsize=(7,4))
    h2d, xbins, ybins = np.histogram2d(raw_reco, vals, bins=(xbins, temp_bins))
    h2d = h2d.T # transpose from image coordinates to data coordinates
    cmesh = axis.pcolormesh(xbins, ybins, h2d, cmap="copper") #pcolormesh uses data coordinates by default, imshow uses array of 1x1 squares
    plt.colorbar(cmesh)


    #plot_raw(diff_ax, temp_bins, temp_hist, color=process_colors[process], label=process_labels[process])
    #diff_ax.vlines(0, 0, 1.1, linestyle="--", color="grey")
    plot_raw(diff_ax2, temp_bins, new_hist, color=process_colors[process], 
                       label=process_labels[process]+" transformed!")

    #spruce_up_single_plot(diff_ax, "H_pT (Reco - Gen) / Gen", "Normalized Events", "Response", 
    #                      final_state_mode, jet_mode, yrange=[0.0, 1.1])
    spruce_up_single_plot(diff_ax2, "Normalized H_pT (Reco - Gen) / Gen", "Normalized Events", "Response", 
                          final_state_mode, jet_mode)
 
    
  plt.savefig("signal_response_plots/" + final_state_mode + "_H_pT_response.png", dpi=200)

  for process in signal_processes: 
    # 2D plots
    recoVars = ["HTT_H_pt", "nCleanJetGT30"]#, "CleanJetGT30_pt_1"]
    genVars  = ["Gen_H_pT", "Gen_nCleanJet"]#, "Gen_pT_j1"]
    varAltBins = [np.array([0, 45, 80, 120, 200, 350, 450, 600]), #H_pT
                  np.array([0, 1, 2, 3, 4])] # nJets
    norm_methods = ["total", "row", "column"]
    for norm_method in norm_methods:
      for bins, varY, varX in zip(varAltBins, recoVars, genVars):
        make_two_dimensional_plot(signal_dictionary[process]["PlotEvents"], final_state_mode,
                                  varX, varY, title=process + f" {norm_method} Unity Normalization Response",
                                  normalization = norm_method,
                                  alt_x_bins=bins, alt_y_bins=bins)
        name = "_".join([process, final_state_mode, norm_method, varX])
        plt.savefig("signal_response_plots/" + name + ".png", dpi=200)
  
  if hide_plots: pass
  else: plt.show()

