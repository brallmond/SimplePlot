import ROOT
import uproot
import numpy as np
from plotting_functions import make_bins, get_binned_data, get_binned_backgrounds, get_binned_signals, get_summed_backgrounds
from file_functions     import sort_combined_processes
from FF_functions       import set_JetFakes_process
import copy

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


def apply_single_cut(input_dict, cut):
  if cut=="1": return input_dict
  output_dict = {}
  vars_to_cut_on = []
  for process in input_dict:
    output_dict[process] = {}

    # Get Variables to be cutted on
    if vars_to_cut_on==[]:
      for var in input_dict[process]["PlotEvents"]:
        if var in cut: vars_to_cut_on.append(var)
      if vars_to_cut_on==[]:
        print(f'Warning! Cut "{cut}" could not be applied, variables not found!')
        print('Existing variables:',[var for var in input_dict[process]["PlotEvents"]])
        return input_dict
    else:
      assert all([var in input_dict[process]["PlotEvents"] for var in vars_to_cut_on])

    # Initialize lists
    for key in input_dict[process]:
      if isinstance(input_dict[process][key], dict):
        output_dict[process][key] = {}
        for branch in input_dict[process][key]:
          output_dict[process][key][branch] = []
      else:
        output_dict[process][key] = []

    # Copy only events to new lists which pass cuts
    for i in range(input_dict[process]["Cuts"]["pass_cuts"].size):
      for var in vars_to_cut_on:
        exec(f'{var} = {input_dict[process]["PlotEvents"][var][i]}')
      if not eval(cut): continue
      for key in input_dict[process]:
        if isinstance(input_dict[process][key], dict):
          for branch in input_dict[process][key]:
            output_dict[process][key][branch].append(input_dict[process][key][branch][i])
        else:
          output_dict[process][key].append(input_dict[process][key][i])

    # Convert lists to numpy arrays
    for key in input_dict[process]:
      if isinstance(input_dict[process][key], dict):
        for branch in input_dict[process][key]:
          output_dict[process][key][branch] = np.array(output_dict[process][key][branch])
      else:
        output_dict[process][key] = np.array(output_dict[process][key])
  return output_dict

