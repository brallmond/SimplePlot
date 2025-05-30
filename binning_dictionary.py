import numpy as np

### README ###
# binning for different variables are defined below and are separated by use-case
# All variables are assumed to be linearly binned.

label_dictionary = {
  "FS_t1_pt"  : r'Leading Tau $p_T$ [GeV]',
  "FS_t1_eta" : r'Leading Tau $\eta$',
  "FS_t1_phi" : r'Leading Tau $\phi$',
  "FS_t1_DeepTauVSjet" : r'Leading Tau DeepTau Vs Jet',
  "FS_t1_DeepTauVSmu"  : r'Leading Tau DeepTau Vs Muon',
  "FS_t1_DeepTauVSe"   : r'Leading Tau DeepTau Vs Electron',
  "FS_t1_rawPNetVSjet" : r'Leading Tau PNet Vs Jet',
  "FS_t1_rawPNetVSmu"  : r'Leading Tau PNet Vs Muon',
  "FS_t1_rawPNetVSe"   : r'Leading Tau PNet Vs Electron',
  "FS_t1_dxy"  : r'Leading Tau $D_{xy}$',
  "FS_t1_dz"   : r'Leading Tau $D_Z$',
  "FS_t1_chg"  : r'Leading Tau Charge',
  "FS_t1_DM"   : r'Leading Tau Decay Mode',
  "FS_t1_mass" : r'Leading Tau Mass',

  "FS_t2_pt"  : r'Sub-leading Tau $p_T$ [GeV]',
  "FS_t2_eta" : r'Sub-leading Tau $\eta$',
  "FS_t2_phi" : r'Sub-leading Tau $\phi$',
  "FS_t2_DeepTauVSjet" : r'Sub-leading Tau DeepTau Vs Jet',
  "FS_t2_DeepTauVSmu"  : r'Sub-leading Tau DeepTau Vs Muon',
  "FS_t2_DeepTauVSe"   : r'Sub-leading Tau DeepTau Vs Electron',
  "FS_t2_rawPNetVSjet" : r'Sub-leading Tau PNet Vs Jet',
  "FS_t2_rawPNetVSmu"  : r'Sub-leading Tau PNet Vs Muon',
  "FS_t2_rawPNetVSe"   : r'Sub-leading Tau PNet Vs Electron',
  "FS_t2_dxy"  : r'Sub-leading Tau $D_{xy}$',
  "FS_t2_dz"   : r'Sub-leading Tau $D_Z$',
  "FS_t2_chg"  : r'Sub-leading Tau Charge',
  "FS_t2_DM"   : r'Sub-leading Tau Decay Mode',
  "FS_t2_mass" : r'Sub-leading Tau Mass',

  "FS_trig_idx" : r'Trigger Indices',
  "FS_pair_DM"  : r'Tau Pair Decay Mode (t1*100 + t2)',

  "FS_mt_t1t2"   : r'$m_T$($\tau_1,\tau_2$) [GeV]',
  "FS_mt_t1_MET" : r'$m_T$($\tau_1$, MET) [GeV]',
  "FS_mt_t2_MET" : r'$m_T$($\tau_2$, MET) [GeV]',
  "FS_mt_TOT"    : r'$m_T$ Total [GeV]',
  "FS_dphi_t1t2" : r'$\Delta\phi_{\tau_1\tau_2}$',
  "FS_deta_t1t2" : r'$\Delta\eta_{\tau_1\tau_2}$',
  "FS_dpt_t1t2"  : r'$\Delta pT_{\tau_1\tau_2}$',
  "FS_dphi_t1MET" : r'$\Delta\phi_{\tau_1MET}$',
  "FS_dphi_t2MET" : r'$\Delta\phi_{\tau_2MET}$',

  "FS_t1_FLsig"  : r'Leading Tau Flight Significance',
  "FS_t1_FLX"    : r'Leading Tau Flight Length X',
  "FS_t1_FLY"    : r'Leading Tau Flight Length Y',
  "FS_t1_FLZ"    : r'Leading Tau Flight Length Z',
  "FS_t1_FLmag"  : r'Leading Tau Flight Length',
  "FS_t1_ipLsig" : r'Leading Tau ip Length Significance',
  "FS_t1_ip3d"   : r'Leading Tau ip 3D',
  "FS_t1_tk_lambda" : r'Leading Tau Track Lambda',
  "FS_t1_tk_qoverp" : r'Leading Tau Track Q Over P',

  "FS_t2_FLsig"  : r'Sub-leading Tau Flight Significance',
  "FS_t2_FLX"    : r'Sub-leading Tau Flight Length X',
  "FS_t2_FLY"    : r'Sub-leading Tau Flight Length Y',
  "FS_t2_FLZ"    : r'Sub-leading Tau Flight Length Z',
  "FS_t2_FLmag"  : r'Sub-leading Tau Flight Length',
  "FS_t2_ipLsig" : r'Sub-leading Tau ip Length Significance',
  "FS_t2_ip3d"   : r'Sub-leading Tau ip 3D',
  "FS_t2_tk_lambda" : r'Sub-leading Tau Track Lambda',
  "FS_t2_tk_qoverp" : r'Sub-leading Tau Track Q Over P',

  "FS_m1_pt"   : r'Leading Muon $p_T$ [GeV]',
  "FS_m1_eta"  : r'Leading Muon $\eta$',
  "FS_m1_phi"  : r'Leading Muon $\phi$',
  "FS_m1_iso"  : r'Leading Muon Isolation',
  "FS_m1_dxy"  : r'Leading Muon $D_{xy}$',
  "FS_m1_dz"   : r'Leading Muon $D_z$',
  "FS_m1_chg"  : r'Leading Muon Charge',

  "FS_m2_pt"   : r'Sub-leading Muon $p_T$ [GeV]',
  "FS_m2_eta"  : r'Sub-leading Muon $\eta$',
  "FS_m2_phi"  : r'Sub-leading Muon $\phi$',
  "FS_m2_iso"  : r'Sub-leading Muon Isolation',
  "FS_m2_dxy"  : r'Sub-leading Muon $D_{xy}$',
  "FS_m2_dz"   : r'Sub-leading Muon $D_z$',
  "FS_m2_chg"  : r'Sub-leading Muon Charge',

  "FS_m_vis_tight" : r'$m_{vis}$ [GeV]',

  "FS_mu_pt"   : r'Muon $p_T$ [GeV]',
  "FS_mu_eta"  : r'Muon $\eta$',
  "FS_mu_phi"  : r'Muon $\phi$',
  "FS_mu_iso"  : r'Muon Isolation',
  "FS_mu_dxy"  : r'Muon $D_{xy}$',
  "FS_mu_dz"   : r'Muon $D_{z}$',
  "FS_mu_chg"  : r'Muon Charge',
  "FS_mu_mass" : r'Muon Mass [GeV]',
  "FS_dphi_mutau" : r'$\Delta\phi_{\mu\tau}$',
  "FS_deta_mutau" : r'$\Delta\eta_{\mu\tau}$',
  "FS_dpt_mutau"  : r'$\Delta pT_{\mu\tau}$',

  "FS_el_pt"   : r'Electron $p_T$ [GeV]',
  "FS_el_eta"  : r'Electron $\eta$',
  "FS_el_phi"  : r'Electron $\phi$',
  "FS_el_iso"  : r'Electron Isolation',
  "FS_el_dxy"  : r'Electron $D_{xy}$',
  "FS_el_dz"   : r'Electron $D_{z}$',
  "FS_el_chg"  : r'Electron Charge',
  "FS_el_mass" : r'Electron Mass [GeV]',
  "FS_dphi_etau" : r'$\Delta\phi_{e\tau}$',
  "FS_deta_etau" : r'$\Delta\eta_{e\tau}$',
  "FS_dpt_etau"  : r'$\Delta pT_{e\tau}$',

  "FS_tau_pt"  : r'Tau $p_T$ [GeV]',
  "FS_tau_eta" : r'Tau $\eta$',
  "FS_tau_phi" : r'Tau $\phi$',
  "FS_tau_dxy" : r'Tau $D_{xy}$',
  "FS_tau_dz"  : r'Tau $D_{z}$',
  "FS_tau_chg" : r'Tau Charge',
  "FS_tau_mass": r'Tau Mass [GeV]',
  "FS_tau_DM"  : r'Tau Decay Mode',
  "FS_tau_rawPNetVSjet" : r'Tau PNet Vs Jet',
  "FS_tau_rawPNetVSmu" : r'Tau PNet Vs Mu',
  "FS_tau_rawPNetVSe" : r'Tau PNet Vs Electron',

  "FS_mt"      : r'Transverse Mass [GeV]',
  "FS_mt_branch" : r'Transverse Mass from branch [GeV]',
  "FS_mt_diff" : r'mT Calc - mT Branch [GeV]',
  "FS_nbJet"   : r'Number of b-tagged Jets',
  "FS_acoplan" : r'Acoplanarity',
  "FS_PZeta"   : r'PZeta',

  "MET_pt"          : r'MET [GeV]',
  "PuppiMET_pt"     : r'PUPPI MET [GeV]',
  "PuppiMET_phi"    : r'PUPPI MET $\phi$',
  "nCleanJetGT30"   : r'Number of Jets',
  "nCleanJet"   : r'Number of Jets from Branch',
  "CleanJetGT30_pt_1"  : r'Leading Jet $p_T$ [GeV]',
  "CleanJet_pt_1"  : r'Leading Jet $p_T$ [GeV] from Branch',
  "CleanJetGT30_eta_1" : r'Leading Jet $\eta$',
  "CleanJetGT30_phi_1" : r'Leading Jet $\phi$',
  "CleanJetGT30_pt_2"  : r'Sub-leading Jet $p_T$ [GeV]',
  "CleanJetGT30_eta_2" : r'Sub-leading Jet $\eta$',
  "CleanJetGT30_phi_2" : r'Sub-leading Jet $\phi$',
  "FS_mjj"    : r'Dijet Mass [GeV]',
  "FS_detajj" : r'|$\Delta\eta$|',
  "FS_j1index" : r'Leading Jet Index of Highest Mjj Pair',
  "FS_j2index" : r'Subeading Jet Index of Highest Mjj Pair',
  "FS_dijet_pair_calc" : r'DiJet Index Combination',
  "FS_dijet_pair_HTT"  : r'DiJet Index Combination - from branch',

  "HTT_DiJet_MassInv_fromHighestMjj" : r'Dijet Mass [GeV] from Highest Mjj Pair',
  "HTT_DiJet_MassInv_fromLeadingJets": r'Dijet Mass [GeV] from Leading Jets',
  "HTT_DiJet_dEta_fromHighestMjj"    : r'|$\Delta\eta$| from Highest Mjj Pair',
  "HTT_DiJet_dEta_fromLeadingJets"   : r'|$\Delta\eta$| from Leading Jets',
  "HTT_DiJet_j1index"                : r'Leading Jet Index of Highest Mjj Pair - from branch',
  "HTT_DiJet_j2index"                : r'Subleading Jet Index of Highest Mjj Pair - from branch',
  "HTT_H_pt"                         : r'Reco Higgs $p_T$ [GeV]',
  "HTT_H_pt_corr_Run2"               : r'Reco Higgs $p_T$ [GeV] (Run2-style Correction)',
  "HTT_H_pt_corr"                    : r'Reco Higgs $p_T$ [GeV] (Run3-style Correction)',
  "HTT_mT_l1l2met"                   : r'$m_T$($\ell_1\ell_2$, MET) [GeV]',
  "HTT_dR"      : r'$\Delta$R',
  "HTT_m_vis"            : r'$m_{vis}$ [GeV]',
  "HTT_m_vis-KSUbinning" : r'$m_{vis}$ [GeV]',
  "HTT_m_vis-SFbinning"  : r'$m_{vis}$ [GeV]',
  "HTT_pT_l1l2" : r'$p_T^{ll}$ [GeV]',
  "FastMTT_PUPPIMET_mT"   : r'Fast MTT Transverse Mass [GeV]',
  "FastMTT_mT"   : r'Fast MTT Transverse Mass [GeV]',
  "FastMTT_PUPPIMET_mass" : r'Fast MTT Mass [GeV]',
  "FastMTT_mass" : r'Fast MTT Mass [GeV]',
  "PV_npvs"     : r'Number of Primary Vertices',
  "Generator_weight" : r'Generator weight',

  "FS_LeadTkPtOverTau" : r'Lead Tau Track $p_T$ / Tau $p_T$',

  "Gen_pT_l1"        : r'Gen pT Leading Lepton [GeV]',
  "Gen_eta_l1"       : r'Gen $\eta$ Leading Lepton',
  "Gen_phi_l1"       : r'Gen $\phi$ Leading Lepton',
  "Gen_pT_l2"        : r'Gen pT Sub-Leading Lepton [GeV]',
  "Gen_eta_l2"       : r'Gen $\eta$ Sub-Leading Lepton',
  "Gen_phi_l2"       : r'Gen $\phi$ Sub-Leading Lepton',
  "Gen_H_pT"         : r'Gen Higgs pT [GeV]',
  "Gen_H_pT_fidMET"  : r'Gen Higgs pT (using fidMET) [GeV]',
  "Gen_pT_ll"        : r'Gen Dilepton pT [GeV]',
  "Gen_m_ll"         : r'Gen Dilepton Invariant Mass [GeV]',
  "Gen_mT"           : r'Gen Transverse Mass (mT) [GeV]',
  "Gen_mT_fidMET"    : r'Gen Transverse Mass (mT) (using fidMET) [GeV]',
  "Gen_DZeta"        : r'Gen DZeta',
  "Gen_DZeta_fidMET" : r'Gen DZeta (using fidMET)',
  "Gen_deltaR_ll"    : r'Gen Dilepton $\Delta$R',
  "Gen_deltaEta_ll"  : r'Gen Dilepton $\Delta\eta$',
  "Gen_deltaPhi_ll"  : r'Gen Dilepton $\Delta\phi$',
  "Gen_nCleanJet"    : r'Gen nCleanJet',
  "Gen_pT_j1"        : r'Gen pT Leading Jet [GeV]',
  "Gen_eta_j1"       : r'Gen $\eta$ Leading Jet',
  "Gen_phi_j1"       : r'Gen $\phi$ Leading Jet',
  "Gen_pT_j2"        : r'Gen pT Sub-Leading Jet [GeV]',
  "Gen_eta_j2"       : r'Gen $\eta$ Sub-Leading Jet',
  "Gen_phi_j2"       : r'Gen $\phi$ Sub-Leading Jet',
  "Gen_pT_j3"        : r'Gen pT 3rd Jet [GeV]',
  "Gen_eta_j3"       : r'Gen $\eta$ 3rd Jet',
  "Gen_phi_j3"       : r'Gen $\phi$ 3rd Jet',
  "Gen_mjj"          : r'Gen Dijet Mass [GeV]',
  "Gen_deltaEta_jj"  : r'Gen Dijet $\Delta\eta$',
}

