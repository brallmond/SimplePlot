# Authored by Braden Allmond, Sep 11, 2023

# libraries
import numpy as np
import sys
import matplotlib.pyplot as plt
import gc

# explicitly import used functions from user files, grouped roughly by call order and relatedness
from file_map_dictionary   import testing_file_map, full_file_map, testing_dimuon_file_map, dimuon_file_map
from file_map_dictionary   import pre2022_file_map

from file_functions        import load_process_from_file, append_to_combined_processes, sort_combined_processes

from luminosity_dictionary import luminosities_with_normtag as luminosities

from cut_and_study_functions import set_branches, set_vars_to_plot # TODO set good events should be here
from cut_and_study_functions import apply_cuts_to_process, apply_AR_cut

from plotting_functions    import get_binned_data, get_binned_backgrounds, get_binned_signals
from plotting_functions    import setup_ratio_plot, make_ratio_plot, spruce_up_plot, spruce_up_legend
from plotting_functions    import plot_data, plot_MC, plot_signal

from get_and_set_functions import set_good_events, make_bins

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info

def match_objects_to_trigger_bit():
  '''
  Current work in progress
  Using the final state object kinematics, check if the filter bit of a used trigger is matched
  '''
  #FS ditau - two taus, match to ditau
  #FS mutau - one tau, one muon
  # - if not cross-trig, match muon to filter
  # - if cross-trig, use cross-trig filters to match both
  match = False
  # step 1 check fired triggers
  # step 2 ensure correct trigger bit is fired
  # step 3 calculate dR and compare with 0.5
  dR_trig_offline = calculate_dR(trig_eta, trig_phi, off_eta, off_phi)

