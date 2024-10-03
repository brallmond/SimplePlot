import uproot
import matplotlib.pyplot as plt
import numpy as np

# all relevant Tau related branches
branches = ["event", "Pileup_nPU",
            "nGenVisTau", "GenVisTau_pt", "GenVisTau_eta", "GenVisTau_phi", "GenVisTau_mass",
            "GenVisTau_status", "GenVisTau_charge", 
            "nGenJet", "GenJet_pt", "GenJet_eta", "GenJet_phi", "GenJet_mass",
            "nGenPart", "GenPart_pt", "GenPart_eta", "GenPart_phi", "GenPart_mass",
            "GenPart_pdgId", "GenPart_status", "GenPart_iso",
            "nL1nnPuppiTau", "L1nnPuppiTau_pt", "L1nnPuppiTau_eta", "L1nnPuppiTau_phi",
            "nL1nnCaloTau", "L1nnCaloTau_pt", "L1nnCaloTau_eta", "L1nnCaloTau_phi",
            "nL1hpsTau", "L1hpsTau_pt", "L1hpsTau_eta", "L1hpsTau_phi",
            "nL1GTnnTau", "L1GTnnTau_pt", "L1GTnnTau_eta", "L1GTnnTau_phi",
            "nL1caloTau", "L1caloTau_pt", "L1caloTau_eta", "L1caloTau_phi",
            "L1_pNNPuppiTauPuppiMet_55_190_final",
            "L1_pDoublePuppiTau52_52_final",
            "HLT_DoubleMediumChargedIsoPFTauHPS40_eta2p1",
            "HLT_DoubleMediumDeepTauPFTauHPS35_eta2p1",]

            # Future
            #"L1_pPuppiTauTkIsoEle45_22_final",
            #"L1_pPuppiTauTkMuon42_18_final",

good_events = "(Flag_METFilters)"

my_data = uproot.concatenate("../L1Upgrade/*.root:Events",
                             branches, cut=good_events, library="np")
#print(my_data.keys()) # all branch names

def get_nEvents(input_dict):
  return len(input_dict["event"])

def apply_cut(input_dict, cut_array): # give new dictionary with a cut applied to all branches
  output_dict = {}
  for branch in input_dict.keys():
    output_dict[branch] = input_dict[branch]
    output_dict[branch] = np.take(output_dict[branch], cut_array)
  return output_dict

# workflow is:
# define a cut and apply it to a dictionary
# make a new dictionary with events only passing that cut
# use the new dictionary as input to next step
# repeat until all cuts are applied, then plot

# add value to cutflow before applying
cutflow = {}
cutflow["NoCuts"] = get_nEvents(my_data)

# require 2 hadronic taus in the event
# zip is a for-loop over multiple variables of the same length
# "range" used in this context gives us a branch index
keep_two_taus = []
for i, nGenVisTau in zip(range(get_nEvents(my_data)), my_data["nGenVisTau"]):
  if (nGenVisTau >= 2): keep_two_taus.append(i)
keep_two_taus = np.array(keep_two_taus)

# new dictionary with cut applied
my_data_2taus = apply_cut(my_data, keep_two_taus)
cutflow["TwoGenTaus"] = get_nEvents(my_data_2taus)

# add branches constructed from existing branches
# optionally, can apply other kinematic requirements here
t1_pt, t1_eta, t1_phi = [], [], []
t2_pt, t2_eta, t2_phi = [], [], []
for i, gen_tau_pt, gen_tau_eta, gen_tau_phi in zip(range(get_nEvents(my_data_2taus)), \
                                                         my_data_2taus["GenVisTau_pt"], \
                                                         my_data_2taus["GenVisTau_eta"], \
                                                         my_data_2taus["GenVisTau_phi"]):
  t1_pt.append(gen_tau_pt[0])
  t1_eta.append(gen_tau_eta[0])
  t1_phi.append(gen_tau_phi[0])
  t2_pt.append(gen_tau_pt[1])
  t2_eta.append(gen_tau_eta[1])
  t2_phi.append(gen_tau_phi[1])

my_data_2taus["my_t1_pt"]  = np.array(t1_pt)
my_data_2taus["my_t1_eta"] = np.array(t1_eta)
my_data_2taus["my_t1_phi"] = np.array(t1_phi)
my_data_2taus["my_t2_pt"]  = np.array(t2_pt)
my_data_2taus["my_t2_eta"] = np.array(t2_eta)
my_data_2taus["my_t2_phi"] = np.array(t2_phi)

