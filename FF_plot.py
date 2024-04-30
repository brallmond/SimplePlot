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
from file_map_dictionary   import testing_file_map, full_file_map, testing_dimuon_file_map, dimuon_file_map
from file_map_dictionary   import pre2022_file_map
from file_functions        import load_process_from_file, append_to_combined_processes, sort_combined_processes

from luminosity_dictionary import luminosities_with_normtag as luminosities

from cut_and_study_functions import set_branches, set_vars_to_plot, set_good_events
from cut_and_study_functions import apply_HTT_FS_cuts_to_process, apply_AR_cut

from plotting_functions    import get_binned_data, get_binned_backgrounds, get_binned_signals
from plotting_functions    import setup_ratio_plot, make_ratio_plot, spruce_up_plot, spruce_up_legend
from plotting_functions    import plot_data, plot_MC, plot_signal, make_bins

from plotting_functions import get_midpoints, setup_single_plot, spruce_up_single_plot

from calculate_functions   import calculate_signal_background_ratio, yields_for_CSV
from utility_functions     import time_print, make_directory, print_setup_info, log_print

from cut_and_study_functions import append_lepton_indices, apply_cut, apply_jet_cut, add_FF_weights
from cut_and_study_functions import load_and_store_NWEvents, customize_DY, append_flavor_indices, set_protected_branches
from cut_ditau_functions import make_ditau_AR_cut, make_ditau_SR_cut, make_ditau_cut, make_ditau_cut_FF
from cut_ditau_functions import make_ditau_AR_aiso_cut, make_ditau_SR_aiso_cut

from binning_dictionary import label_dictionary

def line(x, a, b):
    return a + x * b