def save_fitter_shapes(plot_dir, era, final_state_mode, vars_to_plot, combined_process_dictionary, combined_process_dictionaryFakes, fakesLabel, testing, lumi):
  # PUT SETTINGS HERE: disciminating_variables and categories
  # Discriminating variables are required to have been plotted before
  MC_families = ["NLODYGen", "NLODYLep", "NLODYJet", "ST", "TT", "VV", "WJ", "HWW"]
  disciminating_variables = {"FastMTT_mass" : "mtt",
                             "HTT_m_vis"    : "mttvis"}

  # should have reco/gen tau pt!
  lowTauPt  = "(FS_tau_pt >= 40.) and (FS_tau_pt < 50)"
  midTauPt  = "(FS_tau_pt >= 50.) and (FS_tau_pt < 70)"
  highTauPt = "(FS_tau_pt >= 70.)"
  tauPts = [lowTauPt, midTauPt, highTauPt]
  namesTauPts = ["lowTauPt", "midTauPt", "highTauPt"]

  #"Gen_pT_l2"

  # define reco and gen strings and names to build categories later
  # nJet
  # should be tight instead!
  zeroJet, oneJet, twoJet, threeJet = "nCleanJetGT30==0", "nCleanJetGT30==1", "nCleanJetGT30==2", "nCleanJetGT30==3"
  #zeroJet, oneJet, twoJet, threeJet = "nTightCleanJet==0", "nTightCleanJet==1", "nTightCleanJet==2", "nTightCleanJet==3"
  fourOrMoreJet = "nCleanJetGT30>=4"
  #fourOrMoreJet = "nTightCleanJet>=4"
  nJets = [zeroJet, oneJet, twoJet, threeJet, fourOrMoreJet]
  namesJets = ["0j", "1j", "2j", "3j", "GT4j"]

  # should be tight instead!
  zeroGenJet, oneGenJet, twoGenJet, threeGenJet = "Gen_nCleanJet==0", "Gen_nCleanJet==1", "Gen_nCleanJet==2", "Gen_nCleanJet==3"
  #zeroGenJet, oneGenJet, twoGenJet, threeGenJet = "Gen_nCleanJet==0", "Gen_nCleanJet==1", "Gen_nCleanJet==2", "Gen_nCleanJet==3"
  fourOrMoreGenJet = "Gen_nCleanJet>=4"
  #fourOrMoreJet = "nTightCleanJet>=4"
  nGenJets = [zeroJet, oneJet, twoJet, threeJet, fourOrMoreJet]
  namesGenJets = ["Gen_0j", "Gen_1j", "Gen_2j", "Gen_3j", "Gen_GT4j"]

  # HpT
  HpT_0_45, HpT_45_80      = "(HTT_H_pt > 0) and (HTT_H_pt <= 45)", "(HTT_H_pt > 45) and (HTT_H_pt <= 80)"
  HpT_80_120, HpT_120_200  = "(HTT_H_pt > 80) and (HTT_H_pt <= 120)", "(HTT_H_pt > 120) and (HTT_H_pt <= 200)"
  HpT_200_350, HpT_350_450 = "(HTT_H_pt > 200) and (HTT_H_pt <= 350)", "(HTT_H_pt > 350) and (HTT_H_pt <= 450)"

  HpT_0_45, HpT_45_80      = "(HTT_H_pt > 0)*(HTT_H_pt <= 45)", "(HTT_H_pt > 45)*(HTT_H_pt <= 80)"
  HpT_80_120, HpT_120_200  = "(HTT_H_pt > 80)*(HTT_H_pt <= 120)", "(HTT_H_pt > 120)*(HTT_H_pt <= 200)"
  HpT_200_350, HpT_350_450 = "(HTT_H_pt > 200)*(HTT_H_pt <= 350)", "(HTT_H_pt > 350)*(HTT_H_pt <= 450)"
  HpT_450_inf              = "(HTT_H_pt > 450)"
  HpTs      = [HpT_0_45, HpT_45_80, HpT_80_120, HpT_120_200, HpT_200_350, HpT_350_450, HpT_450_inf]
  namesHpTs = ["HpT_0_45", "HpT_45_80", "HpT_80_120", "HpT_120_200", "HpT_200_350", "HpT_350_450", "HpT_450_inf"]

  GenHpT_0_45, GenHpT_45_80      = "(Gen_H_pT > 0) and (Gen_H_pT <= 45)", "(Gen_H_pT > 45) and (Gen_H_pT <= 80)"
  GenHpT_80_120, GenHpT_120_200  = "(Gen_H_pT > 80) and (Gen_H_pT <= 120)", "(Gen_H_pT > 120) and (Gen_H_pT <= 200)"
  GenHpT_200_350, GenHpT_350_450 = "(Gen_H_pT > 200) and (Gen_H_pT <= 350)", "(Gen_H_pT > 350) and (Gen_H_pT <= 450)"
  GenHpT_450_inf                  = "(Gen_H_pT > 450)"
  GenHpTs      = [GenHpT_0_45, GenHpT_45_80, GenHpT_80_120, GenHpT_120_200, GenHpT_200_350, GenHpT_350_450, GenHpT_450_inf]
  namesGenHpTs = ["GenHpT_0_45", "GenHpT_45_80", "GenHpT_80_120", "GenHpT_120_200", "GenHpT_200_350", "GenHpT_350_450", "GenHpT_450_inf"]

  # leading jet pT
  jetPt_0_30    = "(nTightCleanJet == 0) or (CleanJetGT30_pt_1 <= 30)"
  jetPt_30_60   = "(nTightCleanJet >= 1) and (CleanJetGT30_pt[0] > 30) and (CleanJetGT30_pt[0] <= 60)"
  jetPt_60_120  = "(nTightCleanJet >= 1) and (CleanJetGT30_pt[0] > 60) and (CleanJetGT30_pt[0] <= 120)"
  jetPt_120_200 = "(nTightCleanJet >= 1) and (CleanJetGT30_pt[0] > 120) and (CleanJetGT30_pt[0] <= 200)"
  jetPt_200_350 = "(nTightCleanJet >= 1) and (CleanJetGT30_pt[0] > 200) and (CleanJetGT30_pt[0] <= 350)"
  jetPt_350_inf = "(nTightCleanJet >= 1) and (CleanJetGT30_pt[0] >= 350)"
  jetPts        = [jetPt_0_30, jetPt_30_60, jetPt_60_120, jetPt_120_200, jetPt_200_350, jetPt_350_inf] 
  namesJetPts   = ["j1pT_0_30", "j1pT_30_60", "j1pT_60_120", "j1pT_120_200", "j1pT_200_350", "j1pT_350_inf"]

  GenJetPt_0_30    = "(Gen_nCleanJet == 0) or (Gen_pT_j1 <= 30)"
  GenJetPt_30_60   = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 30) and (Gen_pT_j1 <= 60)"
  GenJetPt_60_120  = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 60) and (Gen_pT_j1 <= 120)"
  GenJetPt_120_200 = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 120) and (Gen_pT_j1 <= 200)"
  GenJetPt_200_350 = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 200) and (Gen_pT_j1 <= 350)"
  GenJetPt_350_inf = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 >= 350)"
  GenJetPts        = [GenJetPt_0_30, GenJetPt_30_60, GenJetPt_60_120, GenJetPt_120_200, GenJetPt_200_350, GenJetPt_350_inf] 
  namesGenJetPts   = ["Genj1pt_0_30", "Genj1pt_30_60", "Genj1pt_60_120", "Genj1pt_120_200", "Genj1pt_200_350", "Genj1pt_350_inf"]

  categories = {"incl"      : "1",
                "lowTauPt"  : lowTauPt,
                "midTauPt"  : midTauPt,
                "highTauPt" : highTauPt,
                #"zerojet" : "nCleanJetGT30==0",
                #"onejet"  : "nCleanJetGT30==1",
                #"twojet"  : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets<=350)",
                #"vbfhigh" : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets>350) and (HTT_H_pt>200)",
                #"vbflow"  : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets>350) and (HTT_H_pt<=200)"
               }


  # some categories are only defined for signal processes (Gen info only stored for Signal...)
  # nonfid signal is treated as a background in the analysis...
  # technically, the nonfid should be indicated in the process name
  #signal_categories = {
  #              "fid_inc" : "(Gen_pT_l1 >= 40) and (Gen_pT_l2 >= 25)",
  #              "fid_low_tau_pt" : "(Gen_pT_l2 >= 25) and (Gen_pT_l2 < 50)",
  #              "fid_med_tau_pt" : "(Gen_pT_l2 >= 50) and (Gen_pT_l2 < 70)",
  #              "fid_high_tau_pt" : "(Gen_pT_l2 >= 70)",
  #              "nonfid_inc" : "!((Gen_pT_l1 >= 40) and (Gen_pT_l2 >= 25))",
  #              "nonfid_low_tau_pt" : "(HTT_Lep_pt >= 25) and (HTT_Lep_pt < 50) and !((Gen_pT_l2 >= 25) and (Gen_pT_l2 < 50)",
  #              "nonfid_med_tau_pt" : "(HTT_Lep_pt >= 50) and (HTT_Lep_pt < 70) and !((Gen_pT_l2 >= 50) and (Gen_pT_l2 < 70)",
  #              "nonfid_high_tau_pt" : "(HTT_Lep_pt > 70) and !(Gen_pT_l2 < 70)",
  #              }

  # copy of categories for MC
  #signal_categories = copy.deepcopy(categories)

  # adding low, mid, high categories split by bins of nTightJet, HpT, and j1pT, both Reco and Gen
  for tauName, tauCategory in zip(namesTauPts, tauPts):
    # nJet
    #for jetName, jetCategory in zip(namesJets, nJets):
    #  categories["_".join((tauName, jetName))] = " and ".join((tauCategory, jetCategory))
    #for jetNameGen, jetCategoryGen in zip(namesGenJets, nGenJets):
    #  signal_categories["_".join((tauName, jetNameGen))] = " and ".join((tauCategory, jetCategoryGen))
    # HpT
    for HpTName, HpTCategory in zip(namesHpTs, HpTs):
      #categories["_".join((tauName, HpTName))] = " and ".join((tauCategory, HpTCategory))
      categories["_".join((tauName, HpTName))] = "*".join((tauCategory, HpTCategory))
    #for GenHpTName, GenHpTCategory in zip(namesGenHpTs, GenHpTs):
    #  signal_categories["_".join((tauName, GenHpTName))] = " and ".join((tauCategory, GenHpTCategory))
    # leading jet pT
    ##for jetPtName, jetPtCategory in zip(namesJetPts, jetPts):
    ##  categories["_".join((tauName, jetPtName))] = " and ".join((tauCategory, jetPtCategory))
    #for GenJetPtName, GenJetPtCategory in zip(namesGenJetPts, GenJetPts):
    #  signal_categories["_".join((tauName, GenJetPtName))] = " and ".join((tauCategory, GenJetPtCategory))
 

  if   era=="2022 CD":  era = "2022_preEE"
  elif era=="2022 EFG": era = "2022_postEE"
  elif era=="2023 C":   era = "2023_preBPix"
  elif era=="2023 D":   era = "2023_postBPix"
  dicts = {}
  for category,cut in categories.items():
    dicts[category] = apply_single_cut(combined_process_dictionary, cut)
  rootfilename = f"HTauTau_{era}_{final_state_mode}_VARIABLE.inputs.root"
  #dicts["Gen_HpT_0_45"] = apply_single_cut(single_process_dictionary, GenHpT_0_45) # wrong, it's not a category

  unrolling = True

  for var in vars_to_plot:
    if var not in disciminating_variables: continue
    xbins = make_bins(var, final_state_mode)
    output_file = uproot.recreate(f"{plot_dir}/{rootfilename.replace('VARIABLE', disciminating_variables[var])}")
    for category in categories:
      data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(dicts[category])
      data_dictionaryFakes, background_dictionaryFakes, signal_dictionaryFakes = sort_combined_processes(combined_process_dictionaryFakes, fakes=True)

      # split signal dictionary
      unrolled_bins = [0, 45, 80, 120, 200, 350, 450]
      #unrolled_bins_signal = make_masks_per_bin(signal_dictionary, "HTT_H_pt", unrolled_bins) # works
      unrolled_bins_signal = make_masks_per_bin(signal_dictionary, "Gen_H_pT", unrolled_bins) # does not...
      h_data = get_binned_data(final_state_mode, testing, data_dictionary, var, xbins, lumi)
      h_backgrounds = get_binned_backgrounds(final_state_mode, testing, background_dictionary, var, xbins, lumi, userMC=MC_families)
      if (unrolling):
        h_signals = {}
        for ith_bin in range(len(unrolled_bins)):
          h_signals_unrolled = get_binned_signals(final_state_mode, testing, signal_dictionary, var, xbins, lumi,
                                                  mask=unrolled_bins_signal, mask_n=ith_bin)
          for process in h_signals_unrolled.keys():
            updated_name = process + "_" + namesGenHpTs[ith_bin]
            h_signals[updated_name] = h_signals_unrolled[process]
      else:
        h_signals = get_binned_signals(final_state_mode, testing, signal_dictionary, var, xbins, lumi)

      h_dataFakes = get_binned_data(final_state_mode, testing, data_dictionaryFakes, var, xbins, lumi)
      h_backgroundsFakes = get_binned_backgrounds(final_state_mode, testing, background_dictionaryFakes, var, xbins, lumi)
      h_summed_backgrounds = get_summed_backgrounds(h_backgroundsFakes)
      h_signalsFakes = get_binned_signals(final_state_mode, testing, signal_dictionaryFakes, var, xbins, lumi)
      h_summed_signals = get_summed_backgrounds(h_signalsFakes)

      jetFakes_background = h_dataFakes["Data"]["BinnedEvents"] - h_summed_backgrounds["Bkgd"]["BinnedEvents"] - (h_summed_signals["Bkgd"]["BinnedEvents"]/100)
      h_JetFakes = {"JetFakes": {}}
      h_JetFakes["JetFakes"]["BinnedEvents"] = jetFakes_background
      h_JetFakes["JetFakes"]["BinnedErrors"] = np.nan_to_num(np.sqrt(jetFakes_background))
      
      root_histograms = {}
      h_sum = dict(h_data)
      h_sum.update(h_backgrounds)
      h_sum.update(h_JetFakes)
      h_sum.update(h_signals)
      for process in h_sum:
        if process=="Data": process_name = "data_obs"
        elif process=="NLODYGen": process_name = "ZTT"
        elif process=="NLODYLep": process_name = "ZL"
        elif process=="NLODYJet": process_name = "ZJ"
        else: process_name = process
        root_histograms[process] = ROOT.TH1D(process_name, process_name, xbins.size-1, xbins)
        for i in range(xbins.size-1):
          root_histograms[process].SetBinContent(i+1, h_sum[process]['BinnedEvents'][i])
          root_histograms[process].SetBinError(i+1, h_sum[process]['BinnedErrors'][i])
        output_file[f'{category}/{process_name}'] = root_histograms[process]


