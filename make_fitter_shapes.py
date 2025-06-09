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
    #print(f"process in apply_single_cut: {process}")
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
      if not eval(cut): continue # this will always throw an error (?) - Braden
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

def save_fitter_shapes(plot_dir, era, final_state_mode, vars_to_plot, combined_process_dictionary, combined_process_dictionaryFakes, fakesLabel, testing, lumi, fitter_mode):
  # PUT SETTINGS HERE: disciminating_variables and categories
  # Discriminating variables are required to have been plotted before
  MC_families = ["NLODYGen", "NLODYLep", "NLODYJet", "ST", "TT", "VV", "WJ", "HWW"]
  disciminating_variables = {"FastMTT_mass" : "mtt",
                             "HTT_m_vis"    : "mttvis"}

  lowTauPt  = "(FS_tau_pt >= 25.) and (FS_tau_pt < 50)" if final_state_mode == "ditau" else "(FS_tau_pt >= 30.) and (FS_tau_pt < 50)"
  midTauPt  = "(FS_tau_pt >= 50.) and (FS_tau_pt < 70)"
  highTauPt = "(FS_tau_pt >= 70.)"
  tauPts = [lowTauPt, midTauPt, highTauPt]
  namesTauPts = ["lowTauPt", "midTauPt", "highTauPt"]


  trig_hike = 0
  ditau_gen          = f"((Gen_pT_l1 >= 35+{trig_hike}) and (Gen_pT_l2 >= 35+{trig_hike}))"
  ditau_plus_jet_gen = f"((Gen_pT_l1 >= 30+{trig_hike}) and (Gen_pT_l2 >= 30+{trig_hike}) and "\
                        "(Gen_nCleanJet>=1) and (Gen_pT_j1 > 60))"
  ditau_VBF_gen      = f"((Gen_pT_l1 >= 45+{trig_hike}) and (Gen_pT_l2 >= 25+{trig_hike}) and "\
                        "(Gen_nCleanJet>=2) and (Gen_pT_j1 > 40) and (Gen_pT_j2 > 40) and (Gen_mjj > 500))"

  # in our analysis "l1" is always the first lepton in the final state name, e.g., "mutau" -> l1 is muon.
  # well, they should. they are actually unsorted here, so l1 might be tau or muon, whichever has higher pT...

  fiducialSelectionDictionary = {
    "ditau" : "((Gen_HTT_FS==-15*15) and (abs(Gen_eta_l1) <= 2.1) and (abs(Gen_eta_l2) <= 2.1) and "+\
              "(" + ditau_gen + " or " + ditau_plus_jet_gen + " or " + ditau_VBF_gen + "))",

    "mutau" : "((Gen_HTT_FS==-13*15) and (Gen_pT_l1 >= 20) and (abs(Gen_eta_l1) <= 2.4) and "+\
              "(Gen_pT_l2 >= 25) and (abs(Gen_eta_l2) <= 2.1) and (Gen_mT <= 65))",
              #"(Gen_pT_l2 >= 25) and (abs(Gen_eta_l2) <= 2.1) and (Gen_mT <= 100))",

    "etau"  : "((Gen_HTT_FS==-11*15) and (Gen_pT_l1 >= XX) and (abs(Gen_eta_l1) <= XX) and "+\
              "(Gen_pT_l2 >= XX) and (abs(Gen_eta_l2) <= XX) and (Gen_mT <= 65))",

    "emu"   : "((Gen_HTT_FS==-11*13) and (Gen_pT_l1 >= XX) and (abs(Gen_eta_l1) <= XX) and "+\
              "(Gen_pT_l2 >= XX) and (abs(Gen_eta_l2) <= XX) and (Gen_DZeta >= -40))",

  }

  fiducialSelection = fiducialSelectionDictionary[final_state_mode]
  nonFiducialSelection = f"(not {fiducialSelection})"
  # nJet
  zeroJet, oneJet, twoJet, threeJet = "nCleanJetGT30==0", "nCleanJetGT30==1", "nCleanJetGT30==2", "nCleanJetGT30==3"
  fourOrMoreJet = "nCleanJetGT30>=4"
  #zeroJet, oneJet, twoJet, threeJet = "nTightCleanJet==0", "nTightCleanJet==1", "nTightCleanJet==2", "nTightCleanJet==3"
  #fourOrMoreJet = "nTightCleanJet>=4"
  nJets = [zeroJet, oneJet, twoJet, threeJet, fourOrMoreJet]
  namesJets = ["nJets_0j", "nJets_1j", "nJets_2j", "nJets_3j", "nJets_GT4j"]

  zeroGenJet, oneGenJet, twoGenJet, threeGenJet = "Gen_nCleanJet==0", "Gen_nCleanJet==1", "Gen_nCleanJet==2", "Gen_nCleanJet==3"
  fourOrMoreGenJet = "Gen_nCleanJet>=4"
  #zeroGenJet, oneGenJet, twoGenJet, threeGenJet = "Gen_nCleanJet==0", "Gen_nCleanJet==1", "Gen_nCleanJet==2", "Gen_nCleanJet==3"
  #fourOrMoreJet = "nTightCleanJet>=4"
  nGenJets = [zeroJet, oneJet, twoJet, threeJet, fourOrMoreJet]
  nGenJets = [fiducialSelection + " and " + nGenJet for nGenJet in nGenJets]
  namesGenJets = ["nGenJet_0j", "nGenJet_1j", "nGenJet_2j", "nGenJet_3j", "nGenJet_GTE4j"]

  # uncorrected HpT
  #HpT_0_45, HpT_45_80      = "(HTT_H_pt > 0) and (HTT_H_pt <= 45)", "(HTT_H_pt > 45) and (HTT_H_pt <= 80)"
  #HpT_80_120, HpT_120_200  = "(HTT_H_pt > 80) and (HTT_H_pt <= 120)", "(HTT_H_pt > 120) and (HTT_H_pt <= 200)"
  #HpT_200_350, HpT_350_450 = "(HTT_H_pt > 200) and (HTT_H_pt <= 350)", "(HTT_H_pt > 350) and (HTT_H_pt <= 450)"
  #HpT_450_inf              = "(HTT_H_pt > 450)"

  # HpT
  HpT_0_45, HpT_45_80      = "(HTT_H_pt_corr > 0) and (HTT_H_pt_corr <= 45)", "(HTT_H_pt_corr > 45) and (HTT_H_pt_corr <= 80)"
  HpT_80_120, HpT_120_200  = "(HTT_H_pt_corr > 80) and (HTT_H_pt_corr <= 120)", "(HTT_H_pt_corr > 120) and (HTT_H_pt_corr <= 200)"
  HpT_200_350, HpT_350_450 = "(HTT_H_pt_corr > 200) and (HTT_H_pt_corr <= 350)", "(HTT_H_pt_corr > 350) and (HTT_H_pt_corr <= 450)"
  HpT_450_inf              = "(HTT_H_pt_corr > 450)"
  HpTs      = [HpT_0_45, HpT_45_80, HpT_80_120, HpT_120_200, HpT_200_350, HpT_350_450, HpT_450_inf]
  namesHpTs = ["HpT_0_45", "HpT_45_80", "HpT_80_120", "HpT_120_200", "HpT_200_350", "HpT_350_450", "HpT_450_inf"]

  GenHpT_0_45, GenHpT_45_80      = "(Gen_H_pT > 0) and (Gen_H_pT <= 45)", "and (Gen_H_pT > 45) and (Gen_H_pT <= 80)"
  GenHpT_80_120, GenHpT_120_200  = "(Gen_H_pT > 80) and (Gen_H_pT <= 120)", "and (Gen_H_pT > 120) and (Gen_H_pT <= 200)"
  GenHpT_200_350, GenHpT_350_450 = "(Gen_H_pT > 200) and (Gen_H_pT <= 350)", "and (Gen_H_pT > 350) and (Gen_H_pT <= 450)"
  GenHpT_450_inf                 = "(Gen_H_pT > 450)"
  GenHpTs      = [GenHpT_0_45, GenHpT_45_80, GenHpT_80_120, GenHpT_120_200, GenHpT_200_350, GenHpT_350_450, GenHpT_450_inf]
  GenHpTs      = [fiducialSelection + " and " + GenHpT for GenHpT in GenHpTs]
  namesGenHpTs = ["GenHpT_0_45", "GenHpT_45_80", "GenHpT_80_120", "GenHpT_120_200", "GenHpT_200_350", "GenHpT_350_450", "GenHpT_450_inf"]

  # leading jet pT
  # broken custom vars
  #jetPt_0_30    = "(nCleanJetGT30 == 0) or (CleanJetGT30_pt[0] <= 30)"
  #jetPt_30_60   = "(nCleanJetGT30 >= 1) and (CleanJetGT30_pt[0] > 30) and (CleanJetGT30_pt[0] <= 60)"
  #jetPt_60_120  = "(nCleanJetGT30 >= 1) and (CleanJetGT30_pt[0] > 60) and (CleanJetGT30_pt[0] <= 120)"
  #jetPt_120_200 = "(nCleanJetGT30 >= 1) and (CleanJetGT30_pt[0] > 120) and (CleanJetGT30_pt[0] <= 200)"
  #jetPt_200_350 = "(nCleanJetGT30 >= 1) and (CleanJetGT30_pt[0] > 200) and (CleanJetGT30_pt[0] <= 350)"
  #jetPt_350_inf = "(nCleanJetGT30 >= 1) and (CleanJetGT30_pt[0] >= 350)"

  jetPt_0_30    = "(nCleanJet == 0) or (CleanJet_pt_1 <= 30)"
  jetPt_30_60   = "(nCleanJet >= 1) and (CleanJet_pt_1 > 30) and (CleanJet_pt_1 <= 60)"
  jetPt_60_120  = "(nCleanJet >= 1) and (CleanJet_pt_1 > 60) and (CleanJet_pt_1 <= 120)"
  jetPt_120_200 = "(nCleanJet >= 1) and (CleanJet_pt_1 > 120) and (CleanJet_pt_1 <= 200)"
  jetPt_200_350 = "(nCleanJet >= 1) and (CleanJet_pt_1 > 200) and (CleanJet_pt_1 <= 350)"
  jetPt_350_inf = "(nCleanJet >= 1) and (CleanJet_pt_1 >= 350)"
  jetPts        = [jetPt_0_30, jetPt_30_60, jetPt_60_120, jetPt_120_200, jetPt_200_350, jetPt_350_inf] 
  namesJetPts   = ["j1pT_0_30", "j1pT_30_60", "j1pT_60_120", "j1pT_120_200", "j1pT_200_350", "j1pT_350_inf"]

  GenJetPt_0_30    = "(Gen_nCleanJet == 0) or (Gen_pT_j1 <= 30)"
  GenJetPt_30_60   = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 30) and (Gen_pT_j1 <= 60)"
  GenJetPt_60_120  = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 60) and (Gen_pT_j1 <= 120)"
  GenJetPt_120_200 = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 120) and (Gen_pT_j1 <= 200)"
  GenJetPt_200_350 = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 > 200) and (Gen_pT_j1 <= 350)"
  GenJetPt_350_inf = "(Gen_nCleanJet >= 1) and (Gen_pT_j1 >= 350)"
  GenJetPts        = [GenJetPt_0_30, GenJetPt_30_60, GenJetPt_60_120, GenJetPt_120_200, GenJetPt_200_350, GenJetPt_350_inf] 
  GenJetPts        = [fiducialSelection + " and " + GenJetPt for GenJetPt in GenJetPts]
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

  # adding low, mid, high categories split by bins of nTightJet, HpT, and j1pT, both Reco and Gen
  binning_mode = fitter_mode # HpT, nJet, j1pT
  for tauName, tauCategory in zip(namesTauPts, tauPts):
    if (binning_mode == "nJet"):
      for jetName, jetCategory in zip(namesJets, nJets):
        categories["_".join((tauName, jetName))] = "*".join((tauCategory, jetCategory))
    elif (binning_mode == "HpT"):
      for HpTName, HpTCategory in zip(namesHpTs, HpTs):
        categories["_".join((tauName, HpTName))] = "*".join((tauCategory, HpTCategory))
    elif (binning_mode == "j1pT"):
      for jetPtName, jetPtCategory in zip(namesJetPts, jetPts):
        categories["_".join((tauName, jetPtName))] = "*".join((tauCategory, jetPtCategory))

  if   era=="2022 CD":  era = "2022_preEE"
  elif era=="2022 EFG": era = "2022_postEE"
  elif era=="2023 C":   era = "2023_preBPix"
  elif era=="2023 D":   era = "2023_postBPix"
  dicts = {}
  dictsFakes = {}
  if (testing): categories = dict(list(categories.items())[3:6]) # get a subset to speed things up
  for category,cut in categories.items():
    dicts[category] = apply_single_cut(combined_process_dictionary, cut)
    dictsFakes[category] = apply_single_cut(combined_process_dictionaryFakes, cut)
    # cut applied here, so category has event restrictions applied already
  rootfilename = f"HTauTau_{era}_{final_state_mode}_{binning_mode}_VARIABLE.inputs.root"

  unrolling = True
  unrolling_dictionary = {
    "HpT"  : ("Gen_H_pT",      [0, 45, 80, 120, 200, 350, 450], namesGenHpTs),
    "nJet" : ("Gen_nCleanJet", [0, 1, 2, 3, 4],                 namesGenJets),
    "j1pT" : ("Gen_pT_j1",     [0, 30, 60, 120, 200, 350],      namesGenJetPts),
  }
  unrolled_bins_var   = unrolling_dictionary[binning_mode][0]
  unrolled_bins       = unrolling_dictionary[binning_mode][1]
  unrolled_bins_names = unrolling_dictionary[binning_mode][2]
  for var in vars_to_plot:
    if var not in disciminating_variables: continue
    xbins = make_bins(var, final_state_mode)
    output_file = uproot.recreate(f"{plot_dir}/{rootfilename.replace('VARIABLE', disciminating_variables[var])}")
    for category in categories:
      data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(dicts[category])
      # apply fid selection to signal only, on top of original cuts
      signal_dictionary_fid = apply_single_cut(signal_dictionary, fiducialSelection)

      data_dictionaryFakes, background_dictionaryFakes, signal_dictionaryFakes = sort_combined_processes(dictsFakes[category], fakes=True)

      unrolled_bins_signal = make_masks_per_bin(signal_dictionary_fid, unrolled_bins_var, unrolled_bins)

      h_data = get_binned_data(final_state_mode, testing, data_dictionary, var, xbins, lumi)
      h_backgrounds = get_binned_backgrounds(final_state_mode, testing, background_dictionary, var, xbins, lumi, userMC=MC_families)


      if (unrolling):
        h_signals = {}
        for ith_bin in range(len(unrolled_bins)):
          # Note, signal_dictionary already has event selections per category applied
          # meaning that for j1pT the 0j or GTE1j requirements should already be in place
          # IT IS NOT! need special handling for those two bins. Actually, we need to consider if
          # that is how we will do this analysis...
          h_signals_unrolled = get_binned_signals(final_state_mode, testing, signal_dictionary_fid, var, xbins, lumi,
                                                  mask=unrolled_bins_signal, mask_n=ith_bin)
          # combine non ggH signals into xH
          first_key = list(signal_dictionary_fid)[0]
          h_signals_unrolled["xH_TauTau"] = {}
          h_signals_unrolled["xH_TauTau"]["BinnedEvents"] = np.zeros(len(h_signals_unrolled[first_key]["BinnedEvents"]))
          h_signals_unrolled["xH_TauTau"]["BinnedErrors"] = np.zeros(len(h_signals_unrolled[first_key]["BinnedErrors"]))
          # ensure all processes exist, even if they're empty after unrolling
          check_names = ["VBF_TauTau", "WpH_TauTau", "WmH_TauTau", "ZH_TauTau", "ttH_nonbb_TauTau"]
          for process in check_names:
            try:
              h_signals_unrolled[process]["BinnedEvents"]
            except KeyError:
              h_signals_unrolled[process] = {}
              h_signals_unrolled[process]["BinnedEvents"] = np.zeros(len(h_signals_unrolled["ggH_TauTau"]["BinnedEvents"]))
              h_signals_unrolled[process]["BinnedErrors"] = np.zeros(len(h_signals_unrolled["ggH_TauTau"]["BinnedErrors"]))
          # combine non-ggH signal processes
          for signal in signal_dictionary_fid:
            if ("ggH" not in signal):
              h_signals_unrolled["xH_TauTau"]["BinnedEvents"] += h_signals_unrolled[signal]["BinnedEvents"]
              h_signals_unrolled["xH_TauTau"]["BinnedErrors"] += h_signals_unrolled[signal]["BinnedErrors"]
              del(h_signals_unrolled[signal])
 
          for process in h_signals_unrolled.keys():
            updated_name = process + "_" + unrolled_bins_names[ith_bin]
            h_signals[updated_name] = h_signals_unrolled[process]
      else:
        h_signals = get_binned_signals(final_state_mode, testing, signal_dictionary_fid, var, xbins, lumi)

      # after normal signal processing, add NonFiducialSignal branch
      signal_dictionary_nonFid = apply_single_cut(signal_dictionary, nonFiducialSelection)
      h_signals_nonFid = get_binned_signals(final_state_mode, testing, signal_dictionary_nonFid, var, xbins, lumi)
      h_signals["NonFiducialSignal"] = {}
      first_key = list(h_signals_nonFid)[0]
      h_signals["NonFiducialSignal"]["BinnedEvents"] = np.zeros(len(h_signals_nonFid[first_key]["BinnedEvents"]))
      h_signals["NonFiducialSignal"]["BinnedErrors"] = np.zeros(len(h_signals_nonFid[first_key]["BinnedErrors"]))
      for process in h_signals_nonFid.keys():
        h_signals["NonFiducialSignal"]["BinnedEvents"] += h_signals_nonFid[process]["BinnedEvents"]
        h_signals["NonFiducialSignal"]["BinnedErrors"] += h_signals_nonFid[process]["BinnedErrors"]
 
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

      # add empty entries for any channel that isn't present
      check_names = ["Data", "NLODYGen", "NLODYLep", "NLODYJet", "ST", "TT", "VV", "HWW", "JetFakes"] # no check for signal
      for process in check_names:
        try:
          h_sum[process]["BinnedEvents"]
        except KeyError:
          h_sum[process] = {}
          h_sum[process]["BinnedEvents"] = np.zeros(len(h_sum["Data"]["BinnedEvents"]))
          h_sum[process]["BinnedErrors"] = np.zeros(len(h_sum["Data"]["BinnedErrors"]))

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


