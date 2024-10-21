import uproot
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

GLOBAL_FLAG = "Run3"
GLOBAL_FLAG = "Phase2"

# all relevant Tau related branches
branches = ["event", "Pileup_nPU",
            "nGenVisTau", "GenVisTau_pt", "GenVisTau_eta", "GenVisTau_phi", "GenVisTau_mass",
            "GenVisTau_status", "GenVisTau_charge", 
            "nGenJet", "GenJet_pt", "GenJet_eta", "GenJet_phi", "GenJet_mass",
            "nGenPart", "GenPart_pt", "GenPart_eta", "GenPart_phi", "GenPart_mass",
            "GenPart_pdgId", "GenPart_status",
           ]

if (GLOBAL_FLAG == "Run3"):
  additional_branches = [
            "nTau",
            "Tau_idDeepTau2018v2p5VSmu", "Tau_idDeepTau2018v2p5VSe", "Tau_idDeepTau2018v2p5VSjet",
            "L1_DoubleIsoTau34er2p1",
            "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
            "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
  ]

else: # Phase2
  additional_branches = [
            "GenPart_iso",
            "nL1nnPuppiTau", "L1nnPuppiTau_pt", "L1nnPuppiTau_eta", "L1nnPuppiTau_phi",
            "nL1nnCaloTau", "L1nnCaloTau_pt", "L1nnCaloTau_eta", "L1nnCaloTau_phi",
            "nL1hpsTau", "L1hpsTau_pt", "L1hpsTau_eta", "L1hpsTau_phi",
            "nL1GTnnTau", "L1GTnnTau_pt", "L1GTnnTau_eta", "L1GTnnTau_phi",
            "nL1caloTau", "L1caloTau_pt", "L1caloTau_eta", "L1caloTau_phi",
            "L1_pNNPuppiTauPuppiMet_55_190_final",
            "L1_pDoublePuppiTau52_52_final",
            "HLT_DoubleMediumChargedIsoPFTauHPS40_eta2p1",
            "HLT_DoubleMediumDeepTauPFTauHPS35_eta2p1",
  ]

for branch in additional_branches:
  branches.append(branch)

            # Future
            #"L1_pPuppiTauTkIsoEle45_22_final",
            #"L1_pPuppiTauTkMuon42_18_final",

good_events = "(Flag_METFilters)"

