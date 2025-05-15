import uproot
import numpy as np

from utility_functions import time_print, text_options, log_print
from MC_dictionary import MC_dictionary

### README ###
# This file contains the main method to load data from root files
# The wildcarding works for the 'concatenate' function of uproot, and might not in the future.
# This file also contains methods relevant to sorting samples from files.


def load_process_from_file(process, file_directory, file_map, log_file,
                           branches, good_events, final_state_mode, 
                           data=False, testing=False, direct_input=None):
  '''
  This will make more sense if you read the documentation on uproot.concatenate first:
  https://uproot.readthedocs.io/en/latest/basic.html#reading-many-files-into-big-arrays
  Most important function! Contains the only call to uproot in this library! 
  Loads into memory files relevant to the given 'final_state_mode' by reading
  'file_map' which is a python dictionary maintained in a separate file. 
  uproot.concatenate grabs all files matching the wildcard in 'file_map[process]'
  and loads ONLY the data specified by 'branches' which pass the cut 'good_events'.
  Both 'branches' and 'good_events' are specified in other places and depend on the
  final state mode.
  library='np' loads the data in a numpy array that looks like this
   {{"branch_1" : [event1, event2, event3, ..., eventN]},
    {"branch_2" : [event1, event2, event3, ..., eventN]},
    {"branch_3" : [event1, event2, event3, ..., eventN]}, etc.
    {"branch_N" : [event1, event2, event3, ..., eventN]}}
  This coding library is built using numpy arrays as the default and will not work
  with other types of arrays (although the methods could be copied and rewritten). 
  Note: that a numpy array is generated for each loaded process, which corresponds
  to a set of files. 
  '''
  if direct_input != None:
    # way to bypass filemapping and load files from different data directories
    log_print(f"Loading {direct_input}", log_file, time=True)
    file_string = direct_input + ".root:Events"
  else:
    log_print(f"Loading {file_map[process]}", log_file, time=True)
    file_string = file_directory + "/" + file_map[process] + ".root:Events"
  if data: 
    # if a branch isn't available in Data, don't try to load it
    branches_not_in_data = ["Generator_weight", "NWEvents", "Tau_genPartFlav", "XSecMCweight",
                            "Weight_DY_Zpt", "Weight_DY_Zpt_LO", "Weight_DY_Zpt_NLO",
                            "TauSFweight", "MuSFweight", "ElSFweight", "BTagSFfull",
                            "PUweight", "Weight_TTbar_NNLO", "Pileup_nPU"]
    for missing_branch in branches_not_in_data:
      branches = [branch for branch in branches if branch != missing_branch]
  if "WJets" not in process:
    branches = [branch for branch in branches if not branch.startswith("StitchWeight_WJets")]
  #if (process not in ["ggH_TauTau", "VBF_TauTau", "WpH_TauTau", "WmH_TauTau", "ZH_TauTau"]):
  #  branches_only_in_signal = [""
  #  for missing_branch in branches_only_in_signal:
  #    branches = [branch for branch in branches if branch != missing_branch]
  try:
    processed_events = uproot.concatenate([file_string], branches, cut=good_events, library="np")
  except FileNotFoundError:
    log_print(text_options["yellow"] + "FILE NOT FOUND! " + text_options["reset"], log_file, end="")
    log_print(f"continuing without loading {file_string}...", log_file)
    return None
  process_list = {}
  process_list[process] = {}
  process_list[process]["info"] = processed_events
 
  return process_list


def sort_combined_processes(combined_processes_dictionary, fakes=False):
  data_dictionary, background_dictionary, signal_dictionary = {}, {}, {}
  for process in combined_processes_dictionary:
    newProcess = process + "Fakes" if fakes==True else process
    if "Data" in newProcess:
      data_dictionary[newProcess]       = combined_processes_dictionary[process]
    elif ("_TauTau" in newProcess): #keeps signal only
      signal_dictionary[newProcess]     = combined_processes_dictionary[process]
    else:
      background_dictionary[newProcess] = combined_processes_dictionary[process]
  return data_dictionary, background_dictionary, signal_dictionary


