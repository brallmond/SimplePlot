from XSec import XSecRun3 as XSec
# introduces crashes
#from ROOT import TColor, kBlack, kWhite, kGray, kAzure, kBlue, kCyan,\
#                 kGreen, kSpring, kTeal, kYellow,\
#                 kOrange, kRed, kPink, kMagenta, kViolet

### README ###
# this file contains small dictionaries combining information for MC processes 
# MC_dictionary SHOULD contain one entry for each type of sample, it should    
# it references the smaller dictionaries color_dictionary and label_dictionary 
# for additionaly information. Plot scaling for all non-signal processes are set to 1 by default.
#
# following most color definitions from here
# https://github.com/oponcet/TauFW/blob/8984be701ef6a5e4d126a16c390b4efb4afe101a/Plotter/python/sample/SampleStyle.py#L116
# except using RGB values converted from here using a color picker
# https://root.cern.ch/doc/master/classTColor.html

color_dictionary = {
  "ggH"   : "#0000ff", # kBlue
  "VBF"   : "#ff0000", # kRed
  "DY"    : "#ffcc66", # DY yellow # kOrange - 4
  "DYGen" : "#ffcc66", # above
  "DYLep" : "#3399cc", # kAzure +5
  "DYJet" : "#66cc66", # kGreen -6
  "TT"    : "#9999cc", # light purple, kBlue - 8 
  "ST"    : "#8cb4dc", # their dark purple, from RGB 140 180 220 # 660099 alt dark purple
  "WJ"    : "#e44e4e", # dark red
  "VV"    : "#de8c6a", # sandy red, from RGB 222 140 106 # 808080 grey
  "HWW"   : "#de8cff", # bluer than VV, probably comes out purplish
  "QCD"   : "#ffccff", # pink kMagenta -10
  "JetFakes"   : "#ffccff", # same as QCD
  "Other" : "#10cadd", # light blue
}

label_dictionary = {
 "ggH" : "ggH",
 "VBF" : "VBF",
 "DY"  : "DY",
 "TT"  : "TT",
 "ST"  : "ST",
 "WJ"  : "WJ",
 "VV"  : "VV",
 "HWW" : "HWW",
 "QCD" : "QCD",
 "myQCD" : "FF Jet Fakes",
 "JetFakes" : "FF Jet Fakes",
 "Other" : "Other",
}
 
