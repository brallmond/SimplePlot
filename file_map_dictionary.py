### README ###
# This file contains mappings of process names (shared with XSec.py) to wildcards for related samples.
# The :testing" file maps are subsets of full filelists for faster processing times.

dataset_dictionary = {"ditau"  : "DataTau", 
                      "mutau"  : "DataMuon", 
                      "etau"   : "DataElectron", 
                      "emu"    : "DataEMu",
                      "dimuon" : "DataMuon",}

reject_dataset_dictionary = {"ditau"  : ["DataMuon", "DataElectron", "DataEMu"],
                             "mutau"  : ["DataTau",  "DataElectron", "DataEMu"],
                             "etau"   : ["DataMuon", "DataTau",      "DataEMu"],
                             "emu"    : ["DataMuon", "DataElectron", "DataTau"],
                             "dimuon" : ["DataTau",  "DataElectron", "DataEMu"], }


def set_dataset_info(final_state_mode):
  use_dataset     = dataset_dictionary[final_state_mode]
  reject_datasets = reject_dataset_dictionary[final_state_mode]
  return use_dataset, reject_datasets


def update_data_filemap(luminosity_key, file_map): 
  if luminosity_key == "2022 C":
    file_map["DataTau"]      = "Data/Tau_Run2022C*"
    file_map["DataMuon"]     = "Data/Muon_Run2022C*"
    file_map["DataElectron"] = "Data/EGamma_Run2022C*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022C*"
  if luminosity_key == "2022 D":
    file_map["DataTau"]      = "Data/Tau_Run2022D*"
    file_map["DataMuon"]     = "Data/Muon_Run2022D*"
    file_map["DataElectron"] = "Data/EGamma_Run2022D*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022D*"
  if luminosity_key == "2022 CD":
    file_map["DataTau"]      = "Data/Tau_Run2022*"
    file_map["DataMuon"]     = "Data/Muon_Run2022*"
    file_map["DataElectron"] = "Data/EGamma_Run2022*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022*"
  if luminosity_key == "2022 E":
    file_map["DataTau"]      = "Data/Tau_Run2022E*"
    file_map["DataMuon"]     = "Data/Muon_Run2022E*"
    file_map["DataElectron"] = "Data/EGamma_Run2022E*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022E*"
  if luminosity_key == "2022 F":
    file_map["DataTau"]      = "Data/Tau_Run2022F*"
    file_map["DataMuon"]     = "Data/Muon_Run2022F*"
    file_map["DataElectron"] = "Data/EGamma_Run2022F*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022F*"
  if luminosity_key == "2022 G":
    file_map["DataTau"]      = "Data/Tau_Run2022G*"
    file_map["DataMuon"]     = "Data/Muon_Run2022G*"
    file_map["DataElectron"] = "Data/EGamma_Run2022G*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022G*"
  if luminosity_key == "2022 EFG":
    file_map["DataTau"]      = "Data/Tau_Run2022*"
    file_map["DataMuon"]     = "Data/Muon_Run2022*"
    file_map["DataElectron"] = "Data/EGamma_Run2022*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022*"
  if luminosity_key == "2022":
    file_map["DataTau"]      = "Data/Tau_Run2022*"
    file_map["DataMuon"]     = "Data/Muon_Run2022*"
    file_map["DataElectron"] = "Data/EGamma_Run2022*"
    file_map["DataEMu"]      = "Data/MuonEG_Run2022*"
  if luminosity_key == "2023 C":
    file_map["DataTau"]      = "Data/Tau_Run2023*"
    file_map["DataMuon"]     = "Data/Muon?_2023*"
    file_map["DataElectron"] = "Data/EGamma?_2023*"
    file_map["DataEMu"]      = "Data/MuonEG_2023*"
  if luminosity_key == "2023 D":
    file_map["DataTau"]      = "Data/Tau_Run2023*"
    file_map["DataMuon"]     = "Data/Muon?_2023*"
    file_map["DataElectron"] = "Data/EGamma?_2023*"
    file_map["DataEMu"]      = "Data/MuonEG_2023*"
  return file_map 


