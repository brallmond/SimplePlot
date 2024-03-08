from cut_ditau_functions import make_ditau_region
from cut_mutau_functions import make_mutau_region

def FF_control_flow(final_state_mode, semilep_mode, region, event_dictionary, DeepTau_version):
  if (final_state_mode == "ditau"):
    if (region == "AR"):        event_dictionary   = make_ditau_AR_cut(event_dictionary, DeepTau_version)
    if (region == "DRsr"):      event_dictionary   = make_ditau_DRsr_cut(event_dictionary, DeepTau_version)
    if (region == "DRar"):      event_dictionary   = make_ditau_DRar_cut(event_dictionary, DeepTau_version)
    if (region == "SR_aiso"):   event_dictionary   = make_ditau_SR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "AR_aiso"):   event_dictionary   = make_ditau_AR_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "DRsr_aiso"): event_dictionary   = make_ditau_DRsr_aiso_cut(event_dictionary, DeepTau_version)
    if (region == "DRar_aiso"): event_dictionary   = make_ditau_DRar_aiso_cut(event_dictionary, DeepTau_version)

  if (final_state_mode == "mutau"):
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

  return event_dictionary

# ditau region cuts
def make_ditau_SR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=-1,
                       pass_DeepTau_t1_req=True, DeepTau_t1_value=5,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=5, DeepTau_version="2p5")
  return event_dictionary

def make_ditau_AR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_AR_cuts" if iso_region == True else "pass_AR_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=-1,
                       pass_DeepTau_t1_req=False, DeepTau_t1_value=5,
                       pass_DeepTau_t2_req=iso_region,  DeepTau_t2_value=5, DeepTau_version="2p5")
  return event_dictionary

def make_ditau_DRsr_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=1,
                       pass_DeepTau_t1_req=True, DeepTau_t1_value=5,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=5, DeepTau_version="2p5")
  return event_dictionary

def make_ditau_DRar_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary = make_ditau_region(event_dictionary, name, FS_pair_sign=1,
                       pass_DeepTau_t1_req=False, DeepTau_t1_value=5,
                       pass_DeepTau_t2_req=iso_region, DeepTau_t2_value=5, DeepTau_version="2p5")
  return event_dictionary

def make_ditau_SR_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_SR_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_AR_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_AR_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_DRsr_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_DRsr_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_ditau_DRar_aiso_cut(event_dictionary, DeepTau_version):
  return make_ditau_DRar_cut(event_dictionary, DeepTau_version, iso_region=False)


### begin mutau region cuts
def make_mutau_AR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_AR_cuts" if iso_region == True else "pass_AR_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=5, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_AR_aiso_cut(event_dictionary, DeepTau_version):
  return make_mutau_AR_cut(event_dictionary, DeepTau_version, iso_region=False)
 

def make_mutau_SR_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_SR_cuts" if iso_region == True else "pass_SR_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name, 
                         FS_pair_sign=-1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=5, DeepTau_version=DeepTau_version,
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_SR_aiso_cut(event_dictionary, DeepTau_version):
  return make_mutau_SR_cut(event_dictionary, DeepTau_version, iso_region=False)
 
### QCD 
def make_mutau_DRsr_QCD_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRsr_aiso_QCD_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRsr_QCD_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_QCD_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRar_aiso_QCD_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_QCD_cut(event_dictionary, DeepTau_version, iso_region=False)

### WJ
def make_mutau_DRsr_WJ_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=False, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRsr_aiso_WJ_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRsr_WJ_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_WJ_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=1, pass_mu_iso_req=iso_region, mu_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=False, mt_value=50, pass_BTag_req=True)
  return event_dictionary

def make_mutau_DRar_aiso_WJ_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_WJ_cut(event_dictionary, DeepTau_version, iso_region=False)

### TTBar (not used)
def make_mutau_DRsr_TT_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRsr_cuts" if iso_region == True else "pass_DRsr_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=True, mu_iso_value=0.15,
                         pass_DeepTau_req=True, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=False)
  return event_dictionary

def make_mutau_DRsr_aiso_TT_cut(event_dictionary, DeepTau_version, iso_region):
  return make_mutau_DRsr_TT_cut(event_dictionary, DeepTau_version, iso_region=False)

def make_mutau_DRar_TT_cut(event_dictionary, DeepTau_version, iso_region=True):
  name = "pass_DRar_cuts" if iso_region == True else "pass_DRar_aiso_cuts"
  event_dictionary   = make_mutau_region(event_dictionary, name,
                         FS_pair_sign=-1, pass_mu_iso_req=True, mu_iso_value=0.15,
                         pass_DeepTau_req=False, DeepTau_value=5, DeepTau_version="2p5",
                         pass_mt_req=True, mt_value=50, pass_BTag_req=False)
  return event_dictionary

def make_mutau_DRar_aiso_TT_cut(event_dictionary, DeepTau_version):
  return make_mutau_DRar_TT_cut(event_dictionary, DeepTau_version, iso_region=False)