# require L1
keep_pass_L1 = []
for i, pass_L1_tau, nL1Taus in zip(range(get_nEvents(my_data_2taus)), \
                                   my_data_2taus["L1_pDoublePuppiTau52_52_final"], \
                                   my_data_2taus["nL1nnPuppiTau"]):
  if ((pass_L1_tau) and (nL1Taus >= 2)): keep_pass_L1.append(i)
keep_pass_L1 = np.array(keep_pass_L1)

# new dictionary with cut applied
my_data_2taus_passL1 = apply_cut(my_data_2taus, keep_pass_L1)
cutflow["PassL1"] = get_nEvents(my_data_2taus_passL1)

# require HLT
keep_pass_HLT = []
#HLT_name = "HLT_DoubleMediumChargedIsoPFTauHPS40_eta2p1"
HLT_name = "HLT_DoubleMediumDeepTauPFTauHPS35_eta2p1"
for i, pass_HLT_tau in zip(range(get_nEvents(my_data_2taus_passL1)), my_data_2taus_passL1[HLT_name]):
  if (pass_HLT_tau): keep_pass_HLT.append(i)
keep_pass_HLT = np.array(keep_pass_HLT)

# new dictionary with cut applied
my_data_2taus_passL1_passHLT = apply_cut(my_data_2taus_passL1, keep_pass_HLT)
cutflow["PassHLT"] = get_nEvents(my_data_2taus_passL1_passHLT)
print(cutflow)

# convert data to histograms before plotting
vars_to_plot = ["my_t1_pt", "my_t1_eta", "my_t1_phi",
                "my_t2_pt", "my_t2_eta", "my_t2_phi"]
binning_dictionary = {
 "my_t1_pt"  : np.linspace(0, 150, 30+1),
 "my_t1_eta" : np.linspace(-3, 3, 60+1),
 "my_t1_phi" : np.linspace(-3.2, 3.2, 32+1),
 "my_t2_pt"  : np.linspace(0, 120, 24+1),
 "my_t2_eta" : np.linspace(-3, 3, 60+1),
 "my_t2_phi" : np.linspace(-3.2, 3.2, 32+1),
}

def get_binned_info(input_dict, vars_to_plot, binning_dictionary):
  binned_info = {}
  for var in vars_to_plot:
    xbins = binning_dictionary[var]
    process_variable = input_dict[var]
    binned_values, _ = np.histogram(process_variable, xbins)
    binned_info[var] = binned_values
  return binned_info

binned_data_2taus                = get_binned_info(my_data_2taus, vars_to_plot, binning_dictionary)
binned_data_2taus_passL1         = get_binned_info(my_data_2taus_passL1, vars_to_plot, binning_dictionary)
binned_data_2taus_passL1_passHLT = get_binned_info(my_data_2taus_passL1_passHLT, vars_to_plot, binning_dictionary)

for var in vars_to_plot:
  # plot setup and styling 
  gs = gridspec_kw = {'height_ratios': [4, 1], 'hspace': 0.09}
  fig, (plot_ax, ratio_ax) = plt.subplots(nrows=2, sharex=True, gridspec_kw=gridspec_kw)
  plot_ax.set_title("Phase2 VBF Sample", loc='right', y=0.98)
  plot_ax.text(0.01, 1.02, "CMS", transform=plot_ax.transAxes, fontsize=16, weight='bold')
  plot_ax.text(0.12, 1.02, "Preliminary", transform=plot_ax.transAxes, fontsize=16, style='italic')
  plot_ax.set_ylabel("Events")
  plot_ax.minorticks_on()
  plot_ax.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  ratio_ax.set_xlabel(var)

  # drawing to plot
  xbins = binning_dictionary[var]
  plot_ax.stairs(binned_data_2taus[var], xbins)
  plot_ax.stairs(binned_data_2taus_passL1[var], xbins)
  plot_ax.stairs(binned_data_2taus_passL1_passHLT[var], xbins)
  ratio_ax.stairs(binned_data_2taus_passL1[var]/binned_data_2taus[var], xbins)

  # making plot look nice
  ylimmin, ylimmax = plot_ax.get_ylim()
  plot_ax.set_ylim(ylimmin, ylimmax*1.5) # scale up graph so legend fits without crazy overlap
  plot_ax.legend(labels=["2GenTaus", "2GenTaus + PassL1", "2GenTaus + PassL1 + PassHLT"])

  ratio_ax.set_ylabel("PassL1 / 2GenTaus")
  ratio_ax.axhline(y=1, color='grey', linestyle='--')
  ratio_ax.minorticks_on()
  ratio_ax.tick_params(which="both", top=True, bottom=True, right=True, direction="in")

plt.show()