files = "VBF_HTT_preEE_TSG*root:Events" if GLOBAL_FLAG == "Run3" else "output_Phase2*.root:Events"
#files = "ggH_HTT_preEE_TSG*root:Events"
my_data = uproot.concatenate("../L1Upgrade/"+files,
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
for i, nGenVisTau, genTauEta in zip(range(get_nEvents(my_data)), my_data["nGenVisTau"], my_data["GenVisTau_eta"]):
  if ((nGenVisTau >= 2) and (abs(genTauEta[0]) < 2.1) and (abs(genTauEta[1]) < 2.1)): keep_two_taus.append(i)
  #if ((nGenVisTau >= 2)): keep_two_taus.append(i)
keep_two_taus = np.array(keep_two_taus)

# new dictionary with cut applied
my_data_2taus = apply_cut(my_data, keep_two_taus)
cutflow["TwoGenTaus"] = get_nEvents(my_data_2taus)

# add branches constructed from existing branches
# optionally, can apply other kinematic requirements here
# actually, better to apply above...
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
L1name = "L1_DoubleIsoTau34er2p1" if GLOBAL_FLAG == "Run3" else "L1_pDoublePuppiTau52_52_final"
keep_pass_L1 = []
if (GLOBAL_FLAG == "Run3"):
  for i, pass_L1_tau in zip(range(get_nEvents(my_data_2taus)), my_data_2taus[L1name]):
    if (pass_L1_tau): keep_pass_L1.append(i)

else: # Phase2
  for i, pass_L1_tau, nL1Taus in zip(range(get_nEvents(my_data_2taus)), \
                                     my_data_2taus[L1name], \
                                     my_data_2taus["nL1nnPuppiTau"]):
    if ((pass_L1_tau) and (nL1Taus >= 2)): keep_pass_L1.append(i)

keep_pass_L1 = np.array(keep_pass_L1)

# new dictionary with cut applied
my_data_2taus_passL1 = apply_cut(my_data_2taus, keep_pass_L1)
cutflow["PassL1"] = get_nEvents(my_data_2taus_passL1)

# require HLT
keep_pass_HLT = []
#HLT_name = "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1" if GLOBAL_FLAG == "Run3" else "HLT_DoubleMediumChargedIsoPFTauHPS40_eta2p1"
HLT_name = "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1" if GLOBAL_FLAG == "Run3" else "HLT_DoubleMediumDeepTauPFTauHPS35_eta2p1"
for i, pass_HLT_tau in zip(range(get_nEvents(my_data_2taus_passL1)), my_data_2taus_passL1[HLT_name]):
  if (pass_HLT_tau): keep_pass_HLT.append(i)
keep_pass_HLT = np.array(keep_pass_HLT)

# new dictionary with cut applied
my_data_2taus_passL1_passHLT = apply_cut(my_data_2taus_passL1, keep_pass_HLT)
cutflow["PassHLT"] = get_nEvents(my_data_2taus_passL1_passHLT)

# require offline TauID for Run3
if (GLOBAL_FLAG == "Run3"):
  keep_pass_TauID = []
  for i, nTau, vsMu, vsEle, vsJet in zip(range(get_nEvents(my_data_2taus_passL1_passHLT)), \
                                   my_data_2taus_passL1_passHLT["nTau"],\
                                   my_data_2taus_passL1_passHLT["Tau_idDeepTau2018v2p5VSmu"],\
                                   my_data_2taus_passL1_passHLT["Tau_idDeepTau2018v2p5VSe"],\
                                   my_data_2taus_passL1_passHLT["Tau_idDeepTau2018v2p5VSjet"]):
    #print(vsMu, vsEle, vsJet)
    if ( (nTau >= 2) and                         # at least 2 offline taus
         ((vsMu[0]  > 1) and (vsMu[1]  > 1)) and # pass Muon
         ((vsEle[0] > 2) and (vsEle[1] > 2)) and # pass Ele
         ((vsJet[0] > 5) and (vsJet[1] > 5)) ):  # pass Jet
      keep_pass_TauID.append(i)

  # new dictionary with cut applied
  my_data_2taus_passL1_passHLT_passTauID = apply_cut(my_data_2taus_passL1_passHLT, keep_pass_TauID)
  cutflow["PassTauID"] = get_nEvents(my_data_2taus_passL1_passHLT_passTauID)

# all cutting finished, now setting up plotting
print(cutflow)

# convert data to histograms before plotting
vars_to_plot = ["my_t1_pt", "my_t1_eta", "my_t1_phi",
                "my_t2_pt", "my_t2_eta", "my_t2_phi"]
binning_dictionary = {
 #"my_t1_pt"  : np.linspace(0, 150, 30+1),
 "my_t1_pt"  : np.linspace(0, 200, 40+1),
 "my_t1_eta" : np.linspace(-3, 3, 60+1),
 "my_t1_phi" : np.linspace(-3.2, 3.2, 32+1),
 #"my_t2_pt"  : np.linspace(0, 120, 24+1),
 "my_t2_pt"  : np.linspace(0, 200, 40+1),
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

def make_plot_pretty(plot_ax):
  plot_ax.set_title(f"{GLOBAL_FLAG} VBF Sample", loc='right', y=0.98)
  plot_ax.text(0.01, 1.02, "CMS", transform=plot_ax.transAxes, fontsize=16, weight='bold')
  plot_ax.text(0.12, 1.02, "Preliminary", transform=plot_ax.transAxes, fontsize=16, style='italic')
  plot_ax.set_ylabel("Events")
  plot_ax.minorticks_on()
  plot_ax.tick_params(which="both", top=True, bottom=True, right=True, direction="in")

total_events = len(my_data_2taus["my_t1_eta"])
print(total_events)
binned_data_2taus                = get_binned_info(my_data_2taus, vars_to_plot, binning_dictionary)
binned_data_2taus_passL1         = get_binned_info(my_data_2taus_passL1, vars_to_plot, binning_dictionary)
binned_data_2taus_passL1_passHLT = get_binned_info(my_data_2taus_passL1_passHLT, vars_to_plot, binning_dictionary)
#binned_data_2taus_passL1_passHLT_passTauID = get_binned_info(my_data_2taus_passL1_passHLT_passTauID, vars_to_plot, binning_dictionary)

plot_gen_eff = True
if (plot_gen_eff == True):
  fig, plot_ax = plt.subplots()
  make_plot_pretty(plot_ax)
  plot_ax.set_ylabel("(Events / 5 GeV) / Total Events")
  plot_ax.set_xlabel(r'$p_T$ [GeV]')

  # drawing to plot
  var1 = "my_t1_pt"
  var2 = "my_t2_pt"
  xbins_var1 = binning_dictionary[var1]
  xbins_var2 = binning_dictionary[var2]
  bin_width_var1  = abs(xbins_var1[0:-1]-xbins_var1[1:])/2 # only works for uniform bin widths
  bin_width_var2  = abs(xbins_var2[0:-1]-xbins_var2[1:])/2 # only works for uniform bin widths
  #plot_ax.errorbar(xbins_var1[:-1], binned_data_2taus[var1], 
  #             xerr=bin_width_var1, yerr=np.sqrt(binned_data_2taus[var1]),
  plot_ax.errorbar(xbins_var1[:-1], binned_data_2taus[var1]/total_events, 
             xerr=bin_width_var1, yerr=np.sqrt(binned_data_2taus[var1])/total_events,
             marker="^", markerfacecolor="white", color="black", linestyle="none")
  #plot_ax.errorbar(xbins_var2[:-1], binned_data_2taus[var2], 
  #             xerr=bin_width_var2, yerr=np.sqrt(binned_data_2taus[var2]),
  plot_ax.errorbar(xbins_var2[:-1], binned_data_2taus[var2]/total_events, 
             xerr=bin_width_var2, yerr=np.sqrt(binned_data_2taus[var2])/total_events,
             marker="v", color="forestgreen", linestyle="none")
  plot_ax.grid(True, linestyle="--")

  #plot_ax.stairs(binned_data_2taus[var1]/total_events, xbins_var1)
  #plot_ax.stairs(binned_data_2taus[var2]/total_events, xbins_var2)

  # making plot look nice
  ylimmin, ylimmax = plot_ax.get_ylim()
  #plot_ax.set_ylim(ylimmin, ylimmax*1.25) # scale up graph so legend fits without crazy overlap
  #plot_ax.set_ylim(0, 0.15) # manually set 
  plot_ax.set_ylim(0, 0.16)
  #plot_ax.set_xlim(0, 200)
  plot_ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
  plot_ax.legend(labels=[r'leading $\tau_h$', r'subleading $\tau_h$'])

make_efficiency_plots = True
if (make_efficiency_plots == True):
  vars_to_plot = ["my_t1_pt", "my_t2_pt"]
  for var in vars_to_plot:
    # plot setup and styling # below two lines are a way to put distributions and efficiencies on one plot
    #gs = gridspec_kw = {'height_ratios': [4, 1], 'hspace': 0.09}
    #fig, (plot_ax, ratio_ax) = plt.subplots(nrows=2, sharex=True, gridspec_kw=gridspec_kw)
    fig, plot_ax = plt.subplots()
    _ , ratio_ax = plt.subplots()
    make_plot_pretty(plot_ax)
    ratio_ax.set_xlabel(var)

    # drawing to plot
    xbins = binning_dictionary[var]
    plot_ax.stairs(binned_data_2taus[var], xbins)
    plot_ax.stairs(binned_data_2taus_passL1[var], xbins)
    plot_ax.stairs(binned_data_2taus_passL1_passHLT[var], xbins)
    #plot_ax.stairs(binned_data_2taus_passL1_passHLT_passTauID[var], xbins)
    #ratio_ax.stairs(binned_data_2taus_passL1[var]/binned_data_2taus[var], xbins)
    ratio_ax.stairs(binned_data_2taus_passL1_passHLT[var]/binned_data_2taus_passL1[var], xbins)
    #ratio_ax.stairs(binned_data_2taus_passL1_passHLT_passTauID[var]/binned_data_2taus_passL1_passHLT[var], xbins)
  
    # making plot look nice
    ylimmin, ylimmax = plot_ax.get_ylim()
    plot_ax.set_ylim(ylimmin, ylimmax*1.5)
    plot_ax.legend(labels=["2GenTaus", "2GenTaus + PassL1", "2GenTaus + PassL1 + PassHLT"])
    #plot_ax.legend(labels=["2GenTaus", "2GenTaus + PassL1", "2GenTaus + PassL1 + PassHLT", "+ PassTauID"])
  
    ratio_ax.set_ylabel("Pass L1+HLT / Pass L1")
    #ratio_ax.set_ylabel("Pass Denom. + 2 Offline Taus + Offline ID / Pass 2GenTaus + L1 + HLT")
    ratio_ax.axhline(y=1, color='grey', linestyle='--')
    ratio_ax.minorticks_on()
    ratio_ax.tick_params(which="both", top=True, bottom=True, right=True, direction="in")

make_comparison_plots = True # won't plot if above set is enabled
if (make_comparison_plots == True):
  # put both tau vars on the same plot together
  tau1var = vars_to_plot[0:3]
  tau2var = vars_to_plot[3:6]
  for t1, t2 in zip(tau1var, tau2var):
    _  , bothTau_ax = plt.subplots()
    make_plot_pretty(bothTau_ax)
    bothTau_ax.set_ylabel("Events")
    xbins = binning_dictionary[t1] # requires binnings to be equal
    bothTau_ax.stairs(binned_data_2taus[t1], xbins)
    #bothTau_ax.stairs(binned_data_2taus_passL1[t1], xbins)
    #bothTau_ax.stairs(binned_data_2taus_passL1_passHLT[t1], xbins)
    bothTau_ax.stairs(binned_data_2taus[t2], xbins)
    #bothTau_ax.stairs(binned_data_2taus_passL1[t2], xbins)
    #bothTau_ax.stairs(binned_data_2taus_passL1_passHLT[t2], xbins)
    bothTau_ax.legend(labels=[t1, t2])
    bothTau_ax.set_xlabel(t1.split("_")[-1])


make_2D_plots = True
if (make_2D_plots == True):
  binning_dictionary = {
   "my_t1_pt"  : np.linspace(0, 150, 15+1),
   "my_t1_eta" : np.linspace(-3, 3, 60+1),
   "my_t1_phi" : np.linspace(-3.2, 3.2, 32+1),
   "my_t2_pt"  : np.linspace(0, 150, 15+1),
   "my_t2_eta" : np.linspace(-3, 3, 60+1),
   "my_t2_phi" : np.linspace(-3.2, 3.2, 32+1),
  }

  x_var = "my_t1_pt"
  y_var = "my_t2_pt"

  x_bins = binning_dictionary[x_var]
  y_bins = binning_dictionary[y_var]

  data_dictionaries = {
    "passGen" : [my_data_2taus[x_var], my_data_2taus[y_var]],
    "passL1"  : [my_data_2taus_passL1[x_var], my_data_2taus_passL1[y_var]],
    "passHLT" : [my_data_2taus_passL1_passHLT[x_var], my_data_2taus_passL1_passHLT[y_var]],
  }

  den_h2d, num_h2d = 0, 0
  for key in data_dictionaries.keys():
    fig, axis_2D = plt.subplots()
    #make_plot_pretty(axis_2D) # not quite right yet
    x_array = data_dictionaries[key][0]
    y_array = data_dictionaries[key][1]
    h2d, xbins, ybins = np.histogram2d(x_array, y_array, bins=(x_bins, y_bins))
    h2d = h2d.T # transpose from image coordinates to data coordinates
    cmesh = axis_2D.pcolormesh(xbins, ybins, h2d) #pcolormesh uses data coordinates by default, imshow uses array of 1x1 squares
    axis_2D.set_title(key)
    axis_2D.set_xlabel(x_var)
    axis_2D.set_ylabel(y_var)
    plt.colorbar(cmesh)

    if (key == "passGen"): den_h2d = h2d
    if (key == "passHLT"): num_h2d = h2d

  # efficiency 2D
  _, eff_axis_2D = plt.subplots()
  eff_cmesh = eff_axis_2D.pcolormesh(xbins, ybins, num_h2d/den_h2d)
  eff_axis_2D.set_title("passGen+L1+HLT / passGen")
  eff_axis_2D.set_xlabel(x_var)
  eff_axis_2D.set_ylabel(y_var)
  plt.colorbar(eff_cmesh)


plt.show()



