import ROOT
import uproot
import numpy as np
from plotting_functions import make_bins, get_binned_data, get_binned_backgrounds, get_binned_signals, get_summed_backgrounds
from file_functions     import sort_combined_processes
from FF_functions       import set_JetFakes_process

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
  categories = {"incl"    : "1",
                "zerojet" : "nCleanJetGT30==0",
                "onejet"  : "nCleanJetGT30==1",
                "twojet"  : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets<=350)",
                "vbfhigh" : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets>350) and (HTT_H_pt>200)",
                "vbflow"  : "(nCleanJetGT30>1) and (HTT_DiJet_MassInv_fromLeadingJets>350) and (HTT_H_pt<=200)"}

  if era=="2022 CD": era = "2022_preEE"
  elif era=="2022 EFG": era = "2022_postEE"
  elif era=="2023 C": era = "2023_preBPix"
  elif era=="2023 D": era = "2023_postBPix"
  dicts = {}
  for category,cut in categories.items():
    dicts[category] = apply_single_cut(combined_process_dictionary, cut)
  rootfilename = f"HTauTau_{era}_{final_state_mode}_VARIABLE.inputs.root"

  for var in vars_to_plot:
    if var not in disciminating_variables: continue
    xbins = make_bins(var, final_state_mode)
    output_file = uproot.recreate(f"{plot_dir}/{rootfilename.replace('VARIABLE', disciminating_variables[var])}")
    for category in categories:
      data_dictionary, background_dictionary, signal_dictionary = sort_combined_processes(dicts[category])
      data_dictionaryFakes, background_dictionaryFakes, signal_dictionaryFakes = sort_combined_processes(combined_process_dictionaryFakes, fakes=True)
      h_data = get_binned_data(final_state_mode, testing, data_dictionary, var, xbins, lumi)
      h_backgrounds = get_binned_backgrounds(final_state_mode, testing, background_dictionary, var, xbins, lumi, userMC=MC_families)
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


