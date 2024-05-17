import numpy as np
from cut_ditau_functions import make_ditau_region
from cut_mutau_functions import make_mutau_region
from cut_etau_functions  import make_etau_region
from cut_dimuon_functions  import make_dimuon_region
from FF_dictionary import FF_fit_values, FF_mvis_weights
from calculate_functions import user_exp

def FF_control_flow(final_state_mode, semilep_mode, region, event_dictionary, DeepTau_version):
  if (final_state_mode == "ditau"):
    if (region == "SR"):        event_dictionary   = make_ditau_SR_cut(event_dictionary, DeepTau_version)
    if (region == "AR"):        event_dictionary   = make_ditau_AR_cut(event_dictionary, DeepTau_version)
    if (region == "DRsr"):      event_dictionary   = make_ditau_DRsr_cut(event_dictionary, DeepTau_version)
    if (region == "DRar"):      event_dictionary   = make_ditau_DRar_cut(event_dictionary, DeepTau_version)
    if (region == "SR_aiso"):   event_dictionary   = make_ditau_SR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "AR_aiso"):   event_dictionary   = make_ditau_AR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "DRsr_aiso"): event_dictionary   = make_ditau_DRsr_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "DRar_aiso"): event_dictionary   = make_ditau_DRar_aiso_cut(event_dictionary, DeepTau_version)

  if (final_state_mode == "mutau"):
    if (region == "SR"):      event_dictionary = make_mutau_SR_cut(event_dictionary, DeepTau_version)
    if (region == "AR"):      event_dictionary = make_mutau_AR_cut(event_dictionary, DeepTau_version)
    if (region == "SR_aiso"): event_dictionary = make_mutau_SR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "AR_aiso"): event_dictionary = make_mutau_AR_aiso_cut(event_dictionary, DeepTau_version)

    if (semilep_mode == "QCD"):
      if (region == "DRsr"):      event_dictionary = make_mutau_DRsr_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRar"):      event_dictionary = make_mutau_DRar_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRsr_aiso"): event_dictionary = make_mutau_DRsr_aiso_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRar_aiso"): event_dictionary = make_mutau_DRar_aiso_QCD_cut(event_dictionary, DeepTau_version)

    if (semilep_mode == "WJ"):
      if (region == "DRsr"):      event_dictionary = make_mutau_DRsr_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRar"):      event_dictionary = make_mutau_DRar_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRsr_aiso"): event_dictionary = make_mutau_DRsr_aiso_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRar_aiso"): event_dictionary = make_mutau_DRar_aiso_WJ_cut(event_dictionary, DeepTau_version)

  if (final_state_mode == "etau"):
    if (region == "SR"):      event_dictionary = make_etau_SR_cut(event_dictionary, DeepTau_version)
    if (region == "AR"):      event_dictionary = make_etau_AR_cut(event_dictionary, DeepTau_version)
    if (region == "SR_aiso"): event_dictionary = make_etau_SR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "AR_aiso"): event_dictionary = make_etau_AR_aiso_cut(event_dictionary, DeepTau_version)

    if (semilep_mode == "QCD"):
      if (region == "DRsr"):      event_dictionary = make_etau_DRsr_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRar"):      event_dictionary = make_etau_DRar_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRsr_aiso"): event_dictionary = make_etau_DRsr_aiso_QCD_cut(event_dictionary, DeepTau_version)
      if (region == "DRar_aiso"): event_dictionary = make_etau_DRar_aiso_QCD_cut(event_dictionary, DeepTau_version)

    if (semilep_mode == "WJ"):
      if (region == "DRsr"):      event_dictionary = make_etau_DRsr_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRar"):      event_dictionary = make_etau_DRar_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRsr_aiso"): event_dictionary = make_etau_DRsr_aiso_WJ_cut(event_dictionary, DeepTau_version)
      if (region == "DRar_aiso"): event_dictionary = make_etau_DRar_aiso_WJ_cut(event_dictionary, DeepTau_version)

  if (final_state_mode == "dimuon"):
    if (region == "SR"):      event_dictionary = make_dimuon_SR_cut(event_dictionary)
    else: print("missing region condition")

  return event_dictionary

ditau_DeepTauVsJet_WP = 5
# ditau region cuts
def make_ditau_SR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=-1,
                       pass_DeepTau_t1_req=True, DeepTau_t1_value=ditau_DeepTauVsJet_WP,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=ditau_DeepTauVsJet_WP, 
                       DeepTau_version="2p5")
  return event_dictionary

