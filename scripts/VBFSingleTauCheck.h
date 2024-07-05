//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Jan 18 11:21:45 2024 by ROOT version 6.28/04
// from TTree Events/Events
// found on file: VBF_postBpix_2023_sample.root
//////////////////////////////////////////////////////////

#ifndef VBFSingleTauCheck_h
#define VBFSingleTauCheck_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class VBFSingleTauCheck {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   UInt_t          run;
   UInt_t          luminosityBlock;
   ULong64_t       event;
   UInt_t          bunchCrossing;
   Int_t           nJet;
   UChar_t         Jet_jetId[16];   //[nJet]
   UChar_t         Jet_nConstituents[16];   //[nJet]
   UChar_t         Jet_nElectrons[16];   //[nJet]
   UChar_t         Jet_nMuons[16];   //[nJet]
   UChar_t         Jet_nSVs[16];   //[nJet]
   Short_t         Jet_electronIdx1[16];   //[nJet]
   Short_t         Jet_electronIdx2[16];   //[nJet]
   Short_t         Jet_muonIdx1[16];   //[nJet]
   Short_t         Jet_muonIdx2[16];   //[nJet]
   Short_t         Jet_svIdx1[16];   //[nJet]
   Short_t         Jet_svIdx2[16];   //[nJet]
   Int_t           Jet_hfadjacentEtaStripsSize[16];   //[nJet]
   Int_t           Jet_hfcentralEtaStripSize[16];   //[nJet]
   Float_t         Jet_PNetRegPtRawCorr[16];   //[nJet]
   Float_t         Jet_PNetRegPtRawCorrNeutrino[16];   //[nJet]
   Float_t         Jet_PNetRegPtRawRes[16];   //[nJet]
   Float_t         Jet_area[16];   //[nJet]
   Float_t         Jet_btagDeepFlavB[16];   //[nJet]
   Float_t         Jet_btagDeepFlavCvB[16];   //[nJet]
   Float_t         Jet_btagDeepFlavCvL[16];   //[nJet]
   Float_t         Jet_btagDeepFlavQG[16];   //[nJet]
   Float_t         Jet_btagPNetB[16];   //[nJet]
   Float_t         Jet_btagPNetCvB[16];   //[nJet]
   Float_t         Jet_btagPNetCvL[16];   //[nJet]
   Float_t         Jet_btagPNetQvG[16];   //[nJet]
   Float_t         Jet_btagPNetTauVJet[16];   //[nJet]
   Float_t         Jet_btagRobustParTAK4B[16];   //[nJet]
   Float_t         Jet_btagRobustParTAK4CvB[16];   //[nJet]
   Float_t         Jet_btagRobustParTAK4CvL[16];   //[nJet]
   Float_t         Jet_btagRobustParTAK4QG[16];   //[nJet]
   Float_t         Jet_chEmEF[16];   //[nJet]
   Float_t         Jet_chHEF[16];   //[nJet]
   Float_t         Jet_eta[16];   //[nJet]
   Float_t         Jet_hfsigmaEtaEta[16];   //[nJet]
   Float_t         Jet_hfsigmaPhiPhi[16];   //[nJet]
   Float_t         Jet_mass[16];   //[nJet]
   Float_t         Jet_muEF[16];   //[nJet]
   Float_t         Jet_muonSubtrFactor[16];   //[nJet]
   Float_t         Jet_neEmEF[16];   //[nJet]
   Float_t         Jet_neHEF[16];   //[nJet]
   Float_t         Jet_phi[16];   //[nJet]
   Float_t         Jet_pt[16];   //[nJet]
   Float_t         Jet_rawFactor[16];   //[nJet]
   Int_t           nTau;
   UChar_t         Tau_decayMode[7];   //[nTau]
   Bool_t          Tau_idAntiEleDeadECal[7];   //[nTau]
   UChar_t         Tau_idAntiMu[7];   //[nTau]
   Bool_t          Tau_idDecayModeNewDMs[7];   //[nTau]
   Bool_t          Tau_idDecayModeOldDMs[7];   //[nTau]
   UChar_t         Tau_idDeepTau2017v2p1VSe[7];   //[nTau]
   UChar_t         Tau_idDeepTau2017v2p1VSjet[7];   //[nTau]
   UChar_t         Tau_idDeepTau2017v2p1VSmu[7];   //[nTau]
   UChar_t         Tau_idDeepTau2018v2p5VSe[7];   //[nTau]
   UChar_t         Tau_idDeepTau2018v2p5VSjet[7];   //[nTau]
   UChar_t         Tau_idDeepTau2018v2p5VSmu[7];   //[nTau]
   UChar_t         Tau_nSVs[7];   //[nTau]
   Short_t         Tau_charge[7];   //[nTau]
   Short_t         Tau_decayModePNet[7];   //[nTau]
   Short_t         Tau_eleIdx[7];   //[nTau]
   Short_t         Tau_jetIdx[7];   //[nTau]
   Short_t         Tau_muIdx[7];   //[nTau]
   Short_t         Tau_svIdx1[7];   //[nTau]
   Short_t         Tau_svIdx2[7];   //[nTau]
   Float_t         Tau_chargedIso[7];   //[nTau]
   Float_t         Tau_dxy[7];   //[nTau]
   Float_t         Tau_dz[7];   //[nTau]
   Float_t         Tau_eta[7];   //[nTau]
   Float_t         Tau_leadTkDeltaEta[7];   //[nTau]
   Float_t         Tau_leadTkDeltaPhi[7];   //[nTau]
   Float_t         Tau_leadTkPtOverTauPt[7];   //[nTau]
   Float_t         Tau_mass[7];   //[nTau]
   Float_t         Tau_neutralIso[7];   //[nTau]
   Float_t         Tau_phi[7];   //[nTau]
   Float_t         Tau_photonsOutsideSignalCone[7];   //[nTau]
   Float_t         Tau_probDM0PNet[7];   //[nTau]
   Float_t         Tau_probDM10PNet[7];   //[nTau]
   Float_t         Tau_probDM11PNet[7];   //[nTau]
   Float_t         Tau_probDM1PNet[7];   //[nTau]
   Float_t         Tau_probDM2PNet[7];   //[nTau]
   Float_t         Tau_pt[7];   //[nTau]
   Float_t         Tau_ptCorrPNet[7];   //[nTau]
   Float_t         Tau_puCorr[7];   //[nTau]
   Float_t         Tau_qConfPNet[7];   //[nTau]
   Float_t         Tau_rawDeepTau2017v2p1VSe[7];   //[nTau]
   Float_t         Tau_rawDeepTau2017v2p1VSjet[7];   //[nTau]
   Float_t         Tau_rawDeepTau2017v2p1VSmu[7];   //[nTau]
   Float_t         Tau_rawDeepTau2018v2p5VSe[7];   //[nTau]
   Float_t         Tau_rawDeepTau2018v2p5VSjet[7];   //[nTau]
   Float_t         Tau_rawDeepTau2018v2p5VSmu[7];   //[nTau]
   Float_t         Tau_rawIso[7];   //[nTau]
   Float_t         Tau_rawIsodR03[7];   //[nTau]
   Float_t         Tau_rawPNetVSe[7];   //[nTau]
   Float_t         Tau_rawPNetVSjet[7];   //[nTau]
   Float_t         Tau_rawPNetVSmu[7];   //[nTau]
   Float_t         TkMET_phi;
   Float_t         TkMET_pt;
   Float_t         TkMET_sumEt;
   Int_t           nTrigObj;
   Short_t         TrigObj_l1charge[68];   //[nTrigObj]
   UShort_t        TrigObj_id[68];   //[nTrigObj]
   Int_t           TrigObj_l1iso[68];   //[nTrigObj]
   Int_t           TrigObj_filterBits[68];   //[nTrigObj]
   Float_t         TrigObj_pt[68];   //[nTrigObj]
   Float_t         TrigObj_eta[68];   //[nTrigObj]
   Float_t         TrigObj_phi[68];   //[nTrigObj]
   Float_t         TrigObj_l1pt[68];   //[nTrigObj]
   Float_t         TrigObj_l1pt_2[68];   //[nTrigObj]
   Float_t         TrigObj_l2pt[68];   //[nTrigObj]
   Int_t           genTtbarId;
   Int_t           nOtherPV;
   Float_t         OtherPV_z[3];   //[nOtherPV]
   Float_t         OtherPV_score[3];   //[nOtherPV]
   UChar_t         PV_npvs;
   UChar_t         PV_npvsGood;
   Float_t         PV_ndof;
   Float_t         PV_x;
   Float_t         PV_y;
   Float_t         PV_z;
   Float_t         PV_chi2;
   Float_t         PV_score;
   Int_t           nSV;
   Short_t         SV_charge[13];   //[nSV]
   Float_t         SV_dlen[13];   //[nSV]
   Float_t         SV_dlenSig[13];   //[nSV]
   Float_t         SV_dxy[13];   //[nSV]
   Float_t         SV_dxySig[13];   //[nSV]
   Float_t         SV_pAngle[13];   //[nSV]
   UChar_t         boostedTau_genPartFlav[4];   //[nboostedTau]
   Short_t         boostedTau_genPartIdx[4];   //[nboostedTau]
   UChar_t         Electron_genPartFlav[7];   //[nElectron]
   Short_t         Electron_genPartIdx[7];   //[nElectron]
   UChar_t         FatJet_hadronFlavour[5];   //[nFatJet]
   UChar_t         FatJet_nBHadrons[5];   //[nFatJet]
   UChar_t         FatJet_nCHadrons[5];   //[nFatJet]
   Short_t         FatJet_genJetAK8Idx[5];   //[nFatJet]
   UChar_t         GenJetAK8_hadronFlavour[5];   //[nGenJetAK8]
   Short_t         GenJetAK8_partonFlavour[5];   //[nGenJetAK8]
   UChar_t         GenJet_hadronFlavour[19];   //[nGenJet]
   Short_t         GenJet_partonFlavour[19];   //[nGenJet]
   Float_t         GenVtx_t0;
   UChar_t         Jet_hadronFlavour[16];   //[nJet]
   Short_t         Jet_genJetIdx[16];   //[nJet]
   Short_t         Jet_partonFlavour[16];   //[nJet]
   UChar_t         LowPtElectron_genPartFlav[7];   //[nLowPtElectron]
   Short_t         LowPtElectron_genPartIdx[7];   //[nLowPtElectron]
   UChar_t         Muon_genPartFlav[8];   //[nMuon]
   Short_t         Muon_genPartIdx[8];   //[nMuon]
   UChar_t         Photon_genPartFlav[7];   //[nPhoton]
   Short_t         Photon_genPartIdx[7];   //[nPhoton]
   Float_t         MET_fiducialGenPhi;
   Float_t         MET_fiducialGenPt;
   UChar_t         SubJet_hadronFlavour[10];   //[nSubJet]
   UChar_t         SubJet_nBHadrons[10];   //[nSubJet]
   UChar_t         SubJet_nCHadrons[10];   //[nSubJet]
   UChar_t         SV_ntracks[13];   //[nSV]
   Float_t         SV_chi2[13];   //[nSV]
   Float_t         SV_eta[13];   //[nSV]
   Float_t         SV_mass[13];   //[nSV]
   Float_t         SV_ndof[13];   //[nSV]
   Float_t         SV_phi[13];   //[nSV]
   Float_t         SV_pt[13];   //[nSV]
   Float_t         SV_x[13];   //[nSV]
   Float_t         SV_y[13];   //[nSV]
   Float_t         SV_z[13];   //[nSV]
   UChar_t         Tau_genPartFlav[7];   //[nTau]
   Short_t         Tau_genPartIdx[7];   //[nTau]
   Bool_t          L1_AlwaysTrue;
   Bool_t          L1_BPTX_AND_Ref1_VME;
   Bool_t          L1_BPTX_AND_Ref3_VME;
   Bool_t          L1_BPTX_AND_Ref4_VME;
   Bool_t          L1_BPTX_BeamGas_B1_VME;
   Bool_t          L1_BPTX_BeamGas_B2_VME;
   Bool_t          L1_BPTX_BeamGas_Ref1_VME;
   Bool_t          L1_BPTX_BeamGas_Ref2_VME;
   Bool_t          L1_BPTX_NotOR_VME;
   Bool_t          L1_BPTX_OR_Ref3_VME;
   Bool_t          L1_BPTX_OR_Ref4_VME;
   Bool_t          L1_BPTX_RefAND_VME;
   Bool_t          L1_BptxMinus;
   Bool_t          L1_BptxOR;
   Bool_t          L1_BptxPlus;
   Bool_t          L1_BptxXOR;
   Bool_t          L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142;
   Bool_t          L1_DoubleEG10_er1p2_dR_Max0p6;
   Bool_t          L1_DoubleEG10p5_er1p2_dR_Max0p6;
   Bool_t          L1_DoubleEG11_er1p2_dR_Max0p6;
   Bool_t          L1_DoubleEG4_er1p2_dR_Max0p9;
   Bool_t          L1_DoubleEG4p5_er1p2_dR_Max0p9;
   Bool_t          L1_DoubleEG5_er1p2_dR_Max0p9;
   Bool_t          L1_DoubleEG5p5_er1p2_dR_Max0p8;
   Bool_t          L1_DoubleEG6_er1p2_dR_Max0p8;
   Bool_t          L1_DoubleEG6p5_er1p2_dR_Max0p8;
   Bool_t          L1_DoubleEG7_er1p2_dR_Max0p8;
   Bool_t          L1_DoubleEG7p5_er1p2_dR_Max0p7;
   Bool_t          L1_DoubleEG8_er1p2_dR_Max0p7;
   Bool_t          L1_DoubleEG8er2p5_HTT260er;
   Bool_t          L1_DoubleEG8er2p5_HTT280er;
   Bool_t          L1_DoubleEG8er2p5_HTT300er;
   Bool_t          L1_DoubleEG8er2p5_HTT320er;
   Bool_t          L1_DoubleEG8er2p5_HTT340er;
   Bool_t          L1_DoubleEG8p5_er1p2_dR_Max0p7;
   Bool_t          L1_DoubleEG9_er1p2_dR_Max0p7;
   Bool_t          L1_DoubleEG9p5_er1p2_dR_Max0p6;
   Bool_t          L1_DoubleEG_15_10_er2p5;
   Bool_t          L1_DoubleEG_20_10_er2p5;
   Bool_t          L1_DoubleEG_22_10_er2p5;
   Bool_t          L1_DoubleEG_25_12_er2p5;
   Bool_t          L1_DoubleEG_25_14_er2p5;
   Bool_t          L1_DoubleEG_27_14_er2p5;
   Bool_t          L1_DoubleEG_LooseIso16_LooseIso12_er1p5;
   Bool_t          L1_DoubleEG_LooseIso18_LooseIso12_er1p5;
   Bool_t          L1_DoubleEG_LooseIso20_LooseIso12_er1p5;
   Bool_t          L1_DoubleEG_LooseIso22_12_er2p5;
   Bool_t          L1_DoubleEG_LooseIso22_LooseIso12_er1p5;
   Bool_t          L1_DoubleEG_LooseIso25_12_er2p5;
   Bool_t          L1_DoubleEG_LooseIso25_LooseIso12_er1p5;
   Bool_t          L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5;
   Bool_t          L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5;
   Bool_t          L1_DoubleIsoTau28er2p1;
   Bool_t          L1_DoubleIsoTau28er2p1_Mass_Max80;
   Bool_t          L1_DoubleIsoTau28er2p1_Mass_Max90;
   Bool_t          L1_DoubleIsoTau30er2p1;
   Bool_t          L1_DoubleIsoTau30er2p1_Mass_Max80;
   Bool_t          L1_DoubleIsoTau30er2p1_Mass_Max90;
   Bool_t          L1_DoubleIsoTau32er2p1;
   Bool_t          L1_DoubleIsoTau32er2p1_Mass_Max80;
   Bool_t          L1_DoubleIsoTau34er2p1;
   Bool_t          L1_DoubleIsoTau35er2p1;
   Bool_t          L1_DoubleIsoTau36er2p1;
   Bool_t          L1_DoubleJet100er2p3_dEta_Max1p6;
   Bool_t          L1_DoubleJet100er2p5;
   Bool_t          L1_DoubleJet112er2p3_dEta_Max1p6;
   Bool_t          L1_DoubleJet120er2p5;
   Bool_t          L1_DoubleJet120er2p5_Mu3_dR_Max0p8;
   Bool_t          L1_DoubleJet150er2p5;
   Bool_t          L1_DoubleJet16er2p5_Mu3_dR_Max0p4;
   Bool_t          L1_DoubleJet30er2p5_Mass_Min225_dEta_Max1p5;
   Bool_t          L1_DoubleJet30er2p5_Mass_Min250_dEta_Max1p5;
   Bool_t          L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5;
   Bool_t          L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5;
   Bool_t          L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5;
   Bool_t          L1_DoubleJet35_Mass_Min450_IsoTau45_RmOvlp;
   Bool_t          L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5;
   Bool_t          L1_DoubleJet35er2p5_Mu3_dR_Max0p4;
   Bool_t          L1_DoubleJet40_Mass_Min450_IsoEG10er2p1_RmOvlp_dR0p2;
   Bool_t          L1_DoubleJet40_Mass_Min450_LooseIsoEG15er2p1_RmOvlp_dR0p2;
   Bool_t          L1_DoubleJet40er2p5;
   Bool_t          L1_DoubleJet45_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5;
   Bool_t          L1_DoubleJet45_Mass_Min450_LooseIsoEG20er2p1_RmOvlp_dR0p2;
   Bool_t          L1_DoubleJet60er2p5_Mu3_dR_Max0p4;
   Bool_t          L1_DoubleJet80er2p5_Mu3_dR_Max0p4;
   Bool_t          L1_DoubleJet_100_30_DoubleJet30_Mass_Min620;
   Bool_t          L1_DoubleJet_100_30_DoubleJet30_Mass_Min800;
   Bool_t          L1_DoubleJet_110_35_DoubleJet35_Mass_Min620;
   Bool_t          L1_DoubleJet_110_35_DoubleJet35_Mass_Min800;
   Bool_t          L1_DoubleJet_115_40_DoubleJet40_Mass_Min620;
   Bool_t          L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28;
   Bool_t          L1_DoubleJet_120_45_DoubleJet45_Mass_Min620;
   Bool_t          L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28;
   Bool_t          L1_DoubleJet_60_30_DoubleJet30_Mass_Min500_DoubleJetCentral50;
   Bool_t          L1_DoubleJet_65_30_DoubleJet30_Mass_Min400_ETMHF65;
   Bool_t          L1_DoubleJet_65_35_DoubleJet35_Mass_Min500_DoubleJetCentral50;
   Bool_t          L1_DoubleJet_70_35_DoubleJet35_Mass_Min400_ETMHF65;
   Bool_t          L1_DoubleJet_80_30_DoubleJet30_Mass_Min500_Mu3OQ;
   Bool_t          L1_DoubleJet_80_30_Mass_Min420_DoubleMu0_SQ;
   Bool_t          L1_DoubleJet_80_30_Mass_Min420_IsoTau40_RmOvlp;
   Bool_t          L1_DoubleJet_80_30_Mass_Min420_Mu8;
   Bool_t          L1_DoubleJet_85_35_DoubleJet35_Mass_Min500_Mu3OQ;
   Bool_t          L1_DoubleJet_90_30_DoubleJet30_Mass_Min620;
   Bool_t          L1_DoubleJet_90_30_DoubleJet30_Mass_Min800;
   Bool_t          L1_DoubleLLPJet40;
   Bool_t          L1_DoubleLooseIsoEG22er2p1;
   Bool_t          L1_DoubleLooseIsoEG24er2p1;
   Bool_t          L1_DoubleMu0;
   Bool_t          L1_DoubleMu0_Mass_Min1;
   Bool_t          L1_DoubleMu0_OQ;
   Bool_t          L1_DoubleMu0_SQ;
   Bool_t          L1_DoubleMu0_SQ_OS;
   Bool_t          L1_DoubleMu0_Upt15_Upt7;
   Bool_t          L1_DoubleMu0_Upt15_Upt7_BMTF_EMTF;
   Bool_t          L1_DoubleMu0_Upt5_Upt5;
   Bool_t          L1_DoubleMu0_Upt5_Upt5_BMTF_EMTF;
   Bool_t          L1_DoubleMu0_Upt6_IP_Min1_Upt4;
   Bool_t          L1_DoubleMu0_Upt6_IP_Min1_Upt4_BMTF_EMTF;
   Bool_t          L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8;
   Bool_t          L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6;
   Bool_t          L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2;
   Bool_t          L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4;
   Bool_t          L1_DoubleMu0er1p5_SQ;
   Bool_t          L1_DoubleMu0er1p5_SQ_OS;
   Bool_t          L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2;
   Bool_t          L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4;
   Bool_t          L1_DoubleMu0er1p5_SQ_dR_Max1p4;
   Bool_t          L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5;
   Bool_t          L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6;
   Bool_t          L1_DoubleMu0er2p0_SQ_dEta_Max1p5;
   Bool_t          L1_DoubleMu0er2p0_SQ_dEta_Max1p6;
   Bool_t          L1_DoubleMu18er2p1_SQ;
   Bool_t          L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20;
   Bool_t          L1_DoubleMu3_SQ_ETMHF30_HTT60er;
   Bool_t          L1_DoubleMu3_SQ_ETMHF30_Jet60er2p5_OR_DoubleJet40er2p5;
   Bool_t          L1_DoubleMu3_SQ_ETMHF40_HTT60er;
   Bool_t          L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5;
   Bool_t          L1_DoubleMu3_SQ_ETMHF50_HTT60er;
   Bool_t          L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5;
   Bool_t          L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5;
   Bool_t          L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5;
   Bool_t          L1_DoubleMu3_SQ_HTT220er;
   Bool_t          L1_DoubleMu3_SQ_HTT240er;
   Bool_t          L1_DoubleMu3_SQ_HTT260er;
   Bool_t          L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8;
   Bool_t          L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6;
   Bool_t          L1_DoubleMu4_SQ_EG9er2p5;
   Bool_t          L1_DoubleMu4_SQ_OS;
   Bool_t          L1_DoubleMu4_SQ_OS_dR_Max1p2;
   Bool_t          L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6;
   Bool_t          L1_DoubleMu4p5_SQ_OS;
   Bool_t          L1_DoubleMu4p5_SQ_OS_dR_Max1p2;
   Bool_t          L1_DoubleMu4p5er2p0_SQ_OS;
   Bool_t          L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18;
   Bool_t          L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7;
   Bool_t          L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20;
   Bool_t          L1_DoubleMu5_SQ_EG9er2p5;
   Bool_t          L1_DoubleMu5_SQ_OS_dR_Max1p6;
   Bool_t          L1_DoubleMu8_SQ;
   Bool_t          L1_DoubleMu9_SQ;
   Bool_t          L1_DoubleMu_12_5;
   Bool_t          L1_DoubleMu_15_5_SQ;
   Bool_t          L1_DoubleMu_15_7;
   Bool_t          L1_DoubleMu_15_7_Mass_Min1;
   Bool_t          L1_DoubleMu_15_7_SQ;
   Bool_t          L1_DoubleTau70er2p1;
   Bool_t          L1_ETM120;
   Bool_t          L1_ETM150;
   Bool_t          L1_ETMHF100;
   Bool_t          L1_ETMHF100_HTT60er;
   Bool_t          L1_ETMHF110;
   Bool_t          L1_ETMHF110_HTT60er;
   Bool_t          L1_ETMHF120;
   Bool_t          L1_ETMHF120_HTT60er;
   Bool_t          L1_ETMHF130;
   Bool_t          L1_ETMHF130_HTT60er;
   Bool_t          L1_ETMHF140;
   Bool_t          L1_ETMHF150;
   Bool_t          L1_ETMHF70;
   Bool_t          L1_ETMHF70_HTT60er;
   Bool_t          L1_ETMHF80;
   Bool_t          L1_ETMHF80_HTT60er;
   Bool_t          L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p1;
   Bool_t          L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p6;
   Bool_t          L1_ETMHF90;
   Bool_t          L1_ETMHF90_HTT60er;
   Bool_t          L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1;
   Bool_t          L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6;
   Bool_t          L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1;
   Bool_t          L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6;
   Bool_t          L1_ETT1600;
   Bool_t          L1_ETT2000;
   Bool_t          L1_FirstBunchAfterTrain;
   Bool_t          L1_FirstBunchBeforeTrain;
   Bool_t          L1_FirstBunchInTrain;
   Bool_t          L1_FirstCollisionInOrbit;
   Bool_t          L1_FirstCollisionInTrain;
   Bool_t          L1_HCAL_LaserMon_Trig;
   Bool_t          L1_HCAL_LaserMon_Veto;
   Bool_t          L1_HTT120_SingleLLPJet40;
   Bool_t          L1_HTT120er;
   Bool_t          L1_HTT160_SingleLLPJet50;
   Bool_t          L1_HTT160er;
   Bool_t          L1_HTT200_SingleLLPJet60;
   Bool_t          L1_HTT200er;
   Bool_t          L1_HTT240_SingleLLPJet70;
   Bool_t          L1_HTT255er;
   Bool_t          L1_HTT280er;
   Bool_t          L1_HTT280er_QuadJet_70_55_40_35_er2p5;
   Bool_t          L1_HTT320er;
   Bool_t          L1_HTT320er_QuadJet_70_55_40_40_er2p5;
   Bool_t          L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3;
   Bool_t          L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3;
   Bool_t          L1_HTT360er;
   Bool_t          L1_HTT400er;
   Bool_t          L1_HTT450er;
   Bool_t          L1_IsoEG32er2p5_Mt40;
   Bool_t          L1_IsoTau52er2p1_QuadJet36er2p5;
   Bool_t          L1_IsolatedBunch;
   Bool_t          L1_LastBunchInTrain;
   Bool_t          L1_LastCollisionInTrain;
   Bool_t          L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3;
   Bool_t          L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3;
   Bool_t          L1_LooseIsoEG24er2p1_HTT100er;
   Bool_t          L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3;
   Bool_t          L1_LooseIsoEG26er2p1_HTT100er;
   Bool_t          L1_LooseIsoEG26er2p1_Jet34er2p5_dR_Min0p3;
   Bool_t          L1_LooseIsoEG28er2p1_HTT100er;
   Bool_t          L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3;
   Bool_t          L1_LooseIsoEG30er2p1_HTT100er;
   Bool_t          L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3;
   Bool_t          L1_MinimumBiasHF0;
   Bool_t          L1_MinimumBiasHF0_AND_BptxAND;
   Bool_t          L1_Mu10er2p3_Jet32er2p3_dR_Max0p4_DoubleJet32er2p3_dEta_Max1p6;
   Bool_t          L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6;
   Bool_t          L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6;
   Bool_t          L1_Mu18er2p1_Tau24er2p1;
   Bool_t          L1_Mu18er2p1_Tau26er2p1;
   Bool_t          L1_Mu18er2p1_Tau26er2p1_Jet55;
   Bool_t          L1_Mu18er2p1_Tau26er2p1_Jet70;
   Bool_t          L1_Mu20_EG10er2p5;
   Bool_t          L1_Mu22er2p1_IsoTau28er2p1;
   Bool_t          L1_Mu22er2p1_IsoTau30er2p1;
   Bool_t          L1_Mu22er2p1_IsoTau32er2p1;
   Bool_t          L1_Mu22er2p1_IsoTau34er2p1;
   Bool_t          L1_Mu22er2p1_IsoTau36er2p1;
   Bool_t          L1_Mu22er2p1_IsoTau40er2p1;
   Bool_t          L1_Mu22er2p1_Tau70er2p1;
   Bool_t          L1_Mu3_Jet120er2p5_dR_Max0p4;
   Bool_t          L1_Mu3_Jet16er2p5_dR_Max0p4;
   Bool_t          L1_Mu3_Jet30er2p5;
   Bool_t          L1_Mu3_Jet60er2p5_dR_Max0p4;
   Bool_t          L1_Mu3er1p5_Jet100er2p5_ETMHF30;
   Bool_t          L1_Mu3er1p5_Jet100er2p5_ETMHF40;
   Bool_t          L1_Mu3er1p5_Jet100er2p5_ETMHF50;
   Bool_t          L1_Mu5_EG23er2p5;
   Bool_t          L1_Mu5_LooseIsoEG20er2p5;
   Bool_t          L1_Mu6_DoubleEG10er2p5;
   Bool_t          L1_Mu6_DoubleEG12er2p5;
   Bool_t          L1_Mu6_DoubleEG15er2p5;
   Bool_t          L1_Mu6_DoubleEG17er2p5;
   Bool_t          L1_Mu6_HTT240er;
   Bool_t          L1_Mu6_HTT250er;
   Bool_t          L1_Mu7_EG20er2p5;
   Bool_t          L1_Mu7_EG23er2p5;
   Bool_t          L1_Mu7_LooseIsoEG20er2p5;
   Bool_t          L1_Mu7_LooseIsoEG23er2p5;
   Bool_t          L1_NotBptxOR;
   Bool_t          L1_QuadJet60er2p5;
   Bool_t          L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0;
   Bool_t          L1_QuadMu0;
   Bool_t          L1_QuadMu0_OQ;
   Bool_t          L1_QuadMu0_SQ;
   Bool_t          L1_SecondBunchInTrain;
   Bool_t          L1_SecondLastBunchInTrain;
   Bool_t          L1_SingleEG10er2p5;
   Bool_t          L1_SingleEG15er2p5;
   Bool_t          L1_SingleEG26er2p5;
   Bool_t          L1_SingleEG28_FWD2p5;
   Bool_t          L1_SingleEG28er1p5;
   Bool_t          L1_SingleEG28er2p1;
   Bool_t          L1_SingleEG28er2p5;
   Bool_t          L1_SingleEG34er2p5;
   Bool_t          L1_SingleEG36er2p5;
   Bool_t          L1_SingleEG38er2p5;
   Bool_t          L1_SingleEG40er2p5;
   Bool_t          L1_SingleEG42er2p5;
   Bool_t          L1_SingleEG45er2p5;
   Bool_t          L1_SingleEG50;
   Bool_t          L1_SingleEG60;
   Bool_t          L1_SingleEG8er2p5;
   Bool_t          L1_SingleIsoEG24er2p1;
   Bool_t          L1_SingleIsoEG26er2p1;
   Bool_t          L1_SingleIsoEG26er2p5;
   Bool_t          L1_SingleIsoEG28_FWD2p5;
   Bool_t          L1_SingleIsoEG28er1p5;
   Bool_t          L1_SingleIsoEG28er2p1;
   Bool_t          L1_SingleIsoEG28er2p5;
   Bool_t          L1_SingleIsoEG30er2p1;
   Bool_t          L1_SingleIsoEG30er2p5;
   Bool_t          L1_SingleIsoEG32er2p1;
   Bool_t          L1_SingleIsoEG32er2p5;
   Bool_t          L1_SingleIsoEG34er2p5;
   Bool_t          L1_SingleIsoTau32er2p1;
   Bool_t          L1_SingleJet10erHE;
   Bool_t          L1_SingleJet120;
   Bool_t          L1_SingleJet120_FWD2p5;
   Bool_t          L1_SingleJet120_FWD3p0;
   Bool_t          L1_SingleJet120er2p5;
   Bool_t          L1_SingleJet12erHE;
   Bool_t          L1_SingleJet140er2p5;
   Bool_t          L1_SingleJet140er2p5_ETMHF90;
   Bool_t          L1_SingleJet160er2p5;
   Bool_t          L1_SingleJet180;
   Bool_t          L1_SingleJet180er2p5;
   Bool_t          L1_SingleJet200;
   Bool_t          L1_SingleJet20er2p5_NotBptxOR;
   Bool_t          L1_SingleJet20er2p5_NotBptxOR_3BX;
   Bool_t          L1_SingleJet35;
   Bool_t          L1_SingleJet35_FWD2p5;
   Bool_t          L1_SingleJet35_FWD3p0;
   Bool_t          L1_SingleJet35er2p5;
   Bool_t          L1_SingleJet43er2p5_NotBptxOR_3BX;
   Bool_t          L1_SingleJet46er2p5_NotBptxOR_3BX;
   Bool_t          L1_SingleJet60;
   Bool_t          L1_SingleJet60_FWD2p5;
   Bool_t          L1_SingleJet8erHE;
   Bool_t          L1_SingleJet90;
   Bool_t          L1_SingleJet90_FWD2p5;
   Bool_t          L1_SingleLooseIsoEG26er1p5;
   Bool_t          L1_SingleLooseIsoEG26er2p5;
   Bool_t          L1_SingleLooseIsoEG28_FWD2p5;
   Bool_t          L1_SingleLooseIsoEG28er1p5;
   Bool_t          L1_SingleLooseIsoEG28er2p1;
   Bool_t          L1_SingleLooseIsoEG28er2p5;
   Bool_t          L1_SingleLooseIsoEG30er1p5;
   Bool_t          L1_SingleLooseIsoEG30er2p5;
   Bool_t          L1_SingleMu0_BMTF;
   Bool_t          L1_SingleMu0_DQ;
   Bool_t          L1_SingleMu0_EMTF;
   Bool_t          L1_SingleMu0_OMTF;
   Bool_t          L1_SingleMu0_Upt10;
   Bool_t          L1_SingleMu0_Upt10_BMTF;
   Bool_t          L1_SingleMu0_Upt10_EMTF;
   Bool_t          L1_SingleMu0_Upt10_OMTF;
   Bool_t          L1_SingleMu12_DQ_BMTF;
   Bool_t          L1_SingleMu12_DQ_EMTF;
   Bool_t          L1_SingleMu12_DQ_OMTF;
   Bool_t          L1_SingleMu15_DQ;
   Bool_t          L1_SingleMu18;
   Bool_t          L1_SingleMu20;
   Bool_t          L1_SingleMu22;
   Bool_t          L1_SingleMu22_BMTF;
   Bool_t          L1_SingleMu22_DQ;
   Bool_t          L1_SingleMu22_EMTF;
   Bool_t          L1_SingleMu22_OMTF;
   Bool_t          L1_SingleMu22_OQ;
   Bool_t          L1_SingleMu25;
   Bool_t          L1_SingleMu3;
   Bool_t          L1_SingleMu5;
   Bool_t          L1_SingleMu7;
   Bool_t          L1_SingleMu7_DQ;
   Bool_t          L1_SingleMuCosmics;
   Bool_t          L1_SingleMuCosmics_BMTF;
   Bool_t          L1_SingleMuCosmics_EMTF;
   Bool_t          L1_SingleMuCosmics_OMTF;
   Bool_t          L1_SingleMuOpen;
   Bool_t          L1_SingleMuOpen_BMTF;
   Bool_t          L1_SingleMuOpen_EMTF;
   Bool_t          L1_SingleMuOpen_NotBptxOR;
   Bool_t          L1_SingleMuOpen_OMTF;
   Bool_t          L1_SingleMuOpen_er1p1_NotBptxOR_3BX;
   Bool_t          L1_SingleMuOpen_er1p4_NotBptxOR_3BX;
   Bool_t          L1_SingleMuShower_Nominal;
   Bool_t          L1_SingleMuShower_Tight;
   Bool_t          L1_SingleTau120er2p1;
   Bool_t          L1_SingleTau130er2p1;
   Bool_t          L1_SingleTau70er2p1;
   Bool_t          L1_TOTEM_1;
   Bool_t          L1_TOTEM_2;
   Bool_t          L1_TOTEM_3;
   Bool_t          L1_TOTEM_4;
   Bool_t          L1_TripleEG16er2p5;
   Bool_t          L1_TripleEG_18_17_8_er2p5;
   Bool_t          L1_TripleEG_18_18_12_er2p5;
   Bool_t          L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5;
   Bool_t          L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5;
   Bool_t          L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5;
   Bool_t          L1_TripleMu0;
   Bool_t          L1_TripleMu0_OQ;
   Bool_t          L1_TripleMu0_SQ;
   Bool_t          L1_TripleMu3;
   Bool_t          L1_TripleMu3_SQ;
   Bool_t          L1_TripleMu_3SQ_2p5SQ_0;
   Bool_t          L1_TripleMu_3SQ_2p5SQ_0_Mass_Max12;
   Bool_t          L1_TripleMu_3SQ_2p5SQ_0_OS_Mass_Max12;
   Bool_t          L1_TripleMu_4SQ_2p5SQ_0_OS_Mass_Max12;
   Bool_t          L1_TripleMu_5SQ_3SQ_0OQ;
   Bool_t          L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9;
   Bool_t          L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9;
   Bool_t          L1_TripleMu_5_3_3;
   Bool_t          L1_TripleMu_5_3_3_SQ;
   Bool_t          L1_TripleMu_5_3p5_2p5;
   Bool_t          L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17;
   Bool_t          L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17;
   Bool_t          L1_TripleMu_5_5_3;
   Bool_t          L1_TwoMuShower_Loose;
   Bool_t          L1_UnpairedBunchBptxMinus;
   Bool_t          L1_UnpairedBunchBptxPlus;
   Bool_t          L1_ZeroBias;
   Bool_t          L1_ZeroBias_copy;
   Bool_t          L1_UnprefireableEvent;
   Bool_t          Flag_HBHENoiseFilter;
   Bool_t          Flag_HBHENoiseIsoFilter;
   Bool_t          Flag_CSCTightHaloFilter;
   Bool_t          Flag_CSCTightHaloTrkMuUnvetoFilter;
   Bool_t          Flag_CSCTightHalo2015Filter;
   Bool_t          Flag_globalTightHalo2016Filter;
   Bool_t          Flag_globalSuperTightHalo2016Filter;
   Bool_t          Flag_HcalStripHaloFilter;
   Bool_t          Flag_hcalLaserEventFilter;
   Bool_t          Flag_EcalDeadCellTriggerPrimitiveFilter;
   Bool_t          Flag_EcalDeadCellBoundaryEnergyFilter;
   Bool_t          Flag_ecalBadCalibFilter;
   Bool_t          Flag_goodVertices;
   Bool_t          Flag_eeBadScFilter;
   Bool_t          Flag_ecalLaserCorrFilter;
   Bool_t          Flag_trkPOGFilters;
   Bool_t          Flag_chargedHadronTrackResolutionFilter;
   Bool_t          Flag_muonBadTrackFilter;
   Bool_t          Flag_BadChargedCandidateFilter;
   Bool_t          Flag_BadPFMuonFilter;
   Bool_t          Flag_BadPFMuonDzFilter;
   Bool_t          Flag_hfNoisyHitsFilter;
   Bool_t          Flag_BadChargedCandidateSummer16Filter;
   Bool_t          Flag_BadPFMuonSummer16Filter;
   Bool_t          Flag_trkPOG_manystripclus53X;
   Bool_t          Flag_trkPOG_toomanystripclus53X;
   Bool_t          Flag_trkPOG_logErrorTooManyClusters;
   Bool_t          Flag_METFilters;
   Bool_t          L1Reco_step;
   Bool_t          L1simulation_step;
   Bool_t          HLTriggerFirstPath;
   Bool_t          HLT_EphemeralPhysics;
   Bool_t          HLT_EphemeralZeroBias;
   Bool_t          HLT_EcalCalibration;
   Bool_t          HLT_HcalCalibration;
   Bool_t          HLT_HcalNZS;
   Bool_t          HLT_HcalPhiSym;
   Bool_t          HLT_Random;
   Bool_t          HLT_Physics;
   Bool_t          HLT_ZeroBias;
   Bool_t          HLT_ZeroBias_Alignment;
   Bool_t          HLT_ZeroBias_Beamspot;
   Bool_t          HLT_ZeroBias_IsolatedBunches;
   Bool_t          HLT_ZeroBias_FirstBXAfterTrain;
   Bool_t          HLT_ZeroBias_FirstCollisionAfterAbortGap;
   Bool_t          HLT_ZeroBias_FirstCollisionInTrain;
   Bool_t          HLT_ZeroBias_LastCollisionInTrain;
   Bool_t          HLT_HT300_Beamspot;
   Bool_t          HLT_IsoTrackHB;
   Bool_t          HLT_IsoTrackHE;
   Bool_t          HLT_PFJet40_GPUvsCPU;
   Bool_t          HLT_AK8PFJet400_MassSD30;
   Bool_t          HLT_AK8PFJet420_MassSD30;
   Bool_t          HLT_AK8PFJet450_MassSD30;
   Bool_t          HLT_AK8PFJet470_MassSD30;
   Bool_t          HLT_AK8PFJet500_MassSD30;
   Bool_t          HLT_AK8DiPFJet250_250_MassSD30;
   Bool_t          HLT_AK8DiPFJet260_260_MassSD30;
   Bool_t          HLT_AK8DiPFJet270_270_MassSD30;
   Bool_t          HLT_AK8DiPFJet280_280_MassSD30;
   Bool_t          HLT_AK8DiPFJet290_290_MassSD30;
   Bool_t          HLT_AK8DiPFJet250_250_MassSD50;
   Bool_t          HLT_AK8DiPFJet260_260_MassSD50;
   Bool_t          HLT_CaloJet500_NoJetID;
   Bool_t          HLT_CaloJet550_NoJetID;
   Bool_t          HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL;
   Bool_t          HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon;
   Bool_t          HLT_Trimuon5_3p5_2_Upsilon_Muon;
   Bool_t          HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon;
   Bool_t          HLT_DoubleEle25_CaloIdL_MW;
   Bool_t          HLT_DoubleEle27_CaloIdL_MW;
   Bool_t          HLT_DoubleEle33_CaloIdL_MW;
   Bool_t          HLT_DoubleEle24_eta2p1_WPTight_Gsf;
   Bool_t          HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350;
   Bool_t          HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350;
   Bool_t          HLT_Mu27_Ele37_CaloIdL_MW;
   Bool_t          HLT_Mu37_Ele27_CaloIdL_MW;
   Bool_t          HLT_Mu37_TkMu27;
   Bool_t          HLT_DoubleMu4_3_Bs;
   Bool_t          HLT_DoubleMu4_3_Jpsi;
   Bool_t          HLT_DoubleMu4_3_LowMass;
   Bool_t          HLT_DoubleMu4_LowMass_Displaced;
   Bool_t          HLT_Mu0_L1DoubleMu;
   Bool_t          HLT_Mu4_L1DoubleMu;
   Bool_t          HLT_DoubleMu4_3_Photon4_BsToMMG;
   Bool_t          HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG;
   Bool_t          HLT_DoubleMu3_Trk_Tau3mu;
   Bool_t          HLT_DoubleMu3_TkMu_DsTau3Mu;
   Bool_t          HLT_DoubleMu4_Mass3p8_DZ_PFHT350;
   Bool_t          HLT_DoubleMu4_MuMuTrk_Displaced;
   Bool_t          HLT_Mu3_PFJet40;
   Bool_t          HLT_Mu7p5_L2Mu2_Jpsi;
   Bool_t          HLT_Mu7p5_L2Mu2_Upsilon;
   Bool_t          HLT_Mu3_L1SingleMu5orSingleMu7;
   Bool_t          HLT_DoublePhoton33_CaloIdL;
   Bool_t          HLT_DoublePhoton70;
   Bool_t          HLT_DoublePhoton85;
   Bool_t          HLT_DiEle27_WPTightCaloOnly_L1DoubleEG;
   Bool_t          HLT_Ele30_WPTight_Gsf;
   Bool_t          HLT_Ele32_WPTight_Gsf;
   Bool_t          HLT_Ele35_WPTight_Gsf;
   Bool_t          HLT_Ele38_WPTight_Gsf;
   Bool_t          HLT_Ele40_WPTight_Gsf;
   Bool_t          HLT_Ele32_WPTight_Gsf_L1DoubleEG;
   Bool_t          HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1;
   Bool_t          HLT_IsoMu20;
   Bool_t          HLT_IsoMu24;
   Bool_t          HLT_IsoMu24_eta2p1;
   Bool_t          HLT_IsoMu27;
   Bool_t          HLT_UncorrectedJetE30_NoBPTX;
   Bool_t          HLT_UncorrectedJetE30_NoBPTX3BX;
   Bool_t          HLT_UncorrectedJetE60_NoBPTX3BX;
   Bool_t          HLT_UncorrectedJetE70_NoBPTX3BX;
   Bool_t          HLT_L1SingleMuCosmics;
   Bool_t          HLT_L2Mu10_NoVertex_NoBPTX3BX;
   Bool_t          HLT_L2Mu10_NoVertex_NoBPTX;
   Bool_t          HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX;
   Bool_t          HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX;
   Bool_t          HLT_L2Mu23NoVtx_2Cha;
   Bool_t          HLT_L2Mu23NoVtx_2Cha_CosmicSeed;
   Bool_t          HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4;
   Bool_t          HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4;
   Bool_t          HLT_DoubleL2Mu50;
   Bool_t          HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed;
   Bool_t          HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed;
   Bool_t          HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4;
   Bool_t          HLT_DoubleL2Mu23NoVtx_2Cha;
   Bool_t          HLT_DoubleL2Mu25NoVtx_2Cha;
   Bool_t          HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL;
   Bool_t          HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ;
   Bool_t          HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8;
   Bool_t          HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8;
   Bool_t          HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8;
   Bool_t          HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8;
   Bool_t          HLT_Mu30_TkMu0_Psi;
   Bool_t          HLT_Mu30_TkMu0_Upsilon;
   Bool_t          HLT_Mu25_TkMu0_Phi;
   Bool_t          HLT_Mu15;
   Bool_t          HLT_Mu20;
   Bool_t          HLT_Mu27;
   Bool_t          HLT_Mu50;
   Bool_t          HLT_Mu55;
   Bool_t          HLT_CascadeMu100;
   Bool_t          HLT_HighPtTkMu100;
   Bool_t          HLT_DiPFJetAve40;
   Bool_t          HLT_DiPFJetAve60;
   Bool_t          HLT_DiPFJetAve80;
   Bool_t          HLT_DiPFJetAve140;
   Bool_t          HLT_DiPFJetAve200;
   Bool_t          HLT_DiPFJetAve260;
   Bool_t          HLT_DiPFJetAve320;
   Bool_t          HLT_DiPFJetAve400;
   Bool_t          HLT_DiPFJetAve500;
   Bool_t          HLT_DiPFJetAve60_HFJEC;
   Bool_t          HLT_DiPFJetAve80_HFJEC;
   Bool_t          HLT_DiPFJetAve100_HFJEC;
   Bool_t          HLT_DiPFJetAve160_HFJEC;
   Bool_t          HLT_DiPFJetAve220_HFJEC;
   Bool_t          HLT_DiPFJetAve260_HFJEC;
   Bool_t          HLT_DiPFJetAve300_HFJEC;
   Bool_t          HLT_AK8PFJet40;
   Bool_t          HLT_AK8PFJet60;
   Bool_t          HLT_AK8PFJet80;
   Bool_t          HLT_AK8PFJet140;
   Bool_t          HLT_AK8PFJet200;
   Bool_t          HLT_AK8PFJet260;
   Bool_t          HLT_AK8PFJet320;
   Bool_t          HLT_AK8PFJet400;
   Bool_t          HLT_AK8PFJet450;
   Bool_t          HLT_AK8PFJet500;
   Bool_t          HLT_AK8PFJet550;
   Bool_t          HLT_PFJet40;
   Bool_t          HLT_PFJet60;
   Bool_t          HLT_PFJet80;
   Bool_t          HLT_PFJet110;
   Bool_t          HLT_PFJet140;
   Bool_t          HLT_PFJet200;
   Bool_t          HLT_PFJet260;
   Bool_t          HLT_PFJet320;
   Bool_t          HLT_PFJet400;
   Bool_t          HLT_PFJet450;
   Bool_t          HLT_PFJet500;
   Bool_t          HLT_PFJet550;
   Bool_t          HLT_PFJetFwd40;
   Bool_t          HLT_PFJetFwd60;
   Bool_t          HLT_PFJetFwd80;
   Bool_t          HLT_PFJetFwd140;
   Bool_t          HLT_PFJetFwd200;
   Bool_t          HLT_PFJetFwd260;
   Bool_t          HLT_PFJetFwd320;
   Bool_t          HLT_PFJetFwd400;
   Bool_t          HLT_PFJetFwd450;
   Bool_t          HLT_PFJetFwd500;
   Bool_t          HLT_AK8PFJetFwd15;
   Bool_t          HLT_AK8PFJetFwd25;
   Bool_t          HLT_AK8PFJetFwd40;
   Bool_t          HLT_AK8PFJetFwd60;
   Bool_t          HLT_AK8PFJetFwd80;
   Bool_t          HLT_AK8PFJetFwd140;
   Bool_t          HLT_AK8PFJetFwd200;
   Bool_t          HLT_AK8PFJetFwd260;
   Bool_t          HLT_AK8PFJetFwd320;
   Bool_t          HLT_AK8PFJetFwd400;
   Bool_t          HLT_AK8PFJetFwd450;
   Bool_t          HLT_AK8PFJetFwd500;
   Bool_t          HLT_PFHT180;
   Bool_t          HLT_PFHT250;
   Bool_t          HLT_PFHT370;
   Bool_t          HLT_PFHT430;
   Bool_t          HLT_PFHT510;
   Bool_t          HLT_PFHT590;
   Bool_t          HLT_PFHT680;
   Bool_t          HLT_PFHT780;
   Bool_t          HLT_PFHT890;
   Bool_t          HLT_PFHT1050;
   Bool_t          HLT_PFHT500_PFMET100_PFMHT100_IDTight;
   Bool_t          HLT_PFHT500_PFMET110_PFMHT110_IDTight;
   Bool_t          HLT_PFHT700_PFMET85_PFMHT85_IDTight;
   Bool_t          HLT_PFHT800_PFMET75_PFMHT75_IDTight;
   Bool_t          HLT_PFMET120_PFMHT120_IDTight;
   Bool_t          HLT_PFMET130_PFMHT130_IDTight;
   Bool_t          HLT_PFMET140_PFMHT140_IDTight;
   Bool_t          HLT_PFMET120_PFMHT120_IDTight_PFHT60;
   Bool_t          HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60;
   Bool_t          HLT_PFMETTypeOne140_PFMHT140_IDTight;
   Bool_t          HLT_PFMETNoMu120_PFMHTNoMu120_IDTight;
   Bool_t          HLT_PFMETNoMu130_PFMHTNoMu130_IDTight;
   Bool_t          HLT_PFMETNoMu140_PFMHTNoMu140_IDTight;
   Bool_t          HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF;
   Bool_t          HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF;
   Bool_t          HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF;
   Bool_t          HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF;
   Bool_t          HLT_L1ETMHadSeeds;
   Bool_t          HLT_CaloMHT90;
   Bool_t          HLT_CaloMET90_NotCleaned;
   Bool_t          HLT_CaloMET350_NotCleaned;
   Bool_t          HLT_PFMET200_NotCleaned;
   Bool_t          HLT_PFMET250_NotCleaned;
   Bool_t          HLT_PFMET300_NotCleaned;
   Bool_t          HLT_PFMET200_BeamHaloCleaned;
   Bool_t          HLT_PFMETTypeOne200_BeamHaloCleaned;
   Bool_t          HLT_MET105_IsoTrk50;
   Bool_t          HLT_MET120_IsoTrk50;
   Bool_t          HLT_Mu12eta2p3;
   Bool_t          HLT_Mu12eta2p3_PFJet40;
   Bool_t          HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71;
   Bool_t          HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71;
   Bool_t          HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71;
   Bool_t          HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71;
   Bool_t          HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71;
   Bool_t          HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets40_PFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets100_PFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets200_PFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets350_PFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71;
   Bool_t          HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71;
   Bool_t          HLT_Photon300_NoHE;
   Bool_t          HLT_Mu8_TrkIsoVVL;
   Bool_t          HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ;
   Bool_t          HLT_Mu8_DiEle12_CaloIdL_TrackIdL;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ;
   Bool_t          HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu17_TrkIsoVVL;
   Bool_t          HLT_Mu19_TrkIsoVVL;
   Bool_t          HLT_BTagMu_AK4DiJet20_Mu5;
   Bool_t          HLT_BTagMu_AK4DiJet40_Mu5;
   Bool_t          HLT_BTagMu_AK4DiJet70_Mu5;
   Bool_t          HLT_BTagMu_AK4DiJet110_Mu5;
   Bool_t          HLT_BTagMu_AK4DiJet170_Mu5;
   Bool_t          HLT_BTagMu_AK4Jet300_Mu5;
   Bool_t          HLT_BTagMu_AK8DiJet170_Mu5;
   Bool_t          HLT_BTagMu_AK8Jet170_DoubleMu5;
   Bool_t          HLT_BTagMu_AK8Jet300_Mu5;
   Bool_t          HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;
   Bool_t          HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;
   Bool_t          HLT_Photon33;
   Bool_t          HLT_Photon50;
   Bool_t          HLT_Photon75;
   Bool_t          HLT_Photon90;
   Bool_t          HLT_Photon120;
   Bool_t          HLT_Photon150;
   Bool_t          HLT_Photon175;
   Bool_t          HLT_Photon200;
   Bool_t          HLT_Photon30EB_TightID_TightIso;
   Bool_t          HLT_Photon50EB_TightID_TightIso;
   Bool_t          HLT_Photon75EB_TightID_TightIso;
   Bool_t          HLT_Photon90EB_TightID_TightIso;
   Bool_t          HLT_Photon110EB_TightID_TightIso;
   Bool_t          HLT_Photon130EB_TightID_TightIso;
   Bool_t          HLT_Photon150EB_TightID_TightIso;
   Bool_t          HLT_Photon175EB_TightID_TightIso;
   Bool_t          HLT_Photon200EB_TightID_TightIso;
   Bool_t          HLT_Photon100EBHE10;
   Bool_t          HLT_Photon50_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon75_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon90_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon120_R9Id90_HE10_IsoM;
   Bool_t          HLT_Photon165_R9Id90_HE10_IsoM;
   Bool_t          HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90;
   Bool_t          HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95;
   Bool_t          HLT_Photon35_TwoProngs35;
   Bool_t          HLT_IsoMu24_TwoProngs35;
   Bool_t          HLT_Dimuon0_Jpsi_L1_NoOS;
   Bool_t          HLT_Dimuon0_Jpsi_NoVertexing_NoOS;
   Bool_t          HLT_Dimuon0_Jpsi;
   Bool_t          HLT_Dimuon0_Jpsi_NoVertexing;
   Bool_t          HLT_Dimuon0_Jpsi_L1_4R_0er1p5R;
   Bool_t          HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R;
   Bool_t          HLT_Dimuon0_Jpsi3p5_Muon2;
   Bool_t          HLT_Dimuon0_Upsilon_L1_4p5;
   Bool_t          HLT_Dimuon0_Upsilon_L1_4p5er2p0;
   Bool_t          HLT_Dimuon0_Upsilon_L1_4p5er2p0M;
   Bool_t          HLT_Dimuon0_Upsilon_NoVertexing;
   Bool_t          HLT_Dimuon0_LowMass_L1_0er1p5R;
   Bool_t          HLT_Dimuon0_LowMass_L1_0er1p5;
   Bool_t          HLT_Dimuon0_LowMass;
   Bool_t          HLT_Dimuon0_LowMass_L1_4;
   Bool_t          HLT_Dimuon0_LowMass_L1_4R;
   Bool_t          HLT_Dimuon0_LowMass_L1_TM530;
   Bool_t          HLT_Dimuon0_Upsilon_Muon_NoL1Mass;
   Bool_t          HLT_TripleMu_5_3_3_Mass3p8_DZ;
   Bool_t          HLT_TripleMu_10_5_5_DZ;
   Bool_t          HLT_TripleMu_12_10_5;
   Bool_t          HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15;
   Bool_t          HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1;
   Bool_t          HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15;
   Bool_t          HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1;
   Bool_t          HLT_DoubleMu3_DZ_PFMET50_PFMHT60;
   Bool_t          HLT_DoubleMu3_DZ_PFMET70_PFMHT70;
   Bool_t          HLT_DoubleMu3_DZ_PFMET90_PFMHT90;
   Bool_t          HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass;
   Bool_t          HLT_DoubleMu4_Jpsi_Displaced;
   Bool_t          HLT_DoubleMu4_Jpsi_NoVertexing;
   Bool_t          HLT_DoubleMu4_JpsiTrkTrk_Displaced;
   Bool_t          HLT_DoubleMu4_JpsiTrk_Bc;
   Bool_t          HLT_DoubleMu43NoFiltersNoVtx;
   Bool_t          HLT_DoubleMu48NoFiltersNoVtx;
   Bool_t          HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL;
   Bool_t          HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL;
   Bool_t          HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL;
   Bool_t          HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL;
   Bool_t          HLT_DiJet110_35_Mjj650_PFMET110;
   Bool_t          HLT_DiJet110_35_Mjj650_PFMET120;
   Bool_t          HLT_DiJet110_35_Mjj650_PFMET130;
   Bool_t          HLT_TripleJet110_35_35_Mjj650_PFMET110;
   Bool_t          HLT_TripleJet110_35_35_Mjj650_PFMET120;
   Bool_t          HLT_TripleJet110_35_35_Mjj650_PFMET130;
   Bool_t          HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned;
   Bool_t          HLT_Ele28_eta2p1_WPTight_Gsf_HT150;
   Bool_t          HLT_Ele28_HighEta_SC20_Mass55;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT450_PFMET50;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT450;
   Bool_t          HLT_Ele50_IsoVVVL_PFHT450;
   Bool_t          HLT_Ele15_IsoVVVL_PFHT600;
   Bool_t          HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;
   Bool_t          HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;
   Bool_t          HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT450_PFMET50;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT450;
   Bool_t          HLT_Mu50_IsoVVVL_PFHT450;
   Bool_t          HLT_Mu15_IsoVVVL_PFHT600;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight;
   Bool_t          HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight;
   Bool_t          HLT_Dimuon10_Upsilon_y1p4;
   Bool_t          HLT_Dimuon12_Upsilon_y1p4;
   Bool_t          HLT_Dimuon14_Phi_Barrel_Seagulls;
   Bool_t          HLT_Dimuon25_Jpsi;
   Bool_t          HLT_Dimuon14_PsiPrime;
   Bool_t          HLT_Dimuon14_PsiPrime_noCorrL1;
   Bool_t          HLT_Dimuon18_PsiPrime;
   Bool_t          HLT_Dimuon18_PsiPrime_noCorrL1;
   Bool_t          HLT_Dimuon24_Upsilon_noCorrL1;
   Bool_t          HLT_Dimuon24_Phi_noCorrL1;
   Bool_t          HLT_Dimuon25_Jpsi_noCorrL1;
   Bool_t          HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8;
   Bool_t          HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ;
   Bool_t          HLT_DiMu9_Ele9_CaloIdL_TrackIdL;
   Bool_t          HLT_DoubleIsoMu20_eta2p1;
   Bool_t          HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx;
   Bool_t          HLT_Mu8;
   Bool_t          HLT_Mu17;
   Bool_t          HLT_Mu19;
   Bool_t          HLT_Mu17_Photon30_IsoCaloId;
   Bool_t          HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;
   Bool_t          HLT_Ele8_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele17_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele23_CaloIdM_TrackIdM_PFJet30;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165;
   Bool_t          HLT_Ele115_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_Ele135_CaloIdVT_GsfTrkIdT;
   Bool_t          HLT_PFHT330PT30_QuadPFJet_75_60_45_40;
   Bool_t          HLT_PFHT400_SixPFJet32;
   Bool_t          HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50;
   Bool_t          HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94;
   Bool_t          HLT_PFHT450_SixPFJet36;
   Bool_t          HLT_PFHT450_SixPFJet36_PNetBTag0p35;
   Bool_t          HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59;
   Bool_t          HLT_PFHT400_FivePFJet_100_100_60_30_30;
   Bool_t          HLT_PFHT350;
   Bool_t          HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350;
   Bool_t          HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380;
   Bool_t          HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400;
   Bool_t          HLT_ECALHT800;
   Bool_t          HLT_DiSC30_18_EIso_AND_HE_Mass70;
   Bool_t          HLT_Photon20_HoverELoose;
   Bool_t          HLT_Photon30_HoverELoose;
   Bool_t          HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142;
   Bool_t          HLT_CDC_L2cosmic_10_er1p0;
   Bool_t          HLT_CDC_L2cosmic_5p5_er1p0;
   Bool_t          HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL;
   Bool_t          HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1;
   Bool_t          HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3;
   Bool_t          HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3;
   Bool_t          HLT_Mu18_Mu9_SameSign;
   Bool_t          HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05;
   Bool_t          HLT_DoubleMu3_DCA_PFMET50_PFMHT60;
   Bool_t          HLT_TripleMu_5_3_3_Mass3p8_DCA;
   Bool_t          HLT_QuadPFJet103_88_75_15;
   Bool_t          HLT_QuadPFJet105_88_76_15;
   Bool_t          HLT_QuadPFJet111_90_80_15;
   Bool_t          HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId;
   Bool_t          HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55;
   Bool_t          HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1;
   Bool_t          HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1;
   Bool_t          HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1;
   Bool_t          HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1;
   Bool_t          HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1;
   Bool_t          HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1;
   Bool_t          HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5;
   Bool_t          HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5;
   Bool_t          HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5;
   Bool_t          HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;
   Bool_t          HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2;
   Bool_t          HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;
   Bool_t          HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2;
   Bool_t          HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;
   Bool_t          HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5;
   Bool_t          HLT_PFHT280_QuadPFJet30;
   Bool_t          HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55;
   Bool_t          HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60;
   Bool_t          HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60;
   Bool_t          HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50;
   Bool_t          HLT_QuadPFJet100_88_70_30;
   Bool_t          HLT_QuadPFJet105_88_75_30;
   Bool_t          HLT_QuadPFJet111_90_80_30;
   Bool_t          HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight;
   Bool_t          HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight;
   Bool_t          HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight;
   Bool_t          HLT_AK8PFJet220_SoftDropMass40;
   Bool_t          HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50;
   Bool_t          HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53;
   Bool_t          HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55;
   Bool_t          HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60;
   Bool_t          HLT_AK8PFJet230_SoftDropMass40;
   Bool_t          HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10;
   Bool_t          HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03;
   Bool_t          HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05;
   Bool_t          HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10;
   Bool_t          HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03;
   Bool_t          HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05;
   Bool_t          HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10;
   Bool_t          HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03;
   Bool_t          HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05;
   Bool_t          HLT_AK8PFJet425_SoftDropMass40;
   Bool_t          HLT_AK8PFJet450_SoftDropMass40;
   Bool_t          HLT_IsoMu50_AK8PFJet220_SoftDropMass40;
   Bool_t          HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_IsoMu50_AK8PFJet230_SoftDropMass40;
   Bool_t          HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06;
   Bool_t          HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30;
   Bool_t          HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50;
   Bool_t          HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60;
   Bool_t          HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1;
   Bool_t          HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1;
   Bool_t          HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1;
   Bool_t          HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm;
   Bool_t          HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm;
   Bool_t          HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm;
   Bool_t          HLT_L2Mu10NoVtx_2Cha;
   Bool_t          HLT_L2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_L3Mu10NoVtx;
   Bool_t          HLT_L3Mu10NoVtx_DxyMin0p01cm;
   Bool_t          HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm;
   Bool_t          HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm;
   Bool_t          HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_L2Mu10NoVtx_2Cha_CosmicSeed;
   Bool_t          HLT_L2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;
   Bool_t          HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm;
   Bool_t          HLT_L3dTksMu10_NoVtx_DxyMin0p01cm;
   Bool_t          HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId;
   Bool_t          HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay3nsInclusive;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive;
   Bool_t          HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay2nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless;
   Bool_t          HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless;
   Bool_t          HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless;
   Bool_t          HLT_L1Mu6HT240;
   Bool_t          HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose;
   Bool_t          HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5;
   Bool_t          HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose;
   Bool_t          HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5;
   Bool_t          HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose;
   Bool_t          HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5;
   Bool_t          HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5;
   Bool_t          HLT_HT350;
   Bool_t          HLT_HT425;
   Bool_t          HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT400_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT430_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT550_DisplacedDijet60_Inclusive;
   Bool_t          HLT_HT650_DisplacedDijet60_Inclusive;
   Bool_t          HLT_CaloMET60_DTCluster50;
   Bool_t          HLT_CaloMET60_DTClusterNoMB1S50;
   Bool_t          HLT_L1MET_DTCluster50;
   Bool_t          HLT_L1MET_DTClusterNoMB1S50;
   Bool_t          HLT_CscCluster_Loose;
   Bool_t          HLT_CscCluster_Medium;
   Bool_t          HLT_CscCluster_Tight;
   Bool_t          HLT_DoubleCscCluster75;
   Bool_t          HLT_DoubleCscCluster100;
   Bool_t          HLT_L1CSCShower_DTCluster50;
   Bool_t          HLT_L1CSCShower_DTCluster75;
   Bool_t          HLT_PFMET105_IsoTrk50;
   Bool_t          HLT_L1SingleLLPJet;
   Bool_t          HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack;
   Bool_t          HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;
   Bool_t          HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;
   Bool_t          HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive;
   Bool_t          HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive;
   Bool_t          HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless;
   Bool_t          HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive;
   Bool_t          HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless;
   Bool_t          HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive;
   Bool_t          HLT_DiPhoton10Time1ns;
   Bool_t          HLT_DiPhoton10Time1p2ns;
   Bool_t          HLT_DiPhoton10Time1p4ns;
   Bool_t          HLT_DiPhoton10Time1p6ns;
   Bool_t          HLT_DiPhoton10Time1p8ns;
   Bool_t          HLT_DiPhoton10Time2ns;
   Bool_t          HLT_DiPhoton10sminlt0p1;
   Bool_t          HLT_DiPhoton10sminlt0p12;
   Bool_t          HLT_DiPhoton10_CaloIdL;
   Bool_t          HLT_DoubleEle4_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle4p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle5p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle6_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle6p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle7_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle7p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle8_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle8p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle9_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle9p5_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle10_eta1p22_mMax6;
   Bool_t          HLT_DoubleEle4_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle6_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle7_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle8_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle9_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle10_eta1p22_mMax6_dz0p8;
   Bool_t          HLT_DoubleEle4_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle6_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle7_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle8_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle9_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_DoubleEle10_eta1p22_mMax6_trkHits10;
   Bool_t          HLT_SingleEle8;
   Bool_t          HLT_SingleEle8_SingleEGL1;
   Bool_t          HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT;
   Bool_t          HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;
   Bool_t          HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT;
   Bool_t          HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;
   Bool_t          HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;
   Bool_t          HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;
   Bool_t          HLT_Mu50_L1SingleMuShower;
   Bool_t          HLT_IsoMu24_OneProng32;
   Bool_t          HLT_Photon32_OneProng32_M50To105;
   Bool_t          HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80;
   Bool_t          HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5;
   Bool_t          HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5;
   Bool_t          HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5;
   Bool_t          HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0;
   Bool_t          HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet;
   Bool_t          HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet;
   Bool_t          HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet;
   Bool_t          HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet;
   Bool_t          HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet;
   Bool_t          HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet;
   Bool_t          HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85;
   Bool_t          HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85;
   Bool_t          HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL;
   Bool_t          HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL;
   Bool_t          HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet;
   Bool_t          HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1;
   Bool_t          HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12;
   Bool_t          HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17;
   Bool_t          HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22;
   Bool_t          HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf;
   Bool_t          HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf;
   Bool_t          HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf;
   Bool_t          HLT_PFJet200_TimeLtNeg2p5ns;
   Bool_t          HLT_PFJet200_TimeGt2p5ns;
   Bool_t          HLT_Photon50_TimeLtNeg2p5ns;
   Bool_t          HLT_Photon50_TimeGt2p5ns;
   Bool_t          HLT_ExpressMuons;
   Bool_t          HLT_PPSMaxTracksPerArm1;
   Bool_t          HLT_PPSMaxTracksPerRP4;
   Bool_t          HLT_PPSRandom;
   Bool_t          HLTriggerFinalPath;

   // List of branches
   TBranch        *b_run;   //!
   TBranch        *b_luminosityBlock;   //!
   TBranch        *b_event;   //!
   TBranch        *b_bunchCrossing;   //!
   TBranch        *b_nJet;   //!
   TBranch        *b_Jet_jetId;   //!
   TBranch        *b_Jet_nConstituents;   //!
   TBranch        *b_Jet_nElectrons;   //!
   TBranch        *b_Jet_nMuons;   //!
   TBranch        *b_Jet_nSVs;   //!
   TBranch        *b_Jet_electronIdx1;   //!
   TBranch        *b_Jet_electronIdx2;   //!
   TBranch        *b_Jet_muonIdx1;   //!
   TBranch        *b_Jet_muonIdx2;   //!
   TBranch        *b_Jet_svIdx1;   //!
   TBranch        *b_Jet_svIdx2;   //!
   TBranch        *b_Jet_hfadjacentEtaStripsSize;   //!
   TBranch        *b_Jet_hfcentralEtaStripSize;   //!
   TBranch        *b_Jet_PNetRegPtRawCorr;   //!
   TBranch        *b_Jet_PNetRegPtRawCorrNeutrino;   //!
   TBranch        *b_Jet_PNetRegPtRawRes;   //!
   TBranch        *b_Jet_area;   //!
   TBranch        *b_Jet_btagDeepFlavB;   //!
   TBranch        *b_Jet_btagDeepFlavCvB;   //!
   TBranch        *b_Jet_btagDeepFlavCvL;   //!
   TBranch        *b_Jet_btagDeepFlavQG;   //!
   TBranch        *b_Jet_btagPNetB;   //!
   TBranch        *b_Jet_btagPNetCvB;   //!
   TBranch        *b_Jet_btagPNetCvL;   //!
   TBranch        *b_Jet_btagPNetQvG;   //!
   TBranch        *b_Jet_btagPNetTauVJet;   //!
   TBranch        *b_Jet_btagRobustParTAK4B;   //!
   TBranch        *b_Jet_btagRobustParTAK4CvB;   //!
   TBranch        *b_Jet_btagRobustParTAK4CvL;   //!
   TBranch        *b_Jet_btagRobustParTAK4QG;   //!
   TBranch        *b_Jet_chEmEF;   //!
   TBranch        *b_Jet_chHEF;   //!
   TBranch        *b_Jet_eta;   //!
   TBranch        *b_Jet_hfsigmaEtaEta;   //!
   TBranch        *b_Jet_hfsigmaPhiPhi;   //!
   TBranch        *b_Jet_mass;   //!
   TBranch        *b_Jet_muEF;   //!
   TBranch        *b_Jet_muonSubtrFactor;   //!
   TBranch        *b_Jet_neEmEF;   //!
   TBranch        *b_Jet_neHEF;   //!
   TBranch        *b_Jet_phi;   //!
   TBranch        *b_Jet_pt;   //!
   TBranch        *b_Jet_rawFactor;   //!
   TBranch        *b_nTau;   //!
   TBranch        *b_Tau_decayMode;   //!
   TBranch        *b_Tau_idAntiEleDeadECal;   //!
   TBranch        *b_Tau_idAntiMu;   //!
   TBranch        *b_Tau_idDecayModeNewDMs;   //!
   TBranch        *b_Tau_idDecayModeOldDMs;   //!
   TBranch        *b_Tau_idDeepTau2017v2p1VSe;   //!
   TBranch        *b_Tau_idDeepTau2017v2p1VSjet;   //!
   TBranch        *b_Tau_idDeepTau2017v2p1VSmu;   //!
   TBranch        *b_Tau_idDeepTau2018v2p5VSe;   //!
   TBranch        *b_Tau_idDeepTau2018v2p5VSjet;   //!
   TBranch        *b_Tau_idDeepTau2018v2p5VSmu;   //!
   TBranch        *b_Tau_nSVs;   //!
   TBranch        *b_Tau_charge;   //!
   TBranch        *b_Tau_decayModePNet;   //!
   TBranch        *b_Tau_eleIdx;   //!
   TBranch        *b_Tau_jetIdx;   //!
   TBranch        *b_Tau_muIdx;   //!
   TBranch        *b_Tau_svIdx1;   //!
   TBranch        *b_Tau_svIdx2;   //!
   TBranch        *b_Tau_chargedIso;   //!
   TBranch        *b_Tau_dxy;   //!
   TBranch        *b_Tau_dz;   //!
   TBranch        *b_Tau_eta;   //!
   TBranch        *b_Tau_leadTkDeltaEta;   //!
   TBranch        *b_Tau_leadTkDeltaPhi;   //!
   TBranch        *b_Tau_leadTkPtOverTauPt;   //!
   TBranch        *b_Tau_mass;   //!
   TBranch        *b_Tau_neutralIso;   //!
   TBranch        *b_Tau_phi;   //!
   TBranch        *b_Tau_photonsOutsideSignalCone;   //!
   TBranch        *b_Tau_probDM0PNet;   //!
   TBranch        *b_Tau_probDM10PNet;   //!
   TBranch        *b_Tau_probDM11PNet;   //!
   TBranch        *b_Tau_probDM1PNet;   //!
   TBranch        *b_Tau_probDM2PNet;   //!
   TBranch        *b_Tau_pt;   //!
   TBranch        *b_Tau_ptCorrPNet;   //!
   TBranch        *b_Tau_puCorr;   //!
   TBranch        *b_Tau_qConfPNet;   //!
   TBranch        *b_Tau_rawDeepTau2017v2p1VSe;   //!
   TBranch        *b_Tau_rawDeepTau2017v2p1VSjet;   //!
   TBranch        *b_Tau_rawDeepTau2017v2p1VSmu;   //!
   TBranch        *b_Tau_rawDeepTau2018v2p5VSe;   //!
   TBranch        *b_Tau_rawDeepTau2018v2p5VSjet;   //!
   TBranch        *b_Tau_rawDeepTau2018v2p5VSmu;   //!
   TBranch        *b_Tau_rawIso;   //!
   TBranch        *b_Tau_rawIsodR03;   //!
   TBranch        *b_Tau_rawPNetVSe;   //!
   TBranch        *b_Tau_rawPNetVSjet;   //!
   TBranch        *b_Tau_rawPNetVSmu;   //!
   TBranch        *b_TkMET_phi;   //!
   TBranch        *b_TkMET_pt;   //!
   TBranch        *b_TkMET_sumEt;   //!
   TBranch        *b_nTrigObj;   //!
   TBranch        *b_TrigObj_l1charge;   //!
   TBranch        *b_TrigObj_id;   //!
   TBranch        *b_TrigObj_l1iso;   //!
   TBranch        *b_TrigObj_filterBits;   //!
   TBranch        *b_TrigObj_pt;   //!
   TBranch        *b_TrigObj_eta;   //!
   TBranch        *b_TrigObj_phi;   //!
   TBranch        *b_TrigObj_l1pt;   //!
   TBranch        *b_TrigObj_l1pt_2;   //!
   TBranch        *b_TrigObj_l2pt;   //!
   TBranch        *b_genTtbarId;   //!
   TBranch        *b_nOtherPV;   //!
   TBranch        *b_OtherPV_z;   //!
   TBranch        *b_OtherPV_score;   //!
   TBranch        *b_PV_npvs;   //!
   TBranch        *b_PV_npvsGood;   //!
   TBranch        *b_PV_ndof;   //!
   TBranch        *b_PV_x;   //!
   TBranch        *b_PV_y;   //!
   TBranch        *b_PV_z;   //!
   TBranch        *b_PV_chi2;   //!
   TBranch        *b_PV_score;   //!
   TBranch        *b_nSV;   //!
   TBranch        *b_SV_charge;   //!
   TBranch        *b_SV_dlen;   //!
   TBranch        *b_SV_dlenSig;   //!
   TBranch        *b_SV_dxy;   //!
   TBranch        *b_SV_dxySig;   //!
   TBranch        *b_SV_pAngle;   //!
   TBranch        *b_boostedTau_genPartFlav;   //!
   TBranch        *b_boostedTau_genPartIdx;   //!
   TBranch        *b_Electron_genPartFlav;   //!
   TBranch        *b_Electron_genPartIdx;   //!
   TBranch        *b_FatJet_hadronFlavour;   //!
   TBranch        *b_FatJet_nBHadrons;   //!
   TBranch        *b_FatJet_nCHadrons;   //!
   TBranch        *b_FatJet_genJetAK8Idx;   //!
   TBranch        *b_GenJetAK8_hadronFlavour;   //!
   TBranch        *b_GenJetAK8_partonFlavour;   //!
   TBranch        *b_GenJet_hadronFlavour;   //!
   TBranch        *b_GenJet_partonFlavour;   //!
   TBranch        *b_GenVtx_t0;   //!
   TBranch        *b_Jet_hadronFlavour;   //!
   TBranch        *b_Jet_genJetIdx;   //!
   TBranch        *b_Jet_partonFlavour;   //!
   TBranch        *b_LowPtElectron_genPartFlav;   //!
   TBranch        *b_LowPtElectron_genPartIdx;   //!
   TBranch        *b_Muon_genPartFlav;   //!
   TBranch        *b_Muon_genPartIdx;   //!
   TBranch        *b_Photon_genPartFlav;   //!
   TBranch        *b_Photon_genPartIdx;   //!
   TBranch        *b_MET_fiducialGenPhi;   //!
   TBranch        *b_MET_fiducialGenPt;   //!
   TBranch        *b_SubJet_hadronFlavour;   //!
   TBranch        *b_SubJet_nBHadrons;   //!
   TBranch        *b_SubJet_nCHadrons;   //!
   TBranch        *b_SV_ntracks;   //!
   TBranch        *b_SV_chi2;   //!
   TBranch        *b_SV_eta;   //!
   TBranch        *b_SV_mass;   //!
   TBranch        *b_SV_ndof;   //!
   TBranch        *b_SV_phi;   //!
   TBranch        *b_SV_pt;   //!
   TBranch        *b_SV_x;   //!
   TBranch        *b_SV_y;   //!
   TBranch        *b_SV_z;   //!
   TBranch        *b_Tau_genPartFlav;   //!
   TBranch        *b_Tau_genPartIdx;   //!
   TBranch        *b_L1_AlwaysTrue;   //!
   TBranch        *b_L1_BPTX_AND_Ref1_VME;   //!
   TBranch        *b_L1_BPTX_AND_Ref3_VME;   //!
   TBranch        *b_L1_BPTX_AND_Ref4_VME;   //!
   TBranch        *b_L1_BPTX_BeamGas_B1_VME;   //!
   TBranch        *b_L1_BPTX_BeamGas_B2_VME;   //!
   TBranch        *b_L1_BPTX_BeamGas_Ref1_VME;   //!
   TBranch        *b_L1_BPTX_BeamGas_Ref2_VME;   //!
   TBranch        *b_L1_BPTX_NotOR_VME;   //!
   TBranch        *b_L1_BPTX_OR_Ref3_VME;   //!
   TBranch        *b_L1_BPTX_OR_Ref4_VME;   //!
   TBranch        *b_L1_BPTX_RefAND_VME;   //!
   TBranch        *b_L1_BptxMinus;   //!
   TBranch        *b_L1_BptxOR;   //!
   TBranch        *b_L1_BptxPlus;   //!
   TBranch        *b_L1_BptxXOR;   //!
   TBranch        *b_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142;   //!
   TBranch        *b_L1_DoubleEG10_er1p2_dR_Max0p6;   //!
   TBranch        *b_L1_DoubleEG10p5_er1p2_dR_Max0p6;   //!
   TBranch        *b_L1_DoubleEG11_er1p2_dR_Max0p6;   //!
   TBranch        *b_L1_DoubleEG4_er1p2_dR_Max0p9;   //!
   TBranch        *b_L1_DoubleEG4p5_er1p2_dR_Max0p9;   //!
   TBranch        *b_L1_DoubleEG5_er1p2_dR_Max0p9;   //!
   TBranch        *b_L1_DoubleEG5p5_er1p2_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleEG6_er1p2_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleEG6p5_er1p2_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleEG7_er1p2_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleEG7p5_er1p2_dR_Max0p7;   //!
   TBranch        *b_L1_DoubleEG8_er1p2_dR_Max0p7;   //!
   TBranch        *b_L1_DoubleEG8er2p5_HTT260er;   //!
   TBranch        *b_L1_DoubleEG8er2p5_HTT280er;   //!
   TBranch        *b_L1_DoubleEG8er2p5_HTT300er;   //!
   TBranch        *b_L1_DoubleEG8er2p5_HTT320er;   //!
   TBranch        *b_L1_DoubleEG8er2p5_HTT340er;   //!
   TBranch        *b_L1_DoubleEG8p5_er1p2_dR_Max0p7;   //!
   TBranch        *b_L1_DoubleEG9_er1p2_dR_Max0p7;   //!
   TBranch        *b_L1_DoubleEG9p5_er1p2_dR_Max0p6;   //!
   TBranch        *b_L1_DoubleEG_15_10_er2p5;   //!
   TBranch        *b_L1_DoubleEG_20_10_er2p5;   //!
   TBranch        *b_L1_DoubleEG_22_10_er2p5;   //!
   TBranch        *b_L1_DoubleEG_25_12_er2p5;   //!
   TBranch        *b_L1_DoubleEG_25_14_er2p5;   //!
   TBranch        *b_L1_DoubleEG_27_14_er2p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso16_LooseIso12_er1p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso18_LooseIso12_er1p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso20_LooseIso12_er1p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso22_12_er2p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso22_LooseIso12_er1p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso25_12_er2p5;   //!
   TBranch        *b_L1_DoubleEG_LooseIso25_LooseIso12_er1p5;   //!
   TBranch        *b_L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5;   //!
   TBranch        *b_L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5;   //!
   TBranch        *b_L1_DoubleIsoTau28er2p1;   //!
   TBranch        *b_L1_DoubleIsoTau28er2p1_Mass_Max80;   //!
   TBranch        *b_L1_DoubleIsoTau28er2p1_Mass_Max90;   //!
   TBranch        *b_L1_DoubleIsoTau30er2p1;   //!
   TBranch        *b_L1_DoubleIsoTau30er2p1_Mass_Max80;   //!
   TBranch        *b_L1_DoubleIsoTau30er2p1_Mass_Max90;   //!
   TBranch        *b_L1_DoubleIsoTau32er2p1;   //!
   TBranch        *b_L1_DoubleIsoTau32er2p1_Mass_Max80;   //!
   TBranch        *b_L1_DoubleIsoTau34er2p1;   //!
   TBranch        *b_L1_DoubleIsoTau35er2p1;   //!
   TBranch        *b_L1_DoubleIsoTau36er2p1;   //!
   TBranch        *b_L1_DoubleJet100er2p3_dEta_Max1p6;   //!
   TBranch        *b_L1_DoubleJet100er2p5;   //!
   TBranch        *b_L1_DoubleJet112er2p3_dEta_Max1p6;   //!
   TBranch        *b_L1_DoubleJet120er2p5;   //!
   TBranch        *b_L1_DoubleJet120er2p5_Mu3_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleJet150er2p5;   //!
   TBranch        *b_L1_DoubleJet16er2p5_Mu3_dR_Max0p4;   //!
   TBranch        *b_L1_DoubleJet30er2p5_Mass_Min225_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleJet30er2p5_Mass_Min250_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleJet35_Mass_Min450_IsoTau45_RmOvlp;   //!
   TBranch        *b_L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5;   //!
   TBranch        *b_L1_DoubleJet35er2p5_Mu3_dR_Max0p4;   //!
   TBranch        *b_L1_DoubleJet40_Mass_Min450_IsoEG10er2p1_RmOvlp_dR0p2;   //!
   TBranch        *b_L1_DoubleJet40_Mass_Min450_LooseIsoEG15er2p1_RmOvlp_dR0p2;   //!
   TBranch        *b_L1_DoubleJet40er2p5;   //!
   TBranch        *b_L1_DoubleJet45_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5;   //!
   TBranch        *b_L1_DoubleJet45_Mass_Min450_LooseIsoEG20er2p1_RmOvlp_dR0p2;   //!
   TBranch        *b_L1_DoubleJet60er2p5_Mu3_dR_Max0p4;   //!
   TBranch        *b_L1_DoubleJet80er2p5_Mu3_dR_Max0p4;   //!
   TBranch        *b_L1_DoubleJet_100_30_DoubleJet30_Mass_Min620;   //!
   TBranch        *b_L1_DoubleJet_100_30_DoubleJet30_Mass_Min800;   //!
   TBranch        *b_L1_DoubleJet_110_35_DoubleJet35_Mass_Min620;   //!
   TBranch        *b_L1_DoubleJet_110_35_DoubleJet35_Mass_Min800;   //!
   TBranch        *b_L1_DoubleJet_115_40_DoubleJet40_Mass_Min620;   //!
   TBranch        *b_L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28;   //!
   TBranch        *b_L1_DoubleJet_120_45_DoubleJet45_Mass_Min620;   //!
   TBranch        *b_L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28;   //!
   TBranch        *b_L1_DoubleJet_60_30_DoubleJet30_Mass_Min500_DoubleJetCentral50;   //!
   TBranch        *b_L1_DoubleJet_65_30_DoubleJet30_Mass_Min400_ETMHF65;   //!
   TBranch        *b_L1_DoubleJet_65_35_DoubleJet35_Mass_Min500_DoubleJetCentral50;   //!
   TBranch        *b_L1_DoubleJet_70_35_DoubleJet35_Mass_Min400_ETMHF65;   //!
   TBranch        *b_L1_DoubleJet_80_30_DoubleJet30_Mass_Min500_Mu3OQ;   //!
   TBranch        *b_L1_DoubleJet_80_30_Mass_Min420_DoubleMu0_SQ;   //!
   TBranch        *b_L1_DoubleJet_80_30_Mass_Min420_IsoTau40_RmOvlp;   //!
   TBranch        *b_L1_DoubleJet_80_30_Mass_Min420_Mu8;   //!
   TBranch        *b_L1_DoubleJet_85_35_DoubleJet35_Mass_Min500_Mu3OQ;   //!
   TBranch        *b_L1_DoubleJet_90_30_DoubleJet30_Mass_Min620;   //!
   TBranch        *b_L1_DoubleJet_90_30_DoubleJet30_Mass_Min800;   //!
   TBranch        *b_L1_DoubleLLPJet40;   //!
   TBranch        *b_L1_DoubleLooseIsoEG22er2p1;   //!
   TBranch        *b_L1_DoubleLooseIsoEG24er2p1;   //!
   TBranch        *b_L1_DoubleMu0;   //!
   TBranch        *b_L1_DoubleMu0_Mass_Min1;   //!
   TBranch        *b_L1_DoubleMu0_OQ;   //!
   TBranch        *b_L1_DoubleMu0_SQ;   //!
   TBranch        *b_L1_DoubleMu0_SQ_OS;   //!
   TBranch        *b_L1_DoubleMu0_Upt15_Upt7;   //!
   TBranch        *b_L1_DoubleMu0_Upt15_Upt7_BMTF_EMTF;   //!
   TBranch        *b_L1_DoubleMu0_Upt5_Upt5;   //!
   TBranch        *b_L1_DoubleMu0_Upt5_Upt5_BMTF_EMTF;   //!
   TBranch        *b_L1_DoubleMu0_Upt6_IP_Min1_Upt4;   //!
   TBranch        *b_L1_DoubleMu0_Upt6_IP_Min1_Upt4_BMTF_EMTF;   //!
   TBranch        *b_L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6;   //!
   TBranch        *b_L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2;   //!
   TBranch        *b_L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4;   //!
   TBranch        *b_L1_DoubleMu0er1p5_SQ;   //!
   TBranch        *b_L1_DoubleMu0er1p5_SQ_OS;   //!
   TBranch        *b_L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2;   //!
   TBranch        *b_L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4;   //!
   TBranch        *b_L1_DoubleMu0er1p5_SQ_dR_Max1p4;   //!
   TBranch        *b_L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6;   //!
   TBranch        *b_L1_DoubleMu0er2p0_SQ_dEta_Max1p5;   //!
   TBranch        *b_L1_DoubleMu0er2p0_SQ_dEta_Max1p6;   //!
   TBranch        *b_L1_DoubleMu18er2p1_SQ;   //!
   TBranch        *b_L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF30_HTT60er;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF30_Jet60er2p5_OR_DoubleJet40er2p5;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF40_HTT60er;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF50_HTT60er;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5;   //!
   TBranch        *b_L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5;   //!
   TBranch        *b_L1_DoubleMu3_SQ_HTT220er;   //!
   TBranch        *b_L1_DoubleMu3_SQ_HTT240er;   //!
   TBranch        *b_L1_DoubleMu3_SQ_HTT260er;   //!
   TBranch        *b_L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8;   //!
   TBranch        *b_L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6;   //!
   TBranch        *b_L1_DoubleMu4_SQ_EG9er2p5;   //!
   TBranch        *b_L1_DoubleMu4_SQ_OS;   //!
   TBranch        *b_L1_DoubleMu4_SQ_OS_dR_Max1p2;   //!
   TBranch        *b_L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6;   //!
   TBranch        *b_L1_DoubleMu4p5_SQ_OS;   //!
   TBranch        *b_L1_DoubleMu4p5_SQ_OS_dR_Max1p2;   //!
   TBranch        *b_L1_DoubleMu4p5er2p0_SQ_OS;   //!
   TBranch        *b_L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18;   //!
   TBranch        *b_L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7;   //!
   TBranch        *b_L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20;   //!
   TBranch        *b_L1_DoubleMu5_SQ_EG9er2p5;   //!
   TBranch        *b_L1_DoubleMu5_SQ_OS_dR_Max1p6;   //!
   TBranch        *b_L1_DoubleMu8_SQ;   //!
   TBranch        *b_L1_DoubleMu9_SQ;   //!
   TBranch        *b_L1_DoubleMu_12_5;   //!
   TBranch        *b_L1_DoubleMu_15_5_SQ;   //!
   TBranch        *b_L1_DoubleMu_15_7;   //!
   TBranch        *b_L1_DoubleMu_15_7_Mass_Min1;   //!
   TBranch        *b_L1_DoubleMu_15_7_SQ;   //!
   TBranch        *b_L1_DoubleTau70er2p1;   //!
   TBranch        *b_L1_ETM120;   //!
   TBranch        *b_L1_ETM150;   //!
   TBranch        *b_L1_ETMHF100;   //!
   TBranch        *b_L1_ETMHF100_HTT60er;   //!
   TBranch        *b_L1_ETMHF110;   //!
   TBranch        *b_L1_ETMHF110_HTT60er;   //!
   TBranch        *b_L1_ETMHF120;   //!
   TBranch        *b_L1_ETMHF120_HTT60er;   //!
   TBranch        *b_L1_ETMHF130;   //!
   TBranch        *b_L1_ETMHF130_HTT60er;   //!
   TBranch        *b_L1_ETMHF140;   //!
   TBranch        *b_L1_ETMHF150;   //!
   TBranch        *b_L1_ETMHF70;   //!
   TBranch        *b_L1_ETMHF70_HTT60er;   //!
   TBranch        *b_L1_ETMHF80;   //!
   TBranch        *b_L1_ETMHF80_HTT60er;   //!
   TBranch        *b_L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p1;   //!
   TBranch        *b_L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p6;   //!
   TBranch        *b_L1_ETMHF90;   //!
   TBranch        *b_L1_ETMHF90_HTT60er;   //!
   TBranch        *b_L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1;   //!
   TBranch        *b_L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6;   //!
   TBranch        *b_L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1;   //!
   TBranch        *b_L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6;   //!
   TBranch        *b_L1_ETT1600;   //!
   TBranch        *b_L1_ETT2000;   //!
   TBranch        *b_L1_FirstBunchAfterTrain;   //!
   TBranch        *b_L1_FirstBunchBeforeTrain;   //!
   TBranch        *b_L1_FirstBunchInTrain;   //!
   TBranch        *b_L1_FirstCollisionInOrbit;   //!
   TBranch        *b_L1_FirstCollisionInTrain;   //!
   TBranch        *b_L1_HCAL_LaserMon_Trig;   //!
   TBranch        *b_L1_HCAL_LaserMon_Veto;   //!
   TBranch        *b_L1_HTT120_SingleLLPJet40;   //!
   TBranch        *b_L1_HTT120er;   //!
   TBranch        *b_L1_HTT160_SingleLLPJet50;   //!
   TBranch        *b_L1_HTT160er;   //!
   TBranch        *b_L1_HTT200_SingleLLPJet60;   //!
   TBranch        *b_L1_HTT200er;   //!
   TBranch        *b_L1_HTT240_SingleLLPJet70;   //!
   TBranch        *b_L1_HTT255er;   //!
   TBranch        *b_L1_HTT280er;   //!
   TBranch        *b_L1_HTT280er_QuadJet_70_55_40_35_er2p5;   //!
   TBranch        *b_L1_HTT320er;   //!
   TBranch        *b_L1_HTT320er_QuadJet_70_55_40_40_er2p5;   //!
   TBranch        *b_L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3;   //!
   TBranch        *b_L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3;   //!
   TBranch        *b_L1_HTT360er;   //!
   TBranch        *b_L1_HTT400er;   //!
   TBranch        *b_L1_HTT450er;   //!
   TBranch        *b_L1_IsoEG32er2p5_Mt40;   //!
   TBranch        *b_L1_IsoTau52er2p1_QuadJet36er2p5;   //!
   TBranch        *b_L1_IsolatedBunch;   //!
   TBranch        *b_L1_LastBunchInTrain;   //!
   TBranch        *b_L1_LastCollisionInTrain;   //!
   TBranch        *b_L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3;   //!
   TBranch        *b_L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3;   //!
   TBranch        *b_L1_LooseIsoEG24er2p1_HTT100er;   //!
   TBranch        *b_L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3;   //!
   TBranch        *b_L1_LooseIsoEG26er2p1_HTT100er;   //!
   TBranch        *b_L1_LooseIsoEG26er2p1_Jet34er2p5_dR_Min0p3;   //!
   TBranch        *b_L1_LooseIsoEG28er2p1_HTT100er;   //!
   TBranch        *b_L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3;   //!
   TBranch        *b_L1_LooseIsoEG30er2p1_HTT100er;   //!
   TBranch        *b_L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3;   //!
   TBranch        *b_L1_MinimumBiasHF0;   //!
   TBranch        *b_L1_MinimumBiasHF0_AND_BptxAND;   //!
   TBranch        *b_L1_Mu10er2p3_Jet32er2p3_dR_Max0p4_DoubleJet32er2p3_dEta_Max1p6;   //!
   TBranch        *b_L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6;   //!
   TBranch        *b_L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6;   //!
   TBranch        *b_L1_Mu18er2p1_Tau24er2p1;   //!
   TBranch        *b_L1_Mu18er2p1_Tau26er2p1;   //!
   TBranch        *b_L1_Mu18er2p1_Tau26er2p1_Jet55;   //!
   TBranch        *b_L1_Mu18er2p1_Tau26er2p1_Jet70;   //!
   TBranch        *b_L1_Mu20_EG10er2p5;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau28er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau30er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau32er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau34er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau36er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_IsoTau40er2p1;   //!
   TBranch        *b_L1_Mu22er2p1_Tau70er2p1;   //!
   TBranch        *b_L1_Mu3_Jet120er2p5_dR_Max0p4;   //!
   TBranch        *b_L1_Mu3_Jet16er2p5_dR_Max0p4;   //!
   TBranch        *b_L1_Mu3_Jet30er2p5;   //!
   TBranch        *b_L1_Mu3_Jet60er2p5_dR_Max0p4;   //!
   TBranch        *b_L1_Mu3er1p5_Jet100er2p5_ETMHF30;   //!
   TBranch        *b_L1_Mu3er1p5_Jet100er2p5_ETMHF40;   //!
   TBranch        *b_L1_Mu3er1p5_Jet100er2p5_ETMHF50;   //!
   TBranch        *b_L1_Mu5_EG23er2p5;   //!
   TBranch        *b_L1_Mu5_LooseIsoEG20er2p5;   //!
   TBranch        *b_L1_Mu6_DoubleEG10er2p5;   //!
   TBranch        *b_L1_Mu6_DoubleEG12er2p5;   //!
   TBranch        *b_L1_Mu6_DoubleEG15er2p5;   //!
   TBranch        *b_L1_Mu6_DoubleEG17er2p5;   //!
   TBranch        *b_L1_Mu6_HTT240er;   //!
   TBranch        *b_L1_Mu6_HTT250er;   //!
   TBranch        *b_L1_Mu7_EG20er2p5;   //!
   TBranch        *b_L1_Mu7_EG23er2p5;   //!
   TBranch        *b_L1_Mu7_LooseIsoEG20er2p5;   //!
   TBranch        *b_L1_Mu7_LooseIsoEG23er2p5;   //!
   TBranch        *b_L1_NotBptxOR;   //!
   TBranch        *b_L1_QuadJet60er2p5;   //!
   TBranch        *b_L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0;   //!
   TBranch        *b_L1_QuadMu0;   //!
   TBranch        *b_L1_QuadMu0_OQ;   //!
   TBranch        *b_L1_QuadMu0_SQ;   //!
   TBranch        *b_L1_SecondBunchInTrain;   //!
   TBranch        *b_L1_SecondLastBunchInTrain;   //!
   TBranch        *b_L1_SingleEG10er2p5;   //!
   TBranch        *b_L1_SingleEG15er2p5;   //!
   TBranch        *b_L1_SingleEG26er2p5;   //!
   TBranch        *b_L1_SingleEG28_FWD2p5;   //!
   TBranch        *b_L1_SingleEG28er1p5;   //!
   TBranch        *b_L1_SingleEG28er2p1;   //!
   TBranch        *b_L1_SingleEG28er2p5;   //!
   TBranch        *b_L1_SingleEG34er2p5;   //!
   TBranch        *b_L1_SingleEG36er2p5;   //!
   TBranch        *b_L1_SingleEG38er2p5;   //!
   TBranch        *b_L1_SingleEG40er2p5;   //!
   TBranch        *b_L1_SingleEG42er2p5;   //!
   TBranch        *b_L1_SingleEG45er2p5;   //!
   TBranch        *b_L1_SingleEG50;   //!
   TBranch        *b_L1_SingleEG60;   //!
   TBranch        *b_L1_SingleEG8er2p5;   //!
   TBranch        *b_L1_SingleIsoEG24er2p1;   //!
   TBranch        *b_L1_SingleIsoEG26er2p1;   //!
   TBranch        *b_L1_SingleIsoEG26er2p5;   //!
   TBranch        *b_L1_SingleIsoEG28_FWD2p5;   //!
   TBranch        *b_L1_SingleIsoEG28er1p5;   //!
   TBranch        *b_L1_SingleIsoEG28er2p1;   //!
   TBranch        *b_L1_SingleIsoEG28er2p5;   //!
   TBranch        *b_L1_SingleIsoEG30er2p1;   //!
   TBranch        *b_L1_SingleIsoEG30er2p5;   //!
   TBranch        *b_L1_SingleIsoEG32er2p1;   //!
   TBranch        *b_L1_SingleIsoEG32er2p5;   //!
   TBranch        *b_L1_SingleIsoEG34er2p5;   //!
   TBranch        *b_L1_SingleIsoTau32er2p1;   //!
   TBranch        *b_L1_SingleJet10erHE;   //!
   TBranch        *b_L1_SingleJet120;   //!
   TBranch        *b_L1_SingleJet120_FWD2p5;   //!
   TBranch        *b_L1_SingleJet120_FWD3p0;   //!
   TBranch        *b_L1_SingleJet120er2p5;   //!
   TBranch        *b_L1_SingleJet12erHE;   //!
   TBranch        *b_L1_SingleJet140er2p5;   //!
   TBranch        *b_L1_SingleJet140er2p5_ETMHF90;   //!
   TBranch        *b_L1_SingleJet160er2p5;   //!
   TBranch        *b_L1_SingleJet180;   //!
   TBranch        *b_L1_SingleJet180er2p5;   //!
   TBranch        *b_L1_SingleJet200;   //!
   TBranch        *b_L1_SingleJet20er2p5_NotBptxOR;   //!
   TBranch        *b_L1_SingleJet20er2p5_NotBptxOR_3BX;   //!
   TBranch        *b_L1_SingleJet35;   //!
   TBranch        *b_L1_SingleJet35_FWD2p5;   //!
   TBranch        *b_L1_SingleJet35_FWD3p0;   //!
   TBranch        *b_L1_SingleJet35er2p5;   //!
   TBranch        *b_L1_SingleJet43er2p5_NotBptxOR_3BX;   //!
   TBranch        *b_L1_SingleJet46er2p5_NotBptxOR_3BX;   //!
   TBranch        *b_L1_SingleJet60;   //!
   TBranch        *b_L1_SingleJet60_FWD2p5;   //!
   TBranch        *b_L1_SingleJet8erHE;   //!
   TBranch        *b_L1_SingleJet90;   //!
   TBranch        *b_L1_SingleJet90_FWD2p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG26er1p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG26er2p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG28_FWD2p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG28er1p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG28er2p1;   //!
   TBranch        *b_L1_SingleLooseIsoEG28er2p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG30er1p5;   //!
   TBranch        *b_L1_SingleLooseIsoEG30er2p5;   //!
   TBranch        *b_L1_SingleMu0_BMTF;   //!
   TBranch        *b_L1_SingleMu0_DQ;   //!
   TBranch        *b_L1_SingleMu0_EMTF;   //!
   TBranch        *b_L1_SingleMu0_OMTF;   //!
   TBranch        *b_L1_SingleMu0_Upt10;   //!
   TBranch        *b_L1_SingleMu0_Upt10_BMTF;   //!
   TBranch        *b_L1_SingleMu0_Upt10_EMTF;   //!
   TBranch        *b_L1_SingleMu0_Upt10_OMTF;   //!
   TBranch        *b_L1_SingleMu12_DQ_BMTF;   //!
   TBranch        *b_L1_SingleMu12_DQ_EMTF;   //!
   TBranch        *b_L1_SingleMu12_DQ_OMTF;   //!
   TBranch        *b_L1_SingleMu15_DQ;   //!
   TBranch        *b_L1_SingleMu18;   //!
   TBranch        *b_L1_SingleMu20;   //!
   TBranch        *b_L1_SingleMu22;   //!
   TBranch        *b_L1_SingleMu22_BMTF;   //!
   TBranch        *b_L1_SingleMu22_DQ;   //!
   TBranch        *b_L1_SingleMu22_EMTF;   //!
   TBranch        *b_L1_SingleMu22_OMTF;   //!
   TBranch        *b_L1_SingleMu22_OQ;   //!
   TBranch        *b_L1_SingleMu25;   //!
   TBranch        *b_L1_SingleMu3;   //!
   TBranch        *b_L1_SingleMu5;   //!
   TBranch        *b_L1_SingleMu7;   //!
   TBranch        *b_L1_SingleMu7_DQ;   //!
   TBranch        *b_L1_SingleMuCosmics;   //!
   TBranch        *b_L1_SingleMuCosmics_BMTF;   //!
   TBranch        *b_L1_SingleMuCosmics_EMTF;   //!
   TBranch        *b_L1_SingleMuCosmics_OMTF;   //!
   TBranch        *b_L1_SingleMuOpen;   //!
   TBranch        *b_L1_SingleMuOpen_BMTF;   //!
   TBranch        *b_L1_SingleMuOpen_EMTF;   //!
   TBranch        *b_L1_SingleMuOpen_NotBptxOR;   //!
   TBranch        *b_L1_SingleMuOpen_OMTF;   //!
   TBranch        *b_L1_SingleMuOpen_er1p1_NotBptxOR_3BX;   //!
   TBranch        *b_L1_SingleMuOpen_er1p4_NotBptxOR_3BX;   //!
   TBranch        *b_L1_SingleMuShower_Nominal;   //!
   TBranch        *b_L1_SingleMuShower_Tight;   //!
   TBranch        *b_L1_SingleTau120er2p1;   //!
   TBranch        *b_L1_SingleTau130er2p1;   //!
   TBranch        *b_L1_SingleTau70er2p1;   //!
   TBranch        *b_L1_TOTEM_1;   //!
   TBranch        *b_L1_TOTEM_2;   //!
   TBranch        *b_L1_TOTEM_3;   //!
   TBranch        *b_L1_TOTEM_4;   //!
   TBranch        *b_L1_TripleEG16er2p5;   //!
   TBranch        *b_L1_TripleEG_18_17_8_er2p5;   //!
   TBranch        *b_L1_TripleEG_18_18_12_er2p5;   //!
   TBranch        *b_L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5;   //!
   TBranch        *b_L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5;   //!
   TBranch        *b_L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5;   //!
   TBranch        *b_L1_TripleMu0;   //!
   TBranch        *b_L1_TripleMu0_OQ;   //!
   TBranch        *b_L1_TripleMu0_SQ;   //!
   TBranch        *b_L1_TripleMu3;   //!
   TBranch        *b_L1_TripleMu3_SQ;   //!
   TBranch        *b_L1_TripleMu_3SQ_2p5SQ_0;   //!
   TBranch        *b_L1_TripleMu_3SQ_2p5SQ_0_Mass_Max12;   //!
   TBranch        *b_L1_TripleMu_3SQ_2p5SQ_0_OS_Mass_Max12;   //!
   TBranch        *b_L1_TripleMu_4SQ_2p5SQ_0_OS_Mass_Max12;   //!
   TBranch        *b_L1_TripleMu_5SQ_3SQ_0OQ;   //!
   TBranch        *b_L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9;   //!
   TBranch        *b_L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9;   //!
   TBranch        *b_L1_TripleMu_5_3_3;   //!
   TBranch        *b_L1_TripleMu_5_3_3_SQ;   //!
   TBranch        *b_L1_TripleMu_5_3p5_2p5;   //!
   TBranch        *b_L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17;   //!
   TBranch        *b_L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17;   //!
   TBranch        *b_L1_TripleMu_5_5_3;   //!
   TBranch        *b_L1_TwoMuShower_Loose;   //!
   TBranch        *b_L1_UnpairedBunchBptxMinus;   //!
   TBranch        *b_L1_UnpairedBunchBptxPlus;   //!
   TBranch        *b_L1_ZeroBias;   //!
   TBranch        *b_L1_ZeroBias_copy;   //!
   TBranch        *b_L1_UnprefireableEvent;   //!
   TBranch        *b_Flag_HBHENoiseFilter;   //!
   TBranch        *b_Flag_HBHENoiseIsoFilter;   //!
   TBranch        *b_Flag_CSCTightHaloFilter;   //!
   TBranch        *b_Flag_CSCTightHaloTrkMuUnvetoFilter;   //!
   TBranch        *b_Flag_CSCTightHalo2015Filter;   //!
   TBranch        *b_Flag_globalTightHalo2016Filter;   //!
   TBranch        *b_Flag_globalSuperTightHalo2016Filter;   //!
   TBranch        *b_Flag_HcalStripHaloFilter;   //!
   TBranch        *b_Flag_hcalLaserEventFilter;   //!
   TBranch        *b_Flag_EcalDeadCellTriggerPrimitiveFilter;   //!
   TBranch        *b_Flag_EcalDeadCellBoundaryEnergyFilter;   //!
   TBranch        *b_Flag_ecalBadCalibFilter;   //!
   TBranch        *b_Flag_goodVertices;   //!
   TBranch        *b_Flag_eeBadScFilter;   //!
   TBranch        *b_Flag_ecalLaserCorrFilter;   //!
   TBranch        *b_Flag_trkPOGFilters;   //!
   TBranch        *b_Flag_chargedHadronTrackResolutionFilter;   //!
   TBranch        *b_Flag_muonBadTrackFilter;   //!
   TBranch        *b_Flag_BadChargedCandidateFilter;   //!
   TBranch        *b_Flag_BadPFMuonFilter;   //!
   TBranch        *b_Flag_BadPFMuonDzFilter;   //!
   TBranch        *b_Flag_hfNoisyHitsFilter;   //!
   TBranch        *b_Flag_BadChargedCandidateSummer16Filter;   //!
   TBranch        *b_Flag_BadPFMuonSummer16Filter;   //!
   TBranch        *b_Flag_trkPOG_manystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_toomanystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_logErrorTooManyClusters;   //!
   TBranch        *b_Flag_METFilters;   //!
   TBranch        *b_L1Reco_step;   //!
   TBranch        *b_L1simulation_step;   //!
   TBranch        *b_HLTriggerFirstPath;   //!
   TBranch        *b_HLT_EphemeralPhysics;   //!
   TBranch        *b_HLT_EphemeralZeroBias;   //!
   TBranch        *b_HLT_EcalCalibration;   //!
   TBranch        *b_HLT_HcalCalibration;   //!
   TBranch        *b_HLT_HcalNZS;   //!
   TBranch        *b_HLT_HcalPhiSym;   //!
   TBranch        *b_HLT_Random;   //!
   TBranch        *b_HLT_Physics;   //!
   TBranch        *b_HLT_ZeroBias;   //!
   TBranch        *b_HLT_ZeroBias_Alignment;   //!
   TBranch        *b_HLT_ZeroBias_Beamspot;   //!
   TBranch        *b_HLT_ZeroBias_IsolatedBunches;   //!
   TBranch        *b_HLT_ZeroBias_FirstBXAfterTrain;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionAfterAbortGap;   //!
   TBranch        *b_HLT_ZeroBias_FirstCollisionInTrain;   //!
   TBranch        *b_HLT_ZeroBias_LastCollisionInTrain;   //!
   TBranch        *b_HLT_HT300_Beamspot;   //!
   TBranch        *b_HLT_IsoTrackHB;   //!
   TBranch        *b_HLT_IsoTrackHE;   //!
   TBranch        *b_HLT_PFJet40_GPUvsCPU;   //!
   TBranch        *b_HLT_AK8PFJet400_MassSD30;   //!
   TBranch        *b_HLT_AK8PFJet420_MassSD30;   //!
   TBranch        *b_HLT_AK8PFJet450_MassSD30;   //!
   TBranch        *b_HLT_AK8PFJet470_MassSD30;   //!
   TBranch        *b_HLT_AK8PFJet500_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet250_250_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet260_260_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet270_270_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet280_280_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet290_290_MassSD30;   //!
   TBranch        *b_HLT_AK8DiPFJet250_250_MassSD50;   //!
   TBranch        *b_HLT_AK8DiPFJet260_260_MassSD50;   //!
   TBranch        *b_HLT_CaloJet500_NoJetID;   //!
   TBranch        *b_HLT_CaloJet550_NoJetID;   //!
   TBranch        *b_HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon;   //!
   TBranch        *b_HLT_Trimuon5_3p5_2_Upsilon_Muon;   //!
   TBranch        *b_HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon;   //!
   TBranch        *b_HLT_DoubleEle25_CaloIdL_MW;   //!
   TBranch        *b_HLT_DoubleEle27_CaloIdL_MW;   //!
   TBranch        *b_HLT_DoubleEle33_CaloIdL_MW;   //!
   TBranch        *b_HLT_DoubleEle24_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350;   //!
   TBranch        *b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350;   //!
   TBranch        *b_HLT_Mu27_Ele37_CaloIdL_MW;   //!
   TBranch        *b_HLT_Mu37_Ele27_CaloIdL_MW;   //!
   TBranch        *b_HLT_Mu37_TkMu27;   //!
   TBranch        *b_HLT_DoubleMu4_3_Bs;   //!
   TBranch        *b_HLT_DoubleMu4_3_Jpsi;   //!
   TBranch        *b_HLT_DoubleMu4_3_LowMass;   //!
   TBranch        *b_HLT_DoubleMu4_LowMass_Displaced;   //!
   TBranch        *b_HLT_Mu0_L1DoubleMu;   //!
   TBranch        *b_HLT_Mu4_L1DoubleMu;   //!
   TBranch        *b_HLT_DoubleMu4_3_Photon4_BsToMMG;   //!
   TBranch        *b_HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG;   //!
   TBranch        *b_HLT_DoubleMu3_Trk_Tau3mu;   //!
   TBranch        *b_HLT_DoubleMu3_TkMu_DsTau3Mu;   //!
   TBranch        *b_HLT_DoubleMu4_Mass3p8_DZ_PFHT350;   //!
   TBranch        *b_HLT_DoubleMu4_MuMuTrk_Displaced;   //!
   TBranch        *b_HLT_Mu3_PFJet40;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Jpsi;   //!
   TBranch        *b_HLT_Mu7p5_L2Mu2_Upsilon;   //!
   TBranch        *b_HLT_Mu3_L1SingleMu5orSingleMu7;   //!
   TBranch        *b_HLT_DoublePhoton33_CaloIdL;   //!
   TBranch        *b_HLT_DoublePhoton70;   //!
   TBranch        *b_HLT_DoublePhoton85;   //!
   TBranch        *b_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG;   //!
   TBranch        *b_HLT_Ele30_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele32_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele35_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele38_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele40_WPTight_Gsf;   //!
   TBranch        *b_HLT_Ele32_WPTight_Gsf_L1DoubleEG;   //!
   TBranch        *b_HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1;   //!
   TBranch        *b_HLT_IsoMu20;   //!
   TBranch        *b_HLT_IsoMu24;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1;   //!
   TBranch        *b_HLT_IsoMu27;   //!
   TBranch        *b_HLT_UncorrectedJetE30_NoBPTX;   //!
   TBranch        *b_HLT_UncorrectedJetE30_NoBPTX3BX;   //!
   TBranch        *b_HLT_UncorrectedJetE60_NoBPTX3BX;   //!
   TBranch        *b_HLT_UncorrectedJetE70_NoBPTX3BX;   //!
   TBranch        *b_HLT_L1SingleMuCosmics;   //!
   TBranch        *b_HLT_L2Mu10_NoVertex_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu10_NoVertex_NoBPTX;   //!
   TBranch        *b_HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX;   //!
   TBranch        *b_HLT_L2Mu23NoVtx_2Cha;   //!
   TBranch        *b_HLT_L2Mu23NoVtx_2Cha_CosmicSeed;   //!
   TBranch        *b_HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4;   //!
   TBranch        *b_HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4;   //!
   TBranch        *b_HLT_DoubleL2Mu50;   //!
   TBranch        *b_HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed;   //!
   TBranch        *b_HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed;   //!
   TBranch        *b_HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4;   //!
   TBranch        *b_HLT_DoubleL2Mu23NoVtx_2Cha;   //!
   TBranch        *b_HLT_DoubleL2Mu25NoVtx_2Cha;   //!
   TBranch        *b_HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ;   //!
   TBranch        *b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8;   //!
   TBranch        *b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8;   //!
   TBranch        *b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8;   //!
   TBranch        *b_HLT_Mu30_TkMu0_Psi;   //!
   TBranch        *b_HLT_Mu30_TkMu0_Upsilon;   //!
   TBranch        *b_HLT_Mu25_TkMu0_Phi;   //!
   TBranch        *b_HLT_Mu15;   //!
   TBranch        *b_HLT_Mu20;   //!
   TBranch        *b_HLT_Mu27;   //!
   TBranch        *b_HLT_Mu50;   //!
   TBranch        *b_HLT_Mu55;   //!
   TBranch        *b_HLT_CascadeMu100;   //!
   TBranch        *b_HLT_HighPtTkMu100;   //!
   TBranch        *b_HLT_DiPFJetAve40;   //!
   TBranch        *b_HLT_DiPFJetAve60;   //!
   TBranch        *b_HLT_DiPFJetAve80;   //!
   TBranch        *b_HLT_DiPFJetAve140;   //!
   TBranch        *b_HLT_DiPFJetAve200;   //!
   TBranch        *b_HLT_DiPFJetAve260;   //!
   TBranch        *b_HLT_DiPFJetAve320;   //!
   TBranch        *b_HLT_DiPFJetAve400;   //!
   TBranch        *b_HLT_DiPFJetAve500;   //!
   TBranch        *b_HLT_DiPFJetAve60_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve80_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve100_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve160_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve220_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve260_HFJEC;   //!
   TBranch        *b_HLT_DiPFJetAve300_HFJEC;   //!
   TBranch        *b_HLT_AK8PFJet40;   //!
   TBranch        *b_HLT_AK8PFJet60;   //!
   TBranch        *b_HLT_AK8PFJet80;   //!
   TBranch        *b_HLT_AK8PFJet140;   //!
   TBranch        *b_HLT_AK8PFJet200;   //!
   TBranch        *b_HLT_AK8PFJet260;   //!
   TBranch        *b_HLT_AK8PFJet320;   //!
   TBranch        *b_HLT_AK8PFJet400;   //!
   TBranch        *b_HLT_AK8PFJet450;   //!
   TBranch        *b_HLT_AK8PFJet500;   //!
   TBranch        *b_HLT_AK8PFJet550;   //!
   TBranch        *b_HLT_PFJet40;   //!
   TBranch        *b_HLT_PFJet60;   //!
   TBranch        *b_HLT_PFJet80;   //!
   TBranch        *b_HLT_PFJet110;   //!
   TBranch        *b_HLT_PFJet140;   //!
   TBranch        *b_HLT_PFJet200;   //!
   TBranch        *b_HLT_PFJet260;   //!
   TBranch        *b_HLT_PFJet320;   //!
   TBranch        *b_HLT_PFJet400;   //!
   TBranch        *b_HLT_PFJet450;   //!
   TBranch        *b_HLT_PFJet500;   //!
   TBranch        *b_HLT_PFJet550;   //!
   TBranch        *b_HLT_PFJetFwd40;   //!
   TBranch        *b_HLT_PFJetFwd60;   //!
   TBranch        *b_HLT_PFJetFwd80;   //!
   TBranch        *b_HLT_PFJetFwd140;   //!
   TBranch        *b_HLT_PFJetFwd200;   //!
   TBranch        *b_HLT_PFJetFwd260;   //!
   TBranch        *b_HLT_PFJetFwd320;   //!
   TBranch        *b_HLT_PFJetFwd400;   //!
   TBranch        *b_HLT_PFJetFwd450;   //!
   TBranch        *b_HLT_PFJetFwd500;   //!
   TBranch        *b_HLT_AK8PFJetFwd15;   //!
   TBranch        *b_HLT_AK8PFJetFwd25;   //!
   TBranch        *b_HLT_AK8PFJetFwd40;   //!
   TBranch        *b_HLT_AK8PFJetFwd60;   //!
   TBranch        *b_HLT_AK8PFJetFwd80;   //!
   TBranch        *b_HLT_AK8PFJetFwd140;   //!
   TBranch        *b_HLT_AK8PFJetFwd200;   //!
   TBranch        *b_HLT_AK8PFJetFwd260;   //!
   TBranch        *b_HLT_AK8PFJetFwd320;   //!
   TBranch        *b_HLT_AK8PFJetFwd400;   //!
   TBranch        *b_HLT_AK8PFJetFwd450;   //!
   TBranch        *b_HLT_AK8PFJetFwd500;   //!
   TBranch        *b_HLT_PFHT180;   //!
   TBranch        *b_HLT_PFHT250;   //!
   TBranch        *b_HLT_PFHT370;   //!
   TBranch        *b_HLT_PFHT430;   //!
   TBranch        *b_HLT_PFHT510;   //!
   TBranch        *b_HLT_PFHT590;   //!
   TBranch        *b_HLT_PFHT680;   //!
   TBranch        *b_HLT_PFHT780;   //!
   TBranch        *b_HLT_PFHT890;   //!
   TBranch        *b_HLT_PFHT1050;   //!
   TBranch        *b_HLT_PFHT500_PFMET100_PFMHT100_IDTight;   //!
   TBranch        *b_HLT_PFHT500_PFMET110_PFMHT110_IDTight;   //!
   TBranch        *b_HLT_PFHT700_PFMET85_PFMHT85_IDTight;   //!
   TBranch        *b_HLT_PFHT800_PFMET75_PFMHT75_IDTight;   //!
   TBranch        *b_HLT_PFMET120_PFMHT120_IDTight;   //!
   TBranch        *b_HLT_PFMET130_PFMHT130_IDTight;   //!
   TBranch        *b_HLT_PFMET140_PFMHT140_IDTight;   //!
   TBranch        *b_HLT_PFMET120_PFMHT120_IDTight_PFHT60;   //!
   TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60;   //!
   TBranch        *b_HLT_PFMETTypeOne140_PFMHT140_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight;   //!
   TBranch        *b_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF;   //!
   TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF;   //!
   TBranch        *b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF;   //!
   TBranch        *b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF;   //!
   TBranch        *b_HLT_L1ETMHadSeeds;   //!
   TBranch        *b_HLT_CaloMHT90;   //!
   TBranch        *b_HLT_CaloMET90_NotCleaned;   //!
   TBranch        *b_HLT_CaloMET350_NotCleaned;   //!
   TBranch        *b_HLT_PFMET200_NotCleaned;   //!
   TBranch        *b_HLT_PFMET250_NotCleaned;   //!
   TBranch        *b_HLT_PFMET300_NotCleaned;   //!
   TBranch        *b_HLT_PFMET200_BeamHaloCleaned;   //!
   TBranch        *b_HLT_PFMETTypeOne200_BeamHaloCleaned;   //!
   TBranch        *b_HLT_MET105_IsoTrk50;   //!
   TBranch        *b_HLT_MET120_IsoTrk50;   //!
   TBranch        *b_HLT_Mu12eta2p3;   //!
   TBranch        *b_HLT_Mu12eta2p3_PFJet40;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets40_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets100_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets200_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets350_PFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71;   //!
   TBranch        *b_HLT_Photon300_NoHE;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ;   //!
   TBranch        *b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ;   //!
   TBranch        *b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu17_TrkIsoVVL;   //!
   TBranch        *b_HLT_Mu19_TrkIsoVVL;   //!
   TBranch        *b_HLT_BTagMu_AK4DiJet20_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK4DiJet40_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK4DiJet70_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK4DiJet110_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK4DiJet170_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK4Jet300_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK8DiJet170_Mu5;   //!
   TBranch        *b_HLT_BTagMu_AK8Jet170_DoubleMu5;   //!
   TBranch        *b_HLT_BTagMu_AK8Jet300_Mu5;   //!
   TBranch        *b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL;   //!
   TBranch        *b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ;   //!
   TBranch        *b_HLT_Photon33;   //!
   TBranch        *b_HLT_Photon50;   //!
   TBranch        *b_HLT_Photon75;   //!
   TBranch        *b_HLT_Photon90;   //!
   TBranch        *b_HLT_Photon120;   //!
   TBranch        *b_HLT_Photon150;   //!
   TBranch        *b_HLT_Photon175;   //!
   TBranch        *b_HLT_Photon200;   //!
   TBranch        *b_HLT_Photon30EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon50EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon75EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon90EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon110EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon130EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon150EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon175EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon200EB_TightID_TightIso;   //!
   TBranch        *b_HLT_Photon100EBHE10;   //!
   TBranch        *b_HLT_Photon50_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon75_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon90_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon120_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Photon165_R9Id90_HE10_IsoM;   //!
   TBranch        *b_HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90;   //!
   TBranch        *b_HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95;   //!
   TBranch        *b_HLT_Photon35_TwoProngs35;   //!
   TBranch        *b_HLT_IsoMu24_TwoProngs35;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_L1_NoOS;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_NoVertexing_NoOS;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_NoVertexing;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_L1_4R_0er1p5R;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R;   //!
   TBranch        *b_HLT_Dimuon0_Jpsi3p5_Muon2;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_L1_4p5;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_L1_4p5er2p0;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_L1_4p5er2p0M;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_NoVertexing;   //!
   TBranch        *b_HLT_Dimuon0_LowMass_L1_0er1p5R;   //!
   TBranch        *b_HLT_Dimuon0_LowMass_L1_0er1p5;   //!
   TBranch        *b_HLT_Dimuon0_LowMass;   //!
   TBranch        *b_HLT_Dimuon0_LowMass_L1_4;   //!
   TBranch        *b_HLT_Dimuon0_LowMass_L1_4R;   //!
   TBranch        *b_HLT_Dimuon0_LowMass_L1_TM530;   //!
   TBranch        *b_HLT_Dimuon0_Upsilon_Muon_NoL1Mass;   //!
   TBranch        *b_HLT_TripleMu_5_3_3_Mass3p8_DZ;   //!
   TBranch        *b_HLT_TripleMu_10_5_5_DZ;   //!
   TBranch        *b_HLT_TripleMu_12_10_5;   //!
   TBranch        *b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15;   //!
   TBranch        *b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1;   //!
   TBranch        *b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15;   //!
   TBranch        *b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1;   //!
   TBranch        *b_HLT_DoubleMu3_DZ_PFMET50_PFMHT60;   //!
   TBranch        *b_HLT_DoubleMu3_DZ_PFMET70_PFMHT70;   //!
   TBranch        *b_HLT_DoubleMu3_DZ_PFMET90_PFMHT90;   //!
   TBranch        *b_HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass;   //!
   TBranch        *b_HLT_DoubleMu4_Jpsi_Displaced;   //!
   TBranch        *b_HLT_DoubleMu4_Jpsi_NoVertexing;   //!
   TBranch        *b_HLT_DoubleMu4_JpsiTrkTrk_Displaced;   //!
   TBranch        *b_HLT_DoubleMu4_JpsiTrk_Bc;   //!
   TBranch        *b_HLT_DoubleMu43NoFiltersNoVtx;   //!
   TBranch        *b_HLT_DoubleMu48NoFiltersNoVtx;   //!
   TBranch        *b_HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL;   //!
   TBranch        *b_HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL;   //!
   TBranch        *b_HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL;   //!
   TBranch        *b_HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL;   //!
   TBranch        *b_HLT_DiJet110_35_Mjj650_PFMET110;   //!
   TBranch        *b_HLT_DiJet110_35_Mjj650_PFMET120;   //!
   TBranch        *b_HLT_DiJet110_35_Mjj650_PFMET130;   //!
   TBranch        *b_HLT_TripleJet110_35_35_Mjj650_PFMET110;   //!
   TBranch        *b_HLT_TripleJet110_35_35_Mjj650_PFMET120;   //!
   TBranch        *b_HLT_TripleJet110_35_35_Mjj650_PFMET130;   //!
   TBranch        *b_HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned;   //!
   TBranch        *b_HLT_Ele28_eta2p1_WPTight_Gsf_HT150;   //!
   TBranch        *b_HLT_Ele28_HighEta_SC20_Mass55;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT450_PFMET50;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT450;   //!
   TBranch        *b_HLT_Ele50_IsoVVVL_PFHT450;   //!
   TBranch        *b_HLT_Ele15_IsoVVVL_PFHT600;   //!
   TBranch        *b_HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60;   //!
   TBranch        *b_HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT450_PFMET50;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT450;   //!
   TBranch        *b_HLT_Mu50_IsoVVVL_PFHT450;   //!
   TBranch        *b_HLT_Mu15_IsoVVVL_PFHT600;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight;   //!
   TBranch        *b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight;   //!
   TBranch        *b_HLT_Dimuon10_Upsilon_y1p4;   //!
   TBranch        *b_HLT_Dimuon12_Upsilon_y1p4;   //!
   TBranch        *b_HLT_Dimuon14_Phi_Barrel_Seagulls;   //!
   TBranch        *b_HLT_Dimuon25_Jpsi;   //!
   TBranch        *b_HLT_Dimuon14_PsiPrime;   //!
   TBranch        *b_HLT_Dimuon14_PsiPrime_noCorrL1;   //!
   TBranch        *b_HLT_Dimuon18_PsiPrime;   //!
   TBranch        *b_HLT_Dimuon18_PsiPrime_noCorrL1;   //!
   TBranch        *b_HLT_Dimuon24_Upsilon_noCorrL1;   //!
   TBranch        *b_HLT_Dimuon24_Phi_noCorrL1;   //!
   TBranch        *b_HLT_Dimuon25_Jpsi_noCorrL1;   //!
   TBranch        *b_HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8;   //!
   TBranch        *b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ;   //!
   TBranch        *b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_DoubleIsoMu20_eta2p1;   //!
   TBranch        *b_HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx;   //!
   TBranch        *b_HLT_Mu8;   //!
   TBranch        *b_HLT_Mu17;   //!
   TBranch        *b_HLT_Mu19;   //!
   TBranch        *b_HLT_Mu17_Photon30_IsoCaloId;   //!
   TBranch        *b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30;   //!
   TBranch        *b_HLT_Ele8_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele17_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele23_CaloIdM_TrackIdM_PFJet30;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165;   //!
   TBranch        *b_HLT_Ele115_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_Ele135_CaloIdVT_GsfTrkIdT;   //!
   TBranch        *b_HLT_PFHT330PT30_QuadPFJet_75_60_45_40;   //!
   TBranch        *b_HLT_PFHT400_SixPFJet32;   //!
   TBranch        *b_HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50;   //!
   TBranch        *b_HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94;   //!
   TBranch        *b_HLT_PFHT450_SixPFJet36;   //!
   TBranch        *b_HLT_PFHT450_SixPFJet36_PNetBTag0p35;   //!
   TBranch        *b_HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59;   //!
   TBranch        *b_HLT_PFHT400_FivePFJet_100_100_60_30_30;   //!
   TBranch        *b_HLT_PFHT350;   //!
   TBranch        *b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350;   //!
   TBranch        *b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380;   //!
   TBranch        *b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400;   //!
   TBranch        *b_HLT_ECALHT800;   //!
   TBranch        *b_HLT_DiSC30_18_EIso_AND_HE_Mass70;   //!
   TBranch        *b_HLT_Photon20_HoverELoose;   //!
   TBranch        *b_HLT_Photon30_HoverELoose;   //!
   TBranch        *b_HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142;   //!
   TBranch        *b_HLT_CDC_L2cosmic_10_er1p0;   //!
   TBranch        *b_HLT_CDC_L2cosmic_5p5_er1p0;   //!
   TBranch        *b_HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL;   //!
   TBranch        *b_HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1;   //!
   TBranch        *b_HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3;   //!
   TBranch        *b_HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3;   //!
   TBranch        *b_HLT_Mu18_Mu9_SameSign;   //!
   TBranch        *b_HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05;   //!
   TBranch        *b_HLT_DoubleMu3_DCA_PFMET50_PFMHT60;   //!
   TBranch        *b_HLT_TripleMu_5_3_3_Mass3p8_DCA;   //!
   TBranch        *b_HLT_QuadPFJet103_88_75_15;   //!
   TBranch        *b_HLT_QuadPFJet105_88_76_15;   //!
   TBranch        *b_HLT_QuadPFJet111_90_80_15;   //!
   TBranch        *b_HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId;   //!
   TBranch        *b_HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55;   //!
   TBranch        *b_HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1;   //!
   TBranch        *b_HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1;   //!
   TBranch        *b_HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5;   //!
   TBranch        *b_HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5;   //!
   TBranch        *b_HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5;   //!
   TBranch        *b_HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;   //!
   TBranch        *b_HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2;   //!
   TBranch        *b_HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;   //!
   TBranch        *b_HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2;   //!
   TBranch        *b_HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1;   //!
   TBranch        *b_HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5;   //!
   TBranch        *b_HLT_PFHT280_QuadPFJet30;   //!
   TBranch        *b_HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55;   //!
   TBranch        *b_HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60;   //!
   TBranch        *b_HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60;   //!
   TBranch        *b_HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50;   //!
   TBranch        *b_HLT_QuadPFJet100_88_70_30;   //!
   TBranch        *b_HLT_QuadPFJet105_88_75_30;   //!
   TBranch        *b_HLT_QuadPFJet111_90_80_30;   //!
   TBranch        *b_HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight;   //!
   TBranch        *b_HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight;   //!
   TBranch        *b_HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight;   //!
   TBranch        *b_HLT_AK8PFJet220_SoftDropMass40;   //!
   TBranch        *b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50;   //!
   TBranch        *b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53;   //!
   TBranch        *b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55;   //!
   TBranch        *b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60;   //!
   TBranch        *b_HLT_AK8PFJet230_SoftDropMass40;   //!
   TBranch        *b_HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10;   //!
   TBranch        *b_HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03;   //!
   TBranch        *b_HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05;   //!
   TBranch        *b_HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10;   //!
   TBranch        *b_HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03;   //!
   TBranch        *b_HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05;   //!
   TBranch        *b_HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10;   //!
   TBranch        *b_HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03;   //!
   TBranch        *b_HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05;   //!
   TBranch        *b_HLT_AK8PFJet425_SoftDropMass40;   //!
   TBranch        *b_HLT_AK8PFJet450_SoftDropMass40;   //!
   TBranch        *b_HLT_IsoMu50_AK8PFJet220_SoftDropMass40;   //!
   TBranch        *b_HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40;   //!
   TBranch        *b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06;   //!
   TBranch        *b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30;   //!
   TBranch        *b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50;   //!
   TBranch        *b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60;   //!
   TBranch        *b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1;   //!
   TBranch        *b_HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1;   //!
   TBranch        *b_HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_L2Mu10NoVtx_2Cha;   //!
   TBranch        *b_HLT_L2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_L3Mu10NoVtx;   //!
   TBranch        *b_HLT_L3Mu10NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm;   //!
   TBranch        *b_HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm;   //!
   TBranch        *b_HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_L2Mu10NoVtx_2Cha_CosmicSeed;   //!
   TBranch        *b_HLT_L2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm;   //!
   TBranch        *b_HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_L3dTksMu10_NoVtx_DxyMin0p01cm;   //!
   TBranch        *b_HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId;   //!
   TBranch        *b_HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay3nsInclusive;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive;   //!
   TBranch        *b_HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay2nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless;   //!
   TBranch        *b_HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless;   //!
   TBranch        *b_HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless;   //!
   TBranch        *b_HLT_L1Mu6HT240;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5;   //!
   TBranch        *b_HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5;   //!
   TBranch        *b_HLT_HT350;   //!
   TBranch        *b_HLT_HT425;   //!
   TBranch        *b_HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT400_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT430_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT550_DisplacedDijet60_Inclusive;   //!
   TBranch        *b_HLT_HT650_DisplacedDijet60_Inclusive;   //!
   TBranch        *b_HLT_CaloMET60_DTCluster50;   //!
   TBranch        *b_HLT_CaloMET60_DTClusterNoMB1S50;   //!
   TBranch        *b_HLT_L1MET_DTCluster50;   //!
   TBranch        *b_HLT_L1MET_DTClusterNoMB1S50;   //!
   TBranch        *b_HLT_CscCluster_Loose;   //!
   TBranch        *b_HLT_CscCluster_Medium;   //!
   TBranch        *b_HLT_CscCluster_Tight;   //!
   TBranch        *b_HLT_DoubleCscCluster75;   //!
   TBranch        *b_HLT_DoubleCscCluster100;   //!
   TBranch        *b_HLT_L1CSCShower_DTCluster50;   //!
   TBranch        *b_HLT_L1CSCShower_DTCluster75;   //!
   TBranch        *b_HLT_PFMET105_IsoTrk50;   //!
   TBranch        *b_HLT_L1SingleLLPJet;   //!
   TBranch        *b_HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack;   //!
   TBranch        *b_HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5;   //!
   TBranch        *b_HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive;   //!
   TBranch        *b_HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless;   //!
   TBranch        *b_HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive;   //!
   TBranch        *b_HLT_DiPhoton10Time1ns;   //!
   TBranch        *b_HLT_DiPhoton10Time1p2ns;   //!
   TBranch        *b_HLT_DiPhoton10Time1p4ns;   //!
   TBranch        *b_HLT_DiPhoton10Time1p6ns;   //!
   TBranch        *b_HLT_DiPhoton10Time1p8ns;   //!
   TBranch        *b_HLT_DiPhoton10Time2ns;   //!
   TBranch        *b_HLT_DiPhoton10sminlt0p1;   //!
   TBranch        *b_HLT_DiPhoton10sminlt0p12;   //!
   TBranch        *b_HLT_DiPhoton10_CaloIdL;   //!
   TBranch        *b_HLT_DoubleEle4_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle4p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle5p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle6_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle6p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle7_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle7p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle8_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle8p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle9_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle9p5_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle10_eta1p22_mMax6;   //!
   TBranch        *b_HLT_DoubleEle4_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle6_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle7_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle8_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle9_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle10_eta1p22_mMax6_dz0p8;   //!
   TBranch        *b_HLT_DoubleEle4_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle6_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle7_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle8_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle9_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_DoubleEle10_eta1p22_mMax6_trkHits10;   //!
   TBranch        *b_HLT_SingleEle8;   //!
   TBranch        *b_HLT_SingleEle8_SingleEGL1;   //!
   TBranch        *b_HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT;   //!
   TBranch        *b_HLT_Mu50_L1SingleMuShower;   //!
   TBranch        *b_HLT_IsoMu24_OneProng32;   //!
   TBranch        *b_HLT_Photon32_OneProng32_M50To105;   //!
   TBranch        *b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80;   //!
   TBranch        *b_HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5;   //!
   TBranch        *b_HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5;   //!
   TBranch        *b_HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5;   //!
   TBranch        *b_HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0;   //!
   TBranch        *b_HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85;   //!
   TBranch        *b_HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85;   //!
   TBranch        *b_HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL;   //!
   TBranch        *b_HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL;   //!
   TBranch        *b_HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet;   //!
   TBranch        *b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1;   //!
   TBranch        *b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12;   //!
   TBranch        *b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17;   //!
   TBranch        *b_HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22;   //!
   TBranch        *b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf;   //!
   TBranch        *b_HLT_PFJet200_TimeLtNeg2p5ns;   //!
   TBranch        *b_HLT_PFJet200_TimeGt2p5ns;   //!
   TBranch        *b_HLT_Photon50_TimeLtNeg2p5ns;   //!
   TBranch        *b_HLT_Photon50_TimeGt2p5ns;   //!
   TBranch        *b_HLT_ExpressMuons;   //!
   TBranch        *b_HLT_PPSMaxTracksPerArm1;   //!
   TBranch        *b_HLT_PPSMaxTracksPerRP4;   //!
   TBranch        *b_HLT_PPSRandom;   //!
   TBranch        *b_HLTriggerFinalPath;   //!

   VBFSingleTauCheck(TTree *tree=0);
   virtual ~VBFSingleTauCheck();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef VBFSingleTauCheck_cxx
