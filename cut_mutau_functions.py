import numpy as np

from calculate_functions import calculate_mt, calculate_acoplan, return_TLorentz_Jets
from branch_functions import add_trigger_branches, add_DeepTau_branches

def make_mutau_cut(era, event_dictionary, DeepTau_version, skip_DeepTau=False, tau_pt_cut="None"):
  '''
  Works similarly to 'make_ditau_cut'. 
  Notably, the mutau cuts are more complicated, but it is simple to 
  extend the existing methods as long as one can stomach the line breaks.
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_mutau = ["Lepton_pt", "Lepton_eta", "Lepton_phi", "Lepton_iso",
                  "Muon_dxy", "Muon_dz", "Muon_charge", "Muon_mass", "Muon_tightId",
                  "Tau_dxy", "Tau_dz", "Tau_charge", "Lepton_mass", "Tau_decayMode",
                  "PuppiMET_pt", "PuppiMET_phi", "HTT_m_vis",
                  "nCleanJet", "CleanJet_pt", "CleanJet_eta", "CleanJet_phi", "CleanJet_mass",
                  "Lepton_tauIdx", "Lepton_muIdx", "l1_indices", "l2_indices", 
                  "CleanJet_btagWP", "Tau_leadTkPtOverTauPt",
                  "Tau_rawPNetVSjet", "Tau_rawPNetVSmu", "Tau_rawPNetVSe", "HTT_mT_lmet",
                 ]
  unpack_mutau = add_DeepTau_branches(unpack_mutau, DeepTau_version)
  unpack_mutau = add_trigger_branches(unpack_mutau, era, final_state_mode="mutau")
  has_singletau_VBF = ("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1" in unpack_mutau)
  has_singlemu_VBF = ("HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL" in unpack_mutau)
  unpack_mutau = (event_dictionary.get(key) for key in unpack_mutau)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_mutau] # "*" unpacks a tuple
  # force to_check to always be the right length, even in eras where a trigger isn't available
  if (not has_singletau_VBF): to_check.append(np.zeros(len(event_dictionary["Lepton_pt"]), dtype=bool))
  if (not has_singlemu_VBF): to_check.append(np.zeros(len(event_dictionary["Lepton_pt"]), dtype=bool))
  FS_mu_pt, FS_mu_eta, FS_mu_phi, FS_mu_iso, FS_mu_dxy, FS_mu_dz, FS_mu_chg, FS_mu_mass = [], [], [], [], [], [], [], []
  FS_tau_pt, FS_tau_eta, FS_tau_phi, FS_tau_dxy, FS_tau_dz, FS_tau_chg, FS_tau_mass, FS_tau_DM = [], [], [], [], [], [], [], []
  pass_cuts, FS_mt, FS_nbJet, FS_acoplan, FS_LeadTkPtOverTau = [], [], [], [], []
  FS_mt_branch, FS_mt_diff = [], []
  FS_dphi_mutau, FS_deta_mutau, FS_dpt_mutau = [], [], []
  FS_tau_PNet_v_jet, FS_tau_PNet_v_mu, FS_tau_PNet_v_ele = [], [], []
  FS_trig_idx = []
  for i, lep_pt, lep_eta, lep_phi, lep_iso,\
      mu_dxy, mu_dz, mu_chg, mu_mass, mu_ID_T,\
      tau_dxy, tau_dz, tau_chg, tau_mass, tau_decayMode,\
      MET_pt, MET_phi, mvis,\
      nJet, jet_pt, jet_eta, jet_phi, jet_mass,\
      tau_idx, mu_idx,\
      l1_idx, l2_idx, btag, tau_LeadTkPtOverTauPt,\
      PNetvJet, PNetvMu, PNetvEle, mt_branch,\
      vJet, vMu, vEle,\
      muon_trig, mutau_trig, singletau_VBF_trig, singlemu_VBF_trig in zip(*to_check):

    # in MuTau, muon is always lepton 1 in FS branches, tau is always lepton 2
   
    muFSLoc      = l1_idx
    muBranchLoc  = mu_idx[l1_idx]
    tauFSLoc     = l2_idx
    tauBranchLoc = tau_idx[l2_idx]

    muPt    = lep_pt[muFSLoc] 
    muEta   = lep_eta[muFSLoc]
    muPhi   = lep_phi[muFSLoc]
    muIso   = lep_iso[muFSLoc]
    muDxy   = abs(mu_dxy[muBranchLoc])
    muDz    = abs(mu_dz[muBranchLoc])
    muChg   = mu_chg[muBranchLoc]
    muMass  = mu_mass[muBranchLoc]

    tauPt   = lep_pt[tauFSLoc] 
    tauEta  = lep_eta[tauFSLoc]
    tauPhi  = lep_phi[tauFSLoc]
    tauDxy  = abs(tau_dxy[tauBranchLoc])
    tauDz   = abs(tau_dz[tauBranchLoc])
    tauChg  = tau_chg[tauBranchLoc]
    tauMass = tau_mass[l2_idx]

    mt      = calculate_mt(muPt, muPhi, MET_pt, MET_phi)
    mt_diff = mt - mt_branch
    acoplan = calculate_acoplan(muPhi, tauPhi)

    dphi_mutau = np.acos(np.cos(muPhi - tauPhi))
    deta_mutau = abs(muEta - tauEta)
    dpt_mutau  = muPt - tauPt

    tauPNetvJet = PNetvJet[tauBranchLoc]
    tauPNetvMu  = PNetvMu[tauBranchLoc]
    tauPNetvEle = PNetvEle[tauBranchLoc]

    # move this to other func
    passTauPtAndEta  = ((tauPt > 25.0) and (abs(tauEta) < 2.5)) # prev 30 pT
    pass25MuPt   = ((muon_trig) and (muPt > 25.0) and (abs(muEta) < 2.4))
    # HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1
    passMuPtCrossTrigger = ((mutau_trig) and ((21.0 < muPt < 25.0) and (abs(muEta) < 2.1))
                                       and ((tauPt > 32.0)       and (abs(tauEta) < 2.1)) ) 
    #passMuPtCrossTrigger = False # dummy to turn off crosstrg

    # assign object pts and etas
    j1_pt, j2_pt, mjj = -999, -999, -999 # dummy values to check kinem function
    deta_jj, avg_eta_jj, zepp = -999, -999, -999
    ST = False # special tag
    if nJet == 0: pass
    elif nJet == 1: j1_pt = jet_pt[0]
    else:
      TLorentzJets, j1_idx, j2_idx, mjj, ST = return_TLorentz_Jets(jet_pt, jet_eta, jet_phi, jet_mass)
      j1_pt = TLorentzJets[j1_idx].Pt()
      j2_pt = TLorentzJets[j2_idx].Pt()
      j1_eta = TLorentzJets[j1_idx].Eta()
      j2_eta = TLorentzJets[j2_idx].Eta()
      deta_jj    = j1_eta - j2_eta
      avg_eta_jj = abs((j1_eta + j2_eta)/2)
      zepp_tau       =  -999 if deta_jj==0 else ( ( tauEta - avg_eta_jj) + (tauEta - avg_eta_jj) ) / (2 * deta_jj)
      zepp_mu        =  -999 if deta_jj==0 else ( ( muEta - avg_eta_jj) + (muEta - avg_eta_jj) ) / (2 * deta_jj)

    nJet_idx = 2 if nJet >= 2 else nJet
    jet_reqs = [True, (j1_pt > 30.), (j1_pt > 30. and j2_pt > 30.)][nJet_idx]

    triggers = [muon_trig, mutau_trig, singletau_VBF_trig, singlemu_VBF_trig]
    trig_results = pass_kinems_by_trigger(triggers, muPt, tauPt, muEta, tauEta, j1_pt, j2_pt, mjj, ST, nJet)
    # veto trigger decisions depending on what is available in data
    # for 2022, veto VBFSingleTau since it's not yet available
    # for 2023, veto VBFRun3 since VBFSingleTau takes precedence over that trigger
    # trig_results = [Muon, MuTau, VBFSingleTau]
    if ("2022" in era): trig_results  = np.logical_and(trig_results, [1, 1, 0, 0])
    if ("2023" in era): trig_results  = np.logical_and(trig_results, [1, 1, 1, 1]) # TODO: more handling here in preBPIX
    trig_results  = np.logical_and(trig_results, [1, 1, 0, 1])
    passKinems = (True in trig_results) # kinematics are passed if any of the above triggers+kinems pass

    #if (singletau_VBF_trig) and (not muon_trig) and (not single_muon):
    #  print(trig_results)
    trig_idx = np.where(trig_results)[0][0] if passKinems else -1

    old_trig = passTauPtAndEta and (pass25MuPt or passMuPtCrossTrigger)
    new_trig = passKinems
    #if (old_trig != new_trig) and (jet_reqs): # looking at differences when Jet req is already satisfied
    #if ((singlemu_VBF_trig) and (not muon_trig) and (tauPt < 32)):
    if (False):
      print("#####################################")
      print("#####################################")
      print("# EVENT INFORMATION #")
      print(f" jet info (njet, j1, j2pt, mjj): {nJet}, {j1_pt}, {j2_pt}, {mjj}")
      print(f" tau pT, tau eta: {tauPt}, {tauEta}")
      print(f" muon pT, muon eta: {muPt}, {muEta}")
      print()
      print(f" raw trigs (1mu, 1mu1tau): {muon_trig}, {mutau_trig}, {singletau_VBF_trig}, {singlemu_VBF_trig}")
      print("# OLD TRIGGER METHOD RESULTS #")
      print(f"Pass Tau Pt and Eta: {passTauPtAndEta}")
      print(f"Pass single mu : {pass25MuPt}")
      print(f"Pass crosstrg  : {passMuPtCrossTrigger}") 
      print()
      print("# NEW TRIGGER METHOD RESULTS #")
      print(f"trig_results (1mu, 1mu1tau, VBF1tau, VBF1mu): {trig_results}")
      print(f"trig_idx = {trig_idx}")
      print("**************************************")
      print("**************************************")

    # Tight v Muon, VVVLoose v Ele
    passTauDTLep  = ((vMu[tauBranchLoc] >= 4) and (vEle[tauBranchLoc] >= 2))

    single_DM_encoder = {0: 0, 1: 1, 10:2, 11:3}
    encoded_tau_decayMode = single_DM_encoder[int(tau_decayMode[tauBranchLoc])]
    #restrictTauDM = (tau_decayMode[tauBranchLoc] == 0)
    restrictTauDM = True

    leadTkPtOverTau = tau_LeadTkPtOverTauPt[tauBranchLoc]
    #passLeadTkRatio = (leadTkPtOverTau < 0.9)
    #passZmassWindow = (mvis < 80.0) #(50.0 < mvis < 90.0)

    cut_map = { "Low" : [25, 50],  "Mid" : [50, 70],  "High" : [70, 10000]  }
    subtau_req = True 
    if (tau_pt_cut == "None"): pass # do nothing
    else:
      subtau_req = (cut_map[tau_pt_cut][0] <= tauPt <= cut_map[tau_pt_cut][1])

    pass_bTag = True
    nbJet = 0
    for value in btag:
      if (value > 1): 
        pass_bTag = False
        nbJet += 1

    #if (True):
    if (passKinems and passTauDTLep and subtau_req and jet_reqs):

    #if  (passTauPtAndEta and (pass25MuPt or passMuPtCrossTrigger) 
    #     and passTauDTLep and restrictTauDM and subtau_req and jet_reqs):
      pass_cuts.append(i)
      FS_mu_pt.append(muPt)
      FS_mu_eta.append(muEta)
      FS_mu_phi.append(muPhi)
      FS_mu_iso.append(muIso)
      FS_mu_dxy.append(muDxy)
      FS_mu_dz.append(muDz)
      FS_mu_chg.append(muChg)
      FS_mu_mass.append(muMass)

      FS_tau_pt.append(tauPt)
      FS_tau_eta.append(tauEta)
      FS_tau_phi.append(tauPhi)
      FS_tau_dxy.append(tauDxy)
      FS_tau_dz.append(tauDz)
      FS_tau_chg.append(tauChg)
      FS_tau_mass.append(tauMass)
      FS_tau_DM.append(encoded_tau_decayMode)

      FS_tau_PNet_v_jet.append(tauPNetvJet)
      FS_tau_PNet_v_mu.append(tauPNetvMu)
      FS_tau_PNet_v_ele.append(tauPNetvEle)

      FS_trig_idx.append(trig_idx)

      FS_mt.append(mt)
      FS_mt_branch.append(mt_branch)
      FS_mt_diff.append(mt_diff)
      FS_nbJet.append(nbJet)
      FS_acoplan.append(acoplan)
      FS_dphi_mutau.append(dphi_mutau)
      FS_deta_mutau.append(deta_mutau)
      FS_dpt_mutau.append(dpt_mutau)

      FS_LeadTkPtOverTau.append(leadTkPtOverTau)

  event_dictionary["pass_cuts"]     = np.array(pass_cuts)
  event_dictionary["FS_mu_pt"]      = np.array(FS_mu_pt)
  event_dictionary["FS_mu_eta"]     = np.array(FS_mu_eta)
  event_dictionary["FS_mu_phi"]     = np.array(FS_mu_phi)
  event_dictionary["FS_mu_iso"]     = np.array(FS_mu_iso)
  event_dictionary["FS_mu_dxy"]     = np.array(FS_mu_dxy)
  event_dictionary["FS_mu_dz"]      = np.array(FS_mu_dz)
  event_dictionary["FS_mu_chg"]     = np.array(FS_mu_chg)
  event_dictionary["FS_mu_mass"]    = np.array(FS_mu_mass)
  event_dictionary["FS_tau_pt"]     = np.array(FS_tau_pt)
  event_dictionary["FS_tau_eta"]    = np.array(FS_tau_eta)
  event_dictionary["FS_tau_phi"]    = np.array(FS_tau_phi)
  event_dictionary["FS_tau_dxy"]    = np.array(FS_tau_dxy)
  event_dictionary["FS_tau_dz"]     = np.array(FS_tau_dz)
  event_dictionary["FS_tau_chg"]    = np.array(FS_tau_chg)
  event_dictionary["FS_tau_mass"]   = np.array(FS_tau_mass)
  event_dictionary["FS_tau_DM"]     = np.array(FS_tau_DM)
  event_dictionary["FS_trig_idx"]   = np.array(FS_trig_idx)
  event_dictionary["FS_mt"]         = np.array(FS_mt)
  event_dictionary["FS_mt_branch"]  = np.array(FS_mt_branch)
  event_dictionary["FS_mt_diff"]    = np.array(FS_mt_diff)
  event_dictionary["FS_nbJet"]      = np.array(FS_nbJet)
  event_dictionary["FS_acoplan"]    = np.array(FS_acoplan)
  event_dictionary["FS_dphi_mutau"] = np.array(FS_dphi_mutau)
  event_dictionary["FS_deta_mutau"] = np.array(FS_deta_mutau)
  event_dictionary["FS_dpt_mutau"]  = np.array(FS_dpt_mutau)
  event_dictionary["FS_LeadTkPtOverTau"]  = np.array(FS_LeadTkPtOverTau)
  event_dictionary["FS_tau_rawPNetVSjet"] = np.array(FS_tau_PNet_v_jet)
  event_dictionary["FS_tau_rawPNetVSmu"]  = np.array(FS_tau_PNet_v_mu)
  event_dictionary["FS_tau_rawPNetVSe"]   = np.array(FS_tau_PNet_v_ele)
  nEvents_postcut = len(np.array(pass_cuts))
  print(f"nEvents before and after mutau cuts = {nEvents_precut}, {nEvents_postcut}")
  return event_dictionary


def pass_kinems_by_trigger(triggers, mu_pt, tau_pt, mu_eta, tau_eta, 
                           j1_pt, j2_pt, mjj, special_tag, nJet):
  '''
  Helper function to apply different object kinematic criteria depending on trigger used
  the if blocks below are intended to be mutually exclusive, prioritizing less complicated triggers over others.
  In 2022, the order is DiTau, DiTau+Jet, DiTau VBFRun3
  In 2023, the order is DiTau, DiTau+Jet, VBF+SingleTau (if available, otherwise DiTau VBFRun3 is used)
  '''

  muon_trig, mutau_trig, singletau_VBF_trig, singlemu_VBF_trig = triggers

  passEventJetKinems = False
  if (nJet == 0):   passEventJetKinems = True # no jet requirements in nJet=0 category
  elif (nJet == 1): passEventJetKinems = (j1_pt > 30.)
  else:             passEventJetKinems = ((j1_pt > 30.) and (j2_pt > 30.) and (mjj > 350)) # nJet >= 2

  #passEventTauKinems  = (tau_pt > 20.) and (abs(tau_eta) < 2.5) # prev 30 pT
  passEventTauKinems  = (tau_pt > 25.) and (abs(tau_eta) < 2.5) # prev 30 pT
  passEventMuonKinems = (mu_pt > 10.)  and (abs(mu_eta) < 2.4)

  #print("# EVENT INFORMATION IN PASS KINEM FUNCTION#")
  #print(f" jet info (njet, j1, j2pt): {nJet}, {j1_pt}, {j2_pt}")
  #print(f" tau pT, tau eta: {tau_pt}, {tau_eta}")
  #print(f" muon pT, muon eta: {mu_pt}, {mu_eta}")
  #print(f" raw trigs (1mu, 1mu1tau): {muon_trig}, {mutau_trig}")

  passTrigMuonKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_single_muon = False
  if muon_trig:
    passTrigMuonKinems = ((passEventMuonKinems) and (mu_pt > 25.))
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 25.))
    passTrigJetKinems  = (passEventJetKinems)
    if (passTrigMuonKinems and passTrigTauKinems and passTrigJetKinems): pass_single_muon = True

  passTrigMuonKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_mutau = False
  if (mutau_trig):
    passTrigMuonKinems = ((passEventMuonKinems) and (mu_pt > 21.) and (mu_pt < 25.) and (abs(mu_eta) < 2.1))
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 32) and (abs(tau_eta) < 2.1))
    passTrigJetKinems  = (passEventJetKinems)
    if (passTrigMuonKinems and passTrigTauKinems and passTrigJetKinems): pass_mutau = True
    if (pass_mutau): pass_single_muon = False # enforce othrogonal trigger coverage
  #print(f" event flags: {passEventMuonKinems}, {passEventTauKinems}, {passEventJetKinems}")
  #print(f" block trig  flags: {passTrigMuonKinems}, {passTrigTauKinems}, {passTrigJetKinems}")
  #print(f" final trig  flags: {pass_single_muon}, {pass_mutau}")#, {pass_singletau_VBF}")
  #print("**************************************")

  passTrigMuonKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_singletau_VBF = False
  #if (singletau_VBF_trig) and not (mutau_trig) and not (muon_trig):
  if (singletau_VBF_trig):
    passTrigMuonKinems = (passEventMuonKinems)
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 45) and (abs(tau_eta) < 2.1))
    passTrigJetKinems  = ((passEventJetKinems) and (j1_pt > 45) and (j2_pt > 45) and (mjj > 500))
    if (passTrigMuonKinems and passTrigTauKinems and passTrigJetKinems): pass_singletau_VBF = True

  passTrigMuonKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_singlemu_VBF = False
  if (singlemu_VBF_trig):
    passTrigMuonKinems = (passEventMuonKinems)
    passTrigTauKinems  = (passEventTauKinems)
    passTrigJetKinems  = ((passEventJetKinems) and (j1_pt > 90) and (j2_pt > 40) and (mjj > 600))
    if (passTrigMuonKinems and passTrigTauKinems and passTrigJetKinems): pass_singlemu_VBF = True

  return [pass_single_muon, pass_mutau, pass_singletau_VBF, pass_singlemu_VBF]
  #return [pass_single_muon, pass_mutau, pass_singletau_VBF]
  #return [pass_single_muon, pass_mutau, False]


def make_mutau_region(event_dictionary, new_branch_name, FS_pair_sign, pass_mu_iso_req, mu_iso_value,
                      pass_DeepTau_req, DeepTau_value, DeepTau_version,
                      pass_mt_req, mt_value, pass_BTag_req):
  unpack_mutau_vars = ["event", "Lepton_tauIdx", "Lepton_muIdx", "Lepton_iso", 
                       "l1_indices", "l2_indices", "HTT_pdgId",
                       "Lepton_pt", "Lepton_phi", "PuppiMET_pt", "PuppiMET_phi", 
                       "CleanJet_btagWP", "HTT_mT_lmet"]
  unpack_mutau_vars = add_DeepTau_branches(unpack_mutau_vars, DeepTau_version)
  unpack_mutau_vars = (event_dictionary.get(key) for key in unpack_mutau_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_mutau_vars]
  pass_cuts = []
  for i, event, tau_idx, mu_idx, lep_iso, l1_idx, l2_idx, signed_pdgId,\
      lep_pt, lep_phi, MET_pt, MET_phi, btag, mt,\
      vJet, vMu, vEle in zip(*to_check):

    muFSLoc      = l1_idx
    muBranchLoc  = mu_idx[l1_idx]
    tauFSLoc     = l2_idx
    tauBranchLoc = tau_idx[l2_idx]

    mu_iso     = lep_iso[muFSLoc]
    # puts mu_iso between 0.05 and 0.15 for DRsr and DRar, but makes aiso cases difficult
    pass_mu_iso = (mu_iso_value[0] <= mu_iso < mu_iso_value[1])

    pass_DeepTau  = (vJet[tauBranchLoc] >= DeepTau_value)

    muPt    = lep_pt[muFSLoc]
    muPhi   = lep_phi[muFSLoc]
    #passMT     = (calculate_mt(muPt, muPhi, MET_pt, MET_phi) < mt_value)
    passMT  = (mt < mt_value)

    passBTag = True
    for value in btag:
      if (value > 1): passBTag = False

    if ( (np.sign(signed_pdgId) == FS_pair_sign) and 
         (pass_mu_iso == pass_mu_iso_req) and (pass_DeepTau == pass_DeepTau_req) and 
         (passMT == pass_mt_req) and (passBTag == pass_BTag_req) ):
      pass_cuts.append(i)
    
  event_dictionary[new_branch_name] = np.array(pass_cuts)
  return event_dictionary