def make_ditau_AR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_AR_cuts" if iso_region == True else "pass_AR_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=-1,
                       pass_DeepTau_t1_req=False, DeepTau_t1_value=ditau_DeepTauVsJet_WP,
                       pass_DeepTau_t2_req=iso_region,  DeepTau_t2_value=ditau_DeepTauVsJet_WP, 
                       DeepTau_version="2p5")
  return event_dictionary

def make_ditau_DRsr_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=1,
                       pass_DeepTau_t1_req=True, DeepTau_t1_value=ditau_DeepTauVsJet_WP,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=ditau_DeepTauVsJet_WP, 
                       DeepTau_version="2p5")
  return event_dictionary

def make_ditau_DRar_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=1,
                       pass_DeepTau_t1_req=False, DeepTau_t1_value=ditau_DeepTauVsJet_WP,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=ditau_DeepTauVsJet_WP, 
                       DeepTau_version="2p5")
  return event_dictionary

def make_ditau_SR_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_SR_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_AR_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_AR_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_DRsr_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_DRsr_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_DRar_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_DRar_cut(event_dictionary, DeepTau_version, iso_region=False)


mutau_DeepTauVsJet_WP = 5
### begin mutau region cuts
def make_mutau_SR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=[0.00,0.15],
                         pass_DeepTau_req=True, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_AR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_AR_cuts" if iso_region == True else "pass_AR_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=[0.00,0.15],
                         pass_DeepTau_req=False, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_SR_aiso_cut(event_dictionary, DeepTau_version):
  return make_mutau_SR_cut(event_dictionary, DeepTau_version, iso_region=False)
 
def make_mutau_AR_aiso_cut(event_dictionary, DeepTau_version):
  return make_mutau_AR_cut(event_dictionary, DeepTau_version, iso_region=False)
 
### QCD 
def make_mutau_DRsr_QCD_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=[0.05,0.15],
                         pass_DeepTau_req=True, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRar_QCD_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=[0.05,0.15],
                         pass_DeepTau_req=False, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRsr_aiso_QCD_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRsr_QCD_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_aiso_QCD_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_QCD_cut(event_dictionary, DeepTau_version, iso_region=False)

### WJ
def make_mutau_DRsr_WJ_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=[0.0,0.15],
                         pass_DeepTau_req=True, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=False, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRar_WJ_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=[0.0,0.15],
                         pass_DeepTau_req=False, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=False, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRsr_aiso_WJ_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRsr_WJ_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_aiso_WJ_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_WJ_cut(event_dictionary, DeepTau_version, iso_region=False)

### TTBar (not used)
def make_mutau_DRsr_TT_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=True, mu_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=False)
  return event_dictionary

def make_mutau_DRar_TT_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=True, mu_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=mutau_DeepTauVsJet_WP, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=False)
  return event_dictionary

def make_mutau_DRsr_aiso_TT_cut(event_dictionary, DeepTau_version, iso_region):
  return make_mutau_DRsr_TT_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_aiso_TT_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_TT_cut(event_dictionary, DeepTau_version, iso_region=False)


# etau
etau_DeepTauVsJet_WP = 5
def make_etau_SR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary   = make_etau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_el_iso_req=iso_region, el_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=etau_DeepTauVsJet_WP, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_etau_AR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_AR_cuts" if iso_region == True else "pass_AR_aiso_cuts"
  event_dictionary   = make_etau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_el_iso_req=iso_region, el_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=etau_DeepTauVsJet_WP, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_etau_SR_aiso_cut(event_dictionary, DeepTau_version):
  return make_etau_SR_cut(event_dictionary, DeepTau_version, iso_region=False)
 
def make_etau_AR_aiso_cut(event_dictionary, DeepTau_version):
  return make_etau_AR_cut(event_dictionary, DeepTau_version, iso_region=False)