#  channel {
#    "var"  : (xmin, xmax, nBins),
#  }
binning_dictionary = {
  "ditau" : {
    "FS_t1_pt"   : np.linspace(0, 180, 36+1),
    "FS_t1_eta"  : np.linspace(-3, 3, 30+1),
    "FS_t1_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_t1_DeepTauVSjet" : np.linspace(1, 9, 8+1),
    "FS_t1_DeepTauVSmu"  : np.linspace(1, 5, 4+1),
    "FS_t1_DeepTauVSe"   : np.linspace(1, 9, 8+1),
    "FS_t1_dxy"  : np.linspace(0, 0.025, 25+1), #np.linspace(0, 0.20, 50+1),
    "FS_t1_dz"   : np.linspace(0, 0.05, 25+1),  #np.linspace(0, 0.25, 50+1),
    "FS_t1_chg"  : np.linspace(-2, 2, 5+1),
    "FS_t1_DM"  : np.linspace(-1, 5, 7+1),
    "FS_t1_mass" : np.linspace(0, 3, 30+1),

    "FS_t1_rawPNetVSjet" : np.linspace(-0.1, 1.1, 60+1),
    "FS_t1_rawPNetVSmu"  : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),
    "FS_t1_rawPNetVSe"   : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),

    "FS_t2_pt"   : np.linspace(0, 120, 24+1),
    "FS_t2_eta"  : np.linspace(-3, 3, 30+1),
    "FS_t2_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_t2_DeepTauVSjet" : np.linspace(1, 9, 8+1),
    "FS_t2_DeepTauVSmu"  : np.linspace(1, 5, 4+1),
    "FS_t2_DeepTauVSe"   : np.linspace(1, 9, 8+1),
    "FS_t2_dxy"  : np.linspace(0, 0.025, 25+1), #np.linspace(0, 0.20, 50+1),
    "FS_t2_dz"   : np.linspace(0, 0.05, 25+1),  #np.linspace(0, 0.25, 50+1),
    "FS_t2_chg"  : np.linspace(-2, 2, 5+1),
    "FS_t2_DM"  : np.linspace(-1, 5, 7+1),
    "FS_t2_mass" : np.linspace(0, 3, 30+1),

    "FS_t2_rawPNetVSjet" : np.linspace(-0.1, 1.1, 60+1),
    "FS_t2_rawPNetVSmu"  : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),
    "FS_t2_rawPNetVSe"   : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),

    "FS_pair_DM" : np.linspace(0, 16, 16+1),

    "FS_mt_t1t2"   : np.linspace(0, 300, 30+1),
    "FS_mt_t1_MET" : np.linspace(0, 150, 30+1),
    "FS_mt_t2_MET" : np.linspace(0, 150, 30+1),
    "FS_mt_TOT"    : np.linspace(0, 50, 50+1),
    "FS_dphi_t1t2" : np.linspace(0, 3.1416, 32+1),
    "FS_deta_t1t2" : np.linspace(0, 4, 32+1),
    "FS_dpt_t1t2"  : np.linspace(-100, 100, 50+1),
    "FS_dphi_t1MET" : np.linspace(0, 3.1416, 32+1),
    "FS_dphi_t2MET" : np.linspace(0, 3.1416, 32+1),

    "FS_t1_FLsig"  : np.linspace(-5, 20, 50+1),
    "FS_t1_FLX"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t1_FLY"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t1_FLZ"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t1_FLmag"  : np.linspace(0, 0.02, 20+1),
    "FS_t1_ipLsig" : np.linspace(-10, 10, 20+1),
    "FS_t1_ip3d"   : np.linspace(-0.02, 0.02, 20+1),
    "FS_t1_tk_lambda" : np.linspace(-1.5, 1.5, 40+1),
    "FS_t1_tk_qoverp" : np.linspace(-0.1, 0.1, 40+1),

    "FS_t2_FLsig"  : np.linspace(-5, 20, 50+1),
    "FS_t2_FLX"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t2_FLY"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t2_FLZ"    : np.linspace(-0.01, 0.01, 20+1),
    "FS_t2_FLmag"  : np.linspace(0, 0.02, 20+1),
    "FS_t2_ipLsig" : np.linspace(-10, 10, 20+1),
    "FS_t2_ip3d"   : np.linspace(-0.02, 0.02, 20+1),
    "FS_t2_tk_lambda" : np.linspace(-1.5, 1.5, 40+1),
    "FS_t2_tk_qoverp" : np.linspace(-0.1, 0.1, 40+1),
  },

  "mutau" : {
    "FS_mu_pt"   : np.linspace(0, 120, 40+1),
    "FS_mu_eta"  : np.linspace(-3, 3, 30+1),
    "FS_mu_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_mu_iso"  : np.linspace(0, 1, 25+1),
    "FS_mu_dxy"  : np.linspace(0, 0.025, 50+1),
    "FS_mu_dz"   : np.linspace(0, 0.05, 50+1), #np.linspace(0, 0.25, 50+1),
    "FS_mu_chg"  : np.linspace(-2, 2, 5+1),
    "FS_mu_mass"  : np.linspace(0.095, 0.115, 100+1), # centered at 105

    "FS_tau_pt"  : np.linspace(0, 180, 36+1),
    "FS_tau_eta" : np.linspace(-3, 3, 30+1),
    "FS_tau_phi" : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_tau_dxy"  : np.linspace(0, 0.025, 50+1), #np.linspace(0, 0.20, 50+1),
    "FS_tau_dz"   : np.linspace(0, 0.05, 50+1),  #np.linspace(0, 0.25, 50+1),
    "FS_tau_chg" : np.linspace(-2, 2, 5+1),
    "FS_tau_DM"  : np.linspace(-1, 5, 7+1),
    "FS_tau_mass" : np.linspace(0, 3, 30+1),

    "FS_dphi_mutau" : np.linspace(0, 3.1416, 32+1),
    "FS_deta_mutau" : np.linspace(0, 4, 32+1),
    "FS_dpt_mutau"  : np.linspace(-100, 100, 50+1),

    "FS_tau_rawPNetVSjet" : np.linspace(-0.1, 1.1, 60+1),
    "FS_tau_rawPNetVSmu"  : np.array([-0.05, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]), # plot logx
    "FS_tau_rawPNetVSe"   : np.array([-0.05, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),

    "FS_LeadTkPtOverTau" : np.linspace(-0.1, 1.1, 60+1),
  },

  "etau" : {
    "FS_el_pt"   : np.linspace(20, 100, 50+1),
    "FS_el_eta"  : np.linspace(-3, 3, 30+1),
    "FS_el_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_el_iso"  : np.linspace(0, 1, 25+1),
    "FS_el_dxy"  : np.linspace(0, 0.05, 50+1),
    "FS_el_dz"   : np.linspace(0, 0.25, 50+1),
    "FS_el_chg"  : np.linspace(-2, 2, 5+1),
    "FS_el_mass" : np.linspace(-0.00002, 0.00002, 30+1),

    "FS_tau_pt"  : np.linspace(20, 100, 50+1),
    "FS_tau_eta" : np.linspace(-3, 3, 30+1),
    "FS_tau_phi" : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_tau_dxy" : np.linspace(0, 0.025, 25+1), #np.linspace(0, 0.20, 50+1),
    "FS_tau_dz"  : np.linspace(0, 0.05, 25+1),  #np.linspace(0, 0.25, 50+1),
    "FS_tau_chg" : np.linspace(-2, 2, 5+1),
    "FS_tau_DM"  : np.linspace(-1, 5, 7+1),
    "FS_tau_mass" : np.linspace(0, 3, 30+1),

    "FS_dphi_etau" : np.linspace(0, 3.1416, 32+1),
    "FS_deta_etau" : np.linspace(0, 4, 32+1),
    "FS_dpt_etau"  : np.linspace(-100, 100, 50+1),

    "FS_tau_rawPNetVSjet" : np.linspace(-0.1, 1.1, 60+1),
    "FS_tau_rawPNetVSmu"  : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]), # plot logx
    "FS_tau_rawPNetVSe"   : np.array([-0.05, 0, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.05]),
  },

  "dimuon" : {
    "FS_m1_pt"   : np.linspace(0, 300, 60+1),
    "FS_m1_eta"  : np.linspace(-2.5, 2.5, 99+1),
    "FS_m1_phi"  : np.linspace(-3.1416, 3.1416, 64+1),
    "FS_m1_iso"  : np.linspace(0, 1, 25+1),
    "FS_m1_dxy"  : np.linspace(0, 0.05, 50+1),
    "FS_m1_dz"   : np.linspace(0, 0.25, 50+1),
    "FS_m1_chg"  : np.linspace(-2, 2, 5+1),

    "FS_m2_pt"   : np.linspace(0, 300, 60+1),
    "FS_m2_eta"  : np.linspace(-2.5, 2.5, 99+1),
    "FS_m2_phi"  : np.linspace(-3.1416, 3.1416, 64+1),
    "FS_m2_iso"  : np.linspace(0, 1, 25+1),
    "FS_m2_dxy"  : np.linspace(0, 0.05, 50+1),
    "FS_m2_dz"   : np.linspace(0, 0.25, 50+1),
    "FS_m2_chg"  : np.linspace(-2, 2, 5+1),
    "FS_m_vis_tight" : np.linspace(70, 110, 80+1),
  },
  "emu" : {
    "FS_el_pt"   : np.linspace(0, 120, 40+1),
    "FS_el_eta"  : np.linspace(-3, 3, 30+1),
    "FS_el_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_el_iso"  : np.linspace(0, 1, 25+1),
    "FS_el_dxy"  : np.linspace(0, 0.05, 50+1),
    "FS_el_dz"   : np.linspace(0, 0.25, 50+1),
    "FS_el_chg"  : np.linspace(-2, 2, 5+1),

    "FS_mu_pt"   : np.linspace(0, 120, 40+1),
    "FS_mu_eta"  : np.linspace(-3, 3, 30+1),
    "FS_mu_phi"  : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_mu_iso"  : np.linspace(0, 1, 25+1),
    "FS_mu_dxy"  : np.linspace(0, 0.025, 50+1),
    "FS_mu_dz"   : np.linspace(0, 0.25, 50+1),
    "FS_mu_chg"  : np.linspace(-2, 2, 5+1),
    "FS_PZeta"   : np.linspace(-100, 100, 30+1),
  },  

  "common" : {
    # calculated on the fly
    "FS_tau_pt"  : np.linspace(0, 180, 36+1), # redundant key to be used by fitter in ditau
    "FS_trig_idx" : np.linspace(0, 4, 4+1),
    "FS_mt"         : np.linspace(0, 200, 40+1),
    "FS_mt_branch"  : np.linspace(0, 200, 40+1),
    "FS_mt_diff"    : np.linspace(-5, 5, 25+1),
    #"FS_nbJet"      : np.linspace(0, 4, 4+1), # original
    "FS_nbJet"      : np.linspace(-1, 9, 20+1), # testing
    "FS_acoplan"    : np.linspace(0, 1, 10+1),
    "nCleanJetGT30" : np.linspace(0, 8, 8+1), # GT(E) = Greater Than (Equal to)
    "CleanJetGT30_pt_1"  : np.linspace(0, 300, 60+1),
    "CleanJet_pt_1"  : np.linspace(-5, 300, 61+1),
    "CleanJetGT30_pt_2"  : np.linspace(0, 300, 60+1),
    "CleanJetGT30_pt_3"  : np.linspace(0, 300, 60+1),
    "CleanJetGT30_eta_1" : np.linspace(-5, 5, 50+1),
    "CleanJetGT30_eta_2" : np.linspace(-5, 5, 50+1),
    "CleanJetGT30_eta_3" : np.linspace(-5, 5, 50+1),
    "CleanJetGT30_phi_1" : np.linspace(-3.1416, 3.1416, 32+1),
    "CleanJetGT30_phi_2" : np.linspace(-3.1416, 3.1416, 32+1),
    "CleanJetGT30_phi_3" : np.linspace(-3.1416, 3.1416, 32+1),
    "FS_mjj"     : np.linspace(0, 1500, 30+1),
    "FS_detajj"  : np.linspace(0, 7, 31+1),
    "FS_j1index" : np.linspace(0, 10, 10+1),
    "FS_j2index" : np.linspace(0, 10, 10+1),
    "FS_dijet_pair_calc" : np.linspace(0, 50, 50+1),
    "FS_dijet_pair_HTT"  : np.linspace(0, 50, 50+1),

    # from branches
    "MET_pt"      : np.linspace(0, 150, 30+1),
    "MET_phi"     : np.linspace(-3.1416, 3.1416, 32+1),
    "PuppiMET_pt" : np.linspace(0, 150, 50+1),
    "PuppiMET_phi": np.linspace(-3.1416, 3.1416, 32+1),
    "nCleanJet"   : np.linspace(0, 8, 8+1),
    "CleanJet_pt" : np.linspace(20, 200, 30+1),
    "CleanJet_eta": np.linspace(-5, 5, 50+1),
    "HTT_DiJet_MassInv_fromHighestMjj" : np.linspace(0, 1500, 30+1),
    "HTT_DiJet_MassInv_fromLeadingJets": np.linspace(0, 1500, 30+1),
    "HTT_DiJet_dEta_fromHighestMjj"    : np.linspace(0, 7, 35+1),
    "HTT_DiJet_dEta_fromLeadingJets"   : np.linspace(0, 7, 35+1),
    "HTT_DiJet_j1index"                : np.linspace(0, 10, 10+1),
    "HTT_DiJet_j2index"                : np.linspace(0, 10, 10+1),
    "HTT_H_pt"                         : np.linspace(0, 500, 50+1),
    "HTT_H_pt_corr"                    : np.linspace(0, 500, 50+1),
    "HTT_mT_l1l2met"                   : np.linspace(0, 300, 30+1),
    "HTT_dR"                : np.linspace(0, 6, 60+1),
    "HTT_m_vis"             : np.linspace(0, 300, 30+1), # same as KSU binning
    #"HTT_m_vis"             : np.linspace(50, 310, 12+1),
    "HTT_pT_l1l2" : np.linspace(0, 250, 50+1),
    "FastMTT_PUPPIMET_mT"   : np.linspace(0, 400, 40+1),
    "FastMTT_mT"   : np.linspace(0, 400, 40+1),
    "FastMTT_PUPPIMET_mass" : np.linspace(50, 290, 12+1),
    "FastMTT_mass" : np.linspace(50, 300, 25+1),
    "FS_t1_flav" : np.linspace(0, 11, 11+1),
    "FS_t2_flav" : np.linspace(0, 11, 11+1),
    "PV_npvs"    : np.linspace(0, 90, 30+1),
    "Generator_weight" : np.linspace(-100, 100, 100+1),
    
    # from branches, signal only
    "Gen_pT_l1"        : np.linspace(0, 200, 40+1),
    "Gen_eta_l1"       : np.linspace(-3, 3, 30+1),
    "Gen_phi_l1"       : np.linspace(-3.1416, 3.1416, 32+1),
    "Gen_pT_l2"        : np.linspace(0, 200, 40+1),
    "Gen_eta_l2"       : np.linspace(-3, 3, 30+1),
    "Gen_phi_l2"       : np.linspace(-3.1416, 3.1416, 32+1),
    "Gen_H_pT"         : np.linspace(0, 500, 50+1),
    "Gen_H_pT_fidMET"  : np.linspace(0, 500, 50+1),
    "Gen_pT_ll"        : np.linspace(0, 250, 50+1),
    "Gen_m_ll"         : np.linspace(0, 300, 30+1),
    "Gen_mT"           : np.linspace(0, 200, 40+1),
    "Gen_mT_fidMET"    : np.linspace(0, 200, 40+1),
    "Gen_DZeta"        : np.linspace(-100, 100, 30+1),
    "Gen_DZeta_fidMET" : np.linspace(-100, 100, 30+1),
    "Gen_deltaR_ll"    : np.linspace(0, 6, 60+1),
    "Gen_deltaEta_ll"  : np.linspace(0, 4, 32+1),
    "Gen_deltaPhi_ll"  : np.linspace(0, 3.1416, 32+1),
    "Gen_nCleanJet"    : np.linspace(0, 8, 8+1),
    "Gen_pT_j1"        : np.linspace(0, 300, 60+1),
    "Gen_eta_j1"       : np.linspace(-5, 5, 50+1),
    "Gen_phi_j1"       : np.linspace(-3.1416, 3.1416, 32+1),
    "Gen_pT_j2"        : np.linspace(0, 300, 60+1),
    "Gen_eta_j2"       : np.linspace(-5, 5, 50+1),
    "Gen_phi_j2"       : np.linspace(-3.1416, 3.1416, 32+1),
    "Gen_pT_j3"        : np.linspace(0, 300, 60+1),
    "Gen_eta_j3"       : np.linspace(-5, 5, 50+1),
    "Gen_phi_j3"       : np.linspace(-3.1416, 3.1416, 32+1),
    "Gen_mjj"          : np.linspace(0, 1500, 30+1),
    "Gen_deltaEta_jj"  : np.linspace(0, 7, 35+1),
  }
}
