from sys import exit
from file_map_dictionary   import testing_file_map, full_file_map, update_data_filemap
from luminosity_dictionary import luminosities_with_normtag as luminosities
from utility_functions     import make_directory, print_setup_info

class setup_handler:
  def __init__(self):
    import argparse 
    self.parser = argparse.ArgumentParser(description='Make a standard Data/MC agreement plot.')
    # What does store_true mean? It means when the argument is supplied, store it's value as true.
    self.parser.add_argument('--testing',      dest='testing',     default=False,       action='store_true')
    self.parser.add_argument('--final_state',  dest='final_state', default="mutau",     action='store')
    self.parser.add_argument('--jet_mode',     dest='jet_mode',    default="Inclusive", action='store')
    self.parser.add_argument('--era',          dest='era',         default="2022 EFG",  action='store')
    self.parser.add_argument('--use_NLO',      dest='use_NLO',     default=True,        action='store')
    self.parser.add_argument('--plot_dir',     dest='plot_dir',    default="plots",     action='store')
    self.parser.add_argument('--DeepTau',      dest='DeepTau_version', default="2p5",   action='store')
    self.parser.add_argument('--hide_plots',   dest='hide_plots',  default=False,       action='store_true')
    self.parser.add_argument('--hide_yields',  dest='hide_yields', default=False,       action='store_true')
    self.parser.add_argument('--do_JetFakes',  dest='do_JetFakes', default=True,        action='store')
    self.parser.add_argument('--semilep_mode', dest='semilep_mode', default="Full",     action='store')
    self.parser.add_argument('--presentation', dest='presentation_mode', default=False, action='store_true')
    self.parser.add_argument('--oneatatime',   dest='oneAtATime',  default=False,       action='store_true')
    self.parser.add_argument('--tau_pt',       dest='tau_pt_cut',  default="None",      action='store')
    self.parser.add_argument('--temp_version', dest='temp_version', default="None",      action='store') # do not commit


    self.parser.add_argument('--one_process',    dest='one_process',    default=None,      action='store')

    args = self.parser.parse_args()
    temp_version = args.temp_version # possible values are V1 and V2 # do not commit
    print(f"HLEP FILE VERSION IS SET TO {temp_version}")
    print()
    print(f"IS YOUR SSD CONNECTED ?!")
    print()

    # state info
    # final_state_mode affects good_events, datasets, plotting vars, etc. automatically
    testing          = args.testing     # False by default, do full dataset unless otherwise specified
    final_state_mode = args.final_state # default mutau [possible values ditau, mutau, etau, dimuon]
    jet_mode         = args.jet_mode    # default Inclusive [possible values 0j, 1j, 2j, GTE1j, GTE2j]
    era              = args.era         # default 2022 EFG [possible values see luminosity dictionary]
    tau_pt_cut       = args.tau_pt_cut  # default None [possible values "Low", "Mid", "High"]
    if testing: era = "2022 G"     # testing overrides era inputs
    lumi = luminosities[era]

    # note: emu case isn't handled yet
    possible_jet_modes = ["Inclusive", "0j", "1j", "GTE2j"] if final_state_mode == "ditau" else ["Inclusive", "0j", "GTE1j"]
    if (jet_mode not in possible_jet_modes):
      print(f"Your jet mode is {jet_mode}. Possible jet modes for {final_state_mode} are {possible_jet_modes}")
      exit()

    # file info
    infile_directory = self.set_infile_directory(era, final_state_mode, temp_version)
    plot_dir_name = "FS_plots/" + args.plot_dir + "_" + final_state_mode + "_" + tau_pt_cut + "TauPtCategory_" + jet_mode
    plot_dir_name = make_directory(plot_dir_name, testing)
    logfile       = open('outputfile.log', 'w')
    use_NLO       = args.use_NLO     # True by default, use LO DY if False
    file_map      = self.set_file_map(testing, use_NLO, era)
    oneAtATime    = args.oneAtATime

    # misc info
    hide_plots  = args.hide_plots  # False by default, show plots unless otherwise specified
    hide_yields = args.hide_yields # False by default, show yields unless otherwise specified
    DeepTau_version = args.DeepTau_version # default is 2p5 [possible values 2p1 and 2p5]
    do_JetFakes  = args.do_JetFakes  # True by default, set to False to remove contributions from Fakes
    if (type(do_JetFakes) != bool):
      print(f"do_JetFakes is somehow not a boolean. It is {do_JetFakes} type: {type(do_JetFakes)}. Manually overriding.")
      if   "T" in do_JetFakes.upper(): do_JetFakes = True
      elif "F" in do_JetFakes.upper(): do_JetFakes = False
      else: print("do_JetFakes isn't True or False, setting to False and hoping for the best.")
      print(f"do_JetFakes = {do_JetFakes}, type: {type(do_JetFakes)}")

    semilep_mode = args.semilep_mode # default is QCD [possible values are Full, QCD, and WJ] (Full is both)
    presentation_mode = args.presentation_mode # default is False, True hides yields and combines minor backgrounds

    # comparison info (for file/process comparisons)
    one_process = args.one_process

    # set three named tuples to collect class information that can be accessed later
    from collections import namedtuple
    state_info_template = namedtuple("State_info", "testing, final_state_mode, jet_mode, era, lumi, tau_pt_cut")
    self.state_info     = state_info_template(testing, final_state_mode, jet_mode, era, lumi, tau_pt_cut)

    file_info_template  = namedtuple("File_info", "infile_directory, plot_dir_name, logfile, use_NLO, file_map, oneAtATime, temp_version")
    self.file_info      = file_info_template(infile_directory, plot_dir_name, logfile, use_NLO, file_map, oneAtATime, temp_version)

    misc_info_template  = namedtuple("Misc_info", "hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, one_process, presentation_mode")
    self.misc_info      = misc_info_template(hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, one_process, presentation_mode)

  # end class init

  def set_infile_directory(self, era, final_state_mode, temp_version):
    #lxplus_redirector = "root://cms-xrd-global.cern.ch//"
    #eos_dir           = "/eos/user/b/ballmond/NanoTauAnalysis/analysis/"
    era_modifier_2022 = "preEE" if (("C" in era) or ("D" in era)) else "postEE"
    era_modifier_2023 = "preBPIX" if ("C" in era) else "postBPIX"
    home_dir = "/Users/ballmond/LocalDesktop/HiggsTauTau" # there's no place like home :)
    SSD_dir  = "/Volumes/IDrive/HTauTau_Data"
    #home_dir = "/Users/nailaislam/htt/new_samples/Hlep/2022postEE/"
    #active_dir_2022 = "/V12_"+era_modifier_2022+"_HLepRareV2/"
    #active_dir_2023 = "/HLep_2023"+era_modifier_2023+"/"

    if   (temp_version == "V1"): 
      active_dir = SSD_dir
      if   (final_state_mode == "ditau"):
        if   ("CD" in era):                     active_dir += "/HLepV1_2022preEE/"
        elif ("EFG" in era):                    active_dir += "/HLepV1_2022postEE/"
        elif ("C" in era) and ("D" not in era): active_dir += "/HLepV1_2023preBPIX/"
        elif ("D" in era) and ("C" not in era): active_dir += "/HLepV1_2023postBPIX/"
      elif (final_state_mode == "mutau"):
        if   ("CD" in era):                     active_dir += "/HLepV1_2022preEE/"
        elif ("EFG" in era):                    active_dir += "/HLepV1_2022postEE/"
        elif ("C" in era) and ("D" not in era): active_dir += "/HLepV1_2023preBPIX/"
        elif ("D" in era) and ("C" not in era): active_dir += "/HLepV1_2023postBPIX/"
      else:
        print(f"don't have files for final state : {final_state_mode}")
    elif (temp_version == "V2"):
      active_dir = home_dir
      if   (final_state_mode == "ditau"):
        if   ("CD" in era):                     active_dir += "/HLepV2_2022preEE/"
        elif ("EFG" in era):                    active_dir += "/HLepV2_2022postEE/"
        elif ("C" in era) and ("D" not in era): active_dir += "/HLepV2_2023preBPIX/"
        elif ("D" in era) and ("C" not in era): active_dir += "/HLepV2_2023postBPIX/"
      elif (final_state_mode == "mutau"):
        if   ("CD" in era):
          active_dir += "/HLepV2_2022preEE/"
        elif ("EFG" in era):
          actie_dir  =  SSD_dir
          active_dir += "/HLepV2_2022postEE/"
          print("actually, that's only on the SSD...")
        elif ("C" in era) and ("D" not in era):
          actie_dir  =  SSD_dir
          active_dir += "/HLepV2_2023preBPIX/"
          print("actually, that's only on the SSD...")
        elif ("D" in era) and ("C" not in era):
          active_dir += "/HLepV2_2023postBPIX/"
      else:
        print(f"don't have files for final state : {final_state_mode}")
    else:
      print("not set up for that")
      print(era, temp_version, final_state_mode)
      exit()
    
    return active_dir + final_state_mode

  
  def set_file_map(self, testing, use_NLO, era):
    file_map = testing_file_map if testing else full_file_map
    NLOsamples = [s for s in file_map if s.endswith("NLO") and (s.startswith("DY") or s.startswith("WJets"))]
    LOsamples = [s for s in file_map if not s.endswith("NLO") and (s.startswith("DY") or s.startswith("WJets"))]
    if (use_NLO == True):
      for s in LOsamples: file_map.pop(s)
    else: 
      for s in NLOsamples: file_map.pop(s)
    file_map = update_data_filemap(era, file_map)
    return file_map


