import numpy as np # TODO is importing this everywhere slowing things down? does python have IFDEF commands?

from calculate_functions import calculate_mt, calculate_acoplan
from branch_functions import add_trigger_branches, add_DeepTau_branches

def make_etau_cut(event_dictionary, DeepTau_version, skip_DeepTau=False, tau_pt_cut="None"):
  '''
  Works similarly to 'make_ditau_cut'. 
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_etau = ["Lepton_pt", "Lepton_eta", "Lepton_phi", "Lepton_iso",
                 "Electron_dxy", "Electron_dz", "Electron_charge", "Electron_mass", 
                 "Tau_dxy", "Tau_dz", "Tau_charge", "Lepton_mass", "Tau_decayMode",
                 "PuppiMET_pt", "PuppiMET_phi", 
                 "Lepton_tauIdx", "Lepton_elIdx", "l1_indices", "l2_indices",
                 #"Tau_rawPNetVSjet", "Tau_rawPNetVSmu", "Tau_rawPNetVSe"
                 "CleanJet_btagWP",
                 ]
  unpack_etau = add_DeepTau_branches(unpack_etau, DeepTau_version)
  unpack_etau = add_trigger_branches(unpack_etau, final_state_mode="etau")
  unpack_etau = (event_dictionary.get(key) for key in unpack_etau)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_etau]
  pass_cuts, FS_mt, FS_nbJet = [], [], []
  FS_el_pt, FS_el_eta, FS_el_phi, FS_el_iso, FS_el_dxy, FS_el_dz, FS_el_chg, FS_el_mass = [], [], [], [], [], [], [], []
  FS_tau_pt, FS_tau_eta, FS_tau_phi, FS_tau_dxy, FS_tau_dz, FS_tau_chg, FS_tau_mass, FS_tau_DM = [], [], [], [], [], [], [], []
  FS_dphi_etau, FS_deta_etau = [], []
  for i, lep_pt, lep_eta, lep_phi, lep_iso,\
      el_dxy, el_dz, el_chg, el_mass, tau_dxy, tau_dz, tau_chg, tau_mass, tau_decayMode,\
      MET_pt, MET_phi, tau_idx, el_idx,\
      l1_idx, l2_idx, btag,\
      vJet, vMu, vEle, trg30el, trg32el, trg35el, crosstrg in zip(*to_check):

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
    elDz    = el_dz[elBranchLoc]
    elChg   = el_chg[elBranchLoc]
    elMass  = el_mass[elBranchLoc]
    tauPt   = lep_pt[tauFSLoc] 
    tauEta  = lep_eta[tauFSLoc]
    tauPhi  = lep_phi[tauFSLoc]
    tauDxy  = abs(tau_dxy[tauBranchLoc])
    tauDz   = tau_dz[tauBranchLoc]
    tauChg  = tau_chg[tauBranchLoc]
    tauMass = tau_mass[l2_idx]
    mt      = calculate_mt(elPt, elPhi, MET_pt, MET_phi)

    dphi_etau = np.acos(np.cos(elPhi - tauPhi))
    deta_etau = abs(elEta - tauEta)

    passTauPtAndEta  = ((tauPt > 25.0) and (abs(tauEta) < 2.5))
    pass31ElPt   = ((trg30el) and (elPt > 31.0) and (abs(elEta) < 2.5))
    pass33ElPt   = ((trg32el) and (elPt > 33.0) and (abs(elEta) < 2.5))
    pass36ElPt   = ((trg35el) and (elPt > 36.0) and (abs(elEta) < 2.5))
    # upper bound on cross trigger will change if lower single electron trigger included
    # HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1
    passElPtCrossTrigger = ((crosstrg) and ((25.0 < elPt < 31.0) and (abs(elEta) < 2.1))
                                       and ((tauPt > 35.0)       and (abs(tauEta) < 2.1)) ) 
    #passElPtCrossTrigger = False # dummy to turn off crosstrg

    # Medium (5) v Jet, VLoose (1) v Muon, Tight (6) v Ele
    passTauDTLep  = ((vMu[tauBranchLoc] >= 1) and (vEle[tauBranchLoc] >= 6))

    single_DM_encoder = {0: 0, 1: 1, 10:2, 11:3}
    encoded_tau_decayMode = single_DM_encoder[int(tau_decayMode[tauBranchLoc])]
    #restrictTauDM = (tau_decayMode[tauBranchLoc] == 0)
    restrictTauDM = True

    pass_bTag = True
    nbJet = 0
    bveto = 0
    for value in btag:
      if (value > 1): 
        bveto += value
        if bveto > 1: pass_bTag = False
        nbJet += 1
    # hacky barrel restriction (can you try removing DM2 also?)
    #if (abs(tauEta) < 1.5):
    #  passTauPtAndEta = False
    #if (abs(elEta) < 1.5):
    #  pass33ElPt, pass36ElPt, passElPtCrossTrigger = False, False, False
    #if (passTauPtAndEta and (pass33ElPt or pass36ElPt or passElPtCrossTrigger) and passTauDTLep and restrict_tau_DM):
    #if (passTauPtAndEta and (pass33ElPt or pass36ElPt or passElPtCrossTrigger) and passTauDTLep):
    if (passTauPtAndEta and (pass31ElPt or pass33ElPt or pass36ElPt or passElPtCrossTrigger) and passTauDTLep):
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

      FS_mt.append(mt)
      FS_nbJet.append(nbJet)
      FS_dphi_etau.append(dphi_etau)
      FS_deta_etau.append(deta_etau)

  event_dictionary["pass_cuts"]  = np.array(pass_cuts)
  event_dictionary["FS_el_pt"]   = np.array(FS_el_pt)
  event_dictionary["FS_el_eta"]  = np.array(FS_el_eta)
  event_dictionary["FS_el_phi"]  = np.array(FS_el_phi)
  event_dictionary["FS_el_iso"]  = np.array(FS_el_iso)
  event_dictionary["FS_el_dxy"]  = np.array(FS_el_dxy)
  event_dictionary["FS_el_dz"]   = np.array(FS_el_dz)
  event_dictionary["FS_el_chg"]  = np.array(FS_el_chg)
  event_dictionary["FS_el_mass"] = np.array(FS_el_mass)
  event_dictionary["FS_tau_pt"]  = np.array(FS_tau_pt)
  event_dictionary["FS_tau_eta"] = np.array(FS_tau_eta)
  event_dictionary["FS_tau_phi"] = np.array(FS_tau_phi)
  event_dictionary["FS_tau_dxy"] = np.array(FS_tau_dxy)
  event_dictionary["FS_tau_dz"]  = np.array(FS_tau_dz)
  event_dictionary["FS_tau_chg"] = np.array(FS_tau_chg)
  event_dictionary["FS_tau_mass"] = np.array(FS_tau_mass)
  event_dictionary["FS_tau_DM"] = np.array(FS_tau_DM)
  event_dictionary["FS_mt"]      = np.array(FS_mt)
  event_dictionary["FS_nbJet"] = np.array(FS_nbJet)
  event_dictionary["FS_dphi_etau"] = np.array(FS_dphi_etau)
  event_dictionary["FS_deta_etau"] = np.array(FS_deta_etau)
  nEvents_postcut = len(np.array(pass_cuts))
  print(f"nEvents before and after etau cuts = {nEvents_precut}, {nEvents_postcut}")
  return event_dictionary

# no longer used?
#def make_etau_AR_cut(event_dictionary, DeepTau_version):
#  unpack_etau_AR_vars = ["event", "Lepton_tauIdx", "Lepton_elIdx", "Lepton_iso", "l1_indices", "l2_indices"]
#  unpack_etau_AR_vars = add_DeepTau_branches(unpack_etau_AR_vars, DeepTau_version)
#  unpack_etau_AR_vars = (event_dictionary.get(key) for key in unpack_etau_AR_vars)
#  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_etau_AR_vars]
#  pass_AR_cuts = []
#  for i, event, tau_idx, ele_idx, lep_iso, l1_idx, l2_idx, vJet, _, _ in zip(*to_check):
#    # keep indices where tau fails and muon passes iso 
#    ele_lep_idx = l1_idx if ele_idx[l1_idx] != -1 else l2_idx
#    ele_iso = lep_iso[ele_lep_idx]
#    tau_branchIdx  = tau_idx[l1_idx] + tau_idx[l2_idx] + 1
#    if ((vJet[tau_branchIdx] < 5) and (ele_iso<0.15)):
#      pass_AR_cuts.append(i)
#  
#  event_dictionary["pass_AR_cuts"] = np.array(pass_AR_cuts)
#  return event_dictionary

def make_etau_region(event_dictionary, new_branch_name, FS_pair_sign, pass_el_iso_req, el_iso_value,
                     pass_DeepTau_req, DeepTau_value, DeepTau_version,
                     pass_mt_req, mt_value, pass_BTag_req):
  unpack_etau_vars = ["event", "Lepton_tauIdx", "Lepton_elIdx", "Lepton_iso", 
                       "l1_indices", "l2_indices", "HTT_pdgId",
                       "Lepton_pt", "Lepton_phi", "PuppiMET_pt", "PuppiMET_phi", 
                       "CleanJet_btagWP"]
  unpack_etau_vars = add_DeepTau_branches(unpack_etau_vars, DeepTau_version)
  unpack_etau_vars = (event_dictionary.get(key) for key in unpack_etau_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_etau_vars]
  pass_cuts = []
  for i, event, tau_idx, el_idx, lep_iso, l1_idx, l2_idx, signed_pdgId,\
      lep_pt, lep_phi, MET_pt, MET_phi, btag,\
      vJet, vMu, vEle in zip(*to_check):

    el_lep_idx = l1_idx if el_idx[l1_idx] != -1 else l2_idx
    el_iso     = lep_iso[el_lep_idx]
    pass_el_iso = (el_iso < el_iso_value)

    tau_branchIdx = tau_idx[l1_idx] + tau_idx[l2_idx] + 1
    pass_DeepTau  = (vJet[tau_branchIdx] >= DeepTau_value)

    elPt    = lep_pt[el_lep_idx]
    elPhi   = lep_phi[el_lep_idx]
    passMT     = (calculate_mt(elPt, elPhi, MET_pt, MET_phi) < mt_value)

    passBTag = True
    bveto = 0
    for value in btag:
      if (value > 0):
        bveto += value
        if bveto > 1: passBTag = False

    if ( (np.sign(signed_pdgId) == FS_pair_sign) and 
         (pass_el_iso == pass_el_iso_req) and (pass_DeepTau == pass_DeepTau_req) and 
         (passMT == pass_mt_req) and (passBTag == pass_BTag_req) ):
      pass_cuts.append(i)
    
  event_dictionary[new_branch_name] = np.array(pass_cuts)
  return event_dictionary