MC_dictionary = {
  "myQCD"    : {"label": "QCD",      "color": color_dictionary["QCD"]},
  "JetFakes" : {"label": "JetFakes", "color": color_dictionary["JetFakes"]},
  "QCD" : {"label": "QCD",     "color": color_dictionary["QCD"]},
  "DY"  : {"label": "DY",      "color": color_dictionary["DY"]},
  "TT"  : {"label": "TT",      "color": color_dictionary["TT"]},
  "ST"  : {"label": "ST",      "color": color_dictionary["ST"]},
  "WJ"  : {"label": "W+Jets",  "color": color_dictionary["WJ"]},
  "VV"  : {"label": "Diboson", "color": color_dictionary["VV"]},
  "HWW" : {"label": "HWW",     "color": color_dictionary["HWW"]},
  "Other" : {"label": "Other", "color": color_dictionary["Other"]},

  #########################################################
  # above are dummy dictionaries for grouped subprocesses #
  # below are real dictionaries for subprocesses          #
  #########################################################

  "ggH_TauTau" : {"label": "ggH", "color": color_dictionary["ggH"], "plot_scaling" : 100},
  "VBF_TauTau" : {"label": "VBF", "color": color_dictionary["VBF"], "plot_scaling" : 100},

  "DYInc"              : {"label": "DYIncLO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654}, # k-factor to NNLO
  "DYJetsToLL_M10to50" : {"label": "DY10to50LO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654},
  "DYJetsToLL_M-50_1J" : {"label": "DY1JLO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654},
  "DYJetsToLL_M-50_2J" : {"label": "DY2JLO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654},
  "DYJetsToLL_M-50_3J" : {"label": "DY3JLO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654},
  "DYJetsToLL_M-50_4J" : {"label": "DY4JLO", "color": color_dictionary["DY"], "plot_scaling" : 1.122955654},

  # TODO: cleanup this file
  # - properly split the DY contributions without so many copies (similarly for WJ)
  # copies of DYInc with different colors and labels
  "DYGen"          : {"label": "DYGenLO", "color": color_dictionary["DYGen"], "plot_scaling" : 1.12},
  "DYLep"          : {"label": "DYLepLO", "color": color_dictionary["DYLep"], "plot_scaling" : 1.12},
  "DYJet"          : {"label": "DYJetLO", "color": color_dictionary["DYJet"], "plot_scaling" : 1.12},
  "DYGen10to50"    : {"label": "DYGen10to50LO", "color": color_dictionary["DYGen"], "plot_scaling" : 1.12},
  "DYLep10to50"    : {"label": "DYLep10to50LO", "color": color_dictionary["DYLep"], "plot_scaling" : 1.12},
  "DYJet10to50"    : {"label": "DYJet10to50LO", "color": color_dictionary["DYJet"], "plot_scaling" : 1.12},

  "DYIncNLO"              : {"label": "DYIncNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712}, # k-factor to NNLO
  "DYJetsToLL_M10to50NLO" : {"label": "DY10to50NLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},
  "DYJetsToLL_M-50_0JNLO" : {"label": "DY0JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},
  "DYJetsToLL_M-50_1JNLO" : {"label": "DY1JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},
  "DYJetsToLL_M-50_2JNLO" : {"label": "DY2JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},

  # copies of DYIncNLO with different colors and labels
  "DYGenNLO"          : {"label": "DYGenNLO", "color": color_dictionary["DYGen"], "plot_scaling" : 1},
  "DYLepNLO"          : {"label": "DYLepNLO", "color": color_dictionary["DYLep"], "plot_scaling" : 1},
  "DYJetNLO"          : {"label": "DYJetNLO", "color": color_dictionary["DYJet"], "plot_scaling" : 1},
  "DYGen10to50NLO"    : {"label": "DYGen10to50NLO", "color": color_dictionary["DYGen"], "plot_scaling" : 1},
  "DYLep10to50NLO"    : {"label": "DYLep10to50NLO", "color": color_dictionary["DYLep"], "plot_scaling" : 1},
  "DYJet10to50NLO"    : {"label": "DYJet10to50NLO", "color": color_dictionary["DYJet"], "plot_scaling" : 1},

  "DY0JNLO"    : {"label": r"DY0JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},
  "DY1JNLO"    : {"label": r"DY1JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},
  "DY2JNLO"    : {"label": r"DY2JNLO", "color": color_dictionary["DY"], "plot_scaling" : 0.992276712},

  "TTTo2L2Nu"          : {"label": "TT2L2Nu", "color": color_dictionary["TT"], "plot_scaling" : 1},
  "TTToFullyHadronic"  : {"label": "TT4Q", "color": color_dictionary["TT"], "plot_scaling" : 1},
  "TTToSemiLeptonic"   : {"label": "TT2Q2L", "color": color_dictionary["TT"], "plot_scaling" : 1},

  "ST_s-channel_Tbar"  : {"label": "ST-sTb", "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_s-channel_T"     : {"label": "ST-sT", "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_t-channel_Tbar"  : {"label": "ST-tTb", "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_t-channel_T"     : {"label": "ST-tT", "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_TWminus_2L2Nu"   : {"label": "STW-2L2Nu", "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_2L2Nu" : {"label": "STbW+2L2Nu", "color": color_dictionary["ST"], "plot_scaling" : 1},
 
  "ST_TWminus_4Q"      : {"label": "STW-4Q", "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_4Q"    : {"label": "STbW+4Q", "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TWminus_LNu2Q"   : {"label": "STW-LNu2Q", "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_LNu2Q" : {"label": "STbW+LNu2Q", "color": color_dictionary["ST"], "plot_scaling" : 1},

  "WJetsInc"           : {"label": "WJIncLo", "color": color_dictionary["WJ"], "plot_scaling" : 1.125552349}, #k-factor from Stitching config in NanoTauAnalysis
  #"WJetsIncNLO"        : {"label": "WJ", "color": color_dictionary["WJ"], "plot_scaling" : 0.984076374},
  "WJetsToLNu_1J"      : {"label": "WJ1LO", "color": color_dictionary["WJ"], "plot_scaling" : 1.125552349},
  "WJetsToLNu_2J"      : {"label": "WJ2LO", "color": color_dictionary["WJ"], "plot_scaling" : 1.125552349},
  "WJetsToLNu_3J"      : {"label": "WJ3LO", "color": color_dictionary["WJ"], "plot_scaling" : 1.125552349},
  "WJetsToLNu_4J"      : {"label": "WJ4LO", "color": color_dictionary["WJ"], "plot_scaling" : 1.125552349},
  #"WJetsToLNu_0JNLO"   : {"label": "WJ", "color": color_dictionary["WJ"], "plot_scaling" : 0.984076374},
  #"WJetsToLNu_1JNLO"   : {"label": "WJ", "color": color_dictionary["WJ"], "plot_scaling" : 0.984076374},
  #"WJetsToLNu_2JNLO"   : {"label": "WJ", "color": color_dictionary["WJ"], "plot_scaling" : 0.984076374},

  # Stiching
  "WJetsIncNLO"        : {"label": "WJIncNLO", "color": color_dictionary["WJ"], "plot_scaling" : 1},
  "WJetsToLNu_0JNLO"   : {"label": "WJ0NLO", "color": color_dictionary["WJ"], "plot_scaling" : 1},
  "WJetsToLNu_1JNLO"   : {"label": "WJ1NLO", "color": color_dictionary["WJ"], "plot_scaling" : 1},
  "WJetsToLNu_2JNLO"   : {"label": "WJ2NLO", "color": color_dictionary["WJ"], "plot_scaling" : 1},

  # VV (WW non Higgs, WZ, ZZ) all have VV Inc samples available, but are not used
  "WWTo2L2Nu"          : {"label": "WW2L2Nu", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WWTo4Q"             : {"label": "WW4Q", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WWToLNu2Q"          : {"label": "WWLNu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},

  "WZTo3LNu"           : {"label": "WZ3LNu", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WZTo2L2Q"           : {"label": "WZ2L2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WZToLNu2Q"          : {"label": "WZLNu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},

  "ZZTo2L2Nu"          : {"label": "ZZ2L2Nu", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo2L2Q"           : {"label": "ZZ2L2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo2Nu2Q"          : {"label": "ZZ2Nu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo4L"             : {"label": "ZZ4L", "color": color_dictionary["VV"], "plot_scaling" : 1},

  # WW (Higgs WW, an SM Higgs background to our analysis)
  "ggH_WW"             : {"label": "ggH_WW", "color": color_dictionary["HWW"], "plot_scaling" : 1},
  "VBF_WW"             : {"label": "VBF_HWW", "color": color_dictionary["HWW"], "plot_scaling" : 1},
  "ttH_nonbb_WW"       : {"label": "ttH_WW", "color": color_dictionary["HWW"], "plot_scaling" : 1},

  # XSecMCweight is defined here for JetFakes process because it isn't set autmatically elsewhere
  "myQCD"              : {"label": "Jet Fakes", "color": color_dictionary["QCD"], "plot_scaling" : 1, "XSecMCweight" : 1},
}
