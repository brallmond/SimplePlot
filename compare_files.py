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
from setup import setup_handler, set_good_events
from branch_functions import set_branches
from plotting_functions import set_vars_to_plot
from file_map_dictionary import set_dataset_info

# import statements for data loading and processing
from file_functions        import load_process_from_file, append_to_combined_processes, sort_combined_processes
from FF_functions        import set_JetFakes_process
from cut_and_study_functions import apply_HTT_FS_cuts_to_process
from cut_and_study_functions import apply_cut, set_protected_branches

# plotting
from plotting_functions import get_midpoints, make_eta_phi_plot
from luminosity_dictionary import luminosities_with_normtag as luminosities
from plotting_functions    import get_binned_data, get_binned_backgrounds, get_binned_signals
from plotting_functions    import setup_ratio_plot, make_ratio_plot, spruce_up_plot, spruce_up_legend
from plotting_functions    import setup_single_plot, spruce_up_single_plot, add_text
from plotting_functions    import plot_data, plot_MC, plot_signal, make_bins, make_pie_chart

from binning_dictionary import label_dictionary

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info, log_print

if __name__ == "__main__":
  # do setup
  setup = setup_handler()
  testing, final_state_mode, jet_mode, era, lumi = setup.state_info
  using_directory, plot_dir, log_file, use_NLO, file_map = setup.file_info
  hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, one_process = setup.misc_info


  print_setup_info(setup)

  print(f"Comparings files for: {one_process}")

  # make and apply cuts to any loaded events, store in new dictionaries for plotting
  combined_process_dictionary = {}

  good_events  = set_good_events(final_state_mode) 
  vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)

  # for normalish local storage
  #home_dir = "/Users/ballmond/LocalDesktop/HiggsTauTau"
  #dir_base = "/V12_PFRel_preEE_notriggermatching/" + final_state_mode
  #dir_alt  = "/V12_preEE_HLepRare_notriggermatching/" + final_state_mode
  # for SSD storage
  home_dir = ""
  dir_base = "/Volumes/IDrive/HTauTau_Data/mutau_postEE_Hlep_comparison/KSU/"
  dir_alt  = "/Volumes/IDrive/HTauTau_Data/mutau_postEE_Hlep_comparison/Hlep/"
  using_directory = "/Volumes/IDrive/HTauTau_Data/mutau_postEE_Hlep_comparison/Hlep/"
  # 
  input_file = one_process
  input_process = one_process.replace("/","")[0:2]
  if (input_process in ["WZ", "ZZ", "WW"]): input_process = "VV"
  if (input_process == "Ta") or (input_process == "Mu"): input_process = "Data"
  input_name = input_file.split('_HTauTau')[0].replace('/','')
  process_list = [input_name + "_KSU", input_name + "_Hlep"]
  if (input_process[0] != "/"): input_process = "/" + input_process
  if (input_file[0]    != "/"): input_file    = "/" + input_file
  direct_input_list = [
    home_dir + dir_base + input_process + input_file + "_step2*",
    home_dir + dir_alt  + input_process + input_file + "_Hlep*",
  ]

  #process_list = ["ggH_old", "ggH_new"]
  #direct_input_list = [
     # home_dir + "/V12_PFRel_postEE_Dennis_test_detector_holes/ditau/Signal/ggH_TauTau_private_HTauTau_2022postEE_step2",
      #home_dir + "/V12_PFRel_preEE_nominal/ditau/Signal/ggH_TauTau_HTauTau_2022preEE_step2",
      #home_dir + "/V12_PFRel_preEE_notriggermatching/ditau/Signal/ggH_TauTau_HTauTau_2022preEE_step2",
      #home_dir + "/V12_PFRel_postEE_nominal/ditau/Signal/ggH_TauTau_HTauTau_2022postEE_step2",
      #home_dir + "/V12_PFRel_postEE_notriggermatching/ditau/Signal/ggH_TauTau_HTauTau_2022postEE_step2",
  #]
  #process_list = ["VBF_old", "VBF_new"]
  #direct_input_list = [
  #    home_dir + "/V12_PFRel_postEE_nominal/ditau/Signal/VBF_TauTau_private_HTauTau_2022postEE_step2",
  #    #home_dir + "/V12_PFRel_postEE_notriggermatching/ditau/Signal/VBFHToTauTau_private_HTauTau_2022postEE_step2",
  #    #home_dir + "/V12_PFRel_postEE_notriggermatching/ditau/Signal/VBF_UD_TauTau_HTauTau_2022postEE_step2",
  #    home_dir + "/V12_PFRel_postEE_nominal/ditau/Signal/VBF_TauTau_HTauTau_2022postEE_step2",
  #]

  for process, direct_input in zip(process_list, direct_input_list):
    if "ST" in input_process:
      tag = process.split("_")[-1]
      process = "_".join(process.split("_")[0:3])
      process = process.replace("antitop","Tbar")
      process = process.replace("top","T")
      process_list = [] if len(process_list) == 2 else process_list
      process_list.append(process + "_" + tag)
    #elif ("WJ" in input_process) and ("LO" in process):
    elif "WJ" in input_process:
      tag = process.split("_")[-1]
      #process = "_".join(process.split("_")[0:2])
      process = "WJetsInc" if "LO" in process else "WJetsIncNLO"
      process_list = [] if len(process_list) == 2 else process_list
      process_list.append(process + "_" + tag)
    elif "DY" in input_process:
      tag = process.split("_")[-1]
      #process = "_".join(process.split("_")[0:3])
      if "10to50" in process:
        process = "DY10to50" if "NLO" not in process else "DY10to50NLO"
      else:
        process = "DYInc" if "NLO" not in process else "DYIncNLO"
      process_list = [] if len(process_list) == 2 else process_list
      process_list.append(process + "_" + tag)
    elif "Run" in process:
      tag = process.split("_")[-1]
      process = "Data_" + "_".join(process.split("_")[0:2])
      process_list = [] if len(process_list) == 2 else process_list
      process_list.append(process + "_" + tag)
    else:
      process, tag = process.split("_") # grabs base name
    data_tag = False if "Run" not in process else True
    branches     = set_branches(final_state_mode, DeepTau_version, process)

    new_process_dictionary = load_process_from_file(process, using_directory, file_map, log_file,
                                              branches, good_events, final_state_mode,
                                              data=data_tag, testing=testing, direct_input=direct_input)
    if new_process_dictionary == None: continue # skip process if empty
    cut_events = apply_HTT_FS_cuts_to_process(process, new_process_dictionary, log_file, final_state_mode, jet_mode,
                                              DeepTau_version=DeepTau_version)
    if cut_events == None: continue

    combined_process_dictionary = append_to_combined_processes(process + "_" + tag, cut_events, vars_to_plot, 
                                                               combined_process_dictionary)

  # end loop, sort big dictionary into three smaller ones
  data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

  if "Data" in process:
    set_dictionary = data_dictionary
  elif ("VBF" not in process) and ("ggH" not in process):
    set_dictionary = background_dictionary
  else:
    set_dictionary = signal_dictionary
  old_dict = {}
  new_dict = {}
  process_org = process_list[0]
  process_alt = process_list[1]
  old_dict[process] = set_dictionary[process_org]
  new_dict[process] = set_dictionary[process_alt]

  log_print("Processing finished!", log_file, time=True)

  vars_to_plot = [var for var in vars_to_plot if "flav" not in var]
  # ditau
  #vars_to_plot = ["HTT_m_vis", "nCleanJetGT30", "PuppiMET_pt", "PuppiMET_phi", "Generator_weight",
  #                "FS_t1_pt", "FS_t1_eta", "FS_t1_phi", "FS_t1_mass", "FS_t1_DM",
  #                "FS_t2_pt", "FS_t2_eta", "FS_t2_phi", "FS_t2_mass", "FS_t2_DM",
  #               ]
  # mutau
  vars_to_plot = ["HTT_m_vis", "nCleanJetGT30", "PuppiMET_pt", "PuppiMET_phi", "Generator_weight",
                  "FS_mu_pt", "FS_mu_eta", "FS_mu_phi", "FS_mu_iso",
                  "FS_tau_pt", "FS_tau_eta", "FS_tau_phi", "FS_tau_mass", "FS_tau_DM"
                 ]
  if "Data" in process: vars_to_plot.remove("Generator_weight")
  # remove mvis, replace with mvis_HTT and mvis_SF
  vars_to_plot.remove("HTT_m_vis")
  vars_to_plot.append("HTT_m_vis-KSUbinning")
  vars_to_plot.append("HTT_m_vis-SFbinning")
  text = ""
  for var in vars_to_plot:
    if DEBUG: log_print(f"Plotting {var}", log_file, time=True)

    if var == "Generator_weight":
      base_var_nparray = old_dict[process][var]
      alt_var_nparray = new_dict[process][var]
      var_min     = np.min([np.min(base_var_nparray), np.min(alt_var_nparray)])
      var_max     = np.max([np.max(base_var_nparray), np.max(alt_var_nparray)])
      buffer = 10
      xbins = np.linspace(var_min-buffer, var_max+buffer, 100+1)
    else:
      xbins = make_bins(var, final_state_mode)
    hist_ax, hist_ratio = setup_ratio_plot()

    temp_var = var # hack to plot the same variable twice with two different binnings
    if "HTT_m_vis" in var: var = "HTT_m_vis"
    h_signals_old = get_binned_signals(final_state_mode, testing, old_dict, var, xbins, lumi) 
    h_signals_new = get_binned_signals(final_state_mode, testing, new_dict, var, xbins, lumi) 
    var = temp_var

    # plot everything :)
    plot_signal( hist_ax, xbins, h_signals_old,     lumi, custom=True, color="red",  label=f"{process_org}")
    plot_signal( hist_ax, xbins, h_signals_new,     lumi, custom=True, color="blue", label=f"{process_alt}")

    make_ratio_plot(hist_ratio, xbins, 
                    h_signals_old[process]["BinnedEvents"], "Data", np.ones(np.shape(h_signals_old)),
                    h_signals_new[process]["BinnedEvents"], "Data", np.ones(np.shape(h_signals_new)))

    # reversed dictionary search for era name based on lumi 
    title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
    title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"
    
    spruce_up_plot(hist_ax, hist_ratio, label_dictionary[var], title, final_state_mode, jet_mode, set_x_log=False)
    spruce_up_legend(hist_ax, final_state_mode)

    plt.savefig(plot_dir + "/" + str(var) + ".png")

  print(f"Plots are in {plot_dir}")
  with open("file_comparisons/comparison_file_directories_postEE_mutau.txt", "a") as myfile:
    myfile.write(plot_dir+'\n')
  
  if hide_plots: pass
  else: plt.show()


