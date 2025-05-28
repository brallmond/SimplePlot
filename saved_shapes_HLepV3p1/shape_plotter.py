import ROOT
ROOT.gErrorIgnoreLevel = 6001 # turns off all errors

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("tauPt", help="lowTauPt, midTauPt, highTauPt")
parser.add_argument("final_state", help="TauTau, MuTau, ETau, EMu")
parser.add_argument("era", help="2022_preEE, 2022_postEE, 2023_preBPix, 2023_postBPix, 2022, 2023, All")
parser.add_argument("var", help="HpT, nJets, j1pT")
args = parser.parse_args()

tauPt = args.tauPt
final_state = args.final_state
era = args.era
var = args.var

FSshort = {
  "TauTau" : "ditau",
  "MuTau"  : "mutau",
  "ETau"   : "etau",
  "EMu"    : "emu",
}
varLabels = {
  "HpT"   : 'Higgs p_{T} [GeV]',
  "nJets" : 'Number of Jets',
  "j1pT"  : 'Leading Jet p_{T} [GeV]',
}
varLabel = varLabels[var]
if var == "nJets": var = "nJet"

directory = "/Users/ballmond/LocalDesktop/HiggsTauTau/SimplePlot/saved_shapes_HLepV3p1/"
plotname = "_".join([era, FSshort[final_state], var])
filename = directory+"HTauTau_"+plotname+"_mtt.inputs.root"
rootfile = ROOT.TFile.Open(filename,"READ")

backgrounds = ["JetFakes", "ZTT", "ZL", "ZJ", "ST", "TT", "VV", "HWW"]
colors = [ROOT.kMagenta-10, ROOT.kOrange-4, ROOT.kAzure+5, ROOT.kGreen-6, ROOT.kBlue-8, 25, 26, ROOT.kAzure]

if   ("HpT" in var):
  signals = ["ggH_TauTau_GenHpT_0_45", "ggH_TauTau_GenHpT_45_80", "ggH_TauTau_GenHpT_80_120", "ggH_TauTau_GenHpT_120_200",
             "ggH_TauTau_GenHpT_200_350", "ggH_TauTau_GenHpT_350_450", "ggH_TauTau_GenHpT_450_inf",
             "xH_TauTau_GenHpT_0_45", "xH_TauTau_GenHpT_45_80", "xH_TauTau_GenHpT_80_120", "xH_TauTau_GenHpT_120_200",
             "xH_TauTau_GenHpT_200_350", "xH_TauTau_GenHpT_350_450", "xH_TauTau_GenHpT_450_inf",
            ]
  nPads = 7
  subdirs = ["HpT_0_45", "HpT_45_80", "HpT_80_120", "HpT_120_200", "HpT_200_350", "HpT_350_450", "HpT_450_inf"]
elif ("j1pT" in var):
  signals = ["ggH_TauTau_Genj1pt_0_30", "ggH_TauTau_Genj1pt_30_60", "ggH_TauTau_Genj1pt_60_120","ggH_TauTau_Genj1pt_120_200",
             "ggH_TauTau_Genj1pt_200_350", "ggH_TauTau_Genj1pt_350_inf",
             "xH_TauTau_Genj1pt_0_30", "xH_TauTau_Genj1pt_30_60", "xH_TauTau_Genj1pt_60_120","xH_TauTau_Genj1pt_120_200",
             "xH_TauTau_Genj1pt_200_350", "xH_TauTau_Genj1pt_350_inf",
            ]
  nPads = 6
  subdirs = ["j1pT_0_30", "j1pT_30_60", "j1pT_60_120", "j1pT_120_200", "j1pT_200_350", "j1pT_350_inf"]
elif ("nJet" in var):
  signals = ["ggH_TauTau_nGenJet_0j", "ggH_TauTau_nGenJet_1j", "ggH_TauTau_nGenJet_2j", "ggH_TauTau_nGenJet_3j", 
             "ggH_TauTau_nGenJet_GTE4j",
             "xH_TauTau_nGenJet_0j", "xH_TauTau_nGenJet_1j", "xH_TauTau_nGenJet_2j", "xH_TauTau_nGenJet_3j", 
             "xH_TauTau_nGenJet_GTE4j"
            ]
  nPads = 5
  subdirs = ["nJets_0j", "nJets_1j", "nJets_2j", "nJets_3j", "nJets_GT4j"]

subdirs = [tauPt+"_"+subdir for subdir in subdirs]