def set_good_events(final_state_mode, era, non_SR_region=False, temp_version="None", disable_triggers=False, useMiniIso=False):
  '''
  Return a string defining a 'good_events' flag used by uproot to preskim input events
  to only those passing these simple requirements. 'good_events' changes based on
  final_state_mode, and the trigger condition is removed if a trigger study is 
  being conducted (since requiring the trigger biases the study).
  '''
  DEBUG = False
  if (DEBUG):
    basic_cuts = "(METfilters) & (LeptonVeto==0)"
    jet_vetomaps = " & (JetMapVeto_EE_30GeV) & (JetMapVeto_HotCold_30GeV)"
    trigger    = " & Trigger_ditau"
    HTT_SR     = " & (HTT_SRevent)"
    type_req   = " & (abs(HTT_pdgId)==15*15)"
    # directly applying restrictions, always use METfilters, string can't be empty
    return basic_cuts + HTT_SR + type_req + trigger
  good_events = ""
  if disable_triggers: print("*"*20 + " removed trigger requirement " + "*"*20)

  # relevant definitions from NanoTauAnalysis /// modules/TauPairSelector.py
  # HTT_SRevent and HTT_ARevent require opposite sign objects
  # HTT_SRevent = ((pdgIdPair < 0) 
  #            and ( ((LeptonIso < 0.2) and (abs(pdgIdPair)==11*13)) or (LeptonIso < 0.15)) 
  #            and TauPassVsJet and (self.leptons[finalpair[1]].pt > 15))
  # HTT_ARevent = ((pdgIdPair < 0) 
  #            and ( ((LeptonIso < 0.2) and (abs(pdgIdPair)==11*13)) or (LeptonIso < 0.15)) 
  #            and (not TauPassVsJet) and (self.leptons[finalpair[1]].pt > 15))
  #     # All SR requirements besides TauPassVsJet
  # HTT_SSevent = ((pdgIdPair > 0) 
  #            and ( ((LeptonIso < 0.2) and (abs(pdgIdPair)==11*13)) or (LeptonIso < 0.15)) 
  #            and TauPassVsJet and (self.leptons[finalpair[1]].pt > 15)) 
  #     # All SR requirements besides opposite sign
  
  good_events =  "(METfilters) & (LeptonVeto==0)"
  jet_vetomaps = ""
  #if ("2023" in era) and any(affected_era in era for affected_era in ["D"]):
  #  jet_vetomaps += " & (JetMapVeto_BPix_15GeV)"
  if ("2022" in era) and any(affected_era in era for affected_era in ["E", "F", "G"]):
    jet_vetomaps += " & (JetMapVeto_EE_15GeV)"
  if (final_state_mode == "mutau"):
    jet_vetomaps += " & (JetMapVeto_TauMuon)"
 
  good_events += jet_vetomaps
  if (non_SR_region): return good_events # give output with MET filters, lepton veto, and veto maps
  good_events += " & (HTT_SRevent)" # preselected events from HTT ntuplizer

  if final_state_mode == "ditau":
    triggersV1 = "(HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1\
               | HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60\
               | HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75\
               | HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1\
               | HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1)" # HLepV1
    if ("2022" in era):
      triggersV2 = "((Trigger_ditau) | (Trigger_ditauplusjet) | (Trigger_VBFditau))"
    else:
      triggersV2 = "((Trigger_ditau) | (Trigger_ditauplusjet) | (Trigger_VBFditau) | (Trigger_VBFsingleTau))" # HLepV2 parking

    triggers = triggersV1 if temp_version == "V1" else triggersV2
    good_events += " & (abs(HTT_pdgId)==15*15) & " + triggers

  elif final_state_mode == "mutau":
    good_eventsV1 = " & (abs(HTT_pdgId)==13*15) & (Trigger_mutau)" # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==13*15) & ((Trigger_mutau) | (Trigger_SingleMuon))" # HLepV2
    good_events += good_eventsV1 if temp_version == "V1" else good_eventsV2

  elif final_state_mode == "etau":
    good_eventsV1 = " & (abs(HTT_pdgId)==11*15) & (Trigger_etau)" # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==11*15) & ((Trigger_etau) | (Trigger_SingleElectron))" # HLepV2
    good_events += good_eventsV1 if temp_version == "V1" else good_eventsV2

  elif final_state_mode == "emu":
    good_eventsV1 = " & (abs(HTT_pdgId)==11*13) & (Trigger_emu) " # HLepV1
    good_eventsV2 = " & (abs(HTT_pdgId)==11*13) & ((Trigger_emu) | (Trigger_mue))" # HLepV2
    good_events += good_eventsV1 if temp_version == "V1" else good_eventsV2

  elif final_state_mode == "dimuon":
    # lepton veto must be applied manually for this final state
    if (useMiniIso == False):
      good_events = "(METfilters) & (HTT_pdgId==-13*13) & (HLT_IsoMu24)"
    if (useMiniIso == True):
      good_events = "(METfilters) & (LeptonVeto==0) & (HTT_pdgId==-13*13) & (HLT_IsoMu24)"
    if disable_triggers: good_events = good_events.replace(" & (HLT_IsoMu24)", "")

  return good_events

if __name__ == "__main__":
  setup = setup_handler()
  testing, final_state_mode, jet_mode, era, lumi, tau_pt_cut = setup.state_info
  infile_directory, plot_dir_name, logfile, use_NLO, file_map, one_file_at_a_time, temp_version = setup.file_info
  hide_plots, hide_yields, DeepTau_version, do_JetFakes, semilep_mode, one_process, presentation_mode = setup.misc_info

  # test setup
  from branch_functions    import set_branches
  from plotting_functions  import set_vars_to_plot
  from file_map_dictionary import set_dataset_info

  good_events  = set_good_events(final_state_mode, era)
  branches     = set_branches(final_state_mode, era, DeepTau_version)
  vars_to_plot = set_vars_to_plot(final_state_mode, jet_mode=jet_mode)
  dataset, reject_datasets = set_dataset_info(final_state_mode)

  # show info to user
  print_setup_info(setup)


