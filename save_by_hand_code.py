  # 2022 Jet Veto Maps
  by_hand_jet_veto_maps = False
  if (final_state_mode == "ditau") and (by_hand_jet_veto_maps==True):
    #### JETVETOMAPS TEMP IMPLEMENTATION for ditau only
    from correctionlib import _core
    fname = "../jetvetomaps.json.gz"
    print(f"fname is : {fname}")
    if fname.endswith(".json.gz"):
      import gzip
      with gzip.open(fname,'rt') as file:
        data = file.read().strip()
        evaluator = _core.CorrectionSet.from_string(data)
    else:
      evaluator = _core.CorrectionSet.from_file(fname)
 
    for process in combined_process_dictionary:
      bad_events = []
      eta1_arr = combined_process_dictionary[process]["PlotEvents"]["FS_t1_eta"]
      phi1_arr = combined_process_dictionary[process]["PlotEvents"]["FS_t1_phi"]
      eta2_arr = combined_process_dictionary[process]["PlotEvents"]["FS_t2_eta"]
      phi2_arr = combined_process_dictionary[process]["PlotEvents"]["FS_t2_phi"]
  
      to_check = (range(len(eta1_arr)), eta1_arr, phi1_arr, eta2_arr, phi2_arr)
      for i, eta1, phi1, eta2, phi2 in zip(*to_check):
        weight = 1
        if abs(phi1) > 3.141592653589793: phi1 = np.sign(phi1)*3.141592653589792 # put values out of bounds at bounds...
        if abs(phi2) > 3.141592653589793: phi2 = np.sign(phi2)*3.141592653589792
  
        eta1, phi1 = np.float64(eta1), np.float64(phi1) # wild hack, float32s just don't cut it
        eta2, phi2 = np.float64(eta2), np.float64(phi2)
  
        # TODO fix weight check method, also add njets
        # 15 GeV -- default jet cut
        # 25 GeV --
        # 30 GeV -- only veto event if jet in that region 
        # all jets, veto if in the region at all
        weight *= evaluator["Winter22Run3_RunE_V1"].evaluate("jetvetomap", eta1, phi1)
        weight *= evaluator["Winter22Run3_RunE_V1"].evaluate("jetvetomap", eta2, phi2)
        if weight != 0:
          bad_events.append(i)
      print(f"{len(bad_events)} in {process}")


  #### Muon ID/Iso/Trig SFs temp implementation
  by_hand_SFs = True # disabling SFs by hand works seemlessly
  if (by_hand_SFs == True) and ((final_state_mode == "dimuon") or (final_state_mode == "mutau")):
    time_print("Adding SFs!")

    from correctionlib import _core
    fname = "SFs/2022EE_schemaV2.json"
    fnamehlt = "SFs/ScaleFactors_Muon_Z_Run2022EE_Prompt_abseta_pT_schemaV2.json"
    evaluator = _core.CorrectionSet.from_file(fname)
    evaluatorhlt = _core.CorrectionSet.from_file(fnamehlt)

    for process in background_dictionary:
      mu_pt_arr  = background_dictionary[process]["PlotEvents"]["FS_mu_pt"] 
      mu_eta_arr = background_dictionary[process]["PlotEvents"]["FS_mu_eta"] 
      mu_chg_arr = background_dictionary[process]["PlotEvents"]["FS_mu_chg"] 
  
      sf_type = "nominal"
      to_use = (range(len(mu_pt_arr)), mu_pt_arr, mu_eta_arr, mu_chg_arr)
      SF_weights = []
      for i, mu_pt, mu_eta, mu_chg in zip(*to_use): 
        weight = 1
        if (mu_pt < 15.0): continue
        if (abs(mu_eta) > 2.4): continue
        mu_pt = 199.9 if mu_pt >= 200 else mu_pt
        mu_pt, mu_eta = np.float64(mu_pt), np.float64(mu_eta) # wild hack, float32s just don't cut it
  
        weight *= evaluator["NUM_MediumID_DEN_TrackerMuons"].evaluate(abs(mu_eta), mu_pt, sf_type)
        #weight *= evaluator["NUM_TightPFIso_DEN_MediumID"].evaluate(abs(mu_eta), mu_pt, sf_type)
        weight *= evaluator["NUM_TightMiniIso_DEN_MediumID"].evaluate(abs(mu_eta), mu_pt, sf_type)
      
        # min trig pt is 26 in the SFs, this should apply trig SFs to muons with pt between 25 and 26 only
        mu_pt = 26.0 if mu_pt < 26.0 else mu_pt
        weight *= evaluatorhlt["NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_and_Run2022EE"].evaluate(
                               np.float64(mu_chg), abs(mu_eta), mu_pt, sf_type)
  
        SF_weights.append(weight)
  
  
      background_dictionary[process]["SF_weight"] = np.array(SF_weights)


