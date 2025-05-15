### README ###
# this file contains styling information for MC processes 
# MC_dictionary SHOULD contain one entry for each type of sample.
# Plot scaling for all non-signal processes are set to 1 by default.
#
# following most color definitions from here
# https://github.com/oponcet/TauFW/blob/8984be701ef6a5e4d126a16c390b4efb4afe101a/Plotter/python/sample/SampleStyle.py#L116
# except using RGB values converted from here using a color picker
# https://root.cern.ch/doc/master/classTColor.html

color_dictionary = {
  "ggH"   : "#0000ff", # kBlue
  "VBF"   : "#ff0000", # kRed
  "VH"    : "#00ff00", # kGreen
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

DY_LOtoNLO_kfac   = 1.122955654
DY_NLOtoNNLO_kfac = 0.992276712

WJ_LOtoNLO_kfac   = 1.125552349
WJ_NLOtoNNLO_kfac = 0.984076374
 
MC_dictionary = {
  "myQCD"    : {"label": "QCD",      "color": color_dictionary["QCD"]},
  "JetFakes" : {"label": "JetFakes", "color": color_dictionary["JetFakes"]},
  "QCD"      : {"label": "QCD",      "color": color_dictionary["QCD"]},
  "DY"       : {"label": "DY",       "color": color_dictionary["DY"]},
  "DYGen"    : {"label": r'Z$\rightarrow\tau\tau$',               "color": color_dictionary["DYGen"]},
  "DYLep"    : {"label": r'Z$\rightarrow ll,l\rightarrow\tau_h$', "color": color_dictionary["DYLep"]},
  "DYJet"    : {"label": r'$DY,j\rightarrow\tau$',                "color": color_dictionary["DYJet"]},
  "NLODYGen" : {"label": r'Z$\rightarrow\tau\tau$',               "color": color_dictionary["DYGen"]},
  "NLODYLep" : {"label": r'Z$\rightarrow ll,l\rightarrow\tau_h$', "color": color_dictionary["DYLep"]},
  "NLODYJet" : {"label": r'$DY,j\rightarrow\tau$',                "color": color_dictionary["DYJet"]},
  "TT"       : {"label": "TT",      "color": color_dictionary["TT"]},
  "ST"       : {"label": "ST",      "color": color_dictionary["ST"]},
  "WJ"       : {"label": "W+Jets",  "color": color_dictionary["WJ"]},
  "VV"       : {"label": "Diboson", "color": color_dictionary["VV"]},
  "VH"       : {"label": "VH",      "color": color_dictionary["VH"],  "plot_scaling" : 1},
  "xH"       : {"label": "xH",      "color": color_dictionary["VBF"], "plot_scaling" : 1},
  "HWW"      : {"label": "HWW",     "color": color_dictionary["HWW"]},
  "Other"    : {"label": "Other",   "color": color_dictionary["Other"]},

  #########################################################
  # above are dummy dictionaries for grouped subprocesses #
  # below are real dictionaries for subprocesses          #
  #########################################################

  # the filterd samples having efficieny factors that are already in their event weight branch
  # they are written out on the right here also
  "ggH_TauTau" : {"label": "ggH", "color": color_dictionary["ggH"], "plot_scaling" : 1}, # 0.3869
  "VBF_TauTau" : {"label": "VBF", "color": color_dictionary["VBF"], "plot_scaling" : 1}, # 0.4216 
  "WpH_TauTau" : {"label": "WpH", "color": color_dictionary["VH"],  "plot_scaling" : 1}, # 0.3582
  "WmH_TauTau" : {"label": "WmH", "color": color_dictionary["VH"],  "plot_scaling" : 1}, # 0.3869
  "ZH_TauTau"  : {"label": "ZH",  "color": color_dictionary["VH"],  "plot_scaling" : 1}, # 0.4030
  "ttH_nonbb_TauTau"  : {"label": "ttH", "color": color_dictionary["HWW"], "plot_scaling" : 1},

  #### LO DY
  "DYInc"              : {"label": "DYIncLO", "color": color_dictionary["DY"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M10to50" : {"label": "DY10to50LO", "color": color_dictionary["DY"], "plot_scaling" : 1}, #no kfac on 10to50
  "DYJetsToLL_M-50_1J" : {"label": "DY1JLO", "color": color_dictionary["DY"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_2J" : {"label": "DY2JLO", "color": color_dictionary["DY"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_3J" : {"label": "DY3JLO", "color": color_dictionary["DY"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_4J" : {"label": "DY4JLO", "color": color_dictionary["DY"], "plot_scaling" : DY_LOtoNLO_kfac},
  
  # copies for flavor splitting
  "DYIncGen"              : {"label": "DYIncLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYIncLep"              : {"label": "DYIncLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYIncJet"              : {"label": "DYIncLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M10to50Gen" : {"label": "DY10to50LOGen", "color": color_dictionary["DYGen"], "plot_scaling" : 1}, #no kfac on 10to50
  "DYJetsToLL_M10to50Lep" : {"label": "DY10to50LOLep", "color": color_dictionary["DYLep"], "plot_scaling" : 1}, #no kfac on 10to50
  "DYJetsToLL_M10to50Jet" : {"label": "DY10to50LOJet", "color": color_dictionary["DYJet"], "plot_scaling" : 1}, #no kfac on 10to50
  "DYJetsToLL_M-50_1JGen" : {"label": "DY1JLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_1JLep" : {"label": "DY1JLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_1JJet" : {"label": "DY1JLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_2JGen" : {"label": "DY2JLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_2JLep" : {"label": "DY2JLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_2JJet" : {"label": "DY2JLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_3JGen" : {"label": "DY3JLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_3JLep" : {"label": "DY3JLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_3JJet" : {"label": "DY3JLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_4JGen" : {"label": "DY4JLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_4JLep" : {"label": "DY4JLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_LOtoNLO_kfac},
  "DYJetsToLL_M-50_4JJet" : {"label": "DY4JLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_LOtoNLO_kfac},

  #### NLO DY
  "DYIncNLO"              : {"label": "DYIncNLO", "color": color_dictionary["DY"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M10to50NLO" : {"label": "DY10to50NLO", "color": color_dictionary["DY"], "plot_scaling" : 1}, # no kfac on 10to50
  "DYJetsToLL_M-50_0JNLO" : {"label": "DY0JNLO", "color": color_dictionary["DY"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_1JNLO" : {"label": "DY1JNLO", "color": color_dictionary["DY"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_2JNLO" : {"label": "DY2JNLO", "color": color_dictionary["DY"], "plot_scaling" : DY_NLOtoNNLO_kfac},

  # copies for flavor splitting
  "DYIncNLODYGen"              : {"label": "DYIncNLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYIncNLODYLep"              : {"label": "DYIncNLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYIncNLODYJet"              : {"label": "DYIncNLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M10to50NLODYGen" : {"label": "DY10to50NLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : 1},
  "DYJetsToLL_M10to50NLODYLep" : {"label": "DY10to50NLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : 1},
  "DYJetsToLL_M10to50NLODYJet" : {"label": "DY10to50NLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : 1},
  "DYJetsToLL_M-50_0JNLODYGen" : {"label": "DY0JNLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_0JNLODYLep" : {"label": "DY0JNLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_0JNLODYJet" : {"label": "DY0JNLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_1JNLODYGen" : {"label": "DY1JNLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_1JNLODYLep" : {"label": "DY1JNLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_1JNLODYJet" : {"label": "DY1JNLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_2JNLODYGen" : {"label": "DY2JNLOGen", "color": color_dictionary["DYGen"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_2JNLODYLep" : {"label": "DY2JNLOLep", "color": color_dictionary["DYLep"], "plot_scaling" : DY_NLOtoNNLO_kfac},
  "DYJetsToLL_M-50_2JNLODYJet" : {"label": "DY2JNLOJet", "color": color_dictionary["DYJet"], "plot_scaling" : DY_NLOtoNNLO_kfac},

  "TTTo2L2Nu"          : {"label": "TT2L2Nu", "color": color_dictionary["TT"], "plot_scaling" : 1},
  "TTToFullyHadronic"  : {"label": "TT4Q",    "color": color_dictionary["TT"], "plot_scaling" : 1},
  "TTToSemiLeptonic"   : {"label": "TT2Q2L",  "color": color_dictionary["TT"], "plot_scaling" : 1},

  "ST_s-channel_Tbar"  : {"label": "ST-sTb",     "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_s-channel_T"     : {"label": "ST-sT",      "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_t-channel_Tbar"  : {"label": "ST-tTb",     "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_t-channel_T"     : {"label": "ST-tT",      "color": color_dictionary["ST"], "plot_scaling": 1},
  "ST_TWminus_2L2Nu"   : {"label": "STW-2L2Nu",  "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_2L2Nu" : {"label": "STbW+2L2Nu", "color": color_dictionary["ST"], "plot_scaling" : 1},
 
  "ST_TWminus_4Q"      : {"label": "STW-4Q",     "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_4Q"    : {"label": "STbW+4Q",    "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TWminus_LNu2Q"   : {"label": "STW-LNu2Q",  "color": color_dictionary["ST"], "plot_scaling" : 1},
  "ST_TbarWplus_LNu2Q" : {"label": "STbW+LNu2Q", "color": color_dictionary["ST"], "plot_scaling" : 1},

  "WJetsInc"           : {"label": "WJIncLO", "color": color_dictionary["WJ"], "plot_scaling" : WJ_LOtoNLO_kfac},
  "WJetsToLNu_1J"      : {"label": "WJ1LO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_LOtoNLO_kfac},
  "WJetsToLNu_2J"      : {"label": "WJ2LO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_LOtoNLO_kfac},
  "WJetsToLNu_3J"      : {"label": "WJ3LO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_LOtoNLO_kfac},
  "WJetsToLNu_4J"      : {"label": "WJ4LO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_LOtoNLO_kfac},

  "WJetsIncNLO"        : {"label": "WJIncNLO", "color": color_dictionary["WJ"], "plot_scaling" : WJ_NLOtoNNLO_kfac},
  "WJetsToLNu_0JNLO"   : {"label": "WJ0NLO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_NLOtoNNLO_kfac},
  "WJetsToLNu_1JNLO"   : {"label": "WJ1NLO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_NLOtoNNLO_kfac},
  "WJetsToLNu_2JNLO"   : {"label": "WJ2NLO",   "color": color_dictionary["WJ"], "plot_scaling" : WJ_NLOtoNNLO_kfac},

  # VV (WW non Higgs, WZ, ZZ) all have VV Inc samples available, but are not used
  "WWTo2L2Nu"          : {"label": "WW2L2Nu", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WWTo4Q"             : {"label": "WW4Q",    "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WWToLNu2Q"          : {"label": "WWLNu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},

  "WZTo3LNu"           : {"label": "WZ3LNu",  "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WZTo2L2Q"           : {"label": "WZ2L2Q",  "color": color_dictionary["VV"], "plot_scaling" : 1},
  "WZToLNu2Q"          : {"label": "WZLNu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},

  "ZZTo2L2Nu"          : {"label": "ZZ2L2Nu", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo2L2Q"           : {"label": "ZZ2L2Q",  "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo2Nu2Q"          : {"label": "ZZ2Nu2Q", "color": color_dictionary["VV"], "plot_scaling" : 1},
  "ZZTo4L"             : {"label": "ZZ4L",    "color": color_dictionary["VV"], "plot_scaling" : 1},

  # WW (Higgs WW, an SM Higgs background to our analysis)
  "ggH_WW"             : {"label": "ggH_WW",  "color": color_dictionary["HWW"], "plot_scaling" : 1},
  "VBF_WW"             : {"label": "VBF_HWW", "color": color_dictionary["HWW"], "plot_scaling" : 1},

  # XSecMCweight is defined here for JetFakes process because it isn't set autmatically elsewhere
  "myQCD"              : {"label": "Jet Fakes", "color": color_dictionary["QCD"], "plot_scaling" : 1, "XSecMCweight" : 1},
}