#c = ROOT.TCanvas("c1", "", 1600, 800)
c = ROOT.TCanvas("c1", "", 3200, 1600) # what is the point of a default constructor if the defaults suck?
c.SetRightMargin(0.08);
c.SetLeftMargin(0.25);
c.SetBottomMargin(0.15);
c.Divide(nPads,1,0,0)

def fill_new_pad(mydir):
  hs = ROOT.THStack(f"hs","")
  
  # combine signals
  sigHist = mydir[signals[0]].Clone()
  sigHist.SetFillColor(ROOT.kRed)
  sigHist.SetLineColor(0)
  sigHist.SetLineWidth(0)
  scale = 10
  for signal in signals:
      if (signal == signals[0]): continue # skip first one
      sigHist += mydir[signal]*scale
  
  otherHist = mydir[backgrounds[-1]].Clone()
  otherHist.SetFillColor(ROOT.kCyan)
  otherHist.SetLineColor(0)
  otherHist.SetLineWidth(0)
  for process, color in zip(backgrounds, colors):
      hist = mydir[process]
      if (process == "JetFakes") or (process == "ZTT"):      
        hist.SetFillColor(color)
        hist.SetLineColor(0)
        hist.SetLineWidth(0)
        hs.Add(hist)
      else:
        otherHist += hist
 
  otherHist.SetName("Other")
  hs.Add(otherHist)
  sigHist.SetName(f"Signal x{scale}")
  hs.Add(sigHist)
 
  #hs.Draw("HIST") # "HIST" option must be set for fill colors to be visible  - though this contradicts the THStack documentation
  return hs

hslist = [] # interestingly, python's garbage collection will automatically remove hs's if you don't put them in a list
            # outside of your loop. Try removing hslist and making the plot to see what I mean.
i = 1
for singledir in subdirs:
  c.cd(i)
  hs = fill_new_pad(rootfile[singledir])
  if i == 1: hs.Draw("HIST")
  else: hs.Draw("A HIST") # remove axis
  hslist.append(hs)
  label = ROOT.TLatex()
  label.SetNDC(True)
  label.SetTextSize(0.070)
  label.DrawLatex(0.50, 0.85, f"{singledir.split(tauPt)[-1]}")
  c.Draw("SAME")
  i += 1

# only need one legend since colors and labels are the same among cuts
legend = ROOT.TLegend(0.45,0.55,0.95,0.7);
for entry in hs:
  legend.AddEntry(entry, f"{entry.GetName()}","f")
legend.SetTextSize(0.070)
legend.Draw()

# crazy ROOT trick. after drawing every pad you want to plot in
# make a transparent pad for annotations or other labels and legends
# ROOT in python is not an elegant language, but I guess the alternative
# is learning C++..
c.cd(0)
blankPad = ROOT.TPad("all", "all", 0, 0, 1, 1)
blankPad.SetFillStyle(4000) # transparent
blankPad.Draw()
blankPad.cd()

# set plot title
title = ROOT.TLatex()
title.SetNDC(True)
title.SetTextSize(0.06)
title.DrawLatex(0.3, 0.92, f"{FSshort[final_state]}  {tauPt}")

# manually set axis labels
xaxisLabel = ROOT.TLatex()
xaxisLabel.SetNDC(True)
xaxisLabel.SetTextSize(0.04)
xaxisLabel.DrawLatex(0.8, 0.05, f"{varLabel}")

yaxisLabel = ROOT.TLatex()
yaxisLabel.SetNDC(True)
yaxisLabel.SetTextSize(0.04)
yaxisLabel.SetTextAngle(90)
yaxisLabel.DrawLatex(0.03, 0.35, f"Events / Bin [10 GeV]")

# set era label
eraLabel = ROOT.TLatex()
eraLabel.SetNDC(True) 
eraLabel.SetTextSize(0.04)
eraLabel.DrawLatex(0.8, 0.92, f"{era}")

# set CMS Preliminary
CMSlabel = ROOT.TLatex()
CMSlabel.SetNDC(True)
CMSlabel.SetTextSize(0.040)
CMSlabel.DrawLatex(0.02, 0.92, "#bf{CMS} #it{Preliminary}")

# draw everything, and make a log version too (doesn't seem to work)
c.Draw()
c.SaveAs(f"plots/{tauPt}_{plotname}.png")
print(f"plotted plots/{tauPt}_{plotname}.png")

#ROOT.gPad.SetLogy(True) # why isn't this working :(
#c.Draw()
#c.SaveAs(f"plots/{tauPt}_{plotname}_log.pdf")
#print(f"plotted plots/{tauPt}_{plotname}_log.pdf")

