#define VBFSingleTauCheck_cxx
#include "VBFSingleTauCheck.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>

float PI = 3.14159265;
float phi_mpi_pi(float input_phi){
  float output_phi = -999;
  // put phi in range [-PI, PI]
  if (input_phi > PI) { output_phi = 2*PI - input_phi; }
  else if (input_phi < -1*PI) { output_phi = 2*PI + input_phi; }
  else { output_phi = input_phi; }
  return output_phi;
}

float deltaR (float eta1, float eta2, float phi1, float phi2) {
  float delta_eta = eta1 - eta2;
  float delta_phi_raw = phi1 - phi2;
  float delta_phi = phi_mpi_pi(delta_phi_raw);
  float dR = sqrt(delta_eta*delta_eta + delta_phi*delta_phi);
  return dR;
}

void VBFSingleTauCheck::Loop()
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   int count_weird = 0;

   int good_objects = 0;
   int matched_to_hlt = 0;

   // singles
   int pass_DiTau_count   = 0;
   int pass_VBF1Tau_count = 0;
   int pass_VBF2Tau_count = 0;
   int pass_VBFInc_count  = 0;
   // doubles
   int pass_DiTau_VBF1Tau_count   = 0;
   int pass_DiTau_VBF2Tau_count   = 0;
   int pass_DiTau_VBFInc_count    = 0;
   int pass_VBF1Tau_VBF2Tau_count = 0;
   int pass_VBF1Tau_VBFInc_count  = 0;
   int pass_VBF2Tau_VBFInc_count  = 0;
   // triples
   int pass_DiTau_VBF1Tau_VBF2Tau_count  = 0;
   int pass_DiTau_VBF1Tau_VBFInc_count   = 0;
   int pass_DiTau_VBF2Tau_VBFInc_count   = 0;
   int pass_VBF1Tau_VBF2Tau_VBFInc_count = 0;

   int pass_all_count       = 0;
   int pass_any_count       = 0;

   bool pass_DiTau_bool   = false;
   bool pass_VBF1Tau_bool = false;
   bool pass_VBF2Tau_bool = false;
   bool pass_VBFInc_bool  = false;

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;

      if (ientry % 1000000 == 0) std::cout << "Entry: " << ientry << std::endl;

      // MET filters, nLeptons, Trigger
      
      bool pass_METfilters = (Flag_METFilters > 0.5);
      if (!(pass_METfilters)) continue;

      bool pass_nLeptons = (nTau >= 2);
      if (!(pass_nLeptons)) continue;

      bool pass_triggers = ( (L1_DoubleIsoTau34er2p1 && HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1) || \
                            //HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 || \
                            //
                            (HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1) );
                            //
                            //HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 || \
                            //
                            //(L1_DoubleJet_110_35_DoubleJet35_Mass_Min620 && HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1));
                            //(L1_DoubleJet_110_35_DoubleJet35_Mass_Min800 && HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1));
      if (!(pass_triggers)) continue;

      // now define offline object collections
      vector<int> looseTaus;
      for (auto i_tau = 0; i_tau < nTau; i_tau++) {
        bool pass_loose_tau_kinem = (Tau_pt[i_tau] > 20 &&\
                                     abs(Tau_eta[i_tau]) < 2.5 &&\
                                     abs(Tau_dz[i_tau]) < 0.2);
        bool pass_tau_decayMode   = (Tau_decayMode[i_tau] == 0 || Tau_decayMode[i_tau] == 1 ||\
                                     Tau_decayMode[i_tau] == 2 ||\
                                     Tau_decayMode[i_tau] == 10 || Tau_decayMode[i_tau] == 11);
        bool pass_tau_charge      = (abs(Tau_charge[i_tau]) == 1);
        bool pass_loose_tau_ID    = (Tau_idDeepTau2018v2p5VSe[i_tau] >= 1 &&  // VVVLoose
                                     Tau_idDeepTau2018v2p5VSmu[i_tau] >= 1 && // VLoose
                                     Tau_idDeepTau2018v2p5VSjet[i_tau] >= 5); // Medium  // 1 // VVLoose
        if (pass_loose_tau_kinem && pass_tau_decayMode &&\
            pass_tau_charge && pass_loose_tau_ID) {looseTaus.push_back(i_tau);}
      }
      if (looseTaus.size() < 2) continue;
      //if (looseTaus.size() > 2) std::cout << "3 or more taus" << std::endl;

      vector<int> looseJets;
      for (auto i_jet = 0; i_jet < nJet; i_jet++) {
        bool pass_loose_jet_kinem = (Jet_pt[i_jet] > 30 && abs(Jet_eta[i_jet]) < 4.7);
        if (pass_loose_jet_kinem) {looseJets.push_back(i_jet);}
      }
      if (looseJets.size() < 2) continue;

      //std::cout << looseJets.size() << " " << looseTaus.size() << std::endl;
      // much simpler than cross-cleaning, find your two best jets and then make sure none of the 4 objects overlap
      float mjj = -999;
      int best_j1 = -1;
      int best_j2 = -1;
      for (auto j_jet = 0; j_jet < looseJets.size(); j_jet++) {
        for (auto k_jet = 0; k_jet < looseJets.size(); k_jet++) {
          if (k_jet <= j_jet) continue;
          TLorentzVector j1;
          TLorentzVector j2;
          j1.SetPtEtaPhiM(Jet_pt[j_jet], Jet_eta[j_jet], Jet_phi[j_jet], Jet_mass[j_jet]);
          j2.SetPtEtaPhiM(Jet_pt[k_jet], Jet_eta[k_jet], Jet_phi[k_jet], Jet_mass[k_jet]);
          float temp_mjj = (j1+j2).M();
          if (temp_mjj > mjj) {
            mjj = temp_mjj;
            best_j1 = j_jet;
            best_j2 = k_jet;
          }
        }
      }
      TLorentzVector sel_j1;
      TLorentzVector sel_j2;
      TLorentzVector sel_t1;
      TLorentzVector sel_t2;
      sel_j1.SetPtEtaPhiM(Jet_pt[best_j1], Jet_eta[best_j1], Jet_phi[best_j1], Jet_mass[best_j1]);
      sel_j2.SetPtEtaPhiM(Jet_pt[best_j2], Jet_eta[best_j2], Jet_phi[best_j2], Jet_mass[best_j2]);
      sel_t1.SetPtEtaPhiM(Tau_pt[0], Tau_eta[0], Tau_phi[0], Tau_mass[0]);
      sel_t2.SetPtEtaPhiM(Tau_pt[1], Tau_eta[1], Tau_phi[1], Tau_mass[1]);

      if ( (sel_j1.DeltaR(sel_j2) < 0.5) || (sel_j1.DeltaR(sel_t1) < 0.5) || (sel_j1.DeltaR(sel_t2) < 0.5) ) continue;
      if ( (sel_j2.DeltaR(sel_t1) < 0.5) || (sel_j2.DeltaR(sel_t2) < 0.5) ) continue;
      if ( (sel_t1.DeltaR(sel_t2) < 0.5) ) continue;

      if (Tau_charge[0]*Tau_charge[1] != -1) continue;

      good_objects += 1;

      bool do_matching = true;
      if (do_matching)
      {
      // match to HLT
      // build container of trig objects, match each object, skip event if no match. Fair?
      std::vector<TLorentzVector> matched_TrigObjs;
      bool j1_matched = false;
      bool j2_matched = false;
      bool t1_matched = false;
      bool t2_matched = false;
      int  j1_trigIdx = -1;
      int  j2_trigIdx = -1;
      int  t1_trigIdx = -1;
      int  t2_trigIdx = -1;
      for (auto i_obj = 0; i_obj < nTrigObj; i_obj++) {
        TLorentzVector temp_TrigObj;
        // only the dR cone is used, so the 0 in the mass is not an issue for this use
        if ( !((TrigObj_id[i_obj] == 1) || (TrigObj_id[i_obj] == 15)) ) continue; // require jet or tau hlt object
        temp_TrigObj.SetPtEtaPhiM(TrigObj_pt[i_obj], TrigObj_eta[i_obj], TrigObj_phi[i_obj], 0);

        // trigger bits for jets
        // 18 -- VBF Inc double jet filter
        // 19 -- VBF DiTau/SingleTau double jet cross cleaned from tau(s) filter
        // trigger bits for taus
        // 10 -- DiTau
        // 29 -- VBF1Tau and VBF2Tau leading tau
        // XX -- no filterbit for VBF2Tau subleading tau
        // XX -- no filterbit for VBFInc taus
        // VBF 2Tau non-covered filter for subleading tau
        // hltHpsDoublePFTau20MediumDitauWPDeepTauNoMatch
        // VBF Inc non-covered final filter for taus
        // hltHpsDoublePFTau20TrackDeepTauDitauWPAgainstMuon
          
        // attempt match to all 4 objects, put in container if matched, and prevent from being matched more than once
        // check dR, //then check if a relevant filterbit is passed
        if ( (sel_j1.DeltaR(temp_TrigObj) < 0.5) && (!j1_matched) ) {
          int trig_filterbit = TrigObj_filterBits[i_obj];
          //if ( (trig_filterbit == (1 << 18)) || (trig_filterbit == (1 << 19)) ) {
            matched_TrigObjs.push_back(temp_TrigObj); 
            j1_matched = true;
            j1_trigIdx = i_obj;
          //}
        }
        else if ( (sel_j2.DeltaR(temp_TrigObj) < 0.5) && (!j2_matched) ) {
          int trig_filterbit = TrigObj_filterBits[i_obj];
          //if ( (trig_filterbit == (1 << 18)) || (trig_filterbit == (1 << 19)) ) {
            matched_TrigObjs.push_back(temp_TrigObj); 
            j2_matched = true;
            j2_trigIdx = i_obj;
          //}
        }
        else if ( (sel_t1.DeltaR(temp_TrigObj) < 0.5) && (!t1_matched) ) {
          int trig_filterbit = TrigObj_filterBits[i_obj];
          //if ( (trig_filterbit == (1 << 3)) || (trig_filterbit == (1 << 10)) || (trig_filterbit == (1 << 29)) ) {
            matched_TrigObjs.push_back(temp_TrigObj);
            t1_matched = true;
            t1_trigIdx = i_obj;
          //}
        }
        else if ( (sel_t2.DeltaR(temp_TrigObj) < 0.5) && (!t2_matched) ) {
          int trig_filterbit = TrigObj_filterBits[i_obj];
          //if ( (trig_filterbit == (1 << 3)) || (trig_filterbit == (1 << 10)) || (trig_filterbit == (1 << 29)) ) {
            matched_TrigObjs.push_back(temp_TrigObj);
            t2_matched = true;
            t2_trigIdx = i_obj;
          //}
        }

      }
      // without all filter bits available, this is the best we can do.
      // This is basically implicitly assuming 100% HLT efficiency, since we match an
      // object and require a trigger, but don't require the filterbit.
      // Meaning the object could have come from some unrelated trigger that also fired
      // and simply isn't considered here. Although I assume that probably isn't happening
      // very often since we've already restricted to 2tau-2jet events.
      //std::cout << matched_TrigObjs.size() << std::endl; // always between 2 and 4
      
      int nMatchedTrigObjs = matched_TrigObjs.size();
      // should be minimum 2 if only DiTau fired
      if ( (HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1) &&\
           !(HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1) &&\
           !(HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1) &&\
           !(HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1) ) {
        /*
        // sometimes there are DiTau events with 3 or 4 trigger matched objects, likely jet fakes
        // not looking into further at this time
        if (nMatchedTrigObjs != 2) {
          std::cout << "weird DiTau event: " << nMatchedTrigObjs << std::endl;
          std::cout << \
          "DiTau:   " << HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1 << '\n' << \
          "VBF1Tau: " << HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 << '\n' << \
          "VBF2Tau: " << HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          "VBFInc:  " << HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          //
          std::endl;
        }
        */
        if (nMatchedTrigObjs < 2) continue;
      }
      // should be minimum 3 if VBFSingleTau fired
      else if (HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1) {
        /*
        // often, VBF2Tau or VBFInc fires with VBF1Tau, and 4 objects are matched
        if (nMatchedTrigObjs != 3) {
          std::cout << "weird VBF1Tau event: " << nMatchedTrigObjs << std::endl;
          std::cout << \
          "DiTau:   " << HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1 << '\n' << \
          "VBF1Tau: " << HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 << '\n' << \
          "VBF2Tau: " << HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          "VBFInc:  " << HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          //
          std::endl;
        }
        */
        if (nMatchedTrigObjs < 3) continue;
      }
      // should be minimum 4 if VBFDiTau or VBFInc fired
      else if ( (HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1) ||\
                (HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1) ) {
        /*
        if (nMatchedTrigObjs != 4) {
        // 32 times in 177000 events, one of these triggers is fired but only 3 objs are matched
        // assuming reconstruction effect, not looking into further at this time
          count_weird += 1;
          std::cout << "weird VBF2Tau/VBFInc event: " << nMatchedTrigObjs << std::endl;
          std::cout << \
          "DiTau:   " << HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1 << '\n' << \
          "VBF1Tau: " << HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 << '\n' << \
          "VBF2Tau: " << HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          "VBFInc:  " << HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
          //
          std::endl;
        }
        */
        if (nMatchedTrigObjs < 4) continue;
      }
      else {
        // never prints, all cases covered
        std::cout << "unhandled event, objs = " << nMatchedTrigObjs << std::endl;
        std::cout << \
        "DiTau:   " << HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1 << '\n' << \
        "VBF1Tau: " << HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 << '\n' << \
        "VBF2Tau: " << HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
        "VBFInc:  " << HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1 << '\n' << \
        //
        std::endl;
      }
      }
      
      matched_to_hlt += 1;

      float t1_pt = sel_t1.Pt();
      float t2_pt = sel_t2.Pt();
      float j1_pt = sel_j1.Pt();
      float j2_pt = sel_j2.Pt();
      float detajj = abs(sel_j1.Eta() - sel_j2.Eta());


      // full offline selection
      // since the VBF1Tau trigger requires a detajj cut in this sample,
      // we apply the same cut to every trigger to get a fair comparison.
      // For 2024, that cut won't be in place. Louis and Olivier have previously
      // studied the detajj cut and determined it doesn't make a large difference.
     
      // HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1
      pass_DiTau_bool = false;
      if (HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1 &&\
          (t1_pt > 40) && (t2_pt > 40) && (j1_pt > 30) && (j2_pt > 30) && (mjj > 600) && (detajj > 2.5)) {
          //(t1_pt > 40) && (t2_pt > 40) && (j1_pt > 30) && (j2_pt > 30) && (mjj > 600)) { // no detajj
        pass_DiTau_bool = true;
        pass_DiTau_count += 1;
      }

      // HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1
      // note Mia also proposed a tighter trigger
      pass_VBF1Tau_bool = false;
      if (HLT_VBF_DiPFJet45_Mjj500_Detajj2p5_MediumDeepTauPFTauHPS45_L2NN_eta2p1 &&\
          //(t1_pt > 50) && (t2_pt > 25) && (j1_pt > 55) && (j2_pt > 55) && (mjj > 600) && (detajj > 2.5)) {
          //(t1_pt > 50) && (t2_pt > 25) && (j1_pt > 60) && (j2_pt > 60) && (mjj > 700) && (detajj > 2.5)) {
          (t1_pt > 50) && (t2_pt > 25) && (j1_pt > 60) && (j2_pt > 60) && (mjj > 750) && (detajj > 2.5)) {
        pass_VBF1Tau_bool = true;
        pass_VBF1Tau_count += 1;
      }

      // HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1
      pass_VBF2Tau_bool = false;
      if (HLT_DoublePFJets40_Mass500_MediumDeepTauPFTauHPS45_L2NN_MediumDeepTauPFTauHPS20_eta2p1 &&\
          (t1_pt > 50) && (t2_pt > 25) && (j1_pt > 50) && (j2_pt > 50) && (mjj > 600) && (detajj > 2.5)) {
          //(t1_pt > 50) && (t2_pt > 25) && (j1_pt > 50) && (j2_pt > 50) && (mjj >600)) { // no detajj
        pass_VBF2Tau_bool = true;
        pass_VBF2Tau_count += 1;
      }

      // HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1
      // note Mia also proposed a tighter L1 
      pass_VBFInc_bool = false;
      if (HLT_VBF_DoubleMediumDeepTauPFTauHPS20_eta2p1 &&\
          //L1_DoubleJet_110_35_DoubleJet35_Mass_Min620 && \
          //
          L1_DoubleJet_110_35_DoubleJet35_Mass_Min800 && \
          //
          //(t1_pt > 25) && (t2_pt > 25) && (j1_pt > 120) && (j2_pt > 45) && (mjj >700) && (detajj > 2.5)) {
          (t1_pt > 25) && (t2_pt > 25) && (j1_pt > 120) && (j2_pt > 45) && (mjj >850) && (detajj > 2.5)) {
          //(t1_pt > 25) && (t2_pt > 25) && (j1_pt > 120) && (j2_pt > 45) && (mjj >700)) { // no detajj
          //(t1_pt > 25) && (t2_pt > 25) && (j1_pt > 120) && (j2_pt > 45) && (mjj >850)) { // no detajj
        pass_VBFInc_bool = true;
        pass_VBFInc_count += 1;
      }


      // Total OR/AND
      if ((pass_DiTau_bool) && (pass_VBF1Tau_bool) && (pass_VBF2Tau_bool) && (pass_VBFInc_bool)) pass_all_count += 1;
      if ((pass_DiTau_bool) || (pass_VBF1Tau_bool) || (pass_VBF2Tau_bool) || (pass_VBFInc_bool)) pass_any_count += 1;
 
      // Double ORs
      if ((pass_DiTau_bool) || (pass_VBF1Tau_bool)) pass_DiTau_VBF1Tau_count += 1;
      if ((pass_DiTau_bool) || (pass_VBF2Tau_bool)) pass_DiTau_VBF2Tau_count += 1;
      if ((pass_DiTau_bool) || (pass_VBFInc_bool))  pass_DiTau_VBFInc_count  += 1;
      if ((pass_VBF1Tau_bool) || (pass_VBF2Tau_bool))  pass_VBF1Tau_VBF2Tau_count += 1;
      if ((pass_VBF1Tau_bool) || (pass_VBFInc_bool))   pass_VBF1Tau_VBFInc_count  += 1;
      if ((pass_VBF2Tau_bool) || (pass_VBFInc_bool))   pass_VBF2Tau_VBFInc_count  += 1;
      
      // Triple ORs
      if ((pass_DiTau_bool) || (pass_VBF1Tau_bool) || (pass_VBF2Tau_bool))  pass_DiTau_VBF1Tau_VBF2Tau_count += 1;
      if ((pass_DiTau_bool) || (pass_VBF1Tau_bool) || (pass_VBFInc_bool))   pass_DiTau_VBF1Tau_VBFInc_count += 1;
      if ((pass_DiTau_bool) || (pass_VBF2Tau_bool) || (pass_VBFInc_bool))   pass_DiTau_VBF2Tau_VBFInc_count += 1;
      if ((pass_VBF1Tau_bool) || (pass_VBF2Tau_bool) || (pass_VBFInc_bool)) pass_VBF1Tau_VBF2Tau_VBFInc_count += 1;

   }
   std::cout << "pass loose offline selection: " << good_objects << std::endl;
   std::cout << "\"matched\" to hlt:           " << matched_to_hlt << std::endl;
   std::cout << "nWeird VBF2Tau/VBFInc events: " << count_weird << std::endl;
   std::cout << \
   "PASS ALL (4-AND): " << pass_all_count << '\n' << \
   "PASS ANY (4-OR) : " << pass_any_count << '\n' << \
   "PASS DiTau:   " << pass_DiTau_count << '\n' << \
   "PASS VBF1Tau: " << pass_VBF1Tau_count << '\n' << \
   "PASS VBF2Tau: " << pass_VBF2Tau_count << '\n' << \
   "PASS VBFInc:  " << pass_VBFInc_count << '\n' << \
   "DOUBLE ORs" << '\n' << \
   "PASS DiTau OR VBF1Tau:   " << pass_DiTau_VBF1Tau_count << '\n' << \
   "PASS DiTau OR VBF2Tau:   " << pass_DiTau_VBF2Tau_count << '\n' << \
   "PASS DiTau OR VBFInc:    " << pass_DiTau_VBFInc_count << '\n' << \
   "PASS VBF1Tau OR VBF2Tau: " << pass_VBF1Tau_VBF2Tau_count << '\n' << \
   "PASS VBF1Tau OR VBFInc:  " << pass_VBF1Tau_VBFInc_count << '\n' << \
   "PASS VBF2Tau OR VBFInc:  " << pass_VBF2Tau_VBFInc_count << '\n' << \
   "TRIPLE ORs" << '\n' << \
   "PASS DiTau OR VBF1Tau OR VBF2Tau:  " << pass_DiTau_VBF1Tau_VBF2Tau_count << '\n' << \
   "PASS DiTau OR VBF1Tau OR VBFInc:   " << pass_DiTau_VBF1Tau_VBFInc_count << '\n' << \
   "PASS DiTau OR VBF2Tau OR VBFInc:   " << pass_DiTau_VBF2Tau_VBFInc_count << '\n' << \
   "PASS VBF1Tau OR VBF2Tau OR VBFInc: " << pass_VBF1Tau_VBF2Tau_VBFInc_count << '\n' << \
   "UNIQUE COUNTS" << '\n' << \
   "PASS DiTau   Unique: " << pass_any_count - pass_VBF1Tau_VBF2Tau_VBFInc_count << '\n' << \
   "PASS VBF1Tau Unique: " << pass_any_count - pass_DiTau_VBF2Tau_VBFInc_count << '\n' << \
   "PASS VBF2Tau Unique: " << pass_any_count - pass_DiTau_VBF1Tau_VBFInc_count << '\n' << \
   "PASS VBFInc  Unique: " << pass_any_count - pass_DiTau_VBF1Tau_VBF2Tau_count << '\n' << \
   //
   std::endl;

}