if __name__ == "__main__":
  '''
  '''

  import argparse 
  parser = argparse.ArgumentParser(description='Make a standard Data-MC agreement plot.')
  # store_true : when the argument is supplied, store it's value as true
  # for 'testing' below, the default value is false if the argument is not specified
  parser.add_argument('--testing',     dest='testing',     default=False,       action='store_true')
  parser.add_argument('--hide_plots',  dest='hide_plots',  default=False,       action='store_true')
  parser.add_argument('--hide_yields', dest='hide_yields', default=False,       action='store_true')
  parser.add_argument('--final_state', dest='final_state', default="mutau",     action='store')
  parser.add_argument('--plot_dir',    dest='plot_dir',    default="plots",     action='store')
  parser.add_argument('--lumi',        dest='lumi',        default="2022 EFG",  action='store')
  parser.add_argument('--jet_mode',    dest='jet_mode',    default="Inclusive", action='store')
  parser.add_argument('--DeepTau',     dest='DeepTau_version', default="2p5",   action='store')
  parser.add_argument('--use_DY_NLO',  dest='use_DY_NLO',  default=True,        action='store')

  args = parser.parse_args() 
  testing     = args.testing     # False by default, do full dataset unless otherwise specified
  hide_plots  = args.hide_plots  # False by default, show plots unless otherwise specified
  hide_yields = args.hide_yields # False by default, show yields unless otherwise specified
  use_DY_NLO  = args.use_DY_NLO  # True  by default, use LO DY if False
  lumi = luminosities["2022 G"] if testing else luminosities[args.lumi]
  DeepTau_version = args.DeepTau_version # default is 2p5 [possible values 2p1 and 2p5]

  # final_state_mode affects many things automatically, including good_events, datasets, plotting vars, etc.
  final_state_mode = args.final_state # default mutau [possible values ditau, mutau, etau, dimuon]
  jet_mode         = args.jet_mode # default Inclusive [possible values 0j, 1j, 2j, GTE2j]

  #lxplus_redirector = "root://cms-xrd-global.cern.ch//"
  eos_user_dir    = "/eos/user/b/ballmond/NanoTauAnalysis/analysis/HTauTau_2022_fromstep1_skimmed/" + final_state_mode
  # there's no place like home :)
  home_dir        = "/Users/ballmond/LocalDesktop/HiggsTauTau/Run3PreEEFSSplitSamples/" + final_state_mode
  era_modifier_2022 = "preEE" if (("C" in args.lumi) or ("D" in args.lumi)) else "postEE"
  home_dir        = "/Users/ballmond/LocalDesktop/HiggsTauTau/V12_PFRel_"+era_modifier_2022+"_Run3FSSplitSamples/" + final_state_mode
  using_directory = home_dir
 
  good_events  = set_good_events(final_state_mode)
  branches     = set_branches(final_state_mode, DeepTau_version)
  vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)
  plot_dir_name = "FS_plots_testing/" if testing==True else "FS_plots/"
  plot_dir = make_directory(plot_dir_name+args.plot_dir, final_state_mode+"_"+jet_mode, testing=testing)

  log_file = open('outputfile.log', 'w')
  # show info to user
  print_setup_info(final_state_mode, lumi, jet_mode, testing, DeepTau_version,
                   using_directory, plot_dir,
                   good_events, branches, vars_to_plot, log_file)

  file_map = testing_file_map if testing else full_file_map
  if (use_DY_NLO == True): 
    file_map.pop("DYInc")
    file_map.pop("WJetsInc")
  else: 
    file_map.pop("DYIncNLO")
    file_map.pop("WJetsIncNLO")

  common_selection = "(METfilters) & (LeptonVeto==0) & (JetMapVeto_EE_30GeV) & (JetMapVeto_HotCold_30GeV)"
  ditau_selection  = common_selection + " & (abs(HTT_pdgId)==15*15) & (Trigger_ditau)"
  final_state_selection = ditau_selection
  OS_region        = final_state_selection + " & (HTT_pdgId < 0)"
  SS_region        = final_state_selection + " & (HTT_pdgId > 0)"

  # SR AR are always OS
  # DR are always SS
  
  # you can just do the whole thing in aiso and 
  # say, well, it's probably fine to do that in SR too

  dataset_dictionary = {"ditau" : "DataTau", "mutau" : "DataMuon", "etau" : "DataElectron", "emu" : "DataEMu"}
  reject_dataset_dictionary = {"ditau" : ["DataMuon", "DataElectron", "DataEMu"],
                               "mutau" : ["DataTau",  "DataElectron", "DataEMu"],
                               "etau"  : ["DataMuon", "DataTau",      "DataEMu"],
                               "emu"   : ["DataMuon", "DataElectron", "DataTau"]}

  dataset = dataset_dictionary[final_state_mode]
  reject_datasets = reject_dataset_dictionary[final_state_mode]

  region_dict = { "OS" :  OS_region, "SS" : SS_region}


  #"AR",   OS_region, make_ditau_AR_cut ("pass_AR_cuts")
  #"SR",   OS_region, make_ditau_SR_cut ("pass_SR_cuts") # not plotted with this script
  #"DRar", SS_region, make_ditau_AR_cut ("pass_AR_cuts")
  #"DRsr", SS_region, make_ditau_SR_cut ("pass_SR_cuts")

  #"AR-aiso", OS_region, make_ditau_AR_aiso_cut ("pass_AR_aiso_cuts")
  #"SR-aiso", OS_region, make_ditau_SR_aiso_cut ("pass_SR_aiso_cuts")
  #"DRar-aiso", SS_region, make_ditau_AR_aiso_cut ("pass_AR_aiso_cuts")
  #"DRsr-aiso", SS_region, make_ditau_SR_aiso_cut ("pass_SR_aiso_cuts")

  store_region_data_dictionary = {}
  store_region_bkgd_dictionary = {}
  store_region_sgnl_dictionary = {}
  pseudo_SR = "DRsr" # need the data from here to compare to
  pseudo_AR = "AR" # need the events from here to make the QCD estimate
  for region in [pseudo_SR, pseudo_AR]:

    region_title = region
    vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)

    if ("DR" in region_title): sign_region = SS_region
    else: sign_region = OS_region

    print(region_title, sign_region)


    # make and apply cuts to any loaded events, store in new dictionaries for plotting
    combined_process_dictionary = {}

    for process in file_map: 

      gc.collect()
      if (process in reject_datasets): continue

      new_process_dictionary = load_process_from_file(process, using_directory, file_map, log_file,
                                              branches, sign_region, final_state_mode,
                                              data=("Data" in process), testing=testing)
      event_dictionary = new_process_dictionary[process]["info"]
      if (event_dictionary == None): continue

      protected_branches = ["None"]
      event_dictionary = append_lepton_indices(event_dictionary)
      if ("Data" not in process):
        load_and_store_NWEvents(process, event_dictionary)
        if ("DY" in process): customize_DY(process, final_state_mode)
        event_dictionary = append_flavor_indices(event_dictionary, final_state_mode, keep_fakes=True)


      if (region_title == "DRsr"):
        event_dictionary   = make_ditau_SR_cut(event_dictionary, DeepTau_version)
        event_dictionary   = apply_cut(event_dictionary, "pass_SR_cuts", protected_branches)

      if (region_title == "AR") or (region_title == "DRar"):
        event_dictionary   = make_ditau_AR_cut(event_dictionary, DeepTau_version)
        event_dictionary   = apply_cut(event_dictionary, "pass_AR_cuts", protected_branches)

      if (region_title == "SR-aiso") or (region_title == "DRsr-aiso"):
        event_dictionary   = make_ditau_SR_aiso_cut(event_dictionary, DeepTau_version)
        event_dictionary   = apply_cut(event_dictionary, "pass_SR_aiso_cuts", protected_branches)

      if (region_title == "AR-aiso") or (region_title == "DRar-aiso"): 
        event_dictionary   = make_ditau_AR_aiso_cut(event_dictionary, DeepTau_version)
        event_dictionary   = apply_cut(event_dictionary, "pass_AR_aiso_cuts", protected_branches)

      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      event_dictionary   = apply_jet_cut(event_dictionary, jet_mode)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      event_dictionary   = make_ditau_cut_FF(event_dictionary, DeepTau_version) # no DeepTau or Charge requirements
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue
      protected_branches = set_protected_branches(final_state_mode=final_state_mode, jet_mode="none")
      event_dictionary   = apply_cut(event_dictionary, "pass_cuts", protected_branches)
      if (event_dictionary==None or len(event_dictionary["run"])==0): continue

      if ("Data" in process): event_dictionary = add_FF_weights(event_dictionary, final_state_mode, 
                                                   jet_mode, DeepTau_version, determining_FF=False,
                                                   # [FF int, slope, OS SS int, slope]
                                                   bypass = [0.278, -0.000577, 1, 0])
                                                   #bypass = [0.01, 1, 1, 1])

      # TODO : extendable to jet cuts (something I've meant to do for some time)
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

    # after loop, sort big dictionary into three smaller ones
    data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(combined_process_dictionary)

    # store dictionaries
    store_region_data_dictionary[region_title] = data_dictionary
    store_region_bkgd_dictionary[region_title] = background_dictionary
    store_region_sgnl_dictionary[region_title] = signal_dictionary


  pseudo_SR_data = store_region_data_dictionary[pseudo_SR] # this has FF weights
  pseudo_SR_bkgd = store_region_bkgd_dictionary[pseudo_SR]
  pseudo_SR_sgnl = store_region_sgnl_dictionary[pseudo_SR]
  pseudo_AR_data = store_region_data_dictionary[pseudo_AR] # this also has FF weights
  pseudo_AR_bkgd = store_region_bkgd_dictionary[pseudo_AR]
  pseudo_AR_sgnl = store_region_sgnl_dictionary[pseudo_AR]


  QCD_dictionary = {}
  QCD_dictionary["QCD"] = {}
  QCD_dictionary["QCD"]["PlotEvents"] = {}
  QCD_dictionary["QCD"]["FF_weight"]  = pseudo_AR_data["DataTau"]["FF_weight"]
  for var in vars_to_plot:
    if ("flav" in var): continue
    QCD_dictionary["QCD"]["PlotEvents"][var] = pseudo_AR_data["DataTau"]["PlotEvents"][var]

  log_print("Processing finished!", log_file, time=True)
  ## end processing loop, begin plotting

  vars_to_plot = [var for var in vars_to_plot if "flav" not in var]
  # remove mvis, replace with mvis_HTT and mvis_SF
  vars_to_plot.remove("HTT_m_vis")
  vars_to_plot.append("HTT_m_vis-KSUbinning")
  vars_to_plot = ["HTT_m_vis-KSUbinning", 
                  "FS_t1_pt", "FS_t1_eta", "FS_t1_phi",
                  "FS_t2_pt", "FS_t2_eta", "FS_t2_phi", "PuppiMET_pt"]
  # and add back variables unique to the jet mode
  if (jet_mode == "1j") or (jet_mode == "GTE2j"): vars_to_plot.append("CleanJetGT30_pt_1")
  if (jet_mode == "GTE2j"): vars_to_plot.append("CleanJetGT30_pt_2")
  for var in vars_to_plot:
    log_print(f"Plotting {var}", log_file, time=True)

    xbins = make_bins(var, final_state_mode)

    ax_hist, ax_ratio = setup_ratio_plot()

    temp_var = var
    if "HTT_m_vis" in var: var = "HTT_m_vis"
    h_pseudo_SR_data = get_binned_data(pseudo_SR_data, var, xbins, lumi)
    h_pseudo_AR_data = get_binned_data(pseudo_AR_data, var, xbins, lumi)
    h_pseudo_SR_backgrounds, h_pseudo_SR_summed_backgrounds = get_binned_backgrounds(pseudo_SR_bkgd, var, xbins, lumi, jet_mode)
    h_pseudo_AR_backgrounds, h_pseudo_AR_summed_backgrounds = get_binned_backgrounds(pseudo_AR_bkgd, var, xbins, lumi, jet_mode)
    #h_pseudo_SR_signals = get_binned_signals(pseudo_SR_sgnl, var, xbins, lumi, jet_mode) 
    #h_pseudo_AR_signals = get_binned_signals(pseudo_AR_sgnl, var, xbins, lumi, jet_mode) 
    h_QCD, h_QCD_for_ratio = get_binned_backgrounds(QCD_dictionary, var, xbins, 1, jet_mode)
    var = temp_var

    h_pseudo_SR_data_m_MC = h_pseudo_SR_data - h_pseudo_SR_summed_backgrounds
    #print(h_pseudo_SR_data_m_MC)
    #print(h_pseudo_SR_data)
    #print(h_pseudo_SR_summed_backgrounds)
    h_pseudo_AR_weight = (h_pseudo_AR_data - h_pseudo_AR_summed_backgrounds) / h_pseudo_AR_data
    #print(h_pseudo_AR_weight)

    # reversed dictionary search for era name based on lumi 
    title_era = [key for key in luminosities.items() if key[1] == lumi][0][0]
    title = f"{title_era}, {lumi:.2f}" + r"$fb^{-1}$"


    # plot everything :)
    plot_data(ax_hist, xbins, h_pseudo_SR_data_m_MC, lumi, color="black", label=f"{pseudo_SR} : Data-MC")
    plot_MC(ax_hist, xbins, h_QCD, lumi) # weight = h_pseudo_AR_weight

    make_ratio_plot(ax_ratio, xbins, h_pseudo_SR_data_m_MC, h_QCD_for_ratio)

    spruce_up_plot(ax_hist, ax_ratio, label_dictionary[var], title, final_state_mode, jet_mode)
    spruce_up_legend(ax_hist, final_state_mode, h_pseudo_SR_data_m_MC)

    plt.savefig(plot_dir + "/" + str(var) + "_" + region + ".png")


  if hide_plots: pass
  else: plt.show()
  log_print(f"Finished plots for FF region!", log_file, time=True)