VBFSingleTauCheck::VBFSingleTauCheck(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      //TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("VBF_postBpix_2023_sample.root"); // original, renamed
      //TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("VBF_NanoAODv12_postBpix_2023_sample.root");
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("combined_VBF_NanoV13.root");
      //TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("VBF_NanoAODv13_2024_realistic.root");
      if (!f || !f->IsOpen()) {
         //f = new TFile("VBF_NanoAODv12_postBpix_2023_sample.root");
         f = new TFile("combined_VBF_NanoV13.root");
         //f = new TFile("VBF_NanoAODv13_2024_realistic.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

VBFSingleTauCheck::~VBFSingleTauCheck()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t VBFSingleTauCheck::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t VBFSingleTauCheck::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void VBFSingleTauCheck::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("luminosityBlock", &luminosityBlock, &b_luminosityBlock);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("bunchCrossing", &bunchCrossing, &b_bunchCrossing);
   fChain->SetBranchAddress("nJet", &nJet, &b_nJet);
   fChain->SetBranchAddress("Jet_jetId", Jet_jetId, &b_Jet_jetId);
   fChain->SetBranchAddress("Jet_nConstituents", Jet_nConstituents, &b_Jet_nConstituents);
   fChain->SetBranchAddress("Jet_nElectrons", Jet_nElectrons, &b_Jet_nElectrons);
   fChain->SetBranchAddress("Jet_nMuons", Jet_nMuons, &b_Jet_nMuons);
   fChain->SetBranchAddress("Jet_nSVs", Jet_nSVs, &b_Jet_nSVs);
   fChain->SetBranchAddress("Jet_electronIdx1", Jet_electronIdx1, &b_Jet_electronIdx1);
   fChain->SetBranchAddress("Jet_electronIdx2", Jet_electronIdx2, &b_Jet_electronIdx2);
   fChain->SetBranchAddress("Jet_muonIdx1", Jet_muonIdx1, &b_Jet_muonIdx1);
   fChain->SetBranchAddress("Jet_muonIdx2", Jet_muonIdx2, &b_Jet_muonIdx2);
   fChain->SetBranchAddress("Jet_svIdx1", Jet_svIdx1, &b_Jet_svIdx1);
   fChain->SetBranchAddress("Jet_svIdx2", Jet_svIdx2, &b_Jet_svIdx2);
   fChain->SetBranchAddress("Jet_hfadjacentEtaStripsSize", Jet_hfadjacentEtaStripsSize, &b_Jet_hfadjacentEtaStripsSize);
   fChain->SetBranchAddress("Jet_hfcentralEtaStripSize", Jet_hfcentralEtaStripSize, &b_Jet_hfcentralEtaStripSize);
   fChain->SetBranchAddress("Jet_PNetRegPtRawCorr", Jet_PNetRegPtRawCorr, &b_Jet_PNetRegPtRawCorr);
   fChain->SetBranchAddress("Jet_PNetRegPtRawCorrNeutrino", Jet_PNetRegPtRawCorrNeutrino, &b_Jet_PNetRegPtRawCorrNeutrino);
   fChain->SetBranchAddress("Jet_PNetRegPtRawRes", Jet_PNetRegPtRawRes, &b_Jet_PNetRegPtRawRes);
   fChain->SetBranchAddress("Jet_area", Jet_area, &b_Jet_area);
   fChain->SetBranchAddress("Jet_btagDeepFlavB", Jet_btagDeepFlavB, &b_Jet_btagDeepFlavB);
   fChain->SetBranchAddress("Jet_btagDeepFlavCvB", Jet_btagDeepFlavCvB, &b_Jet_btagDeepFlavCvB);
   fChain->SetBranchAddress("Jet_btagDeepFlavCvL", Jet_btagDeepFlavCvL, &b_Jet_btagDeepFlavCvL);
   fChain->SetBranchAddress("Jet_btagDeepFlavQG", Jet_btagDeepFlavQG, &b_Jet_btagDeepFlavQG);
   fChain->SetBranchAddress("Jet_btagPNetB", Jet_btagPNetB, &b_Jet_btagPNetB);
   fChain->SetBranchAddress("Jet_btagPNetCvB", Jet_btagPNetCvB, &b_Jet_btagPNetCvB);
   fChain->SetBranchAddress("Jet_btagPNetCvL", Jet_btagPNetCvL, &b_Jet_btagPNetCvL);
   fChain->SetBranchAddress("Jet_btagPNetQvG", Jet_btagPNetQvG, &b_Jet_btagPNetQvG);
   fChain->SetBranchAddress("Jet_btagPNetTauVJet", Jet_btagPNetTauVJet, &b_Jet_btagPNetTauVJet);
   fChain->SetBranchAddress("Jet_btagRobustParTAK4B", Jet_btagRobustParTAK4B, &b_Jet_btagRobustParTAK4B);
   fChain->SetBranchAddress("Jet_btagRobustParTAK4CvB", Jet_btagRobustParTAK4CvB, &b_Jet_btagRobustParTAK4CvB);
   fChain->SetBranchAddress("Jet_btagRobustParTAK4CvL", Jet_btagRobustParTAK4CvL, &b_Jet_btagRobustParTAK4CvL);
   fChain->SetBranchAddress("Jet_btagRobustParTAK4QG", Jet_btagRobustParTAK4QG, &b_Jet_btagRobustParTAK4QG);
   fChain->SetBranchAddress("Jet_chEmEF", Jet_chEmEF, &b_Jet_chEmEF);
   fChain->SetBranchAddress("Jet_chHEF", Jet_chHEF, &b_Jet_chHEF);
   fChain->SetBranchAddress("Jet_eta", Jet_eta, &b_Jet_eta);
   fChain->SetBranchAddress("Jet_hfsigmaEtaEta", Jet_hfsigmaEtaEta, &b_Jet_hfsigmaEtaEta);
   fChain->SetBranchAddress("Jet_hfsigmaPhiPhi", Jet_hfsigmaPhiPhi, &b_Jet_hfsigmaPhiPhi);
   fChain->SetBranchAddress("Jet_mass", Jet_mass, &b_Jet_mass);
   fChain->SetBranchAddress("Jet_muEF", Jet_muEF, &b_Jet_muEF);
   fChain->SetBranchAddress("Jet_muonSubtrFactor", Jet_muonSubtrFactor, &b_Jet_muonSubtrFactor);
   fChain->SetBranchAddress("Jet_neEmEF", Jet_neEmEF, &b_Jet_neEmEF);
   fChain->SetBranchAddress("Jet_neHEF", Jet_neHEF, &b_Jet_neHEF);
   fChain->SetBranchAddress("Jet_phi", Jet_phi, &b_Jet_phi);
   fChain->SetBranchAddress("Jet_pt", Jet_pt, &b_Jet_pt);
   fChain->SetBranchAddress("Jet_rawFactor", Jet_rawFactor, &b_Jet_rawFactor);
   fChain->SetBranchAddress("nTau", &nTau, &b_nTau);
   fChain->SetBranchAddress("Tau_decayMode", Tau_decayMode, &b_Tau_decayMode);
   fChain->SetBranchAddress("Tau_idAntiEleDeadECal", Tau_idAntiEleDeadECal, &b_Tau_idAntiEleDeadECal);
   fChain->SetBranchAddress("Tau_idAntiMu", Tau_idAntiMu, &b_Tau_idAntiMu);
   fChain->SetBranchAddress("Tau_idDecayModeNewDMs", Tau_idDecayModeNewDMs, &b_Tau_idDecayModeNewDMs);
   fChain->SetBranchAddress("Tau_idDecayModeOldDMs", Tau_idDecayModeOldDMs, &b_Tau_idDecayModeOldDMs);
   fChain->SetBranchAddress("Tau_idDeepTau2017v2p1VSe", Tau_idDeepTau2017v2p1VSe, &b_Tau_idDeepTau2017v2p1VSe);
   fChain->SetBranchAddress("Tau_idDeepTau2017v2p1VSjet", Tau_idDeepTau2017v2p1VSjet, &b_Tau_idDeepTau2017v2p1VSjet);
   fChain->SetBranchAddress("Tau_idDeepTau2017v2p1VSmu", Tau_idDeepTau2017v2p1VSmu, &b_Tau_idDeepTau2017v2p1VSmu);
   fChain->SetBranchAddress("Tau_idDeepTau2018v2p5VSe", Tau_idDeepTau2018v2p5VSe, &b_Tau_idDeepTau2018v2p5VSe);
   fChain->SetBranchAddress("Tau_idDeepTau2018v2p5VSjet", Tau_idDeepTau2018v2p5VSjet, &b_Tau_idDeepTau2018v2p5VSjet);
   fChain->SetBranchAddress("Tau_idDeepTau2018v2p5VSmu", Tau_idDeepTau2018v2p5VSmu, &b_Tau_idDeepTau2018v2p5VSmu);
   fChain->SetBranchAddress("Tau_nSVs", Tau_nSVs, &b_Tau_nSVs);
   fChain->SetBranchAddress("Tau_charge", Tau_charge, &b_Tau_charge);
   fChain->SetBranchAddress("Tau_decayModePNet", Tau_decayModePNet, &b_Tau_decayModePNet);
   fChain->SetBranchAddress("Tau_eleIdx", Tau_eleIdx, &b_Tau_eleIdx);
   fChain->SetBranchAddress("Tau_jetIdx", Tau_jetIdx, &b_Tau_jetIdx);
   fChain->SetBranchAddress("Tau_muIdx", Tau_muIdx, &b_Tau_muIdx);
   fChain->SetBranchAddress("Tau_svIdx1", Tau_svIdx1, &b_Tau_svIdx1);
   fChain->SetBranchAddress("Tau_svIdx2", Tau_svIdx2, &b_Tau_svIdx2);
   fChain->SetBranchAddress("Tau_chargedIso", Tau_chargedIso, &b_Tau_chargedIso);
   fChain->SetBranchAddress("Tau_dxy", Tau_dxy, &b_Tau_dxy);
   fChain->SetBranchAddress("Tau_dz", Tau_dz, &b_Tau_dz);
   fChain->SetBranchAddress("Tau_eta", Tau_eta, &b_Tau_eta);
   fChain->SetBranchAddress("Tau_leadTkDeltaEta", Tau_leadTkDeltaEta, &b_Tau_leadTkDeltaEta);
   fChain->SetBranchAddress("Tau_leadTkDeltaPhi", Tau_leadTkDeltaPhi, &b_Tau_leadTkDeltaPhi);
   fChain->SetBranchAddress("Tau_leadTkPtOverTauPt", Tau_leadTkPtOverTauPt, &b_Tau_leadTkPtOverTauPt);
   fChain->SetBranchAddress("Tau_mass", Tau_mass, &b_Tau_mass);
   fChain->SetBranchAddress("Tau_neutralIso", Tau_neutralIso, &b_Tau_neutralIso);
   fChain->SetBranchAddress("Tau_phi", Tau_phi, &b_Tau_phi);
   fChain->SetBranchAddress("Tau_photonsOutsideSignalCone", Tau_photonsOutsideSignalCone, &b_Tau_photonsOutsideSignalCone);
   fChain->SetBranchAddress("Tau_probDM0PNet", Tau_probDM0PNet, &b_Tau_probDM0PNet);
   fChain->SetBranchAddress("Tau_probDM10PNet", Tau_probDM10PNet, &b_Tau_probDM10PNet);
   fChain->SetBranchAddress("Tau_probDM11PNet", Tau_probDM11PNet, &b_Tau_probDM11PNet);
   fChain->SetBranchAddress("Tau_probDM1PNet", Tau_probDM1PNet, &b_Tau_probDM1PNet);
   fChain->SetBranchAddress("Tau_probDM2PNet", Tau_probDM2PNet, &b_Tau_probDM2PNet);
   fChain->SetBranchAddress("Tau_pt", Tau_pt, &b_Tau_pt);
   fChain->SetBranchAddress("Tau_ptCorrPNet", Tau_ptCorrPNet, &b_Tau_ptCorrPNet);
   fChain->SetBranchAddress("Tau_puCorr", Tau_puCorr, &b_Tau_puCorr);
   fChain->SetBranchAddress("Tau_qConfPNet", Tau_qConfPNet, &b_Tau_qConfPNet);
   fChain->SetBranchAddress("Tau_rawDeepTau2017v2p1VSe", Tau_rawDeepTau2017v2p1VSe, &b_Tau_rawDeepTau2017v2p1VSe);
   fChain->SetBranchAddress("Tau_rawDeepTau2017v2p1VSjet", Tau_rawDeepTau2017v2p1VSjet, &b_Tau_rawDeepTau2017v2p1VSjet);
   fChain->SetBranchAddress("Tau_rawDeepTau2017v2p1VSmu", Tau_rawDeepTau2017v2p1VSmu, &b_Tau_rawDeepTau2017v2p1VSmu);
   fChain->SetBranchAddress("Tau_rawDeepTau2018v2p5VSe", Tau_rawDeepTau2018v2p5VSe, &b_Tau_rawDeepTau2018v2p5VSe);
   fChain->SetBranchAddress("Tau_rawDeepTau2018v2p5VSjet", Tau_rawDeepTau2018v2p5VSjet, &b_Tau_rawDeepTau2018v2p5VSjet);
   fChain->SetBranchAddress("Tau_rawDeepTau2018v2p5VSmu", Tau_rawDeepTau2018v2p5VSmu, &b_Tau_rawDeepTau2018v2p5VSmu);
   fChain->SetBranchAddress("Tau_rawIso", Tau_rawIso, &b_Tau_rawIso);
   fChain->SetBranchAddress("Tau_rawIsodR03", Tau_rawIsodR03, &b_Tau_rawIsodR03);
   fChain->SetBranchAddress("Tau_rawPNetVSe", Tau_rawPNetVSe, &b_Tau_rawPNetVSe);
   fChain->SetBranchAddress("Tau_rawPNetVSjet", Tau_rawPNetVSjet, &b_Tau_rawPNetVSjet);
   fChain->SetBranchAddress("Tau_rawPNetVSmu", Tau_rawPNetVSmu, &b_Tau_rawPNetVSmu);
   fChain->SetBranchAddress("TkMET_phi", &TkMET_phi, &b_TkMET_phi);
   fChain->SetBranchAddress("TkMET_pt", &TkMET_pt, &b_TkMET_pt);
   fChain->SetBranchAddress("TkMET_sumEt", &TkMET_sumEt, &b_TkMET_sumEt);
   fChain->SetBranchAddress("nTrigObj", &nTrigObj, &b_nTrigObj);
   fChain->SetBranchAddress("TrigObj_l1charge", TrigObj_l1charge, &b_TrigObj_l1charge);
   fChain->SetBranchAddress("TrigObj_id", TrigObj_id, &b_TrigObj_id);
   fChain->SetBranchAddress("TrigObj_l1iso", TrigObj_l1iso, &b_TrigObj_l1iso);
   fChain->SetBranchAddress("TrigObj_filterBits", TrigObj_filterBits, &b_TrigObj_filterBits);
   fChain->SetBranchAddress("TrigObj_pt", TrigObj_pt, &b_TrigObj_pt);
   fChain->SetBranchAddress("TrigObj_eta", TrigObj_eta, &b_TrigObj_eta);
   fChain->SetBranchAddress("TrigObj_phi", TrigObj_phi, &b_TrigObj_phi);
   fChain->SetBranchAddress("TrigObj_l1pt", TrigObj_l1pt, &b_TrigObj_l1pt);
   fChain->SetBranchAddress("TrigObj_l1pt_2", TrigObj_l1pt_2, &b_TrigObj_l1pt_2);
   fChain->SetBranchAddress("TrigObj_l2pt", TrigObj_l2pt, &b_TrigObj_l2pt);
   fChain->SetBranchAddress("genTtbarId", &genTtbarId, &b_genTtbarId);
   fChain->SetBranchAddress("nOtherPV", &nOtherPV, &b_nOtherPV);
   fChain->SetBranchAddress("OtherPV_z", OtherPV_z, &b_OtherPV_z);
   fChain->SetBranchAddress("OtherPV_score", OtherPV_score, &b_OtherPV_score);
   fChain->SetBranchAddress("PV_npvs", &PV_npvs, &b_PV_npvs);
   fChain->SetBranchAddress("PV_npvsGood", &PV_npvsGood, &b_PV_npvsGood);
   fChain->SetBranchAddress("PV_ndof", &PV_ndof, &b_PV_ndof);
   fChain->SetBranchAddress("PV_x", &PV_x, &b_PV_x);
   fChain->SetBranchAddress("PV_y", &PV_y, &b_PV_y);
   fChain->SetBranchAddress("PV_z", &PV_z, &b_PV_z);
   fChain->SetBranchAddress("PV_chi2", &PV_chi2, &b_PV_chi2);
   fChain->SetBranchAddress("PV_score", &PV_score, &b_PV_score);
   fChain->SetBranchAddress("nSV", &nSV, &b_nSV);
   fChain->SetBranchAddress("SV_charge", SV_charge, &b_SV_charge);
   fChain->SetBranchAddress("SV_dlen", SV_dlen, &b_SV_dlen);
   fChain->SetBranchAddress("SV_dlenSig", SV_dlenSig, &b_SV_dlenSig);
   fChain->SetBranchAddress("SV_dxy", SV_dxy, &b_SV_dxy);
   fChain->SetBranchAddress("SV_dxySig", SV_dxySig, &b_SV_dxySig);
   fChain->SetBranchAddress("SV_pAngle", SV_pAngle, &b_SV_pAngle);
   fChain->SetBranchAddress("boostedTau_genPartFlav", boostedTau_genPartFlav, &b_boostedTau_genPartFlav);
   fChain->SetBranchAddress("boostedTau_genPartIdx", boostedTau_genPartIdx, &b_boostedTau_genPartIdx);
   fChain->SetBranchAddress("Electron_genPartFlav", Electron_genPartFlav, &b_Electron_genPartFlav);
   fChain->SetBranchAddress("Electron_genPartIdx", Electron_genPartIdx, &b_Electron_genPartIdx);
   fChain->SetBranchAddress("FatJet_hadronFlavour", FatJet_hadronFlavour, &b_FatJet_hadronFlavour);
   fChain->SetBranchAddress("FatJet_nBHadrons", FatJet_nBHadrons, &b_FatJet_nBHadrons);
   fChain->SetBranchAddress("FatJet_nCHadrons", FatJet_nCHadrons, &b_FatJet_nCHadrons);
   fChain->SetBranchAddress("FatJet_genJetAK8Idx", FatJet_genJetAK8Idx, &b_FatJet_genJetAK8Idx);
   fChain->SetBranchAddress("GenJetAK8_hadronFlavour", GenJetAK8_hadronFlavour, &b_GenJetAK8_hadronFlavour);
   fChain->SetBranchAddress("GenJetAK8_partonFlavour", GenJetAK8_partonFlavour, &b_GenJetAK8_partonFlavour);
   fChain->SetBranchAddress("GenJet_hadronFlavour", GenJet_hadronFlavour, &b_GenJet_hadronFlavour);
   fChain->SetBranchAddress("GenJet_partonFlavour", GenJet_partonFlavour, &b_GenJet_partonFlavour);
   fChain->SetBranchAddress("GenVtx_t0", &GenVtx_t0, &b_GenVtx_t0);
   fChain->SetBranchAddress("Jet_hadronFlavour", Jet_hadronFlavour, &b_Jet_hadronFlavour);
   fChain->SetBranchAddress("Jet_genJetIdx", Jet_genJetIdx, &b_Jet_genJetIdx);
   fChain->SetBranchAddress("Jet_partonFlavour", Jet_partonFlavour, &b_Jet_partonFlavour);
   fChain->SetBranchAddress("LowPtElectron_genPartFlav", LowPtElectron_genPartFlav, &b_LowPtElectron_genPartFlav);
   fChain->SetBranchAddress("LowPtElectron_genPartIdx", LowPtElectron_genPartIdx, &b_LowPtElectron_genPartIdx);
   fChain->SetBranchAddress("Muon_genPartFlav", Muon_genPartFlav, &b_Muon_genPartFlav);
   fChain->SetBranchAddress("Muon_genPartIdx", Muon_genPartIdx, &b_Muon_genPartIdx);
   fChain->SetBranchAddress("Photon_genPartFlav", Photon_genPartFlav, &b_Photon_genPartFlav);
   fChain->SetBranchAddress("Photon_genPartIdx", Photon_genPartIdx, &b_Photon_genPartIdx);
   fChain->SetBranchAddress("MET_fiducialGenPhi", &MET_fiducialGenPhi, &b_MET_fiducialGenPhi);
   fChain->SetBranchAddress("MET_fiducialGenPt", &MET_fiducialGenPt, &b_MET_fiducialGenPt);
   fChain->SetBranchAddress("SubJet_hadronFlavour", SubJet_hadronFlavour, &b_SubJet_hadronFlavour);
   fChain->SetBranchAddress("SubJet_nBHadrons", SubJet_nBHadrons, &b_SubJet_nBHadrons);
   fChain->SetBranchAddress("SubJet_nCHadrons", SubJet_nCHadrons, &b_SubJet_nCHadrons);
   fChain->SetBranchAddress("SV_ntracks", SV_ntracks, &b_SV_ntracks);
   fChain->SetBranchAddress("SV_chi2", SV_chi2, &b_SV_chi2);
   fChain->SetBranchAddress("SV_eta", SV_eta, &b_SV_eta);
   fChain->SetBranchAddress("SV_mass", SV_mass, &b_SV_mass);
   fChain->SetBranchAddress("SV_ndof", SV_ndof, &b_SV_ndof);
   fChain->SetBranchAddress("SV_phi", SV_phi, &b_SV_phi);
   fChain->SetBranchAddress("SV_pt", SV_pt, &b_SV_pt);
   fChain->SetBranchAddress("SV_x", SV_x, &b_SV_x);
   fChain->SetBranchAddress("SV_y", SV_y, &b_SV_y);
   fChain->SetBranchAddress("SV_z", SV_z, &b_SV_z);
   fChain->SetBranchAddress("Tau_genPartFlav", Tau_genPartFlav, &b_Tau_genPartFlav);
   fChain->SetBranchAddress("Tau_genPartIdx", Tau_genPartIdx, &b_Tau_genPartIdx);
   fChain->SetBranchAddress("L1_AlwaysTrue", &L1_AlwaysTrue, &b_L1_AlwaysTrue);
   fChain->SetBranchAddress("L1_BPTX_AND_Ref1_VME", &L1_BPTX_AND_Ref1_VME, &b_L1_BPTX_AND_Ref1_VME);
   fChain->SetBranchAddress("L1_BPTX_AND_Ref3_VME", &L1_BPTX_AND_Ref3_VME, &b_L1_BPTX_AND_Ref3_VME);
   fChain->SetBranchAddress("L1_BPTX_AND_Ref4_VME", &L1_BPTX_AND_Ref4_VME, &b_L1_BPTX_AND_Ref4_VME);
   fChain->SetBranchAddress("L1_BPTX_BeamGas_B1_VME", &L1_BPTX_BeamGas_B1_VME, &b_L1_BPTX_BeamGas_B1_VME);
   fChain->SetBranchAddress("L1_BPTX_BeamGas_B2_VME", &L1_BPTX_BeamGas_B2_VME, &b_L1_BPTX_BeamGas_B2_VME);
   fChain->SetBranchAddress("L1_BPTX_BeamGas_Ref1_VME", &L1_BPTX_BeamGas_Ref1_VME, &b_L1_BPTX_BeamGas_Ref1_VME);
   fChain->SetBranchAddress("L1_BPTX_BeamGas_Ref2_VME", &L1_BPTX_BeamGas_Ref2_VME, &b_L1_BPTX_BeamGas_Ref2_VME);
   fChain->SetBranchAddress("L1_BPTX_NotOR_VME", &L1_BPTX_NotOR_VME, &b_L1_BPTX_NotOR_VME);
   fChain->SetBranchAddress("L1_BPTX_OR_Ref3_VME", &L1_BPTX_OR_Ref3_VME, &b_L1_BPTX_OR_Ref3_VME);
   fChain->SetBranchAddress("L1_BPTX_OR_Ref4_VME", &L1_BPTX_OR_Ref4_VME, &b_L1_BPTX_OR_Ref4_VME);
   fChain->SetBranchAddress("L1_BPTX_RefAND_VME", &L1_BPTX_RefAND_VME, &b_L1_BPTX_RefAND_VME);
   fChain->SetBranchAddress("L1_BptxMinus", &L1_BptxMinus, &b_L1_BptxMinus);
   fChain->SetBranchAddress("L1_BptxOR", &L1_BptxOR, &b_L1_BptxOR);
   fChain->SetBranchAddress("L1_BptxPlus", &L1_BptxPlus, &b_L1_BptxPlus);
   fChain->SetBranchAddress("L1_BptxXOR", &L1_BptxXOR, &b_L1_BptxXOR);
   fChain->SetBranchAddress("L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142", &L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142, &b_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142);
   fChain->SetBranchAddress("L1_DoubleEG10_er1p2_dR_Max0p6", &L1_DoubleEG10_er1p2_dR_Max0p6, &b_L1_DoubleEG10_er1p2_dR_Max0p6);
   fChain->SetBranchAddress("L1_DoubleEG10p5_er1p2_dR_Max0p6", &L1_DoubleEG10p5_er1p2_dR_Max0p6, &b_L1_DoubleEG10p5_er1p2_dR_Max0p6);
   fChain->SetBranchAddress("L1_DoubleEG11_er1p2_dR_Max0p6", &L1_DoubleEG11_er1p2_dR_Max0p6, &b_L1_DoubleEG11_er1p2_dR_Max0p6);
   fChain->SetBranchAddress("L1_DoubleEG4_er1p2_dR_Max0p9", &L1_DoubleEG4_er1p2_dR_Max0p9, &b_L1_DoubleEG4_er1p2_dR_Max0p9);
   fChain->SetBranchAddress("L1_DoubleEG4p5_er1p2_dR_Max0p9", &L1_DoubleEG4p5_er1p2_dR_Max0p9, &b_L1_DoubleEG4p5_er1p2_dR_Max0p9);
   fChain->SetBranchAddress("L1_DoubleEG5_er1p2_dR_Max0p9", &L1_DoubleEG5_er1p2_dR_Max0p9, &b_L1_DoubleEG5_er1p2_dR_Max0p9);
   fChain->SetBranchAddress("L1_DoubleEG5p5_er1p2_dR_Max0p8", &L1_DoubleEG5p5_er1p2_dR_Max0p8, &b_L1_DoubleEG5p5_er1p2_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleEG6_er1p2_dR_Max0p8", &L1_DoubleEG6_er1p2_dR_Max0p8, &b_L1_DoubleEG6_er1p2_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleEG6p5_er1p2_dR_Max0p8", &L1_DoubleEG6p5_er1p2_dR_Max0p8, &b_L1_DoubleEG6p5_er1p2_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleEG7_er1p2_dR_Max0p8", &L1_DoubleEG7_er1p2_dR_Max0p8, &b_L1_DoubleEG7_er1p2_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleEG7p5_er1p2_dR_Max0p7", &L1_DoubleEG7p5_er1p2_dR_Max0p7, &b_L1_DoubleEG7p5_er1p2_dR_Max0p7);
   fChain->SetBranchAddress("L1_DoubleEG8_er1p2_dR_Max0p7", &L1_DoubleEG8_er1p2_dR_Max0p7, &b_L1_DoubleEG8_er1p2_dR_Max0p7);
   fChain->SetBranchAddress("L1_DoubleEG8er2p5_HTT260er", &L1_DoubleEG8er2p5_HTT260er, &b_L1_DoubleEG8er2p5_HTT260er);
   fChain->SetBranchAddress("L1_DoubleEG8er2p5_HTT280er", &L1_DoubleEG8er2p5_HTT280er, &b_L1_DoubleEG8er2p5_HTT280er);
   fChain->SetBranchAddress("L1_DoubleEG8er2p5_HTT300er", &L1_DoubleEG8er2p5_HTT300er, &b_L1_DoubleEG8er2p5_HTT300er);
   fChain->SetBranchAddress("L1_DoubleEG8er2p5_HTT320er", &L1_DoubleEG8er2p5_HTT320er, &b_L1_DoubleEG8er2p5_HTT320er);
   fChain->SetBranchAddress("L1_DoubleEG8er2p5_HTT340er", &L1_DoubleEG8er2p5_HTT340er, &b_L1_DoubleEG8er2p5_HTT340er);
   fChain->SetBranchAddress("L1_DoubleEG8p5_er1p2_dR_Max0p7", &L1_DoubleEG8p5_er1p2_dR_Max0p7, &b_L1_DoubleEG8p5_er1p2_dR_Max0p7);
   fChain->SetBranchAddress("L1_DoubleEG9_er1p2_dR_Max0p7", &L1_DoubleEG9_er1p2_dR_Max0p7, &b_L1_DoubleEG9_er1p2_dR_Max0p7);
   fChain->SetBranchAddress("L1_DoubleEG9p5_er1p2_dR_Max0p6", &L1_DoubleEG9p5_er1p2_dR_Max0p6, &b_L1_DoubleEG9p5_er1p2_dR_Max0p6);
   fChain->SetBranchAddress("L1_DoubleEG_15_10_er2p5", &L1_DoubleEG_15_10_er2p5, &b_L1_DoubleEG_15_10_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_20_10_er2p5", &L1_DoubleEG_20_10_er2p5, &b_L1_DoubleEG_20_10_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_22_10_er2p5", &L1_DoubleEG_22_10_er2p5, &b_L1_DoubleEG_22_10_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_25_12_er2p5", &L1_DoubleEG_25_12_er2p5, &b_L1_DoubleEG_25_12_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_25_14_er2p5", &L1_DoubleEG_25_14_er2p5, &b_L1_DoubleEG_25_14_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_27_14_er2p5", &L1_DoubleEG_27_14_er2p5, &b_L1_DoubleEG_27_14_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso16_LooseIso12_er1p5", &L1_DoubleEG_LooseIso16_LooseIso12_er1p5, &b_L1_DoubleEG_LooseIso16_LooseIso12_er1p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso18_LooseIso12_er1p5", &L1_DoubleEG_LooseIso18_LooseIso12_er1p5, &b_L1_DoubleEG_LooseIso18_LooseIso12_er1p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso20_LooseIso12_er1p5", &L1_DoubleEG_LooseIso20_LooseIso12_er1p5, &b_L1_DoubleEG_LooseIso20_LooseIso12_er1p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso22_12_er2p5", &L1_DoubleEG_LooseIso22_12_er2p5, &b_L1_DoubleEG_LooseIso22_12_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso22_LooseIso12_er1p5", &L1_DoubleEG_LooseIso22_LooseIso12_er1p5, &b_L1_DoubleEG_LooseIso22_LooseIso12_er1p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso25_12_er2p5", &L1_DoubleEG_LooseIso25_12_er2p5, &b_L1_DoubleEG_LooseIso25_12_er2p5);
   fChain->SetBranchAddress("L1_DoubleEG_LooseIso25_LooseIso12_er1p5", &L1_DoubleEG_LooseIso25_LooseIso12_er1p5, &b_L1_DoubleEG_LooseIso25_LooseIso12_er1p5);
   fChain->SetBranchAddress("L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5", &L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5, &b_L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5);
   fChain->SetBranchAddress("L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5", &L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5, &b_L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5);
   fChain->SetBranchAddress("L1_DoubleIsoTau28er2p1", &L1_DoubleIsoTau28er2p1, &b_L1_DoubleIsoTau28er2p1);
   fChain->SetBranchAddress("L1_DoubleIsoTau28er2p1_Mass_Max80", &L1_DoubleIsoTau28er2p1_Mass_Max80, &b_L1_DoubleIsoTau28er2p1_Mass_Max80);
   fChain->SetBranchAddress("L1_DoubleIsoTau28er2p1_Mass_Max90", &L1_DoubleIsoTau28er2p1_Mass_Max90, &b_L1_DoubleIsoTau28er2p1_Mass_Max90);
   fChain->SetBranchAddress("L1_DoubleIsoTau30er2p1", &L1_DoubleIsoTau30er2p1, &b_L1_DoubleIsoTau30er2p1);
   fChain->SetBranchAddress("L1_DoubleIsoTau30er2p1_Mass_Max80", &L1_DoubleIsoTau30er2p1_Mass_Max80, &b_L1_DoubleIsoTau30er2p1_Mass_Max80);
   fChain->SetBranchAddress("L1_DoubleIsoTau30er2p1_Mass_Max90", &L1_DoubleIsoTau30er2p1_Mass_Max90, &b_L1_DoubleIsoTau30er2p1_Mass_Max90);
   fChain->SetBranchAddress("L1_DoubleIsoTau32er2p1", &L1_DoubleIsoTau32er2p1, &b_L1_DoubleIsoTau32er2p1);
   fChain->SetBranchAddress("L1_DoubleIsoTau32er2p1_Mass_Max80", &L1_DoubleIsoTau32er2p1_Mass_Max80, &b_L1_DoubleIsoTau32er2p1_Mass_Max80);
   fChain->SetBranchAddress("L1_DoubleIsoTau34er2p1", &L1_DoubleIsoTau34er2p1, &b_L1_DoubleIsoTau34er2p1);
   fChain->SetBranchAddress("L1_DoubleIsoTau35er2p1", &L1_DoubleIsoTau35er2p1, &b_L1_DoubleIsoTau35er2p1);
   fChain->SetBranchAddress("L1_DoubleIsoTau36er2p1", &L1_DoubleIsoTau36er2p1, &b_L1_DoubleIsoTau36er2p1);
   fChain->SetBranchAddress("L1_DoubleJet100er2p3_dEta_Max1p6", &L1_DoubleJet100er2p3_dEta_Max1p6, &b_L1_DoubleJet100er2p3_dEta_Max1p6);
   fChain->SetBranchAddress("L1_DoubleJet100er2p5", &L1_DoubleJet100er2p5, &b_L1_DoubleJet100er2p5);
   fChain->SetBranchAddress("L1_DoubleJet112er2p3_dEta_Max1p6", &L1_DoubleJet112er2p3_dEta_Max1p6, &b_L1_DoubleJet112er2p3_dEta_Max1p6);
   fChain->SetBranchAddress("L1_DoubleJet120er2p5", &L1_DoubleJet120er2p5, &b_L1_DoubleJet120er2p5);
   fChain->SetBranchAddress("L1_DoubleJet120er2p5_Mu3_dR_Max0p8", &L1_DoubleJet120er2p5_Mu3_dR_Max0p8, &b_L1_DoubleJet120er2p5_Mu3_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleJet150er2p5", &L1_DoubleJet150er2p5, &b_L1_DoubleJet150er2p5);
   fChain->SetBranchAddress("L1_DoubleJet16er2p5_Mu3_dR_Max0p4", &L1_DoubleJet16er2p5_Mu3_dR_Max0p4, &b_L1_DoubleJet16er2p5_Mu3_dR_Max0p4);
   fChain->SetBranchAddress("L1_DoubleJet30er2p5_Mass_Min225_dEta_Max1p5", &L1_DoubleJet30er2p5_Mass_Min225_dEta_Max1p5, &b_L1_DoubleJet30er2p5_Mass_Min225_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleJet30er2p5_Mass_Min250_dEta_Max1p5", &L1_DoubleJet30er2p5_Mass_Min250_dEta_Max1p5, &b_L1_DoubleJet30er2p5_Mass_Min250_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5", &L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5, &b_L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5", &L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5, &b_L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5", &L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5, &b_L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleJet35_Mass_Min450_IsoTau45_RmOvlp", &L1_DoubleJet35_Mass_Min450_IsoTau45_RmOvlp, &b_L1_DoubleJet35_Mass_Min450_IsoTau45_RmOvlp);
   fChain->SetBranchAddress("L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5", &L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5, &b_L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5);
   fChain->SetBranchAddress("L1_DoubleJet35er2p5_Mu3_dR_Max0p4", &L1_DoubleJet35er2p5_Mu3_dR_Max0p4, &b_L1_DoubleJet35er2p5_Mu3_dR_Max0p4);
   fChain->SetBranchAddress("L1_DoubleJet40_Mass_Min450_IsoEG10er2p1_RmOvlp_dR0p2", &L1_DoubleJet40_Mass_Min450_IsoEG10er2p1_RmOvlp_dR0p2, &b_L1_DoubleJet40_Mass_Min450_IsoEG10er2p1_RmOvlp_dR0p2);
   fChain->SetBranchAddress("L1_DoubleJet40_Mass_Min450_LooseIsoEG15er2p1_RmOvlp_dR0p2", &L1_DoubleJet40_Mass_Min450_LooseIsoEG15er2p1_RmOvlp_dR0p2, &b_L1_DoubleJet40_Mass_Min450_LooseIsoEG15er2p1_RmOvlp_dR0p2);
   fChain->SetBranchAddress("L1_DoubleJet40er2p5", &L1_DoubleJet40er2p5, &b_L1_DoubleJet40er2p5);
   fChain->SetBranchAddress("L1_DoubleJet45_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5", &L1_DoubleJet45_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5, &b_L1_DoubleJet45_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5);
   fChain->SetBranchAddress("L1_DoubleJet45_Mass_Min450_LooseIsoEG20er2p1_RmOvlp_dR0p2", &L1_DoubleJet45_Mass_Min450_LooseIsoEG20er2p1_RmOvlp_dR0p2, &b_L1_DoubleJet45_Mass_Min450_LooseIsoEG20er2p1_RmOvlp_dR0p2);
   fChain->SetBranchAddress("L1_DoubleJet60er2p5_Mu3_dR_Max0p4", &L1_DoubleJet60er2p5_Mu3_dR_Max0p4, &b_L1_DoubleJet60er2p5_Mu3_dR_Max0p4);
   fChain->SetBranchAddress("L1_DoubleJet80er2p5_Mu3_dR_Max0p4", &L1_DoubleJet80er2p5_Mu3_dR_Max0p4, &b_L1_DoubleJet80er2p5_Mu3_dR_Max0p4);
   fChain->SetBranchAddress("L1_DoubleJet_100_30_DoubleJet30_Mass_Min620", &L1_DoubleJet_100_30_DoubleJet30_Mass_Min620, &b_L1_DoubleJet_100_30_DoubleJet30_Mass_Min620);
   fChain->SetBranchAddress("L1_DoubleJet_100_30_DoubleJet30_Mass_Min800", &L1_DoubleJet_100_30_DoubleJet30_Mass_Min800, &b_L1_DoubleJet_100_30_DoubleJet30_Mass_Min800);
   fChain->SetBranchAddress("L1_DoubleJet_110_35_DoubleJet35_Mass_Min620", &L1_DoubleJet_110_35_DoubleJet35_Mass_Min620, &b_L1_DoubleJet_110_35_DoubleJet35_Mass_Min620);
   fChain->SetBranchAddress("L1_DoubleJet_110_35_DoubleJet35_Mass_Min800", &L1_DoubleJet_110_35_DoubleJet35_Mass_Min800, &b_L1_DoubleJet_110_35_DoubleJet35_Mass_Min800);
   fChain->SetBranchAddress("L1_DoubleJet_115_40_DoubleJet40_Mass_Min620", &L1_DoubleJet_115_40_DoubleJet40_Mass_Min620, &b_L1_DoubleJet_115_40_DoubleJet40_Mass_Min620);
   fChain->SetBranchAddress("L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28", &L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28, &b_L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28);
   fChain->SetBranchAddress("L1_DoubleJet_120_45_DoubleJet45_Mass_Min620", &L1_DoubleJet_120_45_DoubleJet45_Mass_Min620, &b_L1_DoubleJet_120_45_DoubleJet45_Mass_Min620);
   fChain->SetBranchAddress("L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28", &L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28, &b_L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28);
   fChain->SetBranchAddress("L1_DoubleJet_60_30_DoubleJet30_Mass_Min500_DoubleJetCentral50", &L1_DoubleJet_60_30_DoubleJet30_Mass_Min500_DoubleJetCentral50, &b_L1_DoubleJet_60_30_DoubleJet30_Mass_Min500_DoubleJetCentral50);
   fChain->SetBranchAddress("L1_DoubleJet_65_30_DoubleJet30_Mass_Min400_ETMHF65", &L1_DoubleJet_65_30_DoubleJet30_Mass_Min400_ETMHF65, &b_L1_DoubleJet_65_30_DoubleJet30_Mass_Min400_ETMHF65);
   fChain->SetBranchAddress("L1_DoubleJet_65_35_DoubleJet35_Mass_Min500_DoubleJetCentral50", &L1_DoubleJet_65_35_DoubleJet35_Mass_Min500_DoubleJetCentral50, &b_L1_DoubleJet_65_35_DoubleJet35_Mass_Min500_DoubleJetCentral50);
   fChain->SetBranchAddress("L1_DoubleJet_70_35_DoubleJet35_Mass_Min400_ETMHF65", &L1_DoubleJet_70_35_DoubleJet35_Mass_Min400_ETMHF65, &b_L1_DoubleJet_70_35_DoubleJet35_Mass_Min400_ETMHF65);
   fChain->SetBranchAddress("L1_DoubleJet_80_30_DoubleJet30_Mass_Min500_Mu3OQ", &L1_DoubleJet_80_30_DoubleJet30_Mass_Min500_Mu3OQ, &b_L1_DoubleJet_80_30_DoubleJet30_Mass_Min500_Mu3OQ);
   fChain->SetBranchAddress("L1_DoubleJet_80_30_Mass_Min420_DoubleMu0_SQ", &L1_DoubleJet_80_30_Mass_Min420_DoubleMu0_SQ, &b_L1_DoubleJet_80_30_Mass_Min420_DoubleMu0_SQ);
   fChain->SetBranchAddress("L1_DoubleJet_80_30_Mass_Min420_IsoTau40_RmOvlp", &L1_DoubleJet_80_30_Mass_Min420_IsoTau40_RmOvlp, &b_L1_DoubleJet_80_30_Mass_Min420_IsoTau40_RmOvlp);
   fChain->SetBranchAddress("L1_DoubleJet_80_30_Mass_Min420_Mu8", &L1_DoubleJet_80_30_Mass_Min420_Mu8, &b_L1_DoubleJet_80_30_Mass_Min420_Mu8);
   fChain->SetBranchAddress("L1_DoubleJet_85_35_DoubleJet35_Mass_Min500_Mu3OQ", &L1_DoubleJet_85_35_DoubleJet35_Mass_Min500_Mu3OQ, &b_L1_DoubleJet_85_35_DoubleJet35_Mass_Min500_Mu3OQ);
   fChain->SetBranchAddress("L1_DoubleJet_90_30_DoubleJet30_Mass_Min620", &L1_DoubleJet_90_30_DoubleJet30_Mass_Min620, &b_L1_DoubleJet_90_30_DoubleJet30_Mass_Min620);
   fChain->SetBranchAddress("L1_DoubleJet_90_30_DoubleJet30_Mass_Min800", &L1_DoubleJet_90_30_DoubleJet30_Mass_Min800, &b_L1_DoubleJet_90_30_DoubleJet30_Mass_Min800);
   fChain->SetBranchAddress("L1_DoubleLLPJet40", &L1_DoubleLLPJet40, &b_L1_DoubleLLPJet40);
   fChain->SetBranchAddress("L1_DoubleLooseIsoEG22er2p1", &L1_DoubleLooseIsoEG22er2p1, &b_L1_DoubleLooseIsoEG22er2p1);
   fChain->SetBranchAddress("L1_DoubleLooseIsoEG24er2p1", &L1_DoubleLooseIsoEG24er2p1, &b_L1_DoubleLooseIsoEG24er2p1);
   fChain->SetBranchAddress("L1_DoubleMu0", &L1_DoubleMu0, &b_L1_DoubleMu0);
   fChain->SetBranchAddress("L1_DoubleMu0_Mass_Min1", &L1_DoubleMu0_Mass_Min1, &b_L1_DoubleMu0_Mass_Min1);
   fChain->SetBranchAddress("L1_DoubleMu0_OQ", &L1_DoubleMu0_OQ, &b_L1_DoubleMu0_OQ);
   fChain->SetBranchAddress("L1_DoubleMu0_SQ", &L1_DoubleMu0_SQ, &b_L1_DoubleMu0_SQ);
   fChain->SetBranchAddress("L1_DoubleMu0_SQ_OS", &L1_DoubleMu0_SQ_OS, &b_L1_DoubleMu0_SQ_OS);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt15_Upt7", &L1_DoubleMu0_Upt15_Upt7, &b_L1_DoubleMu0_Upt15_Upt7);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt15_Upt7_BMTF_EMTF", &L1_DoubleMu0_Upt15_Upt7_BMTF_EMTF, &b_L1_DoubleMu0_Upt15_Upt7_BMTF_EMTF);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt5_Upt5", &L1_DoubleMu0_Upt5_Upt5, &b_L1_DoubleMu0_Upt5_Upt5);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt5_Upt5_BMTF_EMTF", &L1_DoubleMu0_Upt5_Upt5_BMTF_EMTF, &b_L1_DoubleMu0_Upt5_Upt5_BMTF_EMTF);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt6_IP_Min1_Upt4", &L1_DoubleMu0_Upt6_IP_Min1_Upt4, &b_L1_DoubleMu0_Upt6_IP_Min1_Upt4);
   fChain->SetBranchAddress("L1_DoubleMu0_Upt6_IP_Min1_Upt4_BMTF_EMTF", &L1_DoubleMu0_Upt6_IP_Min1_Upt4_BMTF_EMTF, &b_L1_DoubleMu0_Upt6_IP_Min1_Upt4_BMTF_EMTF);
   fChain->SetBranchAddress("L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8", &L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8, &b_L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6", &L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6, &b_L1_DoubleMu0er1p4_OQ_OS_dEta_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2", &L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2, &b_L1_DoubleMu0er1p4_SQ_OS_dEta_Max1p2);
   fChain->SetBranchAddress("L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4", &L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4, &b_L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4);
   fChain->SetBranchAddress("L1_DoubleMu0er1p5_SQ", &L1_DoubleMu0er1p5_SQ, &b_L1_DoubleMu0er1p5_SQ);
   fChain->SetBranchAddress("L1_DoubleMu0er1p5_SQ_OS", &L1_DoubleMu0er1p5_SQ_OS, &b_L1_DoubleMu0er1p5_SQ_OS);
   fChain->SetBranchAddress("L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2", &L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2, &b_L1_DoubleMu0er1p5_SQ_OS_dEta_Max1p2);
   fChain->SetBranchAddress("L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4", &L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4, &b_L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4);
   fChain->SetBranchAddress("L1_DoubleMu0er1p5_SQ_dR_Max1p4", &L1_DoubleMu0er1p5_SQ_dR_Max1p4, &b_L1_DoubleMu0er1p5_SQ_dR_Max1p4);
   fChain->SetBranchAddress("L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5", &L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5, &b_L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6", &L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6, &b_L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu0er2p0_SQ_dEta_Max1p5", &L1_DoubleMu0er2p0_SQ_dEta_Max1p5, &b_L1_DoubleMu0er2p0_SQ_dEta_Max1p5);
   fChain->SetBranchAddress("L1_DoubleMu0er2p0_SQ_dEta_Max1p6", &L1_DoubleMu0er2p0_SQ_dEta_Max1p6, &b_L1_DoubleMu0er2p0_SQ_dEta_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu18er2p1_SQ", &L1_DoubleMu18er2p1_SQ, &b_L1_DoubleMu18er2p1_SQ);
   fChain->SetBranchAddress("L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20", &L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20, &b_L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF30_HTT60er", &L1_DoubleMu3_SQ_ETMHF30_HTT60er, &b_L1_DoubleMu3_SQ_ETMHF30_HTT60er);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF30_Jet60er2p5_OR_DoubleJet40er2p5", &L1_DoubleMu3_SQ_ETMHF30_Jet60er2p5_OR_DoubleJet40er2p5, &b_L1_DoubleMu3_SQ_ETMHF30_Jet60er2p5_OR_DoubleJet40er2p5);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF40_HTT60er", &L1_DoubleMu3_SQ_ETMHF40_HTT60er, &b_L1_DoubleMu3_SQ_ETMHF40_HTT60er);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5", &L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5, &b_L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF50_HTT60er", &L1_DoubleMu3_SQ_ETMHF50_HTT60er, &b_L1_DoubleMu3_SQ_ETMHF50_HTT60er);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5", &L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5, &b_L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5", &L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5, &b_L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5", &L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5, &b_L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_HTT220er", &L1_DoubleMu3_SQ_HTT220er, &b_L1_DoubleMu3_SQ_HTT220er);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_HTT240er", &L1_DoubleMu3_SQ_HTT240er, &b_L1_DoubleMu3_SQ_HTT240er);
   fChain->SetBranchAddress("L1_DoubleMu3_SQ_HTT260er", &L1_DoubleMu3_SQ_HTT260er, &b_L1_DoubleMu3_SQ_HTT260er);
   fChain->SetBranchAddress("L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8", &L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8, &b_L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8);
   fChain->SetBranchAddress("L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6", &L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6, &b_L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu4_SQ_EG9er2p5", &L1_DoubleMu4_SQ_EG9er2p5, &b_L1_DoubleMu4_SQ_EG9er2p5);
   fChain->SetBranchAddress("L1_DoubleMu4_SQ_OS", &L1_DoubleMu4_SQ_OS, &b_L1_DoubleMu4_SQ_OS);
   fChain->SetBranchAddress("L1_DoubleMu4_SQ_OS_dR_Max1p2", &L1_DoubleMu4_SQ_OS_dR_Max1p2, &b_L1_DoubleMu4_SQ_OS_dR_Max1p2);
   fChain->SetBranchAddress("L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6", &L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6, &b_L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu4p5_SQ_OS", &L1_DoubleMu4p5_SQ_OS, &b_L1_DoubleMu4p5_SQ_OS);
   fChain->SetBranchAddress("L1_DoubleMu4p5_SQ_OS_dR_Max1p2", &L1_DoubleMu4p5_SQ_OS_dR_Max1p2, &b_L1_DoubleMu4p5_SQ_OS_dR_Max1p2);
   fChain->SetBranchAddress("L1_DoubleMu4p5er2p0_SQ_OS", &L1_DoubleMu4p5er2p0_SQ_OS, &b_L1_DoubleMu4p5er2p0_SQ_OS);
   fChain->SetBranchAddress("L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18", &L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18, &b_L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18);
   fChain->SetBranchAddress("L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7", &L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7, &b_L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7);
   fChain->SetBranchAddress("L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20", &L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20, &b_L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20);
   fChain->SetBranchAddress("L1_DoubleMu5_SQ_EG9er2p5", &L1_DoubleMu5_SQ_EG9er2p5, &b_L1_DoubleMu5_SQ_EG9er2p5);
   fChain->SetBranchAddress("L1_DoubleMu5_SQ_OS_dR_Max1p6", &L1_DoubleMu5_SQ_OS_dR_Max1p6, &b_L1_DoubleMu5_SQ_OS_dR_Max1p6);
   fChain->SetBranchAddress("L1_DoubleMu8_SQ", &L1_DoubleMu8_SQ, &b_L1_DoubleMu8_SQ);
   fChain->SetBranchAddress("L1_DoubleMu9_SQ", &L1_DoubleMu9_SQ, &b_L1_DoubleMu9_SQ);
   fChain->SetBranchAddress("L1_DoubleMu_12_5", &L1_DoubleMu_12_5, &b_L1_DoubleMu_12_5);
   fChain->SetBranchAddress("L1_DoubleMu_15_5_SQ", &L1_DoubleMu_15_5_SQ, &b_L1_DoubleMu_15_5_SQ);
   fChain->SetBranchAddress("L1_DoubleMu_15_7", &L1_DoubleMu_15_7, &b_L1_DoubleMu_15_7);
   fChain->SetBranchAddress("L1_DoubleMu_15_7_Mass_Min1", &L1_DoubleMu_15_7_Mass_Min1, &b_L1_DoubleMu_15_7_Mass_Min1);
   fChain->SetBranchAddress("L1_DoubleMu_15_7_SQ", &L1_DoubleMu_15_7_SQ, &b_L1_DoubleMu_15_7_SQ);
   fChain->SetBranchAddress("L1_DoubleTau70er2p1", &L1_DoubleTau70er2p1, &b_L1_DoubleTau70er2p1);
   fChain->SetBranchAddress("L1_ETM120", &L1_ETM120, &b_L1_ETM120);
   fChain->SetBranchAddress("L1_ETM150", &L1_ETM150, &b_L1_ETM150);
   fChain->SetBranchAddress("L1_ETMHF100", &L1_ETMHF100, &b_L1_ETMHF100);
   fChain->SetBranchAddress("L1_ETMHF100_HTT60er", &L1_ETMHF100_HTT60er, &b_L1_ETMHF100_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF110", &L1_ETMHF110, &b_L1_ETMHF110);
   fChain->SetBranchAddress("L1_ETMHF110_HTT60er", &L1_ETMHF110_HTT60er, &b_L1_ETMHF110_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF120", &L1_ETMHF120, &b_L1_ETMHF120);
   fChain->SetBranchAddress("L1_ETMHF120_HTT60er", &L1_ETMHF120_HTT60er, &b_L1_ETMHF120_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF130", &L1_ETMHF130, &b_L1_ETMHF130);
   fChain->SetBranchAddress("L1_ETMHF130_HTT60er", &L1_ETMHF130_HTT60er, &b_L1_ETMHF130_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF140", &L1_ETMHF140, &b_L1_ETMHF140);
   fChain->SetBranchAddress("L1_ETMHF150", &L1_ETMHF150, &b_L1_ETMHF150);
   fChain->SetBranchAddress("L1_ETMHF70", &L1_ETMHF70, &b_L1_ETMHF70);
   fChain->SetBranchAddress("L1_ETMHF70_HTT60er", &L1_ETMHF70_HTT60er, &b_L1_ETMHF70_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF80", &L1_ETMHF80, &b_L1_ETMHF80);
   fChain->SetBranchAddress("L1_ETMHF80_HTT60er", &L1_ETMHF80_HTT60er, &b_L1_ETMHF80_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p1", &L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p1, &b_L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p1);
   fChain->SetBranchAddress("L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p6", &L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p6, &b_L1_ETMHF80_SingleJet55er2p5_dPhi_Min2p6);
   fChain->SetBranchAddress("L1_ETMHF90", &L1_ETMHF90, &b_L1_ETMHF90);
   fChain->SetBranchAddress("L1_ETMHF90_HTT60er", &L1_ETMHF90_HTT60er, &b_L1_ETMHF90_HTT60er);
   fChain->SetBranchAddress("L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1", &L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1, &b_L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1);
   fChain->SetBranchAddress("L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6", &L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6, &b_L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6);
   fChain->SetBranchAddress("L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1", &L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1, &b_L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1);
   fChain->SetBranchAddress("L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6", &L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6, &b_L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6);
   fChain->SetBranchAddress("L1_ETT1600", &L1_ETT1600, &b_L1_ETT1600);
   fChain->SetBranchAddress("L1_ETT2000", &L1_ETT2000, &b_L1_ETT2000);
   fChain->SetBranchAddress("L1_FirstBunchAfterTrain", &L1_FirstBunchAfterTrain, &b_L1_FirstBunchAfterTrain);
   fChain->SetBranchAddress("L1_FirstBunchBeforeTrain", &L1_FirstBunchBeforeTrain, &b_L1_FirstBunchBeforeTrain);
   fChain->SetBranchAddress("L1_FirstBunchInTrain", &L1_FirstBunchInTrain, &b_L1_FirstBunchInTrain);
   fChain->SetBranchAddress("L1_FirstCollisionInOrbit", &L1_FirstCollisionInOrbit, &b_L1_FirstCollisionInOrbit);
   fChain->SetBranchAddress("L1_FirstCollisionInTrain", &L1_FirstCollisionInTrain, &b_L1_FirstCollisionInTrain);
   fChain->SetBranchAddress("L1_HCAL_LaserMon_Trig", &L1_HCAL_LaserMon_Trig, &b_L1_HCAL_LaserMon_Trig);
   fChain->SetBranchAddress("L1_HCAL_LaserMon_Veto", &L1_HCAL_LaserMon_Veto, &b_L1_HCAL_LaserMon_Veto);
   fChain->SetBranchAddress("L1_HTT120_SingleLLPJet40", &L1_HTT120_SingleLLPJet40, &b_L1_HTT120_SingleLLPJet40);
   fChain->SetBranchAddress("L1_HTT120er", &L1_HTT120er, &b_L1_HTT120er);
   fChain->SetBranchAddress("L1_HTT160_SingleLLPJet50", &L1_HTT160_SingleLLPJet50, &b_L1_HTT160_SingleLLPJet50);
   fChain->SetBranchAddress("L1_HTT160er", &L1_HTT160er, &b_L1_HTT160er);
   fChain->SetBranchAddress("L1_HTT200_SingleLLPJet60", &L1_HTT200_SingleLLPJet60, &b_L1_HTT200_SingleLLPJet60);
   fChain->SetBranchAddress("L1_HTT200er", &L1_HTT200er, &b_L1_HTT200er);
   fChain->SetBranchAddress("L1_HTT240_SingleLLPJet70", &L1_HTT240_SingleLLPJet70, &b_L1_HTT240_SingleLLPJet70);
   fChain->SetBranchAddress("L1_HTT255er", &L1_HTT255er, &b_L1_HTT255er);
   fChain->SetBranchAddress("L1_HTT280er", &L1_HTT280er, &b_L1_HTT280er);
   fChain->SetBranchAddress("L1_HTT280er_QuadJet_70_55_40_35_er2p5", &L1_HTT280er_QuadJet_70_55_40_35_er2p5, &b_L1_HTT280er_QuadJet_70_55_40_35_er2p5);
   fChain->SetBranchAddress("L1_HTT320er", &L1_HTT320er, &b_L1_HTT320er);
   fChain->SetBranchAddress("L1_HTT320er_QuadJet_70_55_40_40_er2p5", &L1_HTT320er_QuadJet_70_55_40_40_er2p5, &b_L1_HTT320er_QuadJet_70_55_40_40_er2p5);
   fChain->SetBranchAddress("L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3", &L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3, &b_L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3);
   fChain->SetBranchAddress("L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3", &L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3, &b_L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3);
   fChain->SetBranchAddress("L1_HTT360er", &L1_HTT360er, &b_L1_HTT360er);
   fChain->SetBranchAddress("L1_HTT400er", &L1_HTT400er, &b_L1_HTT400er);
   fChain->SetBranchAddress("L1_HTT450er", &L1_HTT450er, &b_L1_HTT450er);
   fChain->SetBranchAddress("L1_IsoEG32er2p5_Mt40", &L1_IsoEG32er2p5_Mt40, &b_L1_IsoEG32er2p5_Mt40);
   fChain->SetBranchAddress("L1_IsoTau52er2p1_QuadJet36er2p5", &L1_IsoTau52er2p1_QuadJet36er2p5, &b_L1_IsoTau52er2p1_QuadJet36er2p5);
   fChain->SetBranchAddress("L1_IsolatedBunch", &L1_IsolatedBunch, &b_L1_IsolatedBunch);
   fChain->SetBranchAddress("L1_LastBunchInTrain", &L1_LastBunchInTrain, &b_L1_LastBunchInTrain);
   fChain->SetBranchAddress("L1_LastCollisionInTrain", &L1_LastCollisionInTrain, &b_L1_LastCollisionInTrain);
   fChain->SetBranchAddress("L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3", &L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3, &b_L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3);
   fChain->SetBranchAddress("L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3", &L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3, &b_L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3);
   fChain->SetBranchAddress("L1_LooseIsoEG24er2p1_HTT100er", &L1_LooseIsoEG24er2p1_HTT100er, &b_L1_LooseIsoEG24er2p1_HTT100er);
   fChain->SetBranchAddress("L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3", &L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3, &b_L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3);
   fChain->SetBranchAddress("L1_LooseIsoEG26er2p1_HTT100er", &L1_LooseIsoEG26er2p1_HTT100er, &b_L1_LooseIsoEG26er2p1_HTT100er);
   fChain->SetBranchAddress("L1_LooseIsoEG26er2p1_Jet34er2p5_dR_Min0p3", &L1_LooseIsoEG26er2p1_Jet34er2p5_dR_Min0p3, &b_L1_LooseIsoEG26er2p1_Jet34er2p5_dR_Min0p3);
   fChain->SetBranchAddress("L1_LooseIsoEG28er2p1_HTT100er", &L1_LooseIsoEG28er2p1_HTT100er, &b_L1_LooseIsoEG28er2p1_HTT100er);
   fChain->SetBranchAddress("L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3", &L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3, &b_L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3);
   fChain->SetBranchAddress("L1_LooseIsoEG30er2p1_HTT100er", &L1_LooseIsoEG30er2p1_HTT100er, &b_L1_LooseIsoEG30er2p1_HTT100er);
   fChain->SetBranchAddress("L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3", &L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3, &b_L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3);
   fChain->SetBranchAddress("L1_MinimumBiasHF0", &L1_MinimumBiasHF0, &b_L1_MinimumBiasHF0);
   fChain->SetBranchAddress("L1_MinimumBiasHF0_AND_BptxAND", &L1_MinimumBiasHF0_AND_BptxAND, &b_L1_MinimumBiasHF0_AND_BptxAND);
   fChain->SetBranchAddress("L1_Mu10er2p3_Jet32er2p3_dR_Max0p4_DoubleJet32er2p3_dEta_Max1p6", &L1_Mu10er2p3_Jet32er2p3_dR_Max0p4_DoubleJet32er2p3_dEta_Max1p6, &b_L1_Mu10er2p3_Jet32er2p3_dR_Max0p4_DoubleJet32er2p3_dEta_Max1p6);
   fChain->SetBranchAddress("L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6", &L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6, &b_L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6);
   fChain->SetBranchAddress("L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6", &L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6, &b_L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6);
   fChain->SetBranchAddress("L1_Mu18er2p1_Tau24er2p1", &L1_Mu18er2p1_Tau24er2p1, &b_L1_Mu18er2p1_Tau24er2p1);
   fChain->SetBranchAddress("L1_Mu18er2p1_Tau26er2p1", &L1_Mu18er2p1_Tau26er2p1, &b_L1_Mu18er2p1_Tau26er2p1);
   fChain->SetBranchAddress("L1_Mu18er2p1_Tau26er2p1_Jet55", &L1_Mu18er2p1_Tau26er2p1_Jet55, &b_L1_Mu18er2p1_Tau26er2p1_Jet55);
   fChain->SetBranchAddress("L1_Mu18er2p1_Tau26er2p1_Jet70", &L1_Mu18er2p1_Tau26er2p1_Jet70, &b_L1_Mu18er2p1_Tau26er2p1_Jet70);
   fChain->SetBranchAddress("L1_Mu20_EG10er2p5", &L1_Mu20_EG10er2p5, &b_L1_Mu20_EG10er2p5);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau28er2p1", &L1_Mu22er2p1_IsoTau28er2p1, &b_L1_Mu22er2p1_IsoTau28er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau30er2p1", &L1_Mu22er2p1_IsoTau30er2p1, &b_L1_Mu22er2p1_IsoTau30er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau32er2p1", &L1_Mu22er2p1_IsoTau32er2p1, &b_L1_Mu22er2p1_IsoTau32er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau34er2p1", &L1_Mu22er2p1_IsoTau34er2p1, &b_L1_Mu22er2p1_IsoTau34er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau36er2p1", &L1_Mu22er2p1_IsoTau36er2p1, &b_L1_Mu22er2p1_IsoTau36er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_IsoTau40er2p1", &L1_Mu22er2p1_IsoTau40er2p1, &b_L1_Mu22er2p1_IsoTau40er2p1);
   fChain->SetBranchAddress("L1_Mu22er2p1_Tau70er2p1", &L1_Mu22er2p1_Tau70er2p1, &b_L1_Mu22er2p1_Tau70er2p1);
   fChain->SetBranchAddress("L1_Mu3_Jet120er2p5_dR_Max0p4", &L1_Mu3_Jet120er2p5_dR_Max0p4, &b_L1_Mu3_Jet120er2p5_dR_Max0p4);
   fChain->SetBranchAddress("L1_Mu3_Jet16er2p5_dR_Max0p4", &L1_Mu3_Jet16er2p5_dR_Max0p4, &b_L1_Mu3_Jet16er2p5_dR_Max0p4);
   fChain->SetBranchAddress("L1_Mu3_Jet30er2p5", &L1_Mu3_Jet30er2p5, &b_L1_Mu3_Jet30er2p5);
   fChain->SetBranchAddress("L1_Mu3_Jet60er2p5_dR_Max0p4", &L1_Mu3_Jet60er2p5_dR_Max0p4, &b_L1_Mu3_Jet60er2p5_dR_Max0p4);
   fChain->SetBranchAddress("L1_Mu3er1p5_Jet100er2p5_ETMHF30", &L1_Mu3er1p5_Jet100er2p5_ETMHF30, &b_L1_Mu3er1p5_Jet100er2p5_ETMHF30);
   fChain->SetBranchAddress("L1_Mu3er1p5_Jet100er2p5_ETMHF40", &L1_Mu3er1p5_Jet100er2p5_ETMHF40, &b_L1_Mu3er1p5_Jet100er2p5_ETMHF40);
   fChain->SetBranchAddress("L1_Mu3er1p5_Jet100er2p5_ETMHF50", &L1_Mu3er1p5_Jet100er2p5_ETMHF50, &b_L1_Mu3er1p5_Jet100er2p5_ETMHF50);
   fChain->SetBranchAddress("L1_Mu5_EG23er2p5", &L1_Mu5_EG23er2p5, &b_L1_Mu5_EG23er2p5);
   fChain->SetBranchAddress("L1_Mu5_LooseIsoEG20er2p5", &L1_Mu5_LooseIsoEG20er2p5, &b_L1_Mu5_LooseIsoEG20er2p5);
   fChain->SetBranchAddress("L1_Mu6_DoubleEG10er2p5", &L1_Mu6_DoubleEG10er2p5, &b_L1_Mu6_DoubleEG10er2p5);
   fChain->SetBranchAddress("L1_Mu6_DoubleEG12er2p5", &L1_Mu6_DoubleEG12er2p5, &b_L1_Mu6_DoubleEG12er2p5);
   fChain->SetBranchAddress("L1_Mu6_DoubleEG15er2p5", &L1_Mu6_DoubleEG15er2p5, &b_L1_Mu6_DoubleEG15er2p5);
   fChain->SetBranchAddress("L1_Mu6_DoubleEG17er2p5", &L1_Mu6_DoubleEG17er2p5, &b_L1_Mu6_DoubleEG17er2p5);
   fChain->SetBranchAddress("L1_Mu6_HTT240er", &L1_Mu6_HTT240er, &b_L1_Mu6_HTT240er);
   fChain->SetBranchAddress("L1_Mu6_HTT250er", &L1_Mu6_HTT250er, &b_L1_Mu6_HTT250er);
   fChain->SetBranchAddress("L1_Mu7_EG20er2p5", &L1_Mu7_EG20er2p5, &b_L1_Mu7_EG20er2p5);
   fChain->SetBranchAddress("L1_Mu7_EG23er2p5", &L1_Mu7_EG23er2p5, &b_L1_Mu7_EG23er2p5);
   fChain->SetBranchAddress("L1_Mu7_LooseIsoEG20er2p5", &L1_Mu7_LooseIsoEG20er2p5, &b_L1_Mu7_LooseIsoEG20er2p5);
   fChain->SetBranchAddress("L1_Mu7_LooseIsoEG23er2p5", &L1_Mu7_LooseIsoEG23er2p5, &b_L1_Mu7_LooseIsoEG23er2p5);
   fChain->SetBranchAddress("L1_NotBptxOR", &L1_NotBptxOR, &b_L1_NotBptxOR);
   fChain->SetBranchAddress("L1_QuadJet60er2p5", &L1_QuadJet60er2p5, &b_L1_QuadJet60er2p5);
   fChain->SetBranchAddress("L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0", &L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0, &b_L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0);
   fChain->SetBranchAddress("L1_QuadMu0", &L1_QuadMu0, &b_L1_QuadMu0);
   fChain->SetBranchAddress("L1_QuadMu0_OQ", &L1_QuadMu0_OQ, &b_L1_QuadMu0_OQ);
   fChain->SetBranchAddress("L1_QuadMu0_SQ", &L1_QuadMu0_SQ, &b_L1_QuadMu0_SQ);
   fChain->SetBranchAddress("L1_SecondBunchInTrain", &L1_SecondBunchInTrain, &b_L1_SecondBunchInTrain);
   fChain->SetBranchAddress("L1_SecondLastBunchInTrain", &L1_SecondLastBunchInTrain, &b_L1_SecondLastBunchInTrain);
   fChain->SetBranchAddress("L1_SingleEG10er2p5", &L1_SingleEG10er2p5, &b_L1_SingleEG10er2p5);
   fChain->SetBranchAddress("L1_SingleEG15er2p5", &L1_SingleEG15er2p5, &b_L1_SingleEG15er2p5);
   fChain->SetBranchAddress("L1_SingleEG26er2p5", &L1_SingleEG26er2p5, &b_L1_SingleEG26er2p5);
   fChain->SetBranchAddress("L1_SingleEG28_FWD2p5", &L1_SingleEG28_FWD2p5, &b_L1_SingleEG28_FWD2p5);
   fChain->SetBranchAddress("L1_SingleEG28er1p5", &L1_SingleEG28er1p5, &b_L1_SingleEG28er1p5);
   fChain->SetBranchAddress("L1_SingleEG28er2p1", &L1_SingleEG28er2p1, &b_L1_SingleEG28er2p1);
   fChain->SetBranchAddress("L1_SingleEG28er2p5", &L1_SingleEG28er2p5, &b_L1_SingleEG28er2p5);
   fChain->SetBranchAddress("L1_SingleEG34er2p5", &L1_SingleEG34er2p5, &b_L1_SingleEG34er2p5);
   fChain->SetBranchAddress("L1_SingleEG36er2p5", &L1_SingleEG36er2p5, &b_L1_SingleEG36er2p5);
   fChain->SetBranchAddress("L1_SingleEG38er2p5", &L1_SingleEG38er2p5, &b_L1_SingleEG38er2p5);
   fChain->SetBranchAddress("L1_SingleEG40er2p5", &L1_SingleEG40er2p5, &b_L1_SingleEG40er2p5);
   fChain->SetBranchAddress("L1_SingleEG42er2p5", &L1_SingleEG42er2p5, &b_L1_SingleEG42er2p5);
   fChain->SetBranchAddress("L1_SingleEG45er2p5", &L1_SingleEG45er2p5, &b_L1_SingleEG45er2p5);
   fChain->SetBranchAddress("L1_SingleEG50", &L1_SingleEG50, &b_L1_SingleEG50);
   fChain->SetBranchAddress("L1_SingleEG60", &L1_SingleEG60, &b_L1_SingleEG60);
   fChain->SetBranchAddress("L1_SingleEG8er2p5", &L1_SingleEG8er2p5, &b_L1_SingleEG8er2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG24er2p1", &L1_SingleIsoEG24er2p1, &b_L1_SingleIsoEG24er2p1);
   fChain->SetBranchAddress("L1_SingleIsoEG26er2p1", &L1_SingleIsoEG26er2p1, &b_L1_SingleIsoEG26er2p1);
   fChain->SetBranchAddress("L1_SingleIsoEG26er2p5", &L1_SingleIsoEG26er2p5, &b_L1_SingleIsoEG26er2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG28_FWD2p5", &L1_SingleIsoEG28_FWD2p5, &b_L1_SingleIsoEG28_FWD2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG28er1p5", &L1_SingleIsoEG28er1p5, &b_L1_SingleIsoEG28er1p5);
   fChain->SetBranchAddress("L1_SingleIsoEG28er2p1", &L1_SingleIsoEG28er2p1, &b_L1_SingleIsoEG28er2p1);
   fChain->SetBranchAddress("L1_SingleIsoEG28er2p5", &L1_SingleIsoEG28er2p5, &b_L1_SingleIsoEG28er2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG30er2p1", &L1_SingleIsoEG30er2p1, &b_L1_SingleIsoEG30er2p1);
   fChain->SetBranchAddress("L1_SingleIsoEG30er2p5", &L1_SingleIsoEG30er2p5, &b_L1_SingleIsoEG30er2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG32er2p1", &L1_SingleIsoEG32er2p1, &b_L1_SingleIsoEG32er2p1);
   fChain->SetBranchAddress("L1_SingleIsoEG32er2p5", &L1_SingleIsoEG32er2p5, &b_L1_SingleIsoEG32er2p5);
   fChain->SetBranchAddress("L1_SingleIsoEG34er2p5", &L1_SingleIsoEG34er2p5, &b_L1_SingleIsoEG34er2p5);
   fChain->SetBranchAddress("L1_SingleIsoTau32er2p1", &L1_SingleIsoTau32er2p1, &b_L1_SingleIsoTau32er2p1);
   fChain->SetBranchAddress("L1_SingleJet10erHE", &L1_SingleJet10erHE, &b_L1_SingleJet10erHE);
   fChain->SetBranchAddress("L1_SingleJet120", &L1_SingleJet120, &b_L1_SingleJet120);
   fChain->SetBranchAddress("L1_SingleJet120_FWD2p5", &L1_SingleJet120_FWD2p5, &b_L1_SingleJet120_FWD2p5);
   fChain->SetBranchAddress("L1_SingleJet120_FWD3p0", &L1_SingleJet120_FWD3p0, &b_L1_SingleJet120_FWD3p0);
   fChain->SetBranchAddress("L1_SingleJet120er2p5", &L1_SingleJet120er2p5, &b_L1_SingleJet120er2p5);
   fChain->SetBranchAddress("L1_SingleJet12erHE", &L1_SingleJet12erHE, &b_L1_SingleJet12erHE);
   fChain->SetBranchAddress("L1_SingleJet140er2p5", &L1_SingleJet140er2p5, &b_L1_SingleJet140er2p5);
   fChain->SetBranchAddress("L1_SingleJet140er2p5_ETMHF90", &L1_SingleJet140er2p5_ETMHF90, &b_L1_SingleJet140er2p5_ETMHF90);
   fChain->SetBranchAddress("L1_SingleJet160er2p5", &L1_SingleJet160er2p5, &b_L1_SingleJet160er2p5);
   fChain->SetBranchAddress("L1_SingleJet180", &L1_SingleJet180, &b_L1_SingleJet180);
   fChain->SetBranchAddress("L1_SingleJet180er2p5", &L1_SingleJet180er2p5, &b_L1_SingleJet180er2p5);
   fChain->SetBranchAddress("L1_SingleJet200", &L1_SingleJet200, &b_L1_SingleJet200);
   fChain->SetBranchAddress("L1_SingleJet20er2p5_NotBptxOR", &L1_SingleJet20er2p5_NotBptxOR, &b_L1_SingleJet20er2p5_NotBptxOR);
   fChain->SetBranchAddress("L1_SingleJet20er2p5_NotBptxOR_3BX", &L1_SingleJet20er2p5_NotBptxOR_3BX, &b_L1_SingleJet20er2p5_NotBptxOR_3BX);
   fChain->SetBranchAddress("L1_SingleJet35", &L1_SingleJet35, &b_L1_SingleJet35);
   fChain->SetBranchAddress("L1_SingleJet35_FWD2p5", &L1_SingleJet35_FWD2p5, &b_L1_SingleJet35_FWD2p5);
   fChain->SetBranchAddress("L1_SingleJet35_FWD3p0", &L1_SingleJet35_FWD3p0, &b_L1_SingleJet35_FWD3p0);
   fChain->SetBranchAddress("L1_SingleJet35er2p5", &L1_SingleJet35er2p5, &b_L1_SingleJet35er2p5);
   fChain->SetBranchAddress("L1_SingleJet43er2p5_NotBptxOR_3BX", &L1_SingleJet43er2p5_NotBptxOR_3BX, &b_L1_SingleJet43er2p5_NotBptxOR_3BX);
   fChain->SetBranchAddress("L1_SingleJet46er2p5_NotBptxOR_3BX", &L1_SingleJet46er2p5_NotBptxOR_3BX, &b_L1_SingleJet46er2p5_NotBptxOR_3BX);
   fChain->SetBranchAddress("L1_SingleJet60", &L1_SingleJet60, &b_L1_SingleJet60);
   fChain->SetBranchAddress("L1_SingleJet60_FWD2p5", &L1_SingleJet60_FWD2p5, &b_L1_SingleJet60_FWD2p5);
   fChain->SetBranchAddress("L1_SingleJet8erHE", &L1_SingleJet8erHE, &b_L1_SingleJet8erHE);
   fChain->SetBranchAddress("L1_SingleJet90", &L1_SingleJet90, &b_L1_SingleJet90);
   fChain->SetBranchAddress("L1_SingleJet90_FWD2p5", &L1_SingleJet90_FWD2p5, &b_L1_SingleJet90_FWD2p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG26er1p5", &L1_SingleLooseIsoEG26er1p5, &b_L1_SingleLooseIsoEG26er1p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG26er2p5", &L1_SingleLooseIsoEG26er2p5, &b_L1_SingleLooseIsoEG26er2p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG28_FWD2p5", &L1_SingleLooseIsoEG28_FWD2p5, &b_L1_SingleLooseIsoEG28_FWD2p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG28er1p5", &L1_SingleLooseIsoEG28er1p5, &b_L1_SingleLooseIsoEG28er1p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG28er2p1", &L1_SingleLooseIsoEG28er2p1, &b_L1_SingleLooseIsoEG28er2p1);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG28er2p5", &L1_SingleLooseIsoEG28er2p5, &b_L1_SingleLooseIsoEG28er2p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG30er1p5", &L1_SingleLooseIsoEG30er1p5, &b_L1_SingleLooseIsoEG30er1p5);
   fChain->SetBranchAddress("L1_SingleLooseIsoEG30er2p5", &L1_SingleLooseIsoEG30er2p5, &b_L1_SingleLooseIsoEG30er2p5);
   fChain->SetBranchAddress("L1_SingleMu0_BMTF", &L1_SingleMu0_BMTF, &b_L1_SingleMu0_BMTF);
   fChain->SetBranchAddress("L1_SingleMu0_DQ", &L1_SingleMu0_DQ, &b_L1_SingleMu0_DQ);
   fChain->SetBranchAddress("L1_SingleMu0_EMTF", &L1_SingleMu0_EMTF, &b_L1_SingleMu0_EMTF);
   fChain->SetBranchAddress("L1_SingleMu0_OMTF", &L1_SingleMu0_OMTF, &b_L1_SingleMu0_OMTF);
   fChain->SetBranchAddress("L1_SingleMu0_Upt10", &L1_SingleMu0_Upt10, &b_L1_SingleMu0_Upt10);
   fChain->SetBranchAddress("L1_SingleMu0_Upt10_BMTF", &L1_SingleMu0_Upt10_BMTF, &b_L1_SingleMu0_Upt10_BMTF);
   fChain->SetBranchAddress("L1_SingleMu0_Upt10_EMTF", &L1_SingleMu0_Upt10_EMTF, &b_L1_SingleMu0_Upt10_EMTF);
   fChain->SetBranchAddress("L1_SingleMu0_Upt10_OMTF", &L1_SingleMu0_Upt10_OMTF, &b_L1_SingleMu0_Upt10_OMTF);
   fChain->SetBranchAddress("L1_SingleMu12_DQ_BMTF", &L1_SingleMu12_DQ_BMTF, &b_L1_SingleMu12_DQ_BMTF);
   fChain->SetBranchAddress("L1_SingleMu12_DQ_EMTF", &L1_SingleMu12_DQ_EMTF, &b_L1_SingleMu12_DQ_EMTF);
   fChain->SetBranchAddress("L1_SingleMu12_DQ_OMTF", &L1_SingleMu12_DQ_OMTF, &b_L1_SingleMu12_DQ_OMTF);
   fChain->SetBranchAddress("L1_SingleMu15_DQ", &L1_SingleMu15_DQ, &b_L1_SingleMu15_DQ);
   fChain->SetBranchAddress("L1_SingleMu18", &L1_SingleMu18, &b_L1_SingleMu18);
   fChain->SetBranchAddress("L1_SingleMu20", &L1_SingleMu20, &b_L1_SingleMu20);
   fChain->SetBranchAddress("L1_SingleMu22", &L1_SingleMu22, &b_L1_SingleMu22);
   fChain->SetBranchAddress("L1_SingleMu22_BMTF", &L1_SingleMu22_BMTF, &b_L1_SingleMu22_BMTF);
   fChain->SetBranchAddress("L1_SingleMu22_DQ", &L1_SingleMu22_DQ, &b_L1_SingleMu22_DQ);
   fChain->SetBranchAddress("L1_SingleMu22_EMTF", &L1_SingleMu22_EMTF, &b_L1_SingleMu22_EMTF);
   fChain->SetBranchAddress("L1_SingleMu22_OMTF", &L1_SingleMu22_OMTF, &b_L1_SingleMu22_OMTF);
   fChain->SetBranchAddress("L1_SingleMu22_OQ", &L1_SingleMu22_OQ, &b_L1_SingleMu22_OQ);
   fChain->SetBranchAddress("L1_SingleMu25", &L1_SingleMu25, &b_L1_SingleMu25);
   fChain->SetBranchAddress("L1_SingleMu3", &L1_SingleMu3, &b_L1_SingleMu3);
   fChain->SetBranchAddress("L1_SingleMu5", &L1_SingleMu5, &b_L1_SingleMu5);
   fChain->SetBranchAddress("L1_SingleMu7", &L1_SingleMu7, &b_L1_SingleMu7);
   fChain->SetBranchAddress("L1_SingleMu7_DQ", &L1_SingleMu7_DQ, &b_L1_SingleMu7_DQ);
   fChain->SetBranchAddress("L1_SingleMuCosmics", &L1_SingleMuCosmics, &b_L1_SingleMuCosmics);
   fChain->SetBranchAddress("L1_SingleMuCosmics_BMTF", &L1_SingleMuCosmics_BMTF, &b_L1_SingleMuCosmics_BMTF);
   fChain->SetBranchAddress("L1_SingleMuCosmics_EMTF", &L1_SingleMuCosmics_EMTF, &b_L1_SingleMuCosmics_EMTF);
   fChain->SetBranchAddress("L1_SingleMuCosmics_OMTF", &L1_SingleMuCosmics_OMTF, &b_L1_SingleMuCosmics_OMTF);
   fChain->SetBranchAddress("L1_SingleMuOpen", &L1_SingleMuOpen, &b_L1_SingleMuOpen);
   fChain->SetBranchAddress("L1_SingleMuOpen_BMTF", &L1_SingleMuOpen_BMTF, &b_L1_SingleMuOpen_BMTF);
   fChain->SetBranchAddress("L1_SingleMuOpen_EMTF", &L1_SingleMuOpen_EMTF, &b_L1_SingleMuOpen_EMTF);
   fChain->SetBranchAddress("L1_SingleMuOpen_NotBptxOR", &L1_SingleMuOpen_NotBptxOR, &b_L1_SingleMuOpen_NotBptxOR);
   fChain->SetBranchAddress("L1_SingleMuOpen_OMTF", &L1_SingleMuOpen_OMTF, &b_L1_SingleMuOpen_OMTF);
   fChain->SetBranchAddress("L1_SingleMuOpen_er1p1_NotBptxOR_3BX", &L1_SingleMuOpen_er1p1_NotBptxOR_3BX, &b_L1_SingleMuOpen_er1p1_NotBptxOR_3BX);
   fChain->SetBranchAddress("L1_SingleMuOpen_er1p4_NotBptxOR_3BX", &L1_SingleMuOpen_er1p4_NotBptxOR_3BX, &b_L1_SingleMuOpen_er1p4_NotBptxOR_3BX);
   fChain->SetBranchAddress("L1_SingleMuShower_Nominal", &L1_SingleMuShower_Nominal, &b_L1_SingleMuShower_Nominal);
   fChain->SetBranchAddress("L1_SingleMuShower_Tight", &L1_SingleMuShower_Tight, &b_L1_SingleMuShower_Tight);
   fChain->SetBranchAddress("L1_SingleTau120er2p1", &L1_SingleTau120er2p1, &b_L1_SingleTau120er2p1);
   fChain->SetBranchAddress("L1_SingleTau130er2p1", &L1_SingleTau130er2p1, &b_L1_SingleTau130er2p1);
   fChain->SetBranchAddress("L1_SingleTau70er2p1", &L1_SingleTau70er2p1, &b_L1_SingleTau70er2p1);
   fChain->SetBranchAddress("L1_TOTEM_1", &L1_TOTEM_1, &b_L1_TOTEM_1);
   fChain->SetBranchAddress("L1_TOTEM_2", &L1_TOTEM_2, &b_L1_TOTEM_2);
   fChain->SetBranchAddress("L1_TOTEM_3", &L1_TOTEM_3, &b_L1_TOTEM_3);
   fChain->SetBranchAddress("L1_TOTEM_4", &L1_TOTEM_4, &b_L1_TOTEM_4);
   fChain->SetBranchAddress("L1_TripleEG16er2p5", &L1_TripleEG16er2p5, &b_L1_TripleEG16er2p5);
   fChain->SetBranchAddress("L1_TripleEG_18_17_8_er2p5", &L1_TripleEG_18_17_8_er2p5, &b_L1_TripleEG_18_17_8_er2p5);
   fChain->SetBranchAddress("L1_TripleEG_18_18_12_er2p5", &L1_TripleEG_18_18_12_er2p5, &b_L1_TripleEG_18_18_12_er2p5);
   fChain->SetBranchAddress("L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5", &L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5, &b_L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5);
   fChain->SetBranchAddress("L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5", &L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5, &b_L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5);
   fChain->SetBranchAddress("L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5", &L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5, &b_L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5);
   fChain->SetBranchAddress("L1_TripleMu0", &L1_TripleMu0, &b_L1_TripleMu0);
   fChain->SetBranchAddress("L1_TripleMu0_OQ", &L1_TripleMu0_OQ, &b_L1_TripleMu0_OQ);
   fChain->SetBranchAddress("L1_TripleMu0_SQ", &L1_TripleMu0_SQ, &b_L1_TripleMu0_SQ);
   fChain->SetBranchAddress("L1_TripleMu3", &L1_TripleMu3, &b_L1_TripleMu3);
   fChain->SetBranchAddress("L1_TripleMu3_SQ", &L1_TripleMu3_SQ, &b_L1_TripleMu3_SQ);
   fChain->SetBranchAddress("L1_TripleMu_3SQ_2p5SQ_0", &L1_TripleMu_3SQ_2p5SQ_0, &b_L1_TripleMu_3SQ_2p5SQ_0);
   fChain->SetBranchAddress("L1_TripleMu_3SQ_2p5SQ_0_Mass_Max12", &L1_TripleMu_3SQ_2p5SQ_0_Mass_Max12, &b_L1_TripleMu_3SQ_2p5SQ_0_Mass_Max12);
   fChain->SetBranchAddress("L1_TripleMu_3SQ_2p5SQ_0_OS_Mass_Max12", &L1_TripleMu_3SQ_2p5SQ_0_OS_Mass_Max12, &b_L1_TripleMu_3SQ_2p5SQ_0_OS_Mass_Max12);
   fChain->SetBranchAddress("L1_TripleMu_4SQ_2p5SQ_0_OS_Mass_Max12", &L1_TripleMu_4SQ_2p5SQ_0_OS_Mass_Max12, &b_L1_TripleMu_4SQ_2p5SQ_0_OS_Mass_Max12);
   fChain->SetBranchAddress("L1_TripleMu_5SQ_3SQ_0OQ", &L1_TripleMu_5SQ_3SQ_0OQ, &b_L1_TripleMu_5SQ_3SQ_0OQ);
   fChain->SetBranchAddress("L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9", &L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9, &b_L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9);
   fChain->SetBranchAddress("L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9", &L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9, &b_L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9);
   fChain->SetBranchAddress("L1_TripleMu_5_3_3", &L1_TripleMu_5_3_3, &b_L1_TripleMu_5_3_3);
   fChain->SetBranchAddress("L1_TripleMu_5_3_3_SQ", &L1_TripleMu_5_3_3_SQ, &b_L1_TripleMu_5_3_3_SQ);
   fChain->SetBranchAddress("L1_TripleMu_5_3p5_2p5", &L1_TripleMu_5_3p5_2p5, &b_L1_TripleMu_5_3p5_2p5);
   fChain->SetBranchAddress("L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17", &L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17, &b_L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17);
   fChain->SetBranchAddress("L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17", &L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17, &b_L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17);
   fChain->SetBranchAddress("L1_TripleMu_5_5_3", &L1_TripleMu_5_5_3, &b_L1_TripleMu_5_5_3);
   fChain->SetBranchAddress("L1_TwoMuShower_Loose", &L1_TwoMuShower_Loose, &b_L1_TwoMuShower_Loose);
   fChain->SetBranchAddress("L1_UnpairedBunchBptxMinus", &L1_UnpairedBunchBptxMinus, &b_L1_UnpairedBunchBptxMinus);
   fChain->SetBranchAddress("L1_UnpairedBunchBptxPlus", &L1_UnpairedBunchBptxPlus, &b_L1_UnpairedBunchBptxPlus);
   fChain->SetBranchAddress("L1_ZeroBias", &L1_ZeroBias, &b_L1_ZeroBias);
   fChain->SetBranchAddress("L1_ZeroBias_copy", &L1_ZeroBias_copy, &b_L1_ZeroBias_copy);
   fChain->SetBranchAddress("L1_UnprefireableEvent", &L1_UnprefireableEvent, &b_L1_UnprefireableEvent);
   fChain->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter, &b_Flag_HBHENoiseFilter);
   fChain->SetBranchAddress("Flag_HBHENoiseIsoFilter", &Flag_HBHENoiseIsoFilter, &b_Flag_HBHENoiseIsoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloFilter", &Flag_CSCTightHaloFilter, &b_Flag_CSCTightHaloFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloTrkMuUnvetoFilter", &Flag_CSCTightHaloTrkMuUnvetoFilter, &b_Flag_CSCTightHaloTrkMuUnvetoFilter);
   fChain->SetBranchAddress("Flag_CSCTightHalo2015Filter", &Flag_CSCTightHalo2015Filter, &b_Flag_CSCTightHalo2015Filter);
   fChain->SetBranchAddress("Flag_globalTightHalo2016Filter", &Flag_globalTightHalo2016Filter, &b_Flag_globalTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_globalSuperTightHalo2016Filter", &Flag_globalSuperTightHalo2016Filter, &b_Flag_globalSuperTightHalo2016Filter);
   fChain->SetBranchAddress("Flag_HcalStripHaloFilter", &Flag_HcalStripHaloFilter, &b_Flag_HcalStripHaloFilter);
   fChain->SetBranchAddress("Flag_hcalLaserEventFilter", &Flag_hcalLaserEventFilter, &b_Flag_hcalLaserEventFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter, &b_Flag_EcalDeadCellTriggerPrimitiveFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellBoundaryEnergyFilter", &Flag_EcalDeadCellBoundaryEnergyFilter, &b_Flag_EcalDeadCellBoundaryEnergyFilter);
   fChain->SetBranchAddress("Flag_ecalBadCalibFilter", &Flag_ecalBadCalibFilter, &b_Flag_ecalBadCalibFilter);
   fChain->SetBranchAddress("Flag_goodVertices", &Flag_goodVertices, &b_Flag_goodVertices);
   fChain->SetBranchAddress("Flag_eeBadScFilter", &Flag_eeBadScFilter, &b_Flag_eeBadScFilter);
   fChain->SetBranchAddress("Flag_ecalLaserCorrFilter", &Flag_ecalLaserCorrFilter, &b_Flag_ecalLaserCorrFilter);
   fChain->SetBranchAddress("Flag_trkPOGFilters", &Flag_trkPOGFilters, &b_Flag_trkPOGFilters);
   fChain->SetBranchAddress("Flag_chargedHadronTrackResolutionFilter", &Flag_chargedHadronTrackResolutionFilter, &b_Flag_chargedHadronTrackResolutionFilter);
   fChain->SetBranchAddress("Flag_muonBadTrackFilter", &Flag_muonBadTrackFilter, &b_Flag_muonBadTrackFilter);
   fChain->SetBranchAddress("Flag_BadChargedCandidateFilter", &Flag_BadChargedCandidateFilter, &b_Flag_BadChargedCandidateFilter);
   fChain->SetBranchAddress("Flag_BadPFMuonFilter", &Flag_BadPFMuonFilter, &b_Flag_BadPFMuonFilter);
   fChain->SetBranchAddress("Flag_BadPFMuonDzFilter", &Flag_BadPFMuonDzFilter, &b_Flag_BadPFMuonDzFilter);
   fChain->SetBranchAddress("Flag_hfNoisyHitsFilter", &Flag_hfNoisyHitsFilter, &b_Flag_hfNoisyHitsFilter);
   fChain->SetBranchAddress("Flag_BadChargedCandidateSummer16Filter", &Flag_BadChargedCandidateSummer16Filter, &b_Flag_BadChargedCandidateSummer16Filter);
   fChain->SetBranchAddress("Flag_BadPFMuonSummer16Filter", &Flag_BadPFMuonSummer16Filter, &b_Flag_BadPFMuonSummer16Filter);
   fChain->SetBranchAddress("Flag_trkPOG_manystripclus53X", &Flag_trkPOG_manystripclus53X, &b_Flag_trkPOG_manystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_toomanystripclus53X", &Flag_trkPOG_toomanystripclus53X, &b_Flag_trkPOG_toomanystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_logErrorTooManyClusters", &Flag_trkPOG_logErrorTooManyClusters, &b_Flag_trkPOG_logErrorTooManyClusters);
   fChain->SetBranchAddress("Flag_METFilters", &Flag_METFilters, &b_Flag_METFilters);
   fChain->SetBranchAddress("L1Reco_step", &L1Reco_step, &b_L1Reco_step);
   fChain->SetBranchAddress("L1simulation_step", &L1simulation_step, &b_L1simulation_step);
   fChain->SetBranchAddress("HLTriggerFirstPath", &HLTriggerFirstPath, &b_HLTriggerFirstPath);
   fChain->SetBranchAddress("HLT_EphemeralPhysics", &HLT_EphemeralPhysics, &b_HLT_EphemeralPhysics);
   fChain->SetBranchAddress("HLT_EphemeralZeroBias", &HLT_EphemeralZeroBias, &b_HLT_EphemeralZeroBias);
   fChain->SetBranchAddress("HLT_EcalCalibration", &HLT_EcalCalibration, &b_HLT_EcalCalibration);
   fChain->SetBranchAddress("HLT_HcalCalibration", &HLT_HcalCalibration, &b_HLT_HcalCalibration);
   fChain->SetBranchAddress("HLT_HcalNZS", &HLT_HcalNZS, &b_HLT_HcalNZS);
   fChain->SetBranchAddress("HLT_HcalPhiSym", &HLT_HcalPhiSym, &b_HLT_HcalPhiSym);
   fChain->SetBranchAddress("HLT_Random", &HLT_Random, &b_HLT_Random);
   fChain->SetBranchAddress("HLT_Physics", &HLT_Physics, &b_HLT_Physics);
   fChain->SetBranchAddress("HLT_ZeroBias", &HLT_ZeroBias, &b_HLT_ZeroBias);
   fChain->SetBranchAddress("HLT_ZeroBias_Alignment", &HLT_ZeroBias_Alignment, &b_HLT_ZeroBias_Alignment);
   fChain->SetBranchAddress("HLT_ZeroBias_Beamspot", &HLT_ZeroBias_Beamspot, &b_HLT_ZeroBias_Beamspot);
   fChain->SetBranchAddress("HLT_ZeroBias_IsolatedBunches", &HLT_ZeroBias_IsolatedBunches, &b_HLT_ZeroBias_IsolatedBunches);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstBXAfterTrain", &HLT_ZeroBias_FirstBXAfterTrain, &b_HLT_ZeroBias_FirstBXAfterTrain);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionAfterAbortGap", &HLT_ZeroBias_FirstCollisionAfterAbortGap, &b_HLT_ZeroBias_FirstCollisionAfterAbortGap);
   fChain->SetBranchAddress("HLT_ZeroBias_FirstCollisionInTrain", &HLT_ZeroBias_FirstCollisionInTrain, &b_HLT_ZeroBias_FirstCollisionInTrain);
   fChain->SetBranchAddress("HLT_ZeroBias_LastCollisionInTrain", &HLT_ZeroBias_LastCollisionInTrain, &b_HLT_ZeroBias_LastCollisionInTrain);
   fChain->SetBranchAddress("HLT_HT300_Beamspot", &HLT_HT300_Beamspot, &b_HLT_HT300_Beamspot);
   fChain->SetBranchAddress("HLT_IsoTrackHB", &HLT_IsoTrackHB, &b_HLT_IsoTrackHB);
   fChain->SetBranchAddress("HLT_IsoTrackHE", &HLT_IsoTrackHE, &b_HLT_IsoTrackHE);
   fChain->SetBranchAddress("HLT_PFJet40_GPUvsCPU", &HLT_PFJet40_GPUvsCPU, &b_HLT_PFJet40_GPUvsCPU);
   fChain->SetBranchAddress("HLT_AK8PFJet400_MassSD30", &HLT_AK8PFJet400_MassSD30, &b_HLT_AK8PFJet400_MassSD30);
   fChain->SetBranchAddress("HLT_AK8PFJet420_MassSD30", &HLT_AK8PFJet420_MassSD30, &b_HLT_AK8PFJet420_MassSD30);
   fChain->SetBranchAddress("HLT_AK8PFJet450_MassSD30", &HLT_AK8PFJet450_MassSD30, &b_HLT_AK8PFJet450_MassSD30);
   fChain->SetBranchAddress("HLT_AK8PFJet470_MassSD30", &HLT_AK8PFJet470_MassSD30, &b_HLT_AK8PFJet470_MassSD30);
   fChain->SetBranchAddress("HLT_AK8PFJet500_MassSD30", &HLT_AK8PFJet500_MassSD30, &b_HLT_AK8PFJet500_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet250_250_MassSD30", &HLT_AK8DiPFJet250_250_MassSD30, &b_HLT_AK8DiPFJet250_250_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet260_260_MassSD30", &HLT_AK8DiPFJet260_260_MassSD30, &b_HLT_AK8DiPFJet260_260_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet270_270_MassSD30", &HLT_AK8DiPFJet270_270_MassSD30, &b_HLT_AK8DiPFJet270_270_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet280_280_MassSD30", &HLT_AK8DiPFJet280_280_MassSD30, &b_HLT_AK8DiPFJet280_280_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet290_290_MassSD30", &HLT_AK8DiPFJet290_290_MassSD30, &b_HLT_AK8DiPFJet290_290_MassSD30);
   fChain->SetBranchAddress("HLT_AK8DiPFJet250_250_MassSD50", &HLT_AK8DiPFJet250_250_MassSD50, &b_HLT_AK8DiPFJet250_250_MassSD50);
   fChain->SetBranchAddress("HLT_AK8DiPFJet260_260_MassSD50", &HLT_AK8DiPFJet260_260_MassSD50, &b_HLT_AK8DiPFJet260_260_MassSD50);
   fChain->SetBranchAddress("HLT_CaloJet500_NoJetID", &HLT_CaloJet500_NoJetID, &b_HLT_CaloJet500_NoJetID);
   fChain->SetBranchAddress("HLT_CaloJet550_NoJetID", &HLT_CaloJet550_NoJetID, &b_HLT_CaloJet550_NoJetID);
   fChain->SetBranchAddress("HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL", &HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL, &b_HLT_DoubleMu5_Upsilon_DoubleEle3_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon", &HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon, &b_HLT_DoubleMu3_DoubleEle7p5_CaloIdL_TrackIdL_Upsilon);
   fChain->SetBranchAddress("HLT_Trimuon5_3p5_2_Upsilon_Muon", &HLT_Trimuon5_3p5_2_Upsilon_Muon, &b_HLT_Trimuon5_3p5_2_Upsilon_Muon);
   fChain->SetBranchAddress("HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon", &HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon, &b_HLT_TrimuonOpen_5_3p5_2_Upsilon_Muon);
   fChain->SetBranchAddress("HLT_DoubleEle25_CaloIdL_MW", &HLT_DoubleEle25_CaloIdL_MW, &b_HLT_DoubleEle25_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_DoubleEle27_CaloIdL_MW", &HLT_DoubleEle27_CaloIdL_MW, &b_HLT_DoubleEle27_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_DoubleEle33_CaloIdL_MW", &HLT_DoubleEle33_CaloIdL_MW, &b_HLT_DoubleEle33_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_DoubleEle24_eta2p1_WPTight_Gsf", &HLT_DoubleEle24_eta2p1_WPTight_Gsf, &b_HLT_DoubleEle24_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350", &HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350, &b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_DZ_PFHT350);
   fChain->SetBranchAddress("HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350", &HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350, &b_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT350);
   fChain->SetBranchAddress("HLT_Mu27_Ele37_CaloIdL_MW", &HLT_Mu27_Ele37_CaloIdL_MW, &b_HLT_Mu27_Ele37_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_Mu37_Ele27_CaloIdL_MW", &HLT_Mu37_Ele27_CaloIdL_MW, &b_HLT_Mu37_Ele27_CaloIdL_MW);
   fChain->SetBranchAddress("HLT_Mu37_TkMu27", &HLT_Mu37_TkMu27, &b_HLT_Mu37_TkMu27);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Bs", &HLT_DoubleMu4_3_Bs, &b_HLT_DoubleMu4_3_Bs);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Jpsi", &HLT_DoubleMu4_3_Jpsi, &b_HLT_DoubleMu4_3_Jpsi);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_LowMass", &HLT_DoubleMu4_3_LowMass, &b_HLT_DoubleMu4_3_LowMass);
   fChain->SetBranchAddress("HLT_DoubleMu4_LowMass_Displaced", &HLT_DoubleMu4_LowMass_Displaced, &b_HLT_DoubleMu4_LowMass_Displaced);
   fChain->SetBranchAddress("HLT_Mu0_L1DoubleMu", &HLT_Mu0_L1DoubleMu, &b_HLT_Mu0_L1DoubleMu);
   fChain->SetBranchAddress("HLT_Mu4_L1DoubleMu", &HLT_Mu4_L1DoubleMu, &b_HLT_Mu4_L1DoubleMu);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Photon4_BsToMMG", &HLT_DoubleMu4_3_Photon4_BsToMMG, &b_HLT_DoubleMu4_3_Photon4_BsToMMG);
   fChain->SetBranchAddress("HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG", &HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG, &b_HLT_DoubleMu4_3_Displaced_Photon4_BsToMMG);
   fChain->SetBranchAddress("HLT_DoubleMu3_Trk_Tau3mu", &HLT_DoubleMu3_Trk_Tau3mu, &b_HLT_DoubleMu3_Trk_Tau3mu);
   fChain->SetBranchAddress("HLT_DoubleMu3_TkMu_DsTau3Mu", &HLT_DoubleMu3_TkMu_DsTau3Mu, &b_HLT_DoubleMu3_TkMu_DsTau3Mu);
   fChain->SetBranchAddress("HLT_DoubleMu4_Mass3p8_DZ_PFHT350", &HLT_DoubleMu4_Mass3p8_DZ_PFHT350, &b_HLT_DoubleMu4_Mass3p8_DZ_PFHT350);
   fChain->SetBranchAddress("HLT_DoubleMu4_MuMuTrk_Displaced", &HLT_DoubleMu4_MuMuTrk_Displaced, &b_HLT_DoubleMu4_MuMuTrk_Displaced);
   fChain->SetBranchAddress("HLT_Mu3_PFJet40", &HLT_Mu3_PFJet40, &b_HLT_Mu3_PFJet40);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Jpsi", &HLT_Mu7p5_L2Mu2_Jpsi, &b_HLT_Mu7p5_L2Mu2_Jpsi);
   fChain->SetBranchAddress("HLT_Mu7p5_L2Mu2_Upsilon", &HLT_Mu7p5_L2Mu2_Upsilon, &b_HLT_Mu7p5_L2Mu2_Upsilon);
   fChain->SetBranchAddress("HLT_Mu3_L1SingleMu5orSingleMu7", &HLT_Mu3_L1SingleMu5orSingleMu7, &b_HLT_Mu3_L1SingleMu5orSingleMu7);
   fChain->SetBranchAddress("HLT_DoublePhoton33_CaloIdL", &HLT_DoublePhoton33_CaloIdL, &b_HLT_DoublePhoton33_CaloIdL);
   fChain->SetBranchAddress("HLT_DoublePhoton70", &HLT_DoublePhoton70, &b_HLT_DoublePhoton70);
   fChain->SetBranchAddress("HLT_DoublePhoton85", &HLT_DoublePhoton85, &b_HLT_DoublePhoton85);
   fChain->SetBranchAddress("HLT_DiEle27_WPTightCaloOnly_L1DoubleEG", &HLT_DiEle27_WPTightCaloOnly_L1DoubleEG, &b_HLT_DiEle27_WPTightCaloOnly_L1DoubleEG);
   fChain->SetBranchAddress("HLT_Ele30_WPTight_Gsf", &HLT_Ele30_WPTight_Gsf, &b_HLT_Ele30_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele32_WPTight_Gsf", &HLT_Ele32_WPTight_Gsf, &b_HLT_Ele32_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele35_WPTight_Gsf", &HLT_Ele35_WPTight_Gsf, &b_HLT_Ele35_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele38_WPTight_Gsf", &HLT_Ele38_WPTight_Gsf, &b_HLT_Ele38_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele40_WPTight_Gsf", &HLT_Ele40_WPTight_Gsf, &b_HLT_Ele40_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_Ele32_WPTight_Gsf_L1DoubleEG", &HLT_Ele32_WPTight_Gsf_L1DoubleEG, &b_HLT_Ele32_WPTight_Gsf_L1DoubleEG);
   fChain->SetBranchAddress("HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1", &HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1, &b_HLT_IsoMu27_MediumDeepTauPFTauHPS20_eta2p1_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu20", &HLT_IsoMu20, &b_HLT_IsoMu20);
   fChain->SetBranchAddress("HLT_IsoMu24", &HLT_IsoMu24, &b_HLT_IsoMu24);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1", &HLT_IsoMu24_eta2p1, &b_HLT_IsoMu24_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu27", &HLT_IsoMu27, &b_HLT_IsoMu27);
   fChain->SetBranchAddress("HLT_UncorrectedJetE30_NoBPTX", &HLT_UncorrectedJetE30_NoBPTX, &b_HLT_UncorrectedJetE30_NoBPTX);
   fChain->SetBranchAddress("HLT_UncorrectedJetE30_NoBPTX3BX", &HLT_UncorrectedJetE30_NoBPTX3BX, &b_HLT_UncorrectedJetE30_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_UncorrectedJetE60_NoBPTX3BX", &HLT_UncorrectedJetE60_NoBPTX3BX, &b_HLT_UncorrectedJetE60_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_UncorrectedJetE70_NoBPTX3BX", &HLT_UncorrectedJetE70_NoBPTX3BX, &b_HLT_UncorrectedJetE70_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L1SingleMuCosmics", &HLT_L1SingleMuCosmics, &b_HLT_L1SingleMuCosmics);
   fChain->SetBranchAddress("HLT_L2Mu10_NoVertex_NoBPTX3BX", &HLT_L2Mu10_NoVertex_NoBPTX3BX, &b_HLT_L2Mu10_NoVertex_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu10_NoVertex_NoBPTX", &HLT_L2Mu10_NoVertex_NoBPTX, &b_HLT_L2Mu10_NoVertex_NoBPTX);
   fChain->SetBranchAddress("HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX", &HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX, &b_HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX", &HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX, &b_HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX);
   fChain->SetBranchAddress("HLT_L2Mu23NoVtx_2Cha", &HLT_L2Mu23NoVtx_2Cha, &b_HLT_L2Mu23NoVtx_2Cha);
   fChain->SetBranchAddress("HLT_L2Mu23NoVtx_2Cha_CosmicSeed", &HLT_L2Mu23NoVtx_2Cha_CosmicSeed, &b_HLT_L2Mu23NoVtx_2Cha_CosmicSeed);
   fChain->SetBranchAddress("HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4", &HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4, &b_HLT_DoubleL2Mu30NoVtx_2Cha_CosmicSeed_Eta2p4);
   fChain->SetBranchAddress("HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4", &HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4, &b_HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4);
   fChain->SetBranchAddress("HLT_DoubleL2Mu50", &HLT_DoubleL2Mu50, &b_HLT_DoubleL2Mu50);
   fChain->SetBranchAddress("HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed", &HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed, &b_HLT_DoubleL2Mu23NoVtx_2Cha_CosmicSeed);
   fChain->SetBranchAddress("HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed", &HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed, &b_HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed);
   fChain->SetBranchAddress("HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4", &HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4, &b_HLT_DoubleL2Mu25NoVtx_2Cha_CosmicSeed_Eta2p4);
   fChain->SetBranchAddress("HLT_DoubleL2Mu23NoVtx_2Cha", &HLT_DoubleL2Mu23NoVtx_2Cha, &b_HLT_DoubleL2Mu23NoVtx_2Cha);
   fChain->SetBranchAddress("HLT_DoubleL2Mu25NoVtx_2Cha", &HLT_DoubleL2Mu25NoVtx_2Cha, &b_HLT_DoubleL2Mu25NoVtx_2Cha);
   fChain->SetBranchAddress("HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4", &HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4, &b_HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL", &HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL, &b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ);
   fChain->SetBranchAddress("HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ", &HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ, &b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8);
   fChain->SetBranchAddress("HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8", &HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8, &b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass8);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8", &HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8, &b_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8);
   fChain->SetBranchAddress("HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8", &HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8, &b_HLT_Mu19_TrkIsoVVL_Mu9_TrkIsoVVL_DZ_Mass3p8);
   fChain->SetBranchAddress("HLT_Mu30_TkMu0_Psi", &HLT_Mu30_TkMu0_Psi, &b_HLT_Mu30_TkMu0_Psi);
   fChain->SetBranchAddress("HLT_Mu30_TkMu0_Upsilon", &HLT_Mu30_TkMu0_Upsilon, &b_HLT_Mu30_TkMu0_Upsilon);
   fChain->SetBranchAddress("HLT_Mu25_TkMu0_Phi", &HLT_Mu25_TkMu0_Phi, &b_HLT_Mu25_TkMu0_Phi);
   fChain->SetBranchAddress("HLT_Mu15", &HLT_Mu15, &b_HLT_Mu15);
   fChain->SetBranchAddress("HLT_Mu20", &HLT_Mu20, &b_HLT_Mu20);
   fChain->SetBranchAddress("HLT_Mu27", &HLT_Mu27, &b_HLT_Mu27);
   fChain->SetBranchAddress("HLT_Mu50", &HLT_Mu50, &b_HLT_Mu50);
   fChain->SetBranchAddress("HLT_Mu55", &HLT_Mu55, &b_HLT_Mu55);
   fChain->SetBranchAddress("HLT_CascadeMu100", &HLT_CascadeMu100, &b_HLT_CascadeMu100);
   fChain->SetBranchAddress("HLT_HighPtTkMu100", &HLT_HighPtTkMu100, &b_HLT_HighPtTkMu100);
   fChain->SetBranchAddress("HLT_DiPFJetAve40", &HLT_DiPFJetAve40, &b_HLT_DiPFJetAve40);
   fChain->SetBranchAddress("HLT_DiPFJetAve60", &HLT_DiPFJetAve60, &b_HLT_DiPFJetAve60);
   fChain->SetBranchAddress("HLT_DiPFJetAve80", &HLT_DiPFJetAve80, &b_HLT_DiPFJetAve80);
   fChain->SetBranchAddress("HLT_DiPFJetAve140", &HLT_DiPFJetAve140, &b_HLT_DiPFJetAve140);
   fChain->SetBranchAddress("HLT_DiPFJetAve200", &HLT_DiPFJetAve200, &b_HLT_DiPFJetAve200);
   fChain->SetBranchAddress("HLT_DiPFJetAve260", &HLT_DiPFJetAve260, &b_HLT_DiPFJetAve260);
   fChain->SetBranchAddress("HLT_DiPFJetAve320", &HLT_DiPFJetAve320, &b_HLT_DiPFJetAve320);
   fChain->SetBranchAddress("HLT_DiPFJetAve400", &HLT_DiPFJetAve400, &b_HLT_DiPFJetAve400);
   fChain->SetBranchAddress("HLT_DiPFJetAve500", &HLT_DiPFJetAve500, &b_HLT_DiPFJetAve500);
   fChain->SetBranchAddress("HLT_DiPFJetAve60_HFJEC", &HLT_DiPFJetAve60_HFJEC, &b_HLT_DiPFJetAve60_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve80_HFJEC", &HLT_DiPFJetAve80_HFJEC, &b_HLT_DiPFJetAve80_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve100_HFJEC", &HLT_DiPFJetAve100_HFJEC, &b_HLT_DiPFJetAve100_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve160_HFJEC", &HLT_DiPFJetAve160_HFJEC, &b_HLT_DiPFJetAve160_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve220_HFJEC", &HLT_DiPFJetAve220_HFJEC, &b_HLT_DiPFJetAve220_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve260_HFJEC", &HLT_DiPFJetAve260_HFJEC, &b_HLT_DiPFJetAve260_HFJEC);
   fChain->SetBranchAddress("HLT_DiPFJetAve300_HFJEC", &HLT_DiPFJetAve300_HFJEC, &b_HLT_DiPFJetAve300_HFJEC);
   fChain->SetBranchAddress("HLT_AK8PFJet40", &HLT_AK8PFJet40, &b_HLT_AK8PFJet40);
   fChain->SetBranchAddress("HLT_AK8PFJet60", &HLT_AK8PFJet60, &b_HLT_AK8PFJet60);
   fChain->SetBranchAddress("HLT_AK8PFJet80", &HLT_AK8PFJet80, &b_HLT_AK8PFJet80);
   fChain->SetBranchAddress("HLT_AK8PFJet140", &HLT_AK8PFJet140, &b_HLT_AK8PFJet140);
   fChain->SetBranchAddress("HLT_AK8PFJet200", &HLT_AK8PFJet200, &b_HLT_AK8PFJet200);
   fChain->SetBranchAddress("HLT_AK8PFJet260", &HLT_AK8PFJet260, &b_HLT_AK8PFJet260);
   fChain->SetBranchAddress("HLT_AK8PFJet320", &HLT_AK8PFJet320, &b_HLT_AK8PFJet320);
   fChain->SetBranchAddress("HLT_AK8PFJet400", &HLT_AK8PFJet400, &b_HLT_AK8PFJet400);
   fChain->SetBranchAddress("HLT_AK8PFJet450", &HLT_AK8PFJet450, &b_HLT_AK8PFJet450);
   fChain->SetBranchAddress("HLT_AK8PFJet500", &HLT_AK8PFJet500, &b_HLT_AK8PFJet500);
   fChain->SetBranchAddress("HLT_AK8PFJet550", &HLT_AK8PFJet550, &b_HLT_AK8PFJet550);
   fChain->SetBranchAddress("HLT_PFJet40", &HLT_PFJet40, &b_HLT_PFJet40);
   fChain->SetBranchAddress("HLT_PFJet60", &HLT_PFJet60, &b_HLT_PFJet60);
   fChain->SetBranchAddress("HLT_PFJet80", &HLT_PFJet80, &b_HLT_PFJet80);
   fChain->SetBranchAddress("HLT_PFJet110", &HLT_PFJet110, &b_HLT_PFJet110);
   fChain->SetBranchAddress("HLT_PFJet140", &HLT_PFJet140, &b_HLT_PFJet140);
   fChain->SetBranchAddress("HLT_PFJet200", &HLT_PFJet200, &b_HLT_PFJet200);
   fChain->SetBranchAddress("HLT_PFJet260", &HLT_PFJet260, &b_HLT_PFJet260);
   fChain->SetBranchAddress("HLT_PFJet320", &HLT_PFJet320, &b_HLT_PFJet320);
   fChain->SetBranchAddress("HLT_PFJet400", &HLT_PFJet400, &b_HLT_PFJet400);
   fChain->SetBranchAddress("HLT_PFJet450", &HLT_PFJet450, &b_HLT_PFJet450);
   fChain->SetBranchAddress("HLT_PFJet500", &HLT_PFJet500, &b_HLT_PFJet500);
   fChain->SetBranchAddress("HLT_PFJet550", &HLT_PFJet550, &b_HLT_PFJet550);
   fChain->SetBranchAddress("HLT_PFJetFwd40", &HLT_PFJetFwd40, &b_HLT_PFJetFwd40);
   fChain->SetBranchAddress("HLT_PFJetFwd60", &HLT_PFJetFwd60, &b_HLT_PFJetFwd60);
   fChain->SetBranchAddress("HLT_PFJetFwd80", &HLT_PFJetFwd80, &b_HLT_PFJetFwd80);
   fChain->SetBranchAddress("HLT_PFJetFwd140", &HLT_PFJetFwd140, &b_HLT_PFJetFwd140);
   fChain->SetBranchAddress("HLT_PFJetFwd200", &HLT_PFJetFwd200, &b_HLT_PFJetFwd200);
   fChain->SetBranchAddress("HLT_PFJetFwd260", &HLT_PFJetFwd260, &b_HLT_PFJetFwd260);
   fChain->SetBranchAddress("HLT_PFJetFwd320", &HLT_PFJetFwd320, &b_HLT_PFJetFwd320);
   fChain->SetBranchAddress("HLT_PFJetFwd400", &HLT_PFJetFwd400, &b_HLT_PFJetFwd400);
   fChain->SetBranchAddress("HLT_PFJetFwd450", &HLT_PFJetFwd450, &b_HLT_PFJetFwd450);
   fChain->SetBranchAddress("HLT_PFJetFwd500", &HLT_PFJetFwd500, &b_HLT_PFJetFwd500);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd15", &HLT_AK8PFJetFwd15, &b_HLT_AK8PFJetFwd15);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd25", &HLT_AK8PFJetFwd25, &b_HLT_AK8PFJetFwd25);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd40", &HLT_AK8PFJetFwd40, &b_HLT_AK8PFJetFwd40);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd60", &HLT_AK8PFJetFwd60, &b_HLT_AK8PFJetFwd60);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd80", &HLT_AK8PFJetFwd80, &b_HLT_AK8PFJetFwd80);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd140", &HLT_AK8PFJetFwd140, &b_HLT_AK8PFJetFwd140);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd200", &HLT_AK8PFJetFwd200, &b_HLT_AK8PFJetFwd200);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd260", &HLT_AK8PFJetFwd260, &b_HLT_AK8PFJetFwd260);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd320", &HLT_AK8PFJetFwd320, &b_HLT_AK8PFJetFwd320);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd400", &HLT_AK8PFJetFwd400, &b_HLT_AK8PFJetFwd400);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd450", &HLT_AK8PFJetFwd450, &b_HLT_AK8PFJetFwd450);
   fChain->SetBranchAddress("HLT_AK8PFJetFwd500", &HLT_AK8PFJetFwd500, &b_HLT_AK8PFJetFwd500);
   fChain->SetBranchAddress("HLT_PFHT180", &HLT_PFHT180, &b_HLT_PFHT180);
   fChain->SetBranchAddress("HLT_PFHT250", &HLT_PFHT250, &b_HLT_PFHT250);
   fChain->SetBranchAddress("HLT_PFHT370", &HLT_PFHT370, &b_HLT_PFHT370);
   fChain->SetBranchAddress("HLT_PFHT430", &HLT_PFHT430, &b_HLT_PFHT430);
   fChain->SetBranchAddress("HLT_PFHT510", &HLT_PFHT510, &b_HLT_PFHT510);
   fChain->SetBranchAddress("HLT_PFHT590", &HLT_PFHT590, &b_HLT_PFHT590);
   fChain->SetBranchAddress("HLT_PFHT680", &HLT_PFHT680, &b_HLT_PFHT680);
   fChain->SetBranchAddress("HLT_PFHT780", &HLT_PFHT780, &b_HLT_PFHT780);
   fChain->SetBranchAddress("HLT_PFHT890", &HLT_PFHT890, &b_HLT_PFHT890);
   fChain->SetBranchAddress("HLT_PFHT1050", &HLT_PFHT1050, &b_HLT_PFHT1050);
   fChain->SetBranchAddress("HLT_PFHT500_PFMET100_PFMHT100_IDTight", &HLT_PFHT500_PFMET100_PFMHT100_IDTight, &b_HLT_PFHT500_PFMET100_PFMHT100_IDTight);
   fChain->SetBranchAddress("HLT_PFHT500_PFMET110_PFMHT110_IDTight", &HLT_PFHT500_PFMET110_PFMHT110_IDTight, &b_HLT_PFHT500_PFMET110_PFMHT110_IDTight);
   fChain->SetBranchAddress("HLT_PFHT700_PFMET85_PFMHT85_IDTight", &HLT_PFHT700_PFMET85_PFMHT85_IDTight, &b_HLT_PFHT700_PFMET85_PFMHT85_IDTight);
   fChain->SetBranchAddress("HLT_PFHT800_PFMET75_PFMHT75_IDTight", &HLT_PFHT800_PFMET75_PFMHT75_IDTight, &b_HLT_PFHT800_PFMET75_PFMHT75_IDTight);
   fChain->SetBranchAddress("HLT_PFMET120_PFMHT120_IDTight", &HLT_PFMET120_PFMHT120_IDTight, &b_HLT_PFMET120_PFMHT120_IDTight);
   fChain->SetBranchAddress("HLT_PFMET130_PFMHT130_IDTight", &HLT_PFMET130_PFMHT130_IDTight, &b_HLT_PFMET130_PFMHT130_IDTight);
   fChain->SetBranchAddress("HLT_PFMET140_PFMHT140_IDTight", &HLT_PFMET140_PFMHT140_IDTight, &b_HLT_PFMET140_PFMHT140_IDTight);
   fChain->SetBranchAddress("HLT_PFMET120_PFMHT120_IDTight_PFHT60", &HLT_PFMET120_PFMHT120_IDTight_PFHT60, &b_HLT_PFMET120_PFMHT120_IDTight_PFHT60);
   fChain->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60);
   fChain->SetBranchAddress("HLT_PFMETTypeOne140_PFMHT140_IDTight", &HLT_PFMETTypeOne140_PFMHT140_IDTight, &b_HLT_PFMETTypeOne140_PFMHT140_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu130_PFMHTNoMu130_IDTight", &HLT_PFMETNoMu130_PFMHTNoMu130_IDTight, &b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu140_PFMHTNoMu140_IDTight", &HLT_PFMETNoMu140_PFMHTNoMu140_IDTight, &b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight);
   fChain->SetBranchAddress("HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF", &HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF, &b_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF);
   fChain->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF);
   fChain->SetBranchAddress("HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF", &HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF, &b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF);
   fChain->SetBranchAddress("HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF", &HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF, &b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF);
   fChain->SetBranchAddress("HLT_L1ETMHadSeeds", &HLT_L1ETMHadSeeds, &b_HLT_L1ETMHadSeeds);
   fChain->SetBranchAddress("HLT_CaloMHT90", &HLT_CaloMHT90, &b_HLT_CaloMHT90);
   fChain->SetBranchAddress("HLT_CaloMET90_NotCleaned", &HLT_CaloMET90_NotCleaned, &b_HLT_CaloMET90_NotCleaned);
   fChain->SetBranchAddress("HLT_CaloMET350_NotCleaned", &HLT_CaloMET350_NotCleaned, &b_HLT_CaloMET350_NotCleaned);
   fChain->SetBranchAddress("HLT_PFMET200_NotCleaned", &HLT_PFMET200_NotCleaned, &b_HLT_PFMET200_NotCleaned);
   fChain->SetBranchAddress("HLT_PFMET250_NotCleaned", &HLT_PFMET250_NotCleaned, &b_HLT_PFMET250_NotCleaned);
   fChain->SetBranchAddress("HLT_PFMET300_NotCleaned", &HLT_PFMET300_NotCleaned, &b_HLT_PFMET300_NotCleaned);
   fChain->SetBranchAddress("HLT_PFMET200_BeamHaloCleaned", &HLT_PFMET200_BeamHaloCleaned, &b_HLT_PFMET200_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_PFMETTypeOne200_BeamHaloCleaned", &HLT_PFMETTypeOne200_BeamHaloCleaned, &b_HLT_PFMETTypeOne200_BeamHaloCleaned);
   fChain->SetBranchAddress("HLT_MET105_IsoTrk50", &HLT_MET105_IsoTrk50, &b_HLT_MET105_IsoTrk50);
   fChain->SetBranchAddress("HLT_MET120_IsoTrk50", &HLT_MET120_IsoTrk50, &b_HLT_MET120_IsoTrk50);
   fChain->SetBranchAddress("HLT_Mu12eta2p3", &HLT_Mu12eta2p3, &b_HLT_Mu12eta2p3);
   fChain->SetBranchAddress("HLT_Mu12eta2p3_PFJet40", &HLT_Mu12eta2p3_PFJet40, &b_HLT_Mu12eta2p3_PFJet40);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71", &HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71, &b_HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets40_PFBTagDeepJet_p71", &HLT_DoublePFJets40_PFBTagDeepJet_p71, &b_HLT_DoublePFJets40_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets100_PFBTagDeepJet_p71", &HLT_DoublePFJets100_PFBTagDeepJet_p71, &b_HLT_DoublePFJets100_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets200_PFBTagDeepJet_p71", &HLT_DoublePFJets200_PFBTagDeepJet_p71, &b_HLT_DoublePFJets200_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets350_PFBTagDeepJet_p71", &HLT_DoublePFJets350_PFBTagDeepJet_p71, &b_HLT_DoublePFJets350_PFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71", &HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71, &b_HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71", &HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71, &b_HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71);
   fChain->SetBranchAddress("HLT_Photon300_NoHE", &HLT_Photon300_NoHE, &b_HLT_Photon300_NoHE);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL", &HLT_Mu8_TrkIsoVVL, &b_HLT_Mu8_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ", &HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ, &b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ);
   fChain->SetBranchAddress("HLT_Mu8_DiEle12_CaloIdL_TrackIdL", &HLT_Mu8_DiEle12_CaloIdL_TrackIdL, &b_HLT_Mu8_DiEle12_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350_DZ);
   fChain->SetBranchAddress("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350", &HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350, &b_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT350);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_CaloDiJet30);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu17_TrkIsoVVL", &HLT_Mu17_TrkIsoVVL, &b_HLT_Mu17_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_Mu19_TrkIsoVVL", &HLT_Mu19_TrkIsoVVL, &b_HLT_Mu19_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_BTagMu_AK4DiJet20_Mu5", &HLT_BTagMu_AK4DiJet20_Mu5, &b_HLT_BTagMu_AK4DiJet20_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK4DiJet40_Mu5", &HLT_BTagMu_AK4DiJet40_Mu5, &b_HLT_BTagMu_AK4DiJet40_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK4DiJet70_Mu5", &HLT_BTagMu_AK4DiJet70_Mu5, &b_HLT_BTagMu_AK4DiJet70_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK4DiJet110_Mu5", &HLT_BTagMu_AK4DiJet110_Mu5, &b_HLT_BTagMu_AK4DiJet110_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK4DiJet170_Mu5", &HLT_BTagMu_AK4DiJet170_Mu5, &b_HLT_BTagMu_AK4DiJet170_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK4Jet300_Mu5", &HLT_BTagMu_AK4Jet300_Mu5, &b_HLT_BTagMu_AK4Jet300_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK8DiJet170_Mu5", &HLT_BTagMu_AK8DiJet170_Mu5, &b_HLT_BTagMu_AK8DiJet170_Mu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK8Jet170_DoubleMu5", &HLT_BTagMu_AK8Jet170_DoubleMu5, &b_HLT_BTagMu_AK8Jet170_DoubleMu5);
   fChain->SetBranchAddress("HLT_BTagMu_AK8Jet300_Mu5", &HLT_BTagMu_AK8Jet300_Mu5, &b_HLT_BTagMu_AK8Jet300_Mu5);
   fChain->SetBranchAddress("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL", &HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", &HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL, &b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL);
   fChain->SetBranchAddress("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ", &HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ, &b_HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ);
   fChain->SetBranchAddress("HLT_Photon33", &HLT_Photon33, &b_HLT_Photon33);
   fChain->SetBranchAddress("HLT_Photon50", &HLT_Photon50, &b_HLT_Photon50);
   fChain->SetBranchAddress("HLT_Photon75", &HLT_Photon75, &b_HLT_Photon75);
   fChain->SetBranchAddress("HLT_Photon90", &HLT_Photon90, &b_HLT_Photon90);
   fChain->SetBranchAddress("HLT_Photon120", &HLT_Photon120, &b_HLT_Photon120);
   fChain->SetBranchAddress("HLT_Photon150", &HLT_Photon150, &b_HLT_Photon150);
   fChain->SetBranchAddress("HLT_Photon175", &HLT_Photon175, &b_HLT_Photon175);
   fChain->SetBranchAddress("HLT_Photon200", &HLT_Photon200, &b_HLT_Photon200);
   fChain->SetBranchAddress("HLT_Photon30EB_TightID_TightIso", &HLT_Photon30EB_TightID_TightIso, &b_HLT_Photon30EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon50EB_TightID_TightIso", &HLT_Photon50EB_TightID_TightIso, &b_HLT_Photon50EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon75EB_TightID_TightIso", &HLT_Photon75EB_TightID_TightIso, &b_HLT_Photon75EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon90EB_TightID_TightIso", &HLT_Photon90EB_TightID_TightIso, &b_HLT_Photon90EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon110EB_TightID_TightIso", &HLT_Photon110EB_TightID_TightIso, &b_HLT_Photon110EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon130EB_TightID_TightIso", &HLT_Photon130EB_TightID_TightIso, &b_HLT_Photon130EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon150EB_TightID_TightIso", &HLT_Photon150EB_TightID_TightIso, &b_HLT_Photon150EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon175EB_TightID_TightIso", &HLT_Photon175EB_TightID_TightIso, &b_HLT_Photon175EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon200EB_TightID_TightIso", &HLT_Photon200EB_TightID_TightIso, &b_HLT_Photon200EB_TightID_TightIso);
   fChain->SetBranchAddress("HLT_Photon100EBHE10", &HLT_Photon100EBHE10, &b_HLT_Photon100EBHE10);
   fChain->SetBranchAddress("HLT_Photon50_R9Id90_HE10_IsoM", &HLT_Photon50_R9Id90_HE10_IsoM, &b_HLT_Photon50_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon75_R9Id90_HE10_IsoM", &HLT_Photon75_R9Id90_HE10_IsoM, &b_HLT_Photon75_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon90_R9Id90_HE10_IsoM", &HLT_Photon90_R9Id90_HE10_IsoM, &b_HLT_Photon90_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon120_R9Id90_HE10_IsoM", &HLT_Photon120_R9Id90_HE10_IsoM, &b_HLT_Photon120_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Photon165_R9Id90_HE10_IsoM", &HLT_Photon165_R9Id90_HE10_IsoM, &b_HLT_Photon165_R9Id90_HE10_IsoM);
   fChain->SetBranchAddress("HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90", &HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90, &b_HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90);
   fChain->SetBranchAddress("HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95", &HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95, &b_HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95);
   fChain->SetBranchAddress("HLT_Photon35_TwoProngs35", &HLT_Photon35_TwoProngs35, &b_HLT_Photon35_TwoProngs35);
   fChain->SetBranchAddress("HLT_IsoMu24_TwoProngs35", &HLT_IsoMu24_TwoProngs35, &b_HLT_IsoMu24_TwoProngs35);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_L1_NoOS", &HLT_Dimuon0_Jpsi_L1_NoOS, &b_HLT_Dimuon0_Jpsi_L1_NoOS);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_NoVertexing_NoOS", &HLT_Dimuon0_Jpsi_NoVertexing_NoOS, &b_HLT_Dimuon0_Jpsi_NoVertexing_NoOS);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi", &HLT_Dimuon0_Jpsi, &b_HLT_Dimuon0_Jpsi);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_NoVertexing", &HLT_Dimuon0_Jpsi_NoVertexing, &b_HLT_Dimuon0_Jpsi_NoVertexing);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_L1_4R_0er1p5R", &HLT_Dimuon0_Jpsi_L1_4R_0er1p5R, &b_HLT_Dimuon0_Jpsi_L1_4R_0er1p5R);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R", &HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R, &b_HLT_Dimuon0_Jpsi_NoVertexing_L1_4R_0er1p5R);
   fChain->SetBranchAddress("HLT_Dimuon0_Jpsi3p5_Muon2", &HLT_Dimuon0_Jpsi3p5_Muon2, &b_HLT_Dimuon0_Jpsi3p5_Muon2);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_L1_4p5", &HLT_Dimuon0_Upsilon_L1_4p5, &b_HLT_Dimuon0_Upsilon_L1_4p5);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_L1_4p5er2p0", &HLT_Dimuon0_Upsilon_L1_4p5er2p0, &b_HLT_Dimuon0_Upsilon_L1_4p5er2p0);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_L1_4p5er2p0M", &HLT_Dimuon0_Upsilon_L1_4p5er2p0M, &b_HLT_Dimuon0_Upsilon_L1_4p5er2p0M);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_NoVertexing", &HLT_Dimuon0_Upsilon_NoVertexing, &b_HLT_Dimuon0_Upsilon_NoVertexing);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass_L1_0er1p5R", &HLT_Dimuon0_LowMass_L1_0er1p5R, &b_HLT_Dimuon0_LowMass_L1_0er1p5R);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass_L1_0er1p5", &HLT_Dimuon0_LowMass_L1_0er1p5, &b_HLT_Dimuon0_LowMass_L1_0er1p5);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass", &HLT_Dimuon0_LowMass, &b_HLT_Dimuon0_LowMass);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass_L1_4", &HLT_Dimuon0_LowMass_L1_4, &b_HLT_Dimuon0_LowMass_L1_4);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass_L1_4R", &HLT_Dimuon0_LowMass_L1_4R, &b_HLT_Dimuon0_LowMass_L1_4R);
   fChain->SetBranchAddress("HLT_Dimuon0_LowMass_L1_TM530", &HLT_Dimuon0_LowMass_L1_TM530, &b_HLT_Dimuon0_LowMass_L1_TM530);
   fChain->SetBranchAddress("HLT_Dimuon0_Upsilon_Muon_NoL1Mass", &HLT_Dimuon0_Upsilon_Muon_NoL1Mass, &b_HLT_Dimuon0_Upsilon_Muon_NoL1Mass);
   fChain->SetBranchAddress("HLT_TripleMu_5_3_3_Mass3p8_DZ", &HLT_TripleMu_5_3_3_Mass3p8_DZ, &b_HLT_TripleMu_5_3_3_Mass3p8_DZ);
   fChain->SetBranchAddress("HLT_TripleMu_10_5_5_DZ", &HLT_TripleMu_10_5_5_DZ, &b_HLT_TripleMu_10_5_5_DZ);
   fChain->SetBranchAddress("HLT_TripleMu_12_10_5", &HLT_TripleMu_12_10_5, &b_HLT_TripleMu_12_10_5);
   fChain->SetBranchAddress("HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15", &HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15, &b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15);
   fChain->SetBranchAddress("HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1", &HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1, &b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_Tau15_Charge1);
   fChain->SetBranchAddress("HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15", &HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15, &b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15);
   fChain->SetBranchAddress("HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1", &HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1, &b_HLT_Tau3Mu_Mu7_Mu1_TkMu1_IsoTau15_Charge1);
   fChain->SetBranchAddress("HLT_DoubleMu3_DZ_PFMET50_PFMHT60", &HLT_DoubleMu3_DZ_PFMET50_PFMHT60, &b_HLT_DoubleMu3_DZ_PFMET50_PFMHT60);
   fChain->SetBranchAddress("HLT_DoubleMu3_DZ_PFMET70_PFMHT70", &HLT_DoubleMu3_DZ_PFMET70_PFMHT70, &b_HLT_DoubleMu3_DZ_PFMET70_PFMHT70);
   fChain->SetBranchAddress("HLT_DoubleMu3_DZ_PFMET90_PFMHT90", &HLT_DoubleMu3_DZ_PFMET90_PFMHT90, &b_HLT_DoubleMu3_DZ_PFMET90_PFMHT90);
   fChain->SetBranchAddress("HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass", &HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass, &b_HLT_DoubleMu3_Trk_Tau3mu_NoL1Mass);
   fChain->SetBranchAddress("HLT_DoubleMu4_Jpsi_Displaced", &HLT_DoubleMu4_Jpsi_Displaced, &b_HLT_DoubleMu4_Jpsi_Displaced);
   fChain->SetBranchAddress("HLT_DoubleMu4_Jpsi_NoVertexing", &HLT_DoubleMu4_Jpsi_NoVertexing, &b_HLT_DoubleMu4_Jpsi_NoVertexing);
   fChain->SetBranchAddress("HLT_DoubleMu4_JpsiTrkTrk_Displaced", &HLT_DoubleMu4_JpsiTrkTrk_Displaced, &b_HLT_DoubleMu4_JpsiTrkTrk_Displaced);
   fChain->SetBranchAddress("HLT_DoubleMu4_JpsiTrk_Bc", &HLT_DoubleMu4_JpsiTrk_Bc, &b_HLT_DoubleMu4_JpsiTrk_Bc);
   fChain->SetBranchAddress("HLT_DoubleMu43NoFiltersNoVtx", &HLT_DoubleMu43NoFiltersNoVtx, &b_HLT_DoubleMu43NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_DoubleMu48NoFiltersNoVtx", &HLT_DoubleMu48NoFiltersNoVtx, &b_HLT_DoubleMu48NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL", &HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL, &b_HLT_Mu43NoFiltersNoVtx_Photon43_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL", &HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL, &b_HLT_Mu48NoFiltersNoVtx_Photon48_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL", &HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL, &b_HLT_Mu38NoFiltersNoVtxDisplaced_Photon38_CaloIdL);
   fChain->SetBranchAddress("HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL", &HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL, &b_HLT_Mu43NoFiltersNoVtxDisplaced_Photon43_CaloIdL);
   fChain->SetBranchAddress("HLT_DiJet110_35_Mjj650_PFMET110", &HLT_DiJet110_35_Mjj650_PFMET110, &b_HLT_DiJet110_35_Mjj650_PFMET110);
   fChain->SetBranchAddress("HLT_DiJet110_35_Mjj650_PFMET120", &HLT_DiJet110_35_Mjj650_PFMET120, &b_HLT_DiJet110_35_Mjj650_PFMET120);
   fChain->SetBranchAddress("HLT_DiJet110_35_Mjj650_PFMET130", &HLT_DiJet110_35_Mjj650_PFMET130, &b_HLT_DiJet110_35_Mjj650_PFMET130);
   fChain->SetBranchAddress("HLT_TripleJet110_35_35_Mjj650_PFMET110", &HLT_TripleJet110_35_35_Mjj650_PFMET110, &b_HLT_TripleJet110_35_35_Mjj650_PFMET110);
   fChain->SetBranchAddress("HLT_TripleJet110_35_35_Mjj650_PFMET120", &HLT_TripleJet110_35_35_Mjj650_PFMET120, &b_HLT_TripleJet110_35_35_Mjj650_PFMET120);
   fChain->SetBranchAddress("HLT_TripleJet110_35_35_Mjj650_PFMET130", &HLT_TripleJet110_35_35_Mjj650_PFMET130, &b_HLT_TripleJet110_35_35_Mjj650_PFMET130);
   fChain->SetBranchAddress("HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned", &HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned, &b_HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned);
   fChain->SetBranchAddress("HLT_Ele28_eta2p1_WPTight_Gsf_HT150", &HLT_Ele28_eta2p1_WPTight_Gsf_HT150, &b_HLT_Ele28_eta2p1_WPTight_Gsf_HT150);
   fChain->SetBranchAddress("HLT_Ele28_HighEta_SC20_Mass55", &HLT_Ele28_HighEta_SC20_Mass55, &b_HLT_Ele28_HighEta_SC20_Mass55);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT450_PFMET50", &HLT_Ele15_IsoVVVL_PFHT450_PFMET50, &b_HLT_Ele15_IsoVVVL_PFHT450_PFMET50);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT450", &HLT_Ele15_IsoVVVL_PFHT450, &b_HLT_Ele15_IsoVVVL_PFHT450);
   fChain->SetBranchAddress("HLT_Ele50_IsoVVVL_PFHT450", &HLT_Ele50_IsoVVVL_PFHT450, &b_HLT_Ele50_IsoVVVL_PFHT450);
   fChain->SetBranchAddress("HLT_Ele15_IsoVVVL_PFHT600", &HLT_Ele15_IsoVVVL_PFHT600, &b_HLT_Ele15_IsoVVVL_PFHT600);
   fChain->SetBranchAddress("HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60", &HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60, &b_HLT_Mu4_TrkIsoVVL_DiPFJet90_40_DEta3p5_MJJ750_HTT300_PFMETNoMu60);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60", &HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60, &b_HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60);
   fChain->SetBranchAddress("HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60", &HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60, &b_HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT450_PFMET50", &HLT_Mu15_IsoVVVL_PFHT450_PFMET50, &b_HLT_Mu15_IsoVVVL_PFHT450_PFMET50);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT450", &HLT_Mu15_IsoVVVL_PFHT450, &b_HLT_Mu15_IsoVVVL_PFHT450);
   fChain->SetBranchAddress("HLT_Mu50_IsoVVVL_PFHT450", &HLT_Mu50_IsoVVVL_PFHT450, &b_HLT_Mu50_IsoVVVL_PFHT450);
   fChain->SetBranchAddress("HLT_Mu15_IsoVVVL_PFHT600", &HLT_Mu15_IsoVVVL_PFHT600, &b_HLT_Mu15_IsoVVVL_PFHT600);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMET80_PFMHT80_IDTight);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMET90_PFMHT90_IDTight);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMET100_PFMHT100_IDTight);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu80_PFMHTNoMu80_IDTight);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu90_PFMHTNoMu90_IDTight);
   fChain->SetBranchAddress("HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight", &HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight, &b_HLT_Mu3er1p5_PFJet100er2p5_PFMETNoMu100_PFMHTNoMu100_IDTight);
   fChain->SetBranchAddress("HLT_Dimuon10_Upsilon_y1p4", &HLT_Dimuon10_Upsilon_y1p4, &b_HLT_Dimuon10_Upsilon_y1p4);
   fChain->SetBranchAddress("HLT_Dimuon12_Upsilon_y1p4", &HLT_Dimuon12_Upsilon_y1p4, &b_HLT_Dimuon12_Upsilon_y1p4);
   fChain->SetBranchAddress("HLT_Dimuon14_Phi_Barrel_Seagulls", &HLT_Dimuon14_Phi_Barrel_Seagulls, &b_HLT_Dimuon14_Phi_Barrel_Seagulls);
   fChain->SetBranchAddress("HLT_Dimuon25_Jpsi", &HLT_Dimuon25_Jpsi, &b_HLT_Dimuon25_Jpsi);
   fChain->SetBranchAddress("HLT_Dimuon14_PsiPrime", &HLT_Dimuon14_PsiPrime, &b_HLT_Dimuon14_PsiPrime);
   fChain->SetBranchAddress("HLT_Dimuon14_PsiPrime_noCorrL1", &HLT_Dimuon14_PsiPrime_noCorrL1, &b_HLT_Dimuon14_PsiPrime_noCorrL1);
   fChain->SetBranchAddress("HLT_Dimuon18_PsiPrime", &HLT_Dimuon18_PsiPrime, &b_HLT_Dimuon18_PsiPrime);
   fChain->SetBranchAddress("HLT_Dimuon18_PsiPrime_noCorrL1", &HLT_Dimuon18_PsiPrime_noCorrL1, &b_HLT_Dimuon18_PsiPrime_noCorrL1);
   fChain->SetBranchAddress("HLT_Dimuon24_Upsilon_noCorrL1", &HLT_Dimuon24_Upsilon_noCorrL1, &b_HLT_Dimuon24_Upsilon_noCorrL1);
   fChain->SetBranchAddress("HLT_Dimuon24_Phi_noCorrL1", &HLT_Dimuon24_Phi_noCorrL1, &b_HLT_Dimuon24_Phi_noCorrL1);
   fChain->SetBranchAddress("HLT_Dimuon25_Jpsi_noCorrL1", &HLT_Dimuon25_Jpsi_noCorrL1, &b_HLT_Dimuon25_Jpsi_noCorrL1);
   fChain->SetBranchAddress("HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8", &HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8, &b_HLT_DiMu4_Ele9_CaloIdL_TrackIdL_DZ_Mass3p8);
   fChain->SetBranchAddress("HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ", &HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ, &b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ);
   fChain->SetBranchAddress("HLT_DiMu9_Ele9_CaloIdL_TrackIdL", &HLT_DiMu9_Ele9_CaloIdL_TrackIdL, &b_HLT_DiMu9_Ele9_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_DoubleIsoMu20_eta2p1", &HLT_DoubleIsoMu20_eta2p1, &b_HLT_DoubleIsoMu20_eta2p1);
   fChain->SetBranchAddress("HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx", &HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx, &b_HLT_TrkMu12_DoubleTrkMu5NoFiltersNoVtx);
   fChain->SetBranchAddress("HLT_Mu8", &HLT_Mu8, &b_HLT_Mu8);
   fChain->SetBranchAddress("HLT_Mu17", &HLT_Mu17, &b_HLT_Mu17);
   fChain->SetBranchAddress("HLT_Mu19", &HLT_Mu19, &b_HLT_Mu19);
   fChain->SetBranchAddress("HLT_Mu17_Photon30_IsoCaloId", &HLT_Mu17_Photon30_IsoCaloId, &b_HLT_Mu17_Photon30_IsoCaloId);
   fChain->SetBranchAddress("HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30", &HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30, &b_HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30);
   fChain->SetBranchAddress("HLT_Ele8_CaloIdM_TrackIdM_PFJet30", &HLT_Ele8_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele8_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele17_CaloIdM_TrackIdM_PFJet30", &HLT_Ele17_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele17_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele23_CaloIdM_TrackIdM_PFJet30", &HLT_Ele23_CaloIdM_TrackIdM_PFJet30, &b_HLT_Ele23_CaloIdM_TrackIdM_PFJet30);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165", &HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165);
   fChain->SetBranchAddress("HLT_Ele115_CaloIdVT_GsfTrkIdT", &HLT_Ele115_CaloIdVT_GsfTrkIdT, &b_HLT_Ele115_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_Ele135_CaloIdVT_GsfTrkIdT", &HLT_Ele135_CaloIdVT_GsfTrkIdT, &b_HLT_Ele135_CaloIdVT_GsfTrkIdT);
   fChain->SetBranchAddress("HLT_PFHT330PT30_QuadPFJet_75_60_45_40", &HLT_PFHT330PT30_QuadPFJet_75_60_45_40, &b_HLT_PFHT330PT30_QuadPFJet_75_60_45_40);
   fChain->SetBranchAddress("HLT_PFHT400_SixPFJet32", &HLT_PFHT400_SixPFJet32, &b_HLT_PFHT400_SixPFJet32);
   fChain->SetBranchAddress("HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50", &HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50, &b_HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50);
   fChain->SetBranchAddress("HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94", &HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94, &b_HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94);
   fChain->SetBranchAddress("HLT_PFHT450_SixPFJet36", &HLT_PFHT450_SixPFJet36, &b_HLT_PFHT450_SixPFJet36);
   fChain->SetBranchAddress("HLT_PFHT450_SixPFJet36_PNetBTag0p35", &HLT_PFHT450_SixPFJet36_PNetBTag0p35, &b_HLT_PFHT450_SixPFJet36_PNetBTag0p35);
   fChain->SetBranchAddress("HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59", &HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59, &b_HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59);
   fChain->SetBranchAddress("HLT_PFHT400_FivePFJet_100_100_60_30_30", &HLT_PFHT400_FivePFJet_100_100_60_30_30, &b_HLT_PFHT400_FivePFJet_100_100_60_30_30);
   fChain->SetBranchAddress("HLT_PFHT350", &HLT_PFHT350, &b_HLT_PFHT350);
   fChain->SetBranchAddress("HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350", &HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350, &b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350);
   fChain->SetBranchAddress("HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380", &HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380, &b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT380);
   fChain->SetBranchAddress("HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400", &HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400, &b_HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT400);
   fChain->SetBranchAddress("HLT_ECALHT800", &HLT_ECALHT800, &b_HLT_ECALHT800);
   fChain->SetBranchAddress("HLT_DiSC30_18_EIso_AND_HE_Mass70", &HLT_DiSC30_18_EIso_AND_HE_Mass70, &b_HLT_DiSC30_18_EIso_AND_HE_Mass70);
   fChain->SetBranchAddress("HLT_Photon20_HoverELoose", &HLT_Photon20_HoverELoose, &b_HLT_Photon20_HoverELoose);
   fChain->SetBranchAddress("HLT_Photon30_HoverELoose", &HLT_Photon30_HoverELoose, &b_HLT_Photon30_HoverELoose);
   fChain->SetBranchAddress("HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142", &HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142, &b_HLT_L1_CDC_SingleMu_3_er1p2_TOP120_DPHI2p618_3p142);
   fChain->SetBranchAddress("HLT_CDC_L2cosmic_10_er1p0", &HLT_CDC_L2cosmic_10_er1p0, &b_HLT_CDC_L2cosmic_10_er1p0);
   fChain->SetBranchAddress("HLT_CDC_L2cosmic_5p5_er1p0", &HLT_CDC_L2cosmic_5p5_er1p0, &b_HLT_CDC_L2cosmic_5p5_er1p0);
   fChain->SetBranchAddress("HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL", &HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL, &b_HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL);
   fChain->SetBranchAddress("HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1", &HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1, &b_HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1);
   fChain->SetBranchAddress("HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3", &HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3, &b_HLT_Photon60_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3);
   fChain->SetBranchAddress("HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3", &HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3, &b_HLT_Photon75_R9Id90_HE10_IsoM_EBOnly_PFJetsMJJ300DEta3);
   fChain->SetBranchAddress("HLT_Mu18_Mu9_SameSign", &HLT_Mu18_Mu9_SameSign, &b_HLT_Mu18_Mu9_SameSign);
   fChain->SetBranchAddress("HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05", &HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05, &b_HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05);
   fChain->SetBranchAddress("HLT_DoubleMu3_DCA_PFMET50_PFMHT60", &HLT_DoubleMu3_DCA_PFMET50_PFMHT60, &b_HLT_DoubleMu3_DCA_PFMET50_PFMHT60);
   fChain->SetBranchAddress("HLT_TripleMu_5_3_3_Mass3p8_DCA", &HLT_TripleMu_5_3_3_Mass3p8_DCA, &b_HLT_TripleMu_5_3_3_Mass3p8_DCA);
   fChain->SetBranchAddress("HLT_QuadPFJet103_88_75_15", &HLT_QuadPFJet103_88_75_15, &b_HLT_QuadPFJet103_88_75_15);
   fChain->SetBranchAddress("HLT_QuadPFJet105_88_76_15", &HLT_QuadPFJet105_88_76_15, &b_HLT_QuadPFJet105_88_76_15);
   fChain->SetBranchAddress("HLT_QuadPFJet111_90_80_15", &HLT_QuadPFJet111_90_80_15, &b_HLT_QuadPFJet111_90_80_15);
   fChain->SetBranchAddress("HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId", &HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId, &b_HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId);
   fChain->SetBranchAddress("HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55", &HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55, &b_HLT_Diphoton30_18_R9IdL_AND_HE_AND_IsoCaloId_Mass55);
   fChain->SetBranchAddress("HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1", &HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1, &b_HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1);
   fChain->SetBranchAddress("HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1", &HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1, &b_HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1", &HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1, &b_HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1", &HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1, &b_HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS180_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1", &HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1, &b_HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1", &HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1, &b_HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1);
   fChain->SetBranchAddress("HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5", &HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5, &b_HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5);
   fChain->SetBranchAddress("HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5", &HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5, &b_HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5);
   fChain->SetBranchAddress("HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5", &HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5, &b_HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5);
   fChain->SetBranchAddress("HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1", &HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1, &b_HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1);
   fChain->SetBranchAddress("HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2", &HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2, &b_HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2);
   fChain->SetBranchAddress("HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1", &HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1, &b_HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1);
   fChain->SetBranchAddress("HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2", &HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2, &b_HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2);
   fChain->SetBranchAddress("HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1", &HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1, &b_HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1);
   fChain->SetBranchAddress("HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2", &HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2, &b_HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5);
   fChain->SetBranchAddress("HLT_PFHT280_QuadPFJet30", &HLT_PFHT280_QuadPFJet30, &b_HLT_PFHT280_QuadPFJet30);
   fChain->SetBranchAddress("HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55", &HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55, &b_HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p55);
   fChain->SetBranchAddress("HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60", &HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60, &b_HLT_PFHT280_QuadPFJet30_PNet2BTagMean0p60);
   fChain->SetBranchAddress("HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60", &HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60, &b_HLT_PFHT280_QuadPFJet35_PNet2BTagMean0p60);
   fChain->SetBranchAddress("HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70", &HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70, &b_HLT_PFHT340_QuadPFJet70_50_40_40_PNet2BTagMean0p70);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFHT280_QuadPFJet30_PNet2BTagMean0p55);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PNet2BTagMean0p50);
   fChain->SetBranchAddress("HLT_QuadPFJet100_88_70_30", &HLT_QuadPFJet100_88_70_30, &b_HLT_QuadPFJet100_88_70_30);
   fChain->SetBranchAddress("HLT_QuadPFJet105_88_75_30", &HLT_QuadPFJet105_88_75_30, &b_HLT_QuadPFJet105_88_75_30);
   fChain->SetBranchAddress("HLT_QuadPFJet111_90_80_30", &HLT_QuadPFJet111_90_80_30, &b_HLT_QuadPFJet111_90_80_30);
   fChain->SetBranchAddress("HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight", &HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight, &b_HLT_QuadPFJet100_88_70_30_PNet1CvsAll0p5_VBF3Tight);
   fChain->SetBranchAddress("HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight", &HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight, &b_HLT_QuadPFJet105_88_75_30_PNet1CvsAll0p5_VBF3Tight);
   fChain->SetBranchAddress("HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight", &HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight, &b_HLT_QuadPFJet111_90_80_30_PNet1CvsAll0p6_VBF3Tight);
   fChain->SetBranchAddress("HLT_AK8PFJet220_SoftDropMass40", &HLT_AK8PFJet220_SoftDropMass40, &b_HLT_AK8PFJet220_SoftDropMass40);
   fChain->SetBranchAddress("HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50", &HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50, &b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p50);
   fChain->SetBranchAddress("HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53", &HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53, &b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p53);
   fChain->SetBranchAddress("HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55", &HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55, &b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p55);
   fChain->SetBranchAddress("HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60", &HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60, &b_HLT_AK8PFJet220_SoftDropMass40_PNetBB0p06_DoubleAK4PFJet60_30_PNet2BTagMean0p60);
   fChain->SetBranchAddress("HLT_AK8PFJet230_SoftDropMass40", &HLT_AK8PFJet230_SoftDropMass40, &b_HLT_AK8PFJet230_SoftDropMass40);
   fChain->SetBranchAddress("HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06", &HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06, &b_HLT_AK8PFJet230_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10", &HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10, &b_HLT_AK8PFJet230_SoftDropMass40_PNetBB0p10);
   fChain->SetBranchAddress("HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03", &HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03, &b_HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p03);
   fChain->SetBranchAddress("HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05", &HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05, &b_HLT_AK8PFJet230_SoftDropMass40_PNetTauTau0p05);
   fChain->SetBranchAddress("HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06", &HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06, &b_HLT_AK8PFJet250_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10", &HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10, &b_HLT_AK8PFJet250_SoftDropMass40_PNetBB0p10);
   fChain->SetBranchAddress("HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03", &HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03, &b_HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p03);
   fChain->SetBranchAddress("HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05", &HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05, &b_HLT_AK8PFJet250_SoftDropMass40_PNetTauTau0p05);
   fChain->SetBranchAddress("HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06", &HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06, &b_HLT_AK8PFJet275_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10", &HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10, &b_HLT_AK8PFJet275_SoftDropMass40_PNetBB0p10);
   fChain->SetBranchAddress("HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03", &HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03, &b_HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p03);
   fChain->SetBranchAddress("HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05", &HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05, &b_HLT_AK8PFJet275_SoftDropMass40_PNetTauTau0p05);
   fChain->SetBranchAddress("HLT_AK8PFJet425_SoftDropMass40", &HLT_AK8PFJet425_SoftDropMass40, &b_HLT_AK8PFJet425_SoftDropMass40);
   fChain->SetBranchAddress("HLT_AK8PFJet450_SoftDropMass40", &HLT_AK8PFJet450_SoftDropMass40, &b_HLT_AK8PFJet450_SoftDropMass40);
   fChain->SetBranchAddress("HLT_IsoMu50_AK8PFJet220_SoftDropMass40", &HLT_IsoMu50_AK8PFJet220_SoftDropMass40, &b_HLT_IsoMu50_AK8PFJet220_SoftDropMass40);
   fChain->SetBranchAddress("HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06", &HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06, &b_HLT_IsoMu50_AK8PFJet220_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_IsoMu50_AK8PFJet230_SoftDropMass40", &HLT_IsoMu50_AK8PFJet230_SoftDropMass40, &b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40);
   fChain->SetBranchAddress("HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06", &HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06, &b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10", &HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10, &b_HLT_IsoMu50_AK8PFJet230_SoftDropMass40_PNetBB0p10);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40", &HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06", &HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet220_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40", &HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06", &HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p06);
   fChain->SetBranchAddress("HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10", &HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10, &b_HLT_Ele50_CaloIdVT_GsfTrkIdT_AK8PFJet230_SoftDropMass40_PNetBB0p10);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30);
   fChain->SetBranchAddress("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50", &HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50, &b_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_DoubleAK4PFJet60_30_PNet2BTagMean0p50);
   fChain->SetBranchAddress("HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60", &HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60, &b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60);
   fChain->SetBranchAddress("HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75", &HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75, &b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1);
   fChain->SetBranchAddress("HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1", &HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1, &b_HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1", &HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1, &b_HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1);
   fChain->SetBranchAddress("HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm", &HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm, &b_HLT_DoubleL2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm", &HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm, &b_HLT_DoubleL2Mu12NoVtx_2Cha_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm", &HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm, &b_HLT_DoubleL2Mu14NoVtx_2Cha_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm", &HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm, &b_HLT_DoubleL3Mu16_10NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm", &HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm, &b_HLT_DoubleL3Mu18_10NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm", &HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm, &b_HLT_DoubleL3Mu20_10NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_L2Mu10NoVtx_2Cha", &HLT_L2Mu10NoVtx_2Cha, &b_HLT_L2Mu10NoVtx_2Cha);
   fChain->SetBranchAddress("HLT_L2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm", &HLT_L2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm, &b_HLT_L2Mu10NoVtx_2Cha_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_L3Mu10NoVtx", &HLT_L3Mu10NoVtx, &b_HLT_L3Mu10NoVtx);
   fChain->SetBranchAddress("HLT_L3Mu10NoVtx_DxyMin0p01cm", &HLT_L3Mu10NoVtx_DxyMin0p01cm, &b_HLT_L3Mu10NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm", &HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm, &b_HLT_DoubleL2Mu_L3Mu16NoVtx_VetoL3Mu0DxyMax0p1cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm", &HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm, &b_HLT_DoubleL2Mu_L3Mu18NoVtx_VetoL3Mu0DxyMax0p1cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm", &HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm, &b_HLT_DoubleL2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm", &HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm, &b_HLT_DoubleL2Mu12NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_L2Mu10NoVtx_2Cha_CosmicSeed", &HLT_L2Mu10NoVtx_2Cha_CosmicSeed, &b_HLT_L2Mu10NoVtx_2Cha_CosmicSeed);
   fChain->SetBranchAddress("HLT_L2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm", &HLT_L2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm, &b_HLT_L2Mu10NoVtx_2Cha_CosmicSeed_VetoL3Mu0DxyMax1cm);
   fChain->SetBranchAddress("HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm", &HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm, &b_HLT_DoubleL3dTksMu16_10NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_L3dTksMu10_NoVtx_DxyMin0p01cm", &HLT_L3dTksMu10_NoVtx_DxyMin0p01cm, &b_HLT_L3dTksMu10_NoVtx_DxyMin0p01cm);
   fChain->SetBranchAddress("HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId", &HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId, &b_HLT_Mu20NoFiltersNoVtxDisplaced_Photon20_CaloCustomId);
   fChain->SetBranchAddress("HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1", &HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1, &b_HLT_DoubleMediumChargedIsoDisplacedPFTauHPS32_Trk1_eta2p1);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay1p5To3p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay1p6To3p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay1p75To3p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay3nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay3nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay3nsInclusive);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay3p25nsInclusive);
   fChain->SetBranchAddress("HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive", &HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive, &b_HLT_HT350_DelayedJet40_SingleDelay3p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay0p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay1nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay1nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay1To1p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay1p1To1p6nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay1p25To1p75nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay1p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay2nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay2nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay2nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay2p25nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive", &HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive, &b_HLT_HT430_DelayedJet40_SingleDelay2p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless", &HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless, &b_HLT_HT430_DelayedJet40_SingleDelay0p5nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1nsTrackless", &HLT_HT430_DelayedJet40_SingleDelay1nsTrackless, &b_HLT_HT430_DelayedJet40_SingleDelay1nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless", &HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless, &b_HLT_HT430_DelayedJet40_SingleDelay1p25nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless", &HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless, &b_HLT_HT430_DelayedJet40_SingleDelay1p5nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive", &HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive, &b_HLT_HT430_DelayedJet40_DoubleDelay0p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive", &HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive, &b_HLT_HT430_DelayedJet40_DoubleDelay1nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive", &HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive, &b_HLT_HT430_DelayedJet40_DoubleDelay1p25nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive", &HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive, &b_HLT_HT430_DelayedJet40_DoubleDelay1p5nsInclusive);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless", &HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless, &b_HLT_HT430_DelayedJet40_DoubleDelay0p5nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless", &HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless, &b_HLT_HT430_DelayedJet40_DoubleDelay0p75nsTrackless);
   fChain->SetBranchAddress("HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless", &HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless, &b_HLT_HT430_DelayedJet40_DoubleDelay1nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay2p5To4nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay2p6To4nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay2p75To4nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay3p5nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay3p75nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive", &HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive, &b_HLT_L1Tau_DelayedJet40_SingleDelay4nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless", &HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless, &b_HLT_L1Tau_DelayedJet40_SingleDelay2p5nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless", &HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless, &b_HLT_L1Tau_DelayedJet40_SingleDelay2p75nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless", &HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless, &b_HLT_L1Tau_DelayedJet40_SingleDelay3nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive", &HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive, &b_HLT_L1Tau_DelayedJet40_DoubleDelay0p75nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive", &HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive", &HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive", &HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1p75nsInclusive);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless", &HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless, &b_HLT_L1Tau_DelayedJet40_DoubleDelay0p5nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless", &HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless", &HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1p25nsTrackless);
   fChain->SetBranchAddress("HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless", &HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless, &b_HLT_L1Tau_DelayedJet40_DoubleDelay1p5nsTrackless);
   fChain->SetBranchAddress("HLT_L1Mu6HT240", &HLT_L1Mu6HT240, &b_HLT_L1Mu6HT240);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose", &HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose, &b_HLT_Mu6HT240_DisplacedDijet30_Inclusive1PtrkShortSig5_DisplacedLoose);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5", &HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5, &b_HLT_Mu6HT240_DisplacedDijet35_Inclusive0PtrkShortSig5);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose", &HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose, &b_HLT_Mu6HT240_DisplacedDijet35_Inclusive1PtrkShortSig5_DisplacedLoose);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5", &HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5, &b_HLT_Mu6HT240_DisplacedDijet40_Inclusive0PtrkShortSig5);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose", &HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose, &b_HLT_Mu6HT240_DisplacedDijet40_Inclusive1PtrkShortSig5_DisplacedLoose);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5", &HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5, &b_HLT_Mu6HT240_DisplacedDijet45_Inclusive0PtrkShortSig5);
   fChain->SetBranchAddress("HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5", &HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5, &b_HLT_Mu6HT240_DisplacedDijet50_Inclusive0PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT350", &HLT_HT350, &b_HLT_HT350);
   fChain->SetBranchAddress("HLT_HT425", &HLT_HT425, &b_HLT_HT425);
   fChain->SetBranchAddress("HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT360_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5", &HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5, &b_HLT_HT360_DisplacedDijet45_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT390_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5", &HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5, &b_HLT_HT390_DisplacedDijet45_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT390eta2p0_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT430_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT400_DisplacedDijet40_DisplacedTrack", &HLT_HT400_DisplacedDijet40_DisplacedTrack, &b_HLT_HT400_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT430_DisplacedDijet40_DisplacedTrack", &HLT_HT430_DisplacedDijet40_DisplacedTrack, &b_HLT_HT430_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT550_DisplacedDijet60_Inclusive", &HLT_HT550_DisplacedDijet60_Inclusive, &b_HLT_HT550_DisplacedDijet60_Inclusive);
   fChain->SetBranchAddress("HLT_HT650_DisplacedDijet60_Inclusive", &HLT_HT650_DisplacedDijet60_Inclusive, &b_HLT_HT650_DisplacedDijet60_Inclusive);
   fChain->SetBranchAddress("HLT_CaloMET60_DTCluster50", &HLT_CaloMET60_DTCluster50, &b_HLT_CaloMET60_DTCluster50);
   fChain->SetBranchAddress("HLT_CaloMET60_DTClusterNoMB1S50", &HLT_CaloMET60_DTClusterNoMB1S50, &b_HLT_CaloMET60_DTClusterNoMB1S50);
   fChain->SetBranchAddress("HLT_L1MET_DTCluster50", &HLT_L1MET_DTCluster50, &b_HLT_L1MET_DTCluster50);
   fChain->SetBranchAddress("HLT_L1MET_DTClusterNoMB1S50", &HLT_L1MET_DTClusterNoMB1S50, &b_HLT_L1MET_DTClusterNoMB1S50);
   fChain->SetBranchAddress("HLT_CscCluster_Loose", &HLT_CscCluster_Loose, &b_HLT_CscCluster_Loose);
   fChain->SetBranchAddress("HLT_CscCluster_Medium", &HLT_CscCluster_Medium, &b_HLT_CscCluster_Medium);
   fChain->SetBranchAddress("HLT_CscCluster_Tight", &HLT_CscCluster_Tight, &b_HLT_CscCluster_Tight);
   fChain->SetBranchAddress("HLT_DoubleCscCluster75", &HLT_DoubleCscCluster75, &b_HLT_DoubleCscCluster75);
   fChain->SetBranchAddress("HLT_DoubleCscCluster100", &HLT_DoubleCscCluster100, &b_HLT_DoubleCscCluster100);
   fChain->SetBranchAddress("HLT_L1CSCShower_DTCluster50", &HLT_L1CSCShower_DTCluster50, &b_HLT_L1CSCShower_DTCluster50);
   fChain->SetBranchAddress("HLT_L1CSCShower_DTCluster75", &HLT_L1CSCShower_DTCluster75, &b_HLT_L1CSCShower_DTCluster75);
   fChain->SetBranchAddress("HLT_PFMET105_IsoTrk50", &HLT_PFMET105_IsoTrk50, &b_HLT_PFMET105_IsoTrk50);
   fChain->SetBranchAddress("HLT_L1SingleLLPJet", &HLT_L1SingleLLPJet, &b_HLT_L1SingleLLPJet);
   fChain->SetBranchAddress("HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack", &HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack, &b_HLT_HT170_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack", &HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack, &b_HLT_HT200_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack", &HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack, &b_HLT_HT200_L1SingleLLPJet_DisplacedDijet60_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack", &HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack, &b_HLT_HT270_L1SingleLLPJet_DisplacedDijet40_DisplacedTrack);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5", &HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5, &b_HLT_HT200_L1SingleLLPJet_DisplacedDijet35_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT200_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT240_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5", &HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5, &b_HLT_HT280_L1SingleLLPJet_DisplacedDijet40_Inclusive1PtrkShortSig5);
   fChain->SetBranchAddress("HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive", &HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive, &b_HLT_HT320_L1SingleLLPJet_DisplacedDijet60_Inclusive);
   fChain->SetBranchAddress("HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive", &HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive, &b_HLT_HT420_L1SingleLLPJet_DisplacedDijet60_Inclusive);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless", &HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless, &b_HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay1nsTrackless);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive", &HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive, &b_HLT_HT200_L1SingleLLPJet_DelayedJet40_SingleDelay2nsInclusive);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless", &HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless, &b_HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay0p5nsTrackless);
   fChain->SetBranchAddress("HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive", &HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive, &b_HLT_HT200_L1SingleLLPJet_DelayedJet40_DoubleDelay1nsInclusive);
   fChain->SetBranchAddress("HLT_DiPhoton10Time1ns", &HLT_DiPhoton10Time1ns, &b_HLT_DiPhoton10Time1ns);
   fChain->SetBranchAddress("HLT_DiPhoton10Time1p2ns", &HLT_DiPhoton10Time1p2ns, &b_HLT_DiPhoton10Time1p2ns);
   fChain->SetBranchAddress("HLT_DiPhoton10Time1p4ns", &HLT_DiPhoton10Time1p4ns, &b_HLT_DiPhoton10Time1p4ns);
   fChain->SetBranchAddress("HLT_DiPhoton10Time1p6ns", &HLT_DiPhoton10Time1p6ns, &b_HLT_DiPhoton10Time1p6ns);
   fChain->SetBranchAddress("HLT_DiPhoton10Time1p8ns", &HLT_DiPhoton10Time1p8ns, &b_HLT_DiPhoton10Time1p8ns);
   fChain->SetBranchAddress("HLT_DiPhoton10Time2ns", &HLT_DiPhoton10Time2ns, &b_HLT_DiPhoton10Time2ns);
   fChain->SetBranchAddress("HLT_DiPhoton10sminlt0p1", &HLT_DiPhoton10sminlt0p1, &b_HLT_DiPhoton10sminlt0p1);
   fChain->SetBranchAddress("HLT_DiPhoton10sminlt0p12", &HLT_DiPhoton10sminlt0p12, &b_HLT_DiPhoton10sminlt0p12);
   fChain->SetBranchAddress("HLT_DiPhoton10_CaloIdL", &HLT_DiPhoton10_CaloIdL, &b_HLT_DiPhoton10_CaloIdL);
   fChain->SetBranchAddress("HLT_DoubleEle4_eta1p22_mMax6", &HLT_DoubleEle4_eta1p22_mMax6, &b_HLT_DoubleEle4_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle4p5_eta1p22_mMax6", &HLT_DoubleEle4p5_eta1p22_mMax6, &b_HLT_DoubleEle4p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle5_eta1p22_mMax6", &HLT_DoubleEle5_eta1p22_mMax6, &b_HLT_DoubleEle5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle5p5_eta1p22_mMax6", &HLT_DoubleEle5p5_eta1p22_mMax6, &b_HLT_DoubleEle5p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle6_eta1p22_mMax6", &HLT_DoubleEle6_eta1p22_mMax6, &b_HLT_DoubleEle6_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle6p5_eta1p22_mMax6", &HLT_DoubleEle6p5_eta1p22_mMax6, &b_HLT_DoubleEle6p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle7_eta1p22_mMax6", &HLT_DoubleEle7_eta1p22_mMax6, &b_HLT_DoubleEle7_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle7p5_eta1p22_mMax6", &HLT_DoubleEle7p5_eta1p22_mMax6, &b_HLT_DoubleEle7p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle8_eta1p22_mMax6", &HLT_DoubleEle8_eta1p22_mMax6, &b_HLT_DoubleEle8_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle8p5_eta1p22_mMax6", &HLT_DoubleEle8p5_eta1p22_mMax6, &b_HLT_DoubleEle8p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle9_eta1p22_mMax6", &HLT_DoubleEle9_eta1p22_mMax6, &b_HLT_DoubleEle9_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle9p5_eta1p22_mMax6", &HLT_DoubleEle9p5_eta1p22_mMax6, &b_HLT_DoubleEle9p5_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle10_eta1p22_mMax6", &HLT_DoubleEle10_eta1p22_mMax6, &b_HLT_DoubleEle10_eta1p22_mMax6);
   fChain->SetBranchAddress("HLT_DoubleEle4_eta1p22_mMax6_dz0p8", &HLT_DoubleEle4_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle4_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle4p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle5p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle6_eta1p22_mMax6_dz0p8", &HLT_DoubleEle6_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle6_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle6p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle7_eta1p22_mMax6_dz0p8", &HLT_DoubleEle7_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle7_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle7p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle8_eta1p22_mMax6_dz0p8", &HLT_DoubleEle8_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle8_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle8p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle9_eta1p22_mMax6_dz0p8", &HLT_DoubleEle9_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle9_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8", &HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle9p5_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle10_eta1p22_mMax6_dz0p8", &HLT_DoubleEle10_eta1p22_mMax6_dz0p8, &b_HLT_DoubleEle10_eta1p22_mMax6_dz0p8);
   fChain->SetBranchAddress("HLT_DoubleEle4_eta1p22_mMax6_trkHits10", &HLT_DoubleEle4_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle4_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle4p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle5p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle6_eta1p22_mMax6_trkHits10", &HLT_DoubleEle6_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle6_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle6p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle7_eta1p22_mMax6_trkHits10", &HLT_DoubleEle7_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle7_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle7p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle8_eta1p22_mMax6_trkHits10", &HLT_DoubleEle8_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle8_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle8p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle9_eta1p22_mMax6_trkHits10", &HLT_DoubleEle9_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle9_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10", &HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle9p5_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_DoubleEle10_eta1p22_mMax6_trkHits10", &HLT_DoubleEle10_eta1p22_mMax6_trkHits10, &b_HLT_DoubleEle10_eta1p22_mMax6_trkHits10);
   fChain->SetBranchAddress("HLT_SingleEle8", &HLT_SingleEle8, &b_HLT_SingleEle8);
   fChain->SetBranchAddress("HLT_SingleEle8_SingleEGL1", &HLT_SingleEle8_SingleEGL1, &b_HLT_SingleEle8_SingleEGL1);
   fChain->SetBranchAddress("HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT", &HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT, &b_HLT_Diphoton20_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT", &HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT, &b_HLT_Diphoton20_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT", &HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT, &b_HLT_Diphoton22_14_eta1p5_R9IdL_AND_HE_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT", &HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT, &b_HLT_Diphoton22_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT", &HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT, &b_HLT_Diphoton24_14_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT", &HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT, &b_HLT_Diphoton24_16_eta1p5_R9IdL_AND_HET_AND_IsoTCaloIdT);
   fChain->SetBranchAddress("HLT_Mu50_L1SingleMuShower", &HLT_Mu50_L1SingleMuShower, &b_HLT_Mu50_L1SingleMuShower);
   fChain->SetBranchAddress("HLT_IsoMu24_OneProng32", &HLT_IsoMu24_OneProng32, &b_HLT_IsoMu24_OneProng32);
   fChain->SetBranchAddress("HLT_Photon32_OneProng32_M50To105", &HLT_Photon32_OneProng32_M50To105, &b_HLT_Photon32_OneProng32_M50To105);
   fChain->SetBranchAddress("HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80", &HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80, &b_HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_OneProng_M5to80);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5", &HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5, &b_HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet", &HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet, &b_HLT_VBF_DiPFJet105_40_Mjj1000_Detajj3p5_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5", &HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5, &b_HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet", &HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet, &b_HLT_VBF_DiPFJet110_40_Mjj1000_Detajj3p5_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5", &HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5, &b_HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet", &HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet, &b_HLT_VBF_DiPFJet125_45_Mjj1000_Detajj3p5_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0", &HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0, &b_HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet", &HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet, &b_HLT_VBF_DiPFJet125_45_Mjj720_Detajj3p0_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet", &HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet, &b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet", &HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet, &b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet", &HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet, &b_HLT_VBF_DiPFJet70_40_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet", &HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet, &b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingQuadJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet", &HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet, &b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingFiveJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet", &HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet, &b_HLT_VBF_DiPFJet75_45_Mjj600_Detajj2p5_DiPFJet60_JetMatchingSixJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85", &HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85, &b_HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet", &HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet, &b_HLT_VBF_DiPFJet75_40_Mjj500_Detajj2p5_PFMET85_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85", &HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85, &b_HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet", &HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet, &b_HLT_VBF_DiPFJet80_45_Mjj500_Detajj2p5_PFMET85_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL", &HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL, &b_HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet", &HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet, &b_HLT_VBF_DiPFJet90_40_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL", &HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL, &b_HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet", &HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet, &b_HLT_VBF_DiPFJet95_45_Mjj600_Detajj2p5_Mu3_TrkIsoVVL_TriplePFJet);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1", &HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1, &b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12", &HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12, &b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon12);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17", &HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17, &b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Photon17);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22", &HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22, &b_HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Photon22);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf", &HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf, &b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele12_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf", &HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf, &b_HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_Ele17_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf", &HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf, &b_HLT_VBF_DiPFJet50_Mjj500_Detajj2p5_Ele22_eta2p1_WPTight_Gsf);
   fChain->SetBranchAddress("HLT_PFJet200_TimeLtNeg2p5ns", &HLT_PFJet200_TimeLtNeg2p5ns, &b_HLT_PFJet200_TimeLtNeg2p5ns);
   fChain->SetBranchAddress("HLT_PFJet200_TimeGt2p5ns", &HLT_PFJet200_TimeGt2p5ns, &b_HLT_PFJet200_TimeGt2p5ns);
   fChain->SetBranchAddress("HLT_Photon50_TimeLtNeg2p5ns", &HLT_Photon50_TimeLtNeg2p5ns, &b_HLT_Photon50_TimeLtNeg2p5ns);
   fChain->SetBranchAddress("HLT_Photon50_TimeGt2p5ns", &HLT_Photon50_TimeGt2p5ns, &b_HLT_Photon50_TimeGt2p5ns);
   fChain->SetBranchAddress("HLT_ExpressMuons", &HLT_ExpressMuons, &b_HLT_ExpressMuons);
   fChain->SetBranchAddress("HLT_PPSMaxTracksPerArm1", &HLT_PPSMaxTracksPerArm1, &b_HLT_PPSMaxTracksPerArm1);
   fChain->SetBranchAddress("HLT_PPSMaxTracksPerRP4", &HLT_PPSMaxTracksPerRP4, &b_HLT_PPSMaxTracksPerRP4);
   fChain->SetBranchAddress("HLT_PPSRandom", &HLT_PPSRandom, &b_HLT_PPSRandom);
   fChain->SetBranchAddress("HLTriggerFinalPath", &HLTriggerFinalPath, &b_HLTriggerFinalPath);
   Notify();
}

Bool_t VBFSingleTauCheck::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void VBFSingleTauCheck::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t VBFSingleTauCheck::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef VBFSingleTauCheck_cxx