if __name__ == "__main__":
  '''
  Dimuon plotting
  '''

  import argparse 
  parser = argparse.ArgumentParser(description='Make a standard Data-MC agreement plot.')
  # store_true : when the argument is supplied, store it's value as true
  # for 'testing' below, the default value is false if the argument is not specified
  parser.add_argument('--testing',     dest='testing',     default=False,       action='store_true')
  parser.add_argument('--hide_plots',  dest='hide_plots',  default=False,       action='store_true')
  parser.add_argument('--hide_yields', dest='hide_yields', default=False,       action='store_true')
  parser.add_argument('--final_state', dest='final_state', default="dimuon",    action='store')
  parser.add_argument('--plot_dir',    dest='plot_dir',    default="plots",     action='store')
  parser.add_argument('--lumi',        dest='lumi',        default="2022 F&G",  action='store')
  parser.add_argument('--jet_mode',    dest='jet_mode',    default="Inclusive", action='store')
  parser.add_argument('--DeepTau',     dest='DeepTau_version', default="2p5",   action='store')

  args = parser.parse_args() 
  testing     = args.testing     # False by default, do full dataset unless otherwise specified
  hide_plots  = args.hide_plots  # False by default, show plots unless otherwise specified
  hide_yields = args.hide_yields # False by default, show yields unless otherwise specified
  lumi = luminosities["2022 G"] if testing else luminosities[args.lumi]
  DeepTau_version = args.DeepTau_version # default is 2p5 [possible values 2p1 and 2p5]

  # final_state_mode affects many things automatically, including good_events, datasets, plotting vars, etc.
  final_state_mode = args.final_state # default mutau [possible values ditau, mutau, etau, dimuon]
  jet_mode         = args.jet_mode # default Inclusive [possible values 0j, 1j, 2j, GTE2j]

  #using_directory = "/Volumes/IDrive/HTauTau_Data/2022postEE/" # full dataset
  using_directory = "/Volumes/IDrive/HTauTau_Data/skims/dimuon_2022postEE/"
 
  good_events  = set_good_events(final_state_mode)
  branches     = set_branches(final_state_mode, DeepTau_version)
  vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)
  plot_dir = make_directory("FS_plots/"+args.plot_dir, final_state_mode + "_" + jet_mode, testing=testing)

  # show info to user
  print_setup_info(final_state_mode, lumi, jet_mode, testing, DeepTau_version,
                   using_directory, plot_dir,
                   good_events, branches, vars_to_plot)

  file_map = testing_dimuon_file_map if testing else dimuon_file_map

  # make and apply cuts to any loaded events, store in new dictionaries for plotting
  combined_process_dictionary = {}
  for process in file_map: 

    gc.collect()

    if "Data" in process: continue # skip data files

    new_process_dictionary = load_process_from_file(process, using_directory, file_map,
                                              branches, good_events, final_state_mode,
                                              data=("Data" in process), testing=testing)
    if new_process_dictionary == None: continue # skip process if empty

    cut_events = apply_cuts_to_process(process, new_process_dictionary, final_state_mode, jet_mode,
                                       DeepTau_version=DeepTau_version)
    if cut_events == None: continue

    combined_process_dictionary = append_to_combined_processes(process, cut_events, vars_to_plot, 
                                                               combined_process_dictionary)

  # after loop, sort big dictionary into three smaller ones
  data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

  # no accumulation until plotting
  # man someone should really write these things down
  time_print("Adding SFs!")

  from correctionlib import _core
  fname = "../2022EE_schemaV2.json"
  evaluator = _core.CorrectionSet.from_file(fname)

  for DY in ["DYInc1", "DYInc2"]:
    m1_pt_arr  = background_dictionary[DY]["PlotEvents"]["FS_m1_pt"] 
    m1_eta_arr = background_dictionary[DY]["PlotEvents"]["FS_m1_eta"] 
    m2_pt_arr  = background_dictionary[DY]["PlotEvents"]["FS_m2_pt"] 
    m2_eta_arr = background_dictionary[DY]["PlotEvents"]["FS_m2_eta"] 
  
    sf_type = "nominal"
    to_use = (range(len(m1_pt_arr)), m1_pt_arr, m1_eta_arr, m2_pt_arr, m2_eta_arr)
    dimuon_SF_weights = []
    for i, m1_pt, m1_eta, m2_pt, m2_eta in zip(*to_use): 
      weight = 1
      if (m1_pt < 15.0): continue
      if (m2_pt < 15.0): continue
      if (abs(m1_eta) > 2.4): continue
      if (abs(m2_eta) > 2.4): continue
      m1_pt = 199.9 if m1_pt >= 200 else m1_pt
      m2_pt = 199.9 if m2_pt >= 200 else m2_pt
      m1_pt, m1_eta = np.float64(m1_pt), np.float64(m1_eta) # wild hack, float32s just don't cut it
      m2_pt, m2_eta = np.float64(m2_pt), np.float64(m2_eta) 
      weight *= evaluator["NUM_MediumID_DEN_TrackerMuons"].evaluate(abs(m1_eta), m1_pt, sf_type)
      #weight *= evaluator["NUM_TightPFIso_DEN_MediumID"].evaluate(abs(m1_eta), m1_pt, sf_type)
      weight *= evaluator["NUM_TightMiniIso_DEN_MediumID"].evaluate(abs(m1_eta), m1_pt, sf_type)
      weight *= evaluator["NUM_MediumID_DEN_TrackerMuons"].evaluate(abs(m2_eta), m2_pt, sf_type)
      #weight *= evaluator["NUM_TightPFIso_DEN_MediumID"].evaluate(abs(m2_eta), m2_pt, sf_type)
      weight *= evaluator["NUM_TightMiniIso_DEN_MediumID"].evaluate(abs(m2_eta), m2_pt, sf_type)
      dimuon_SF_weights.append(weight)
      # need to redo with the loose iso
  
    background_dictionary[DY]["SF_weight"] = np.array(dimuon_SF_weights)

  DY_dict_1 = {"DYInc" : background_dictionary["DYInc1"]}
  DY_dict_2 = {"DYInc" : background_dictionary["DYInc2"]}

  time_print("Processing finished!")
  ## end processing loop, begin plotting

  for var in vars_to_plot:
    time_print(f"Plotting {var}")

    xbins = make_bins(var)
    hist_ax, hist_ratio = setup_ratio_plot()

    h_DY_1, _ = get_binned_backgrounds(DY_dict_1, var, xbins, lumi, jet_mode)
    h_DY_2, _ = get_binned_backgrounds(DY_dict_2, var, xbins, lumi, jet_mode)

    # plot everything :)
    plot_MC(hist_ax, xbins, h_DY_1, lumi, custom=True, color="red", label="DYInc1", fill=False)
    plot_MC(hist_ax, xbins, h_DY_2, lumi, custom=True, color="blue", label="DYInc2", fill=False)

    # reversed dictionary search for era name based on lumi 
    title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
    title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"
    spruce_up_plot(hist_ax, hist_ratio, var, title, final_state_mode, jet_mode)
    spruce_up_legend(hist_ax, final_state_mode="skip_dimuon_handling")

    plt.savefig(plot_dir + "/" + str(var) + ".png")

  if hide_plots: pass
  else: plt.show()

