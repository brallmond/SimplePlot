from cut_ditau_functions import make_ditau_region
from cut_mutau_functions import make_mutau_region
from cut_etau_functions  import make_etau_region
from cut_dimuon_functions  import make_dimuon_region

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

