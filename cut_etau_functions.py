import numpy as np

from calculate_functions import calculate_mt, calculate_acoplan, return_TLorentz_Jets
from branch_functions import add_trigger_branches, add_DeepTau_branches

def make_etau_cut(era, event_dictionary, DeepTau_version, skip_DeepTau=False, tau_pt_cut="None"):
  '''
  Works similarly to 'make_ditau_cut'. 
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_etau = ["Lepton_pt", "Lepton_eta", "Lepton_phi", "Lepton_iso",
                 "Electron_dxy", "Electron_dz", "Electron_charge", "Electron_mass", 
                 "Tau_dxy", "Tau_dz", "Tau_charge", "Lepton_mass", "Tau_decayMode",
                 "PuppiMET_pt", "PuppiMET_phi", "HTT_m_vis",
                 "nCleanJet", "CleanJet_pt", "CleanJet_eta", "CleanJet_phi", "CleanJet_mass",
                 "Lepton_tauIdx", "Lepton_elIdx", "l1_indices", "l2_indices",
                 "CleanJet_btagWP", "HTT_mT_lmet",
                 "Tau_rawPNetVSjet", "Tau_rawPNetVSmu", "Tau_rawPNetVSe"
                 ]
  unpack_etau = add_DeepTau_branches(unpack_etau, DeepTau_version)
  unpack_etau = add_trigger_branches(unpack_etau, era, final_state_mode="etau")
  has_singletau_VBF = ("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1" in unpack_etau)
  has_singleele_VBF = ("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf" in unpack_etau)
  unpack_etau = (event_dictionary.get(key) for key in unpack_etau)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_etau]
  # force to_check to always be the right length, even in eras where a trigger isn't available
  if (not has_singletau_VBF): to_check.append(np.zeros(len(event_dictionary["Lepton_pt"]), dtype=bool))
  if (not has_singleele_VBF): to_check.append(np.zeros(len(event_dictionary["Lepton_pt"]), dtype=bool))
  FS_el_pt, FS_el_eta, FS_el_phi, FS_el_iso, FS_el_dxy, FS_el_dz, FS_el_chg, FS_el_mass = [], [], [], [], [], [], [], []
  FS_tau_pt, FS_tau_eta, FS_tau_phi, FS_tau_dxy, FS_tau_dz, FS_tau_chg, FS_tau_mass, FS_tau_DM = [], [], [], [], [], [], [], []
  pass_cuts, FS_mt, FS_nbJet, FS_acoplan = [], [], [], []
  FS_dphi_etau, FS_deta_etau, FS_dpt_etau = [], [], []
  FS_tau_PNet_v_jet, FS_tau_PNet_v_mu, FS_tau_PNet_v_ele = [], [], []
  FS_trig_idx = []
  for i, lep_pt, lep_eta, lep_phi, lep_iso,\
      el_dxy, el_dz, el_chg, el_mass,\
      tau_dxy, tau_dz, tau_chg, tau_mass, tau_decayMode,\
      MET_pt, MET_phi, mvis,\
      nJet, jet_pt, jet_eta, jet_phi, jet_mass,\
      tau_idx, el_idx, l1_idx, l2_idx,\
      btag, mt_branch,\
      PNetvJet, PNetvMu, PNetvEle,\
      vJet, vMu, vEle, ele_trig, etau_trig, singletau_VBF_trig, singleele_VBF_trig in zip(*to_check):

    # in ETau, electron is always lepton 1 in FS branches, tau is always lepton 2

    elFSLoc      = l1_idx
    elBranchLoc  = el_idx[l1_idx]
    tauFSLoc     = l2_idx
    tauBranchLoc = tau_idx[l2_idx]

    elPt    = lep_pt[elFSLoc] 
    elEta   = lep_eta[elFSLoc]
    elPhi   = lep_phi[elFSLoc]
    elIso   = lep_iso[elFSLoc]
    elDxy   = abs(el_dxy[elBranchLoc])
    elDz    = abs(el_dz[elBranchLoc])
    elChg   = el_chg[elBranchLoc]
    elMass  = el_mass[elBranchLoc]

    tauPt   = lep_pt[tauFSLoc] 
    tauEta  = lep_eta[tauFSLoc]
    tauPhi  = lep_phi[tauFSLoc]
    tauDxy  = abs(tau_dxy[tauBranchLoc])
    tauDz   = abs(tau_dz[tauBranchLoc])
    tauChg  = tau_chg[tauBranchLoc]
    tauMass = tau_mass[l2_idx]

    mt      = calculate_mt(elPt, elPhi, MET_pt, MET_phi)
    acoplan = calculate_acoplan(elPhi, tauPhi)

    try:
      dphi_etau = np.acos(np.cos(elPhi - tauPhi))
    except AttributeError:
      dphi_etau = np.arccos(np.cos(elPhi - tauPhi))
    deta_etau = abs(elEta - tauEta)
    dpt_etau  = elPt - tauPt

    tauPNetvJet = PNetvJet[tauBranchLoc]
    tauPNetvMu  = PNetvMu[tauBranchLoc]
    tauPNetvEle = PNetvEle[tauBranchLoc]


    passTauPtAndEta  = ((tauPt > 25.0) and (abs(tauEta) < 2.5))
    pass31ElPt   = ((ele_trig) and (elPt > 31.0) and (abs(elEta) < 2.5))
    # upper bound on cross trigger will change if lower single electron trigger included
    # HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1
    passElPtCrossTrigger = ((etau_trig) and ((25.0 < elPt < 31.0) and (abs(elEta) < 2.1))
                                       and ((tauPt > 35.0)       and (abs(tauEta) < 2.1)) ) 
    #passElPtCrossTrigger = False # dummy to turn off crosstrg

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
      zepp_mu        =  -999 if deta_jj==0 else ( ( elEta - avg_eta_jj) + (elEta - avg_eta_jj) ) / (2 * deta_jj)

    nJet_idx = 2 if nJet >= 2 else nJet
    jet_reqs = [True, (j1_pt > 30.), (j1_pt > 30. and j2_pt > 30.)][nJet_idx]

    triggers = [ele_trig, etau_trig, singletau_VBF_trig, singleele_VBF_trig]
    trig_results = pass_kinems_by_trigger(triggers, elPt, tauPt, elEta, tauEta, j1_pt, j2_pt, mjj, ST, nJet)
    # veto trigger decisions depending on what is available in data
    # for 2022, veto VBFSingleTau since it's not yet available
    # for 2023, veto VBFRun3 since VBFSingleTau takes precedence over that trigger
    # trig_results = [Ele, ETau, VBFSingleTau, VBFSingleEle]
    if ("2022" in era): trig_results  = np.logical_and(trig_results, [1, 1, 0, 0])
    if ("2023" in era): trig_results  = np.logical_and(trig_results, [1, 1, 1, 1]) # TODO: more handling here in preBPIX
    trig_results  = np.logical_and(trig_results, [1, 1, 0, 1])
    passKinems = (True in trig_results) # kinematics are passed if any of the above triggers+kinems pass

    trig_idx = np.where(trig_results)[0][0] if passKinems else -1

    old_trig = passTauPtAndEta and (pass31ElPt or passElPtCrossTrigger)
    new_trig = passKinems
    #if (old_trig != new_trig) and (jet_reqs): # looking at differences when Jet req is already satisfied
    #if ((singlemu_VBF_trig) and (not muon_trig) and (tauPt < 32)):
    if (False):
      print("#####################################")
      print("#####################################")
      print("# EVENT INFORMATION #")
      print(f" jet info (njet, j1, j2pt, mjj): {nJet}, {j1_pt}, {j2_pt}, {mjj}")
      print(f" tau pT, tau eta: {tauPt}, {tauEta}")
      print(f" ele pT, ele eta: {elPt}, {elEta}")
      print()
      print(f" raw trigs (1e, 1e1tau): {ele_trig}, {etau_trig}, {singletau_VBF_trig}, {singleele_VBF_trig}")
      print("# OLD TRIGGER METHOD RESULTS #")
      print(f"Pass Tau Pt and Eta: {passTauPtAndEta}")
      print(f"Pass single e : {pass31ElPt}")
      print(f"Pass crosstrg  : {passElPtCrossTrigger}") 
      print()
      print("# NEW TRIGGER METHOD RESULTS #")
      print(f"trig_results (1e, 1e1tau, VBF1tau, VBF1e): {trig_results}")
      print(f"trig_idx = {trig_idx}")
      print("**************************************")
      print("**************************************")

    # Medium (5) v Jet, VLoose (1) v Muon, Tight (6) v Ele
    passTauDTLep  = ((vMu[tauBranchLoc] >= 1) and (vEle[tauBranchLoc] >= 6))

    single_DM_encoder = {0: 0, 1: 1, 10:2, 11:3}
    encoded_tau_decayMode = single_DM_encoder[int(tau_decayMode[tauBranchLoc])]
    #restrictTauDM = (tau_decayMode[tauBranchLoc] == 0)
    restrictTauDM = True

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

    #if (passTauPtAndEta and (pass31ElPt or passElPtCrossTrigger) 
    #     and passTauDTLep and restrictTauDM and subtau_req and jet_reqs):
      pass_cuts.append(i)
      FS_el_pt.append(elPt)
      FS_el_eta.append(elEta)
      FS_el_phi.append(elPhi)
      FS_el_iso.append(elIso)
      FS_el_dxy.append(elDxy)
      FS_el_dz.append(elDz)
      FS_el_chg.append(elChg)
      FS_el_mass.append(elMass)

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
      FS_nbJet.append(nbJet)
      FS_acoplan.append(acoplan)
      FS_dphi_etau.append(dphi_etau)
      FS_deta_etau.append(deta_etau)
      FS_dpt_etau.append(dpt_etau)

  event_dictionary["pass_cuts"]    = np.array(pass_cuts)
  event_dictionary["FS_el_pt"]     = np.array(FS_el_pt)
  event_dictionary["FS_el_eta"]    = np.array(FS_el_eta)
  event_dictionary["FS_el_phi"]    = np.array(FS_el_phi)
  event_dictionary["FS_el_iso"]    = np.array(FS_el_iso)
  event_dictionary["FS_el_dxy"]    = np.array(FS_el_dxy)
  event_dictionary["FS_el_dz"]     = np.array(FS_el_dz)
  event_dictionary["FS_el_chg"]    = np.array(FS_el_chg)
  event_dictionary["FS_el_mass"]   = np.array(FS_el_mass)
  event_dictionary["FS_tau_pt"]    = np.array(FS_tau_pt)
  event_dictionary["FS_tau_eta"]   = np.array(FS_tau_eta)
  event_dictionary["FS_tau_phi"]   = np.array(FS_tau_phi)
  event_dictionary["FS_tau_dxy"]   = np.array(FS_tau_dxy)
  event_dictionary["FS_tau_dz"]    = np.array(FS_tau_dz)
  event_dictionary["FS_tau_chg"]   = np.array(FS_tau_chg)
  event_dictionary["FS_tau_mass"]  = np.array(FS_tau_mass)
  event_dictionary["FS_tau_DM"]    = np.array(FS_tau_DM)
  event_dictionary["FS_trig_idx"]   = np.array(FS_trig_idx)
  event_dictionary["FS_mt"]        = np.array(FS_mt)
  event_dictionary["FS_nbJet"]     = np.array(FS_nbJet)
  event_dictionary["FS_acoplan"]   = np.array(FS_acoplan)
  event_dictionary["FS_dphi_etau"] = np.array(FS_dphi_etau)
  event_dictionary["FS_deta_etau"] = np.array(FS_deta_etau)
  event_dictionary["FS_dpt_etau"]  = np.array(FS_dpt_etau)
  event_dictionary["FS_tau_rawPNetVSjet"] = np.array(FS_tau_PNet_v_jet)
  event_dictionary["FS_tau_rawPNetVSmu"]  = np.array(FS_tau_PNet_v_mu)
  event_dictionary["FS_tau_rawPNetVSe"]   = np.array(FS_tau_PNet_v_ele)
  nEvents_postcut = len(np.array(pass_cuts))
  print(f"nEvents before and after etau cuts = {nEvents_precut}, {nEvents_postcut}")
  return event_dictionary


def pass_kinems_by_trigger(triggers, el_pt, tau_pt, el_eta, tau_eta,
                           j1_pt, j2_pt, mjj, special_tag, nJet):
  '''
  Helper function to apply different object kinematic criteria depending on trigger used
  the if blocks below are intended to be mutually exclusive, prioritizing less complicated triggers over others.
  '''

  ele_trig, etau_trig, singletau_VBF_trig, singleele_VBF_trig = triggers

  passEventJetKinems = False
  if (nJet == 0):   passEventJetKinems = True # no jet requirements in nJet=0 category
  elif (nJet == 1): passEventJetKinems = (j1_pt > 30.)
  else:             passEventJetKinems = ((j1_pt > 30.) and (j2_pt > 30.)) # nJet >= 2
  #else:             passEventJetKinems = ((j1_pt > 30.) and (j2_pt > 30.) and (mjj > 350)) # nJet >= 2

  #passEventTauKinems  = (tau_pt > 20.) and (abs(tau_eta) < 2.5)
  passEventTauKinems  = (tau_pt > 25.) and (abs(tau_eta) < 2.5)
  passEventEleKinems = (el_pt > 10.)  and (abs(el_eta) < 2.5)

  #print("# EVENT INFORMATION IN PASS KINEM FUNCTION#")
  #print(f" jet info (njet, j1, j2pt): {nJet}, {j1_pt}, {j2_pt}")
  #print(f" tau pT, tau eta: {tau_pt}, {tau_eta}")
  #print(f" ele pT, ele eta: {el_pt}, {el_eta}")
  #print(f" raw trigs (1e, 1e1tau): {ele_trig}, {etau_trig}")

  passTrigEleKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_single_ele = False
  if ele_trig:
    passTrigEleKinems  = ((passEventEleKinems) and (el_pt > 31.))
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 25.))
    passTrigJetKinems  = (passEventJetKinems)
    if (passTrigEleKinems and passTrigTauKinems and passTrigJetKinems): pass_single_ele = True

  passTrigEleKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_etau = False
  if (etau_trig):
    passTrigEleKinems  = ((passEventEleKinems) and (el_pt > 25.) and (el_pt < 31.) and (abs(el_eta) < 2.1))
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 35) and (abs(tau_eta) < 2.1))
    passTrigJetKinems  = (passEventJetKinems)
    if (passTrigEleKinems and passTrigTauKinems and passTrigJetKinems): pass_etau = True
    if (pass_etau): pass_single_ele = False # enforce othrogonal trigger coverage

  passTrigEleKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_singletau_VBF = False
  if (singletau_VBF_trig):
    passTrigEleKinems  = (passEventEleKinems)
    passTrigTauKinems  = ((passEventTauKinems) and (tau_pt > 45) and (abs(tau_eta) < 2.1))
    passTrigJetKinems  = ((passEventJetKinems) and (j1_pt > 45) and (j2_pt > 45) and (mjj > 500))
    if (passTrigEleKinems and passTrigTauKinems and passTrigJetKinems): pass_singletau_VBF = True

  passTrigEleKinems, passTrigTauKinems, passTrigJetKinems = False, False, False
  pass_singleele_VBF = False
  if (singleele_VBF_trig):
    passTrigEleKinems  = ((passEventEleKinems) and (el_pt > 18) and (abs(el_eta) < 2.1))
    passTrigTauKinems  = (passEventTauKinems)
    passTrigJetKinems  = ((passEventJetKinems) and (j1_pt > 50) and (j2_pt > 50) and (mjj > 550))
    if (passTrigEleKinems and passTrigTauKinems and passTrigJetKinems): pass_singleele_VBF = True

  return [pass_single_ele, pass_etau, pass_singletau_VBF, pass_singleele_VBF]


def make_etau_region(event_dictionary, new_branch_name, FS_pair_sign, pass_el_iso_req, el_iso_value,
                     pass_DeepTau_req, DeepTau_value, DeepTau_version,
                     pass_mt_req, mt_value, pass_BTag_req):
  unpack_etau_vars = ["event", "Lepton_tauIdx", "Lepton_elIdx", "Lepton_iso", 
                       "l1_indices", "l2_indices", "HTT_pdgId",
                       "Lepton_pt", "Lepton_phi", "PuppiMET_pt", "PuppiMET_phi", 
                       "CleanJet_btagWP", "HTT_mT_lmet"]
  unpack_etau_vars = add_DeepTau_branches(unpack_etau_vars, DeepTau_version)
  unpack_etau_vars = (event_dictionary.get(key) for key in unpack_etau_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_etau_vars]
  pass_cuts = []
  for i, event, tau_idx, el_idx, lep_iso, l1_idx, l2_idx, signed_pdgId,\
      lep_pt, lep_phi, MET_pt, MET_phi, btag, mt,\
      vJet, vMu, vEle in zip(*to_check):

    elFSLoc      = l1_idx
    elBranchLoc  = el_idx[l1_idx]
    tauFSLoc     = l2_idx
    tauBranchLoc = tau_idx[l2_idx]

    el_iso     = lep_iso[elFSLoc]
    # puts el_iso between 0.05 and 0.15 for DRsr and DRar QCD
    pass_el_iso = (el_iso_value[0] <= el_iso < el_iso_value[1])

    pass_DeepTau  = (vJet[tauBranchLoc] >= DeepTau_value)

    elPt    = lep_pt[elFSLoc]
    elPhi   = lep_phi[elFSLoc]
    passMT     = (mt < mt_value)

    passBTag = True
    for value in btag:
      if (value > 1): passBTag = False

    if ( (np.sign(signed_pdgId) == FS_pair_sign) and 
         (pass_el_iso == pass_el_iso_req) and (pass_DeepTau == pass_DeepTau_req) and 
         (passMT == pass_mt_req) and (passBTag == pass_BTag_req) ):
      pass_cuts.append(i)
    
  event_dictionary[new_branch_name] = np.array(pass_cuts)
  return event_dictionary
