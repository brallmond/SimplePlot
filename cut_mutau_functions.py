import numpy as np

from calculate_functions import calculate_mt, calculate_acoplan
from branch_functions import add_trigger_branches, add_DeepTau_branches

def make_mutau_cut(era, event_dictionary, DeepTau_version, skip_DeepTau=False, tau_pt_cut="None"):
  '''
  Works similarly to 'make_ditau_cut'. 
  Notably, the mutau cuts are more complicated, but it is simple to 
  extend the existing methods as long as one can stomach the line breaks.
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_mutau = ["Lepton_pt", "Lepton_eta", "Lepton_phi", "Lepton_iso",
                  "Muon_dxy", "Muon_dz", "Muon_charge", "Muon_mass",
                  "Tau_dxy", "Tau_dz", "Tau_charge", "Lepton_mass", "Tau_decayMode",
                  "PuppiMET_pt", "PuppiMET_phi", "HTT_m_vis",
                  "Lepton_tauIdx", "Lepton_muIdx", "l1_indices", "l2_indices", 
                  "Tau_rawPNetVSjet", "Tau_rawPNetVSmu", "Tau_rawPNetVSe"
                  "CleanJet_btagWP", "Tau_leadTkPtOverTauPt"
                 ]
  unpack_mutau = add_DeepTau_branches(unpack_mutau, DeepTau_version)
  unpack_mutau = add_trigger_branches(unpack_mutau, era, final_state_mode="mutau")
  unpack_mutau = (event_dictionary.get(key) for key in unpack_mutau)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_mutau] # "*" unpacks a tuple
  FS_mu_pt, FS_mu_eta, FS_mu_phi, FS_mu_iso, FS_mu_dxy, FS_mu_dz, FS_mu_chg, FS_mu_mass = [], [], [], [], [], [], [], []
  FS_tau_pt, FS_tau_eta, FS_tau_phi, FS_tau_dxy, FS_tau_dz, FS_tau_chg, FS_tau_mass, FS_tau_DM = [], [], [], [], [], [], [], []
  pass_cuts, FS_mt, FS_nbJet, FS_acoplan, FS_LeadTkPtOverTau = [], [], [], [], []
  FS_dphi_mutau, FS_deta_mutau = [], []
  FS_tau_PNet_v_jet, FS_tau_PNet_v_mu, FS_tau_PNet_v_ele = [], [], []
  for i, lep_pt, lep_eta, lep_phi, lep_iso,\
      mu_dxy, mu_dz, mu_chg, mu_mass,\
      tau_dxy, tau_dz, tau_chg, tau_mass, tau_decayMode,\
      MET_pt, MET_phi, mvis, tau_idx, mu_idx,\
      l1_idx, l2_idx, PNetvJet, PNetvMu, PNetvEle, btag, tau_LeadTkPtOverTauPt,\
      vJet, vMu, vEle, trg24mu, trg27mu, crosstrg in zip(*to_check):

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
    acoplan = calculate_acoplan(muPhi, tauPhi)

    dphi_mutau = np.acos(np.cos(muPhi - tauPhi))
    deta_mutau = abs(muEta - tauEta)

    tauPNetvJet = PNetvJet[tauBranchLoc]
    tauPNetvMu  = PNetvMu[tauBranchLoc]
    tauPNetvEle = PNetvEle[tauBranchLoc]

    passTauPtAndEta  = ((tauPt > 30.0) and (abs(tauEta) < 2.5))
    pass25MuPt   = ((trg24mu) and (muPt > 25.0) and (abs(muEta) < 2.4))
    pass28MuPt   = ((trg27mu) and (muPt > 28.0) and (abs(muEta) < 2.4))
    # HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1
    passMuPtCrossTrigger = ((crosstrg) and ((21.0 < muPt < 25.0) and (abs(muEta) < 2.1))
                                       and ((tauPt > 32.0)       and (abs(tauEta) < 2.1)) ) 
    #passMuPtCrossTrigger = False # dummy to turn off crosstrg

    # Tight v Muon, VVVLoose v Ele
    passTauDTLep  = ((vMu[tauBranchLoc] >= 4) and (vEle[tauBranchLoc] >= 2))

    single_DM_encoder = {0: 0, 1: 1, 10:2, 11:3}
    encoded_tau_decayMode = single_DM_encoder[int(tau_decayMode[tauBranchLoc])]
    #restrictTauDM = (tau_decayMode[tauBranchLoc] == 0)
    restrictTauDM = True

    leadTkPtOverTau = tau_LeadTkPtOverTauPt[tauBranchLoc]
    passLeadTkRatio = (leadTkPtOverTau < 0.9)
    passZmassWindow = (mvis < 80.0) #(50.0 < mvis < 90.0)

    cut_map = { "Low" : [30, 50],  "Mid" : [50, 70],  "High" : [70, 10000]  }
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

    if  (passTauPtAndEta and (pass25MuPt or pass28MuPt or passMuPtCrossTrigger) 
         and passTauDTLep and restrictTauDM and subtau_req):
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

      FS_mt.append(mt)
      FS_nbJet.append(nbJet)
      FS_acoplan.append(acoplan)
      FS_dphi_mutau.append(dphi_mutau)
      FS_deta_mutau.append(deta_mutau)

      FS_LeadTkPtOverTau.append(leadTkPtOverTau)

  event_dictionary["pass_cuts"] = np.array(pass_cuts)
  event_dictionary["FS_mu_pt"]  = np.array(FS_mu_pt)
  event_dictionary["FS_mu_eta"] = np.array(FS_mu_eta)
  event_dictionary["FS_mu_phi"] = np.array(FS_mu_phi)
  event_dictionary["FS_mu_iso"] = np.array(FS_mu_iso)
  event_dictionary["FS_mu_dxy"] = np.array(FS_mu_dxy)
  event_dictionary["FS_mu_dz"]  = np.array(FS_mu_dz)
  event_dictionary["FS_mu_chg"] = np.array(FS_mu_chg)
  event_dictionary["FS_mu_mass"] = np.array(FS_mu_mass)
  event_dictionary["FS_tau_pt"]  = np.array(FS_tau_pt)
  event_dictionary["FS_tau_eta"] = np.array(FS_tau_eta)
  event_dictionary["FS_tau_phi"] = np.array(FS_tau_phi)
  event_dictionary["FS_tau_dxy"] = np.array(FS_tau_dxy)
  event_dictionary["FS_tau_dz"]  = np.array(FS_tau_dz)
  event_dictionary["FS_tau_chg"] = np.array(FS_tau_chg)
  event_dictionary["FS_tau_mass"] = np.array(FS_tau_mass)
  event_dictionary["FS_tau_DM"]  = np.array(FS_tau_DM)
  event_dictionary["FS_mt"]    = np.array(FS_mt)
  event_dictionary["FS_nbJet"] = np.array(FS_nbJet)
  event_dictionary["FS_acoplan"] = np.array(FS_acoplan)
  event_dictionary["FS_dphi_mutau"] = np.array(FS_dphi_mutau)
  event_dictionary["FS_deta_mutau"] = np.array(FS_deta_mutau)
  event_dictionary["FS_LeadTkPtOverTau"] = np.array(FS_LeadTkPtOverTau)
  event_dictionary["FS_tau_rawPNetVSjet"] = np.array(FS_tau_PNet_v_jet)
  event_dictionary["FS_tau_rawPNetVSmu"]  = np.array(FS_tau_PNet_v_mu)
  event_dictionary["FS_tau_rawPNetVSe"]   = np.array(FS_tau_PNet_v_ele)
  nEvents_postcut = len(np.array(pass_cuts))
  print(f"nEvents before and after mutau cuts = {nEvents_precut}, {nEvents_postcut}")
  return event_dictionary


def make_mutau_region(event_dictionary, new_branch_name, FS_pair_sign, pass_mu_iso_req, mu_iso_value,
                      pass_DeepTau_req, DeepTau_value, DeepTau_version,
                      pass_mt_req, mt_value, pass_BTag_req):
  unpack_mutau_vars = ["event", "Lepton_tauIdx", "Lepton_muIdx", "Lepton_iso", 
                       "l1_indices", "l2_indices", "HTT_pdgId",
                       "Lepton_pt", "Lepton_phi", "PuppiMET_pt", "PuppiMET_phi", 
                       "CleanJet_btagWP"]
  unpack_mutau_vars = add_DeepTau_branches(unpack_mutau_vars, DeepTau_version)
  unpack_mutau_vars = (event_dictionary.get(key) for key in unpack_mutau_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_mutau_vars]
  pass_cuts = []
  for i, event, tau_idx, mu_idx, lep_iso, l1_idx, l2_idx, signed_pdgId,\
      lep_pt, lep_phi, MET_pt, MET_phi, btag,\
      vJet, vMu, vEle in zip(*to_check):

    mu_lep_idx = l1_idx if mu_idx[l1_idx] != -1 else l2_idx
    mu_iso     = lep_iso[mu_lep_idx]
    # puts mu_iso between 0.05 and 0.15 for DRsr and DRar, but makes aiso cases difficult
    pass_mu_iso = (mu_iso_value[0] < mu_iso < mu_iso_value[1])

    tau_branchIdx = tau_idx[l1_idx] + tau_idx[l2_idx] + 1
    pass_DeepTau  = (vJet[tau_branchIdx] >= DeepTau_value)

    muPt    = lep_pt[mu_lep_idx]
    muPhi   = lep_phi[mu_lep_idx]
    passMT     = (calculate_mt(muPt, muPhi, MET_pt, MET_phi) < mt_value)

    passBTag = True
    for value in btag:
      if (value > 0): passBTag = False

    if ( (np.sign(signed_pdgId) == FS_pair_sign) and 
         (pass_mu_iso == pass_mu_iso_req) and (pass_DeepTau == pass_DeepTau_req) and 
         (passMT == pass_mt_req) and (passBTag == pass_BTag_req) ):
      pass_cuts.append(i)
    
  event_dictionary[new_branch_name] = np.array(pass_cuts)
  return event_dictionary