testing_file_map = {
  "DataTau"      : "Data/Tau_Run*G*",
  "DataMuon"     : "Data/Muon_Run*G*",
  "DataElectron" : "Data/EGamma*G*",
  "DataEMu"      : "Data/MuonEG_Run*G*",

  "DYJetsToLL_M-50_0JNLO" : "DY/DY0JetsToLL_M-50_NLO*",
  "DYJetsToLL_M-50_1JNLO" : "DY/DY1JetsToLL_M-50_NLO*",
  "DYJetsToLL_M-50_2JNLO" : "DY/DY2JetsToLL_M-50_NLO*",

  "VBF_TauTau" : "Signal/VBF_TauTau_Filtered*",
  "ggH_TauTau" : "Signal/ggH_TauTau_Filtered*",
}


# DY and WJ samples must end with LO or NLO
# not the entry itself, but the filemapping
# "entry" : "file/mapping*"
full_file_map = {
  # Data
  "DataTau"      : "Data/Tau_Run*",
  "DataMuon"     : "Data/Muon_Run*",
  "DataElectron" : "Data/EGamma_Run*",
  "DataEMu"      : "Data/MuonEG_Run*",

  # Signal
  "ggH_TauTau" : "Signal/ggH_TauTau_Filtered*",
  "VBF_TauTau" : "Signal/VBF_TauTau_Filtered*",

  # DY
  "DYJetsToLL_M-50_0JNLO" : "DY/DY0JetsToLL_M-50_NLO*",
  "DYJetsToLL_M-50_1JNLO" : "DY/DY1JetsToLL_M-50_NLO*",
  "DYJetsToLL_M-50_2JNLO" : "DY/DY2JetsToLL_M-50_NLO*",

  # TT
  "TTTo2L2Nu"         : "TT/TTTo2L2Nu*",
  "TTToFullyHadronic" : "TT/TTToFullyHadronic*",
  "TTToSemiLeptonic"  : "TT/TTToSemiLeptonic*",

  # ST
  "ST_s-channel_Tbar"  : "ST/ST_s-channel_antitop*",
  "ST_t-channel_Tbar"  : "ST/ST_t-channel_antitop*",
  "ST_TbarWplus_2L2Nu" : "ST/ST_TbarWplus_2L2Nu*",
  "ST_TbarWplus_4Q"    : "ST/ST_TbarWplus_4Q*",
  "ST_TbarWplus_LNu2Q" : "ST/ST_TbarWplus_LNu2Q*",
  "ST_s-channel_T"     : "ST/ST_s-channel_top*",
  "ST_t-channel_T"     : "ST/ST_t-channel_top*",
  "ST_TWminus_2L2Nu"   : "ST/ST_TWminus_2L2Nu*", 
  "ST_TWminus_4Q"      : "ST/ST_TWminus_4Q*",
  "ST_TWminus_LNu2Q"   : "ST/ST_TWminus_LNu2Q*",

  # WJ
  #"WJetsIncNLO"      : "WJ/WJetsToLNu_HTauTau*",
  "WJetsToLNu_0JNLO" : "WJ/W0JetsToLNu_HTauTau*",
  "WJetsToLNu_1JNLO" : "WJ/W1JetsToLNu_HTauTau*",
  "WJetsToLNu_2JNLO" : "WJ/W2JetsToLNu_HTauTau*",

  # VV (WW non Higgs, WZ, ZZ) all have VV Inc samples available, but are not used
  "WWTo2L2Nu" : "VV/WWTo2L2Nu*",
  "WWTo4Q"    : "VV/WWTo4Q*",
  "WWToLNu2Q" : "VV/WWToLNu2Q*",

  "WZTo3LNu"  : "VV/WZTo3LNu*",
  "WZTo2L2Q"  : "VV/WZTo2L2Q*",
  "WZToLNu2Q" : "VV/WZToLNu2Q*",

  "ZZTo2L2Nu" : "VV/ZZTo2L2Nu*",
  "ZZTo2L2Q"  : "VV/ZZTo2L2Q*", 
  "ZZTo2Nu2Q" : "VV/ZZTo2Nu2Q*",
  "ZZTo4L"    : "VV/ZZTo4L*", 

  # WW (Higgs WW, an SM Higgs background to our analysis)
  "VBF_WW"       : "WW/VBF_WW*",
  "ggH_WW"       : "WW/ggH_WW*",
  "ttH_nonbb_WW" : "WW/ttH_nonbb*",

}