# dimuon
def make_dimuon_SR_cut(event_dictionary, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary     = make_dimuon_region(event_dictionary, name, FS_pair_sign=-1)
  return event_dictionary

# FF weighting
def set_FF_values(final_state_mode, jet_mode_and_DeepTau_version, determining_FF):
  # should have aiso/iso as well
  FF_values = {
    # FS : { "jet_mode" : [intercept, slope] }  
    "ditau" : { 
      # updated March 19th
      "custom_0j_2p5_FF"    :    [0.278,-0.000577],
      "custom_1j_2p5_FF"    :    [0.230,-0.000493],
      "custom_GTE2j_2p5_FF" :    [0.236,-0.000953],
      ### from V12 samples
      #"custom_0j_2p5_FF" :    [0.278,-0.000577],
      #"custom_1j_2p5_FF" :    [0.231,-0.000509],
      #"custom_GTE2j_2p5_FF" :    [0.237,-0.000970],
      #"custom_0j_2p5_FF" :    [0.277605,-0.000507954],
      #"custom_1j_2p5_FF" :    [0.245381,-0.00054067],
      #"custom_GTE2j_2p5_FF" : [0.232493,-0.000626524],

      "custom_0j_2p5_CH" :    [1.03281, 0.000366355], # i think this is an underestimate
      "custom_1j_2p5_CH" :    [1.08724, 3.92753e-05], # same here
      "custom_GTE2j_2p5_CH" : [1.11779, 0.000141817],
      ###
    },
    "mutau" : {  # wrong 2p5
      "0j_2p5"     : [0.037884, 0.000648851],
      "1j_2p5"     : [0.0348384, 0.000630731],
      "GTE2j_2p5"  : [0.0342287, 0.000358899],

      #"custom_0j_2p5_FF" :    [0.0262364,-1.88738e-05], # combined fit, by hand
      #"custom_1j_2p5_FF" :    [0.0262364,-1.88738e-05],
      #"custom_GTE2j_2p5_FF" : [0.0262364,-1.88738e-05],

      #"custom_0j_2p5_FF" :    [0.0790,0.000444], # combined fit, w framework, QCD only
      #"custom_1j_2p5_FF" :    [0.0790,0.000444],
      #"custom_GTE2j_2p5_FF" : [0.0790,0.000444],

      "custom_0j_2p5_FF"    : [0.0827,0.000420], #split by jet, w framework, QCD only
      "custom_1j_2p5_FF"    : [0.110,-0.000591], 
      "custom_GTE2j_2p5_FF" : [0.108,0], # set slope to zero otherwise negative QCD... 

      "custom_0j_2p5_CH"    : [1.1, 0], # ad-hoc scaling
      "custom_1j_2p5_CH"    : [1.1, 0],
      "custom_GTE2j_2p5_CH" : [1.1, 0],

    },
    "etau"  : {#Dummy values
      "0j_2p5"     : [1, 1], 
      "1j_2p5"     : [1, 1],
      "GTE2j_2p5"  : [1, 1],

      "custom_0j_2p5_FF" : [0.0483552, -4.68741e-05], # combined fit, by hand
      "custom_1j_2p5_FF" : [0.0483552, -4.68741e-05],
      "custom_GTE2j_2p5_FF" : [0.0483552, -4.68741e-05],

      "custom_0j_2p5_CH"    : [1.1, 0], # ad-hoc scaling
      "custom_1j_2p5_CH"    : [1.1, 0],
      "custom_GTE2j_2p5_CH" : [1.1, 0],

    },
  } 
  if (determining_FF == True):
    print("determining FF dictionary, setting dummy values and not plotting QCD")
    intercept, slope = 0.2, 1.1
  else:
    intercept = FF_values[final_state_mode][jet_mode_and_DeepTau_version][0]
    slope     = FF_values[final_state_mode][jet_mode_and_DeepTau_version][1]
    #slope2    = FF_values[final_state_mode][jet_mode_and_DeepTau_version][2]

  #return intercept, slope, slope2
  return intercept, slope


def old_add_FF_weights(event_dictionary, final_state_mode, jet_mode, DeepTau_version, determining_FF=False, bypass=None):
  unpack_FFVars = ["Lepton_pt", "HTT_m_vis", "l1_indices", "l2_indices"]
  unpack_FFVars = (event_dictionary.get(key) for key in unpack_FFVars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_FFVars]
  FF_weights = []
  bins = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 250, 300]
  ditau_weight_map = {
    # these are all very close to 0.999, which means in the most pessimistic case
    # you lose 10 events in every 10000 events.
    # since we have at most 90000 events in the 0j case, the biggest error we can have is
    # 90 events. This is not big enough to effect plots dramatically, so as long as the
    # probs are close to 0.999, they don't need to be updated every time
    # SHOULD update them the final time
    "Inclusive_2p5" : [bins, # estimated, values not derived
                 [0.999, # < 50
                  0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999,
                  0.999, 0.999, 0.999, 0.999, 0.999, 0.999, 0.999,
                  0.999, 0.999, 0.999]], # > 200
    "0j_2p5" : [bins,
          [0.998869, # < 50
           0.999233, 0.999735, 0.999866, 0.999873, 0.999901, 0.999944, 0.999944, 0.999939, 
           0.999930, 0.999924, 0.999921, 0.999913, 0.999900, 0.999899, 0.999885, 
           0.999871, 0.999826, 0.999691]], # > 200
    "1j_2p5" : [bins,
          [0.999676, 
           0.999512, 0.999607, 0.999771, 0.999810, 0.999827, 0.999864, 0.999851, 0.999826, 
           0.999807, 0.999795, 0.999776, 0.999775, 0.999743, 0.999740, 0.999726, 
           0.999700, 0.999630, 0.999492]],
    "GTE2j_2p5" : [bins,
          [0.999411, 
           0.999046, 0.999038, 0.999246, 0.999336, 0.999382, 0.999425, 0.999362, 0.999296, 
           0.999252, 0.999181, 0.999143, 0.999101, 0.999101, 0.999038, 0.999003, 
           0.998991, 0.998904, 0.998680]],
    "0j_2p1" : [bins,
          [0.996032, 
           0.997514, 0.999023, 0.999554, 0.999771, 0.999772, 0.999850, 0.999858, 
           0.999850, 0.999843, 0.999824, 0.999811, 0.999792, 0.999783, 0.999781, 0.999735, 
           0.999683, 0.999594, 0.999428]],
    "1j_2p1" : [bins,
          [0.998659, 
           0.998212, 0.998626, 0.999254, 0.999635, 0.999633, 0.999658, 0.999630, 
           0.999600, 0.999549, 0.999526, 0.999469, 0.999428, 0.999394, 0.999348, 0.999345, 
           0.999223, 0.999137, 0.998901]],
    "GTE2j_2p1" : [bins,
          [0.997985, 
           0.997208, 0.997390, 0.998144, 0.998912, 0.998832, 0.998663, 0.998491, 
           0.998358, 0.998206, 0.998065, 0.998010, 0.997843, 0.997769, 0.997668, 0.997625, 
           0.997477, 0.997151, 0.997048]],
  }
  
  FF_key = jet_mode + "_" + DeepTau_version

  if (bypass != None):
    intercept = bypass[0]
    slope     = bypass[1]
    OSSS_bias_intercept = bypass[2]
    OSSS_bias_slope     = bypass[3]
    ditau_weight_map[FF_key] = {}
    ditau_weight_map[FF_key] = [bins,[1 for i in range(18)]]

  else:
    intercept, slope = set_FF_values(final_state_mode, "custom_"+jet_mode+"_2p5_FF", determining_FF)
    OSSS_bias_intercept, OSSS_bias_slope = set_FF_values(final_state_mode, "custom_"+jet_mode+"_2p5_CH", determining_FF)

  #intercept, slope = set_FF_values("ditau", FF_key)
  #closure_intercept, closure_slope = set_FF_values("ditau", "Closure_" + DeepTau_version)
  #OSSS_bias_intercept, OSSS_bias_slope = set_FF_values("ditau", "OSSS_Bias_" + DeepTau_version)

  #intercept, slope, slope2 = set_FF_values("ditau", "custom_"+jet_mode+"_2p5_check_FF")
  #closure_intercept, closure_slope, closure_slope2 = set_FF_values("ditau", "custom_"+jet_mode+"_2p5_check_Clos")
  #OSSS_bias_intercept, OSSS_bias_slope, OSSS_bias_slope2 = set_FF_values("ditau", "custom_"+jet_mode+"_2p5_check_CH")

  for i, lep_pt, m_vis, l1_idx, l2_idx in zip(*to_check):
    if m_vis < bins[0]: # 50
      one_minus_MC_over_data_weight = ditau_weight_map[FF_key][1][0] # first weight
    elif m_vis > bins[-3]: # > 200
      if m_vis > bins[-1]: # > 300
        one_minus_MC_over_data_weight = ditau_weight_map[FF_key][1][-1] # last weight
      elif bins[-2] < m_vis < bins[-1]: # between 250 and 300
        one_minus_MC_over_data_weight = ditau_weight_map[FF_key][1][-2]
      elif bins[-3] < m_vis < bins[-2]: # between 200 and 250
        one_minus_MC_over_data_weight = ditau_weight_map[FF_key][1][-3]
    else: # mvis between 50 and 200
      m_vis_idx = int(m_vis // 10) - 5 # makes 50 bin zero idx
      m_vis_weight_idx = m_vis_idx + 1 # 0 in weights is < 50 weight
      one_minus_MC_over_data_weight = ditau_weight_map[FF_key][1][m_vis_weight_idx]

    #l1_pt = lep_pt[l1_idx] if lep_pt[l1_idx] < 120.0 else 120.0
    #l2_pt = lep_pt[l2_idx] if lep_pt[l2_idx] < 200.0 else 200.0
    l1_pt = lep_pt[l1_idx]
    l2_pt = lep_pt[l2_idx]
    m_vis = m_vis if m_vis < 350.0 else 350.0
    FF_weight = one_minus_MC_over_data_weight*(intercept + l1_pt * slope)
    #FF_weight *= (closure_intercept + lep_pt[l2_idx] * closure_slope)
    FF_weight *= (OSSS_bias_intercept + m_vis * OSSS_bias_slope)

    #FF_weight = one_minus_MC_over_data_weight*(intercept + l1_pt * slope + l1_pt*l1_pt*slope2)
    #FF_weight *= (closure_intercept + l2_pt * closure_slope + l2_pt*l2_pt*closure_slope2)
    #FF_weight *= (OSSS_bias_intercept + m_vis * OSSS_bias_slope + m_vis*m_vis*OSSS_bias_slope2)

    FF_weights.append(FF_weight)
  event_dictionary["FF_weight"] = np.array(FF_weights)
  return event_dictionary

def add_FF_weights(event_dictionary, final_state_mode, jet_mode, semilep_mode, full_FF, closure=False, testing=True, bypass=[]):
  # interface to read FF_dictionary
  unpack_FF_vars = ["Lepton_pt", "HTT_m_vis", "l1_indices", "l2_indices"]
  unpack_FF_vars = (event_dictionary.get(key) for key in unpack_FF_vars)
  to_check = [range(len(event_dictionary["Lepton_pt"])), *unpack_FF_vars]
  FF_weights = []
  jet_mode = jet_mode + "_testing" if testing else jet_mode
  QCD_fitvals   = FF_fit_values[final_state_mode][jet_mode]["QCD"]
  WJ_fitvals   = FF_fit_values[final_state_mode][jet_mode]["WJ"]
  if bypass != []:  QCD_fitvals, WJ_fitvals = bypass, bypass
  for i, lep_pt, m_vis, l1_idx, l2_idx in zip(*to_check):
    #FF_weight = 1
    m_vis = m_vis if m_vis < 300.0 else 299.0 # exactly 300 breaks index hack below
    l1_pt = lep_pt[l1_idx]
    l1_pt = l1_pt if l1_pt > 32.5 else 32.5 # using midpoint value of fit (lowest nonzero...)
    m_vis_idx = int(m_vis // 10) # hard-coding mvis bins of 10 GeV, starting at 0 and ending at 300 ( // is modulo division )
    f_QCD     = FF_mvis_weights[final_state_mode][jet_mode]["QCD"][m_vis_idx] if not closure else 1
    FF_QCD    = user_exp(l1_pt, *QCD_fitvals)
    if (final_state_mode != "ditau"): # else pass
      f_WJ       = FF_mvis_weights[final_state_mode][jet_mode]["WJ"][m_vis_idx] if not closure else 1
      FF_WJ      = user_exp(l1_pt, *WJ_fitvals)
    else: pass
    if (full_FF == True):
      FF_weight = f_QCD * FF_QCD
      if (final_state_mode != "ditau"):
        FF_weight += f_WJ * FF_WJ
    else: 
      if   (semilep_mode == "QCD"):  FF_weight = f_QCD * FF_QCD
      elif (semilep_mode == "WJ"):   FF_weight = f_WJ  * FF_WJ
      else: print("add_FF_weights function error")
    if (FF_weight <= 0):
      print("negative FF weights!")
      print("FF_weight: ", FF_weight)
      print("l1_pt: ", l1_pt)
      print("value from fit: ", user_exp(lep_pt[l1_idx], *QCD_fitvals))
      print("m_vis, m_vis_idx: ", m_vis, m_vis_idx)
    FF_weights.append(FF_weight)
  event_dictionary["FF_weight"] = np.array(FF_weights)
  return event_dictionary





