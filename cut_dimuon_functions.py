import numpy as np

def make_dimuon_cut(event_dictionary, useMiniIso=False):
  '''
  Works similarly to 'make_ditau_cut'. 
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_dimuon = ["Lepton_pt", "Lepton_eta", "Lepton_phi", "Lepton_iso", 
                   "Lepton_muIdx", "Muon_dxy", "Muon_dz",
                   "HTT_m_vis", "HTT_dR", "l1_indices", "l2_indices"]
  unpack_dimuon = (event_dictionary.get(key) for key in unpack_dimuon)
  to_check      = [range(len(event_dictionary["Lepton_pt"])), *unpack_dimuon]
  pass_cuts = []
  FS_m1_pt, FS_m1_eta, FS_m1_phi, FS_m1_iso, FS_m1_dxy, FS_m1_dz = [], [], [], [], [], []
  FS_m2_pt, FS_m2_eta, FS_m2_phi, FS_m2_iso, FS_m2_dxy, FS_m2_dz = [], [], [], [], [], []
  for i, pt, eta, phi, iso, muIdx, mu_dxy, mu_dz, mvis, dR, l1_idx, l2_idx in zip(*to_check):
    # removed (dR > 0.5) and changed (mvis > 20) cut. Our minimum dR is 0.3 from skim level
    #passKinematics = (pt[l1_idx] > 26 and pt[l2_idx] > 20 and (mvis > 20) and (dR > 0.5)
    passKinematics = (pt[l1_idx] > 26 and pt[l2_idx] > 20 and (70 < mvis < 130))
    if (useMiniIso == False):
      passIso      = (iso[l1_idx] < 0.25 and iso[l2_idx] < 0.25) # for PFRelIso, Loose 25, Medium 20, Tight 15
    if (useMiniIso == True):
      passIso      = (iso[l1_idx] < 0.40 and iso[l2_idx] < 0.40) # for MiniIso, Loose 40, Medium 20, Tight 10
    if (passKinematics and passIso):
      pass_cuts.append(i)
      FS_m1_pt.append(pt[l1_idx])
      FS_m1_eta.append(eta[l1_idx])
      FS_m1_phi.append(phi[l1_idx])
      FS_m1_iso.append(iso[l1_idx])
      FS_m1_dxy.append(abs(mu_dxy[muIdx[l1_idx]]))
      FS_m1_dz.append(mu_dz[muIdx[l1_idx]])
      FS_m2_pt.append(pt[l2_idx])
      FS_m2_eta.append(eta[l2_idx])
      FS_m2_phi.append(phi[l2_idx])
      FS_m2_iso.append(iso[l2_idx])
      FS_m2_dxy.append(abs(mu_dxy[muIdx[l2_idx]]))
      FS_m2_dz.append(mu_dz[muIdx[l2_idx]])

  event_dictionary["pass_cuts"] = np.array(pass_cuts)
  event_dictionary["FS_m1_pt"]  = np.array(FS_m1_pt)
  event_dictionary["FS_m1_eta"] = np.array(FS_m1_eta)
  event_dictionary["FS_m1_phi"] = np.array(FS_m1_phi)
  event_dictionary["FS_m1_iso"] = np.array(FS_m1_iso)
  event_dictionary["FS_m1_dxy"] = np.array(FS_m1_dxy)
  event_dictionary["FS_m1_dz"] = np.array(FS_m1_dz)
  event_dictionary["FS_m2_pt"]  = np.array(FS_m2_pt)
  event_dictionary["FS_m2_eta"] = np.array(FS_m2_eta)
  event_dictionary["FS_m2_phi"] = np.array(FS_m2_phi)
  event_dictionary["FS_m2_iso"] = np.array(FS_m2_iso)
  event_dictionary["FS_m2_dxy"] = np.array(FS_m2_dxy)
  event_dictionary["FS_m2_dz"] = np.array(FS_m2_dz)
  print(f"events before and after dimuon cuts = {nEvents_precut}, {len(np.array(pass_cuts))}")
  return event_dictionary

def make_dimuon_region(event_dictionary, new_branch_name, FS_pair_sign):
  unpack_dimuon_vars = ["l1_indices", "l2_indices", "HTT_pdgId"]
  unpack_dimuon_vars = (event_dictionary.get(key) for key in unpack_dimuon_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_dimuon_vars]
  pass_cuts = []
  for i, l1_idx, l2_idx, signed_pdgId in zip(*to_check):

    if (np.sign(signed_pdgId) == FS_pair_sign):
      pass_cuts.append(i)
  
  event_dictionary[new_branch_name] = np.array(pass_cuts)
  return event_dictionary


def manual_dimuon_lepton_veto(event_dictionary):
  '''
  Works similarly to 'make_ditau_cut' except the branch "pass_manual_lepton_veto"
  is made specifically for the dimuon final state. Some special handling is required
  due to the way events are selected in step2 of the NanoTauFramework
  '''
  nEvents_precut = len(event_dictionary["Lepton_pt"])
  unpack_veto = ["Lepton_pdgId", "Lepton_iso"]
  unpack_veto = (event_dictionary.get(key) for key in unpack_veto)
  to_check    = [range(len(event_dictionary["Lepton_pt"])), *unpack_veto]
  pass_manual_lepton_veto = []
  for i, lep_pdgId_array, lep_iso_array in zip(*to_check):
    event_passes_manual_lepton_veto = False
    nIsoEle, nIsoMu = 0, 0 # there are many pdgId=15 particles, but we assume those are fake taus
    for pdgId, iso in zip(lep_pdgId_array, lep_iso_array):
      if (abs(pdgId) == 11) and (iso < 0.3):
        nIsoEle += 1
      elif (abs(pdgId) == 13) and (iso < 0.3):
        nIsoMu  += 1
      else:
        pass

      if nIsoEle > 0:
        event_passes_manual_lepton_veto = False
      elif nIsoMu > 2:
        event_passes_manual_lepton_veto = False
      else:
        event_passes_manual_lepton_veto = True

    if event_passes_manual_lepton_veto:
      pass_manual_lepton_veto.append(i)

  event_dictionary["pass_manual_lepton_veto"] = np.array(pass_manual_lepton_veto)
  print(f"events before and after manual dimuon lepton veto = {nEvents_precut}, {len(np.array(pass_manual_lepton_veto))}")
  return event_dictionary