def append_to_combined_processes(process, cut_events, vars_to_plot, combined_processes, one_file_at_a_time):
  orig_process = ""
  if process in combined_processes.keys():
    if not one_file_at_a_time: print(f" !@#$%^&*&^%$#@! ADDING DUPLICATE PROCESS DATA FOR {process} NAMED {process}_alt !@#$%^&*&^%$#@!")
    orig_process = process
    process = process+"_alt"
  if "Data" not in process:
    combined_processes[process] = {
      "PlotEvents"        : {}, 
      "Cuts"              : {},
      "Generator_weight"  : cut_events["Generator_weight"],
      "Weight_TTbar_NNLO" : cut_events["Weight_TTbar_NNLO"],
      "Weight_DY_Zpt"     : cut_events["Weight_DY_Zpt"],
      "TauSFweight"       : cut_events["TauSFweight"],
      "MuSFweight"        : cut_events["MuSFweight"],
      "ElSFweight"        : cut_events["ElSFweight"],
      "BTagSFfull"        : cut_events["BTagSFfull"],
      "PUweight"          : cut_events["PUweight"],
      "XSecMCweight"      : cut_events["XSecMCweight"],
      "SF_weight"         : np.ones(cut_events["Generator_weight"].shape)
    }
  elif "Data" in process:
    combined_processes[process] = { 
      "PlotEvents": {},
      "Cuts": {},
      "FFweight": cut_events["FFweight"] # TODO: somehow reconcile the old and new FF storage method...
    }
    if ("FF_weight" in cut_events.keys()):
      combined_processes[process]["FF_weight"] = cut_events["FF_weight"]

  # remove this to get previous behavior
  combined_processes[process]["FFweight"] = cut_events["FFweight"]
  combined_processes[process]["FFweight_QCD"] = cut_events["FFweight_QCD"]
  combined_processes[process]["FFweight_WJ"] = cut_events["FFweight_WJ"]
  combined_processes[process]["FFweight_FractionQCD"] = cut_events["FFweight_FractionQCD"]

  #if "WJets" in process:
  #  combined_processes[process]["StitchWeight_WJets_NLO"] = cut_events["StitchWeight_WJets_NLO"]
    
  for var in vars_to_plot:
    if ("Data" in process) and (("flav" in var) or ("Generator" in var)): continue
    combined_processes[process]["PlotEvents"][var] = cut_events[var]
    if ("_TauTau" in process) and ("Fakes" not in process): # keep some gen vars just for signal
      for extra_var in ["Gen_H_pT", "Gen_pT_j1", "Gen_pT_l1", "Gen_nCleanJet"]:
        combined_processes[process]["PlotEvents"][extra_var] = cut_events[extra_var]

  for cut in ["pass_cuts", "event_flavor",
              "pass_0j_cuts", "pass_1j_cuts", "pass_2j_cuts", "pass_3j_cuts",
              "pass_GTE2j_cuts"]:
    if cut in cut_events.keys():
      if ("Data" in process) and ("flav" in cut): continue
      combined_processes[process]["Cuts"][cut] = cut_events[cut]

  if one_file_at_a_time and process.endswith("_alt") and orig_process!="":
    for key1 in combined_processes[orig_process]:
      assert key1 in combined_processes[process]
      if isinstance(combined_processes[orig_process][key1], dict):
        for key2 in combined_processes[orig_process][key1]:
          assert key2 in combined_processes[process][key1]
          combined_processes[orig_process][key1][key2] = np.append(combined_processes[orig_process][key1][key2], combined_processes[process][key1][key2])
      elif isinstance(combined_processes[orig_process][key1], np.ndarray):
        combined_processes[orig_process][key1] = np.append(combined_processes[orig_process][key1], combined_processes[process][key1])
      else:
        print("I don't know what happened here ('append_to_combined_processes' in file_functions.py)")
    del combined_processes[process]

  return combined_processes

def load_and_store_NWEvents(process, event_dictionary):
  '''
  Read the NWEvents value for a sample and store it in the MC_dictionary,
  overriding the hardcoded values from V11 samples. Delete the NWEvents branch after.
  '''
  MC_dictionary[process]["XSecMCweight"] = event_dictionary["XSecMCweight"][0]
  if ("DY" in process):
    MC_dictionary[process+"DYGen"]["XSecMCweight"] = event_dictionary["XSecMCweight"][0]
    MC_dictionary[process+"DYLep"]["XSecMCweight"] = event_dictionary["XSecMCweight"][0]
    MC_dictionary[process+"DYJet"]["XSecMCweight"] = event_dictionary["XSecMCweight"][0]


