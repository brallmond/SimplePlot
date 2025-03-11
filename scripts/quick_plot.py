import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

from calculate_functions import user_exp

def Dennis_func(x, a, b, c):
  #ROOT: [0]+[1]*(x-[2])*(erf(-999*(x-[2]))+1)
  #return a + b*(x-c)*(erf(-999.9*(x-c)) + 1) # numpy doesn't have erf somehow
  erf_on = np.where((x > c), 1, 0)
  return a + b*(x-c)*(-erf_on + 1)


def user_line_p_const(x, a, b, c): # line + const y = a*x + b if x < c, else y = a*c + b
    return np.piecewise(x, [x < c], [lambda x: a * x + b, lambda x: a * c + b])

do_compare_Dennis_lines = False
if do_compare_Dennis_lines:
  fig, ax2 = plt.subplots()

  xvals = np.linspace(0, 200, 800)

  pw_0j_vals = [0.0038, -0.0396, 40.7537] # newest :)
  pw_GTE1j_vals = [0.0023, -0.0097, 44.4960]

  D_0j_vals = [0.12729434, 2*0.0016799194, 45.222911] 
  D_GTE1j_vals = [0.092159171, 2*0.0011025717, 42.500311]

  ax2.plot(xvals, user_line_p_const(xvals, *pw_0j_vals), color="black", label="Braden: 0j")
  ax2.plot(xvals, Dennis_func(xvals, *D_0j_vals), color="red", label="Dennis: 0j")
  
  ax2.plot(xvals, user_line_p_const(xvals, *pw_GTE1j_vals), color="black", label="Braden: GTE1j", linestyle='--')
  ax2.plot(xvals, Dennis_func(xvals, *D_GTE1j_vals), color="red", label="Dennis: GTE1j", linestyle='--')

  ax2.set_ylim([0.0, 0.15])
  ax2.yaxis.set_minor_locator(MultipleLocator(0.005))  

  ax2.legend()
  
  ax2.set_title("MuTau QCD Fake Factor Comparison")
  
  ax2.set_xlabel(r'Tau $p_{T}$ [GeV]')

  plt.show()


   
do_compare_my_lines_ditau = False
if do_compare_my_lines_ditau:
  fig, ax = plt.subplots()
  
  xvals = np.linspace(0, 200, 200)
  
  pw_old_0j_vals  = [-0.000712, 0.2772, 110.9336]
  pw_new_0j_vals  = [-0.000313, 0.0469, 95.0819]
  
  ax.plot(xvals, user_line_p_const(xvals, *pw_old_0j_vals), color="black", label="old method: 0j")
  ax.plot(xvals, user_line_p_const(xvals, *pw_new_0j_vals), color="red", label="new method: 0j")
  
  ax.set_ylim([0.0, 0.5])
  ax.legend()
  
  ax.set_title("DiTau QCD Fake Factor Comparison")
  
  ax.set_xlabel(r'Leading Tau $p_{T}$ [GeV]')

  plt.show()

 
do_compare_my_lines = False
if do_compare_my_lines:
  fig, ax = plt.subplots()
  
  xvals = np.linspace(0, 200, 200)
  
  old_0j_vals = [-37.44,   0.634,   21.16,  0.118]
  new_0j_vals = [-0.68144, 0.10065, 2.0416, 0.11628]
  pw_0j_vals  = [0.003725, -0.03897, 39.89, 0.1128]
  pw_0j_vals  = [1,1,1]
  
  old_GTE1j_vals = [-3.42,    0.152,   3.89,   0.116]
  new_GTE1j_vals = [-0.50797, 0.10009, 1.6509, 0.09222]
  pw_GTE1j_vals  = [0.001936, 0.001851, 39.79, 0.094061]
  pw_GTE1j_vals  = [1,1,1]
  
  #ax.plot(xvals, user_exp(xvals, *old_0j_vals), color="red", label="old: 0j", linestyle="--")
  ax.plot(xvals, user_exp(xvals, *new_0j_vals), color="red", label="exponential: 0j")
  ax.plot(xvals, user_line_p_const(xvals, *pw_0j_vals), color="black", label="piecewise: 0j")
  
  #ax.plot(xvals, user_exp(xvals, *old_GTE1j_vals), color="blue", label="old: GTE1j", linestyle="--")
  ax.plot(xvals, user_exp(xvals, *new_GTE1j_vals), color="blue", label="exponential: GTE1j")
  ax.plot(xvals, user_line_p_const(xvals, *pw_GTE1j_vals), color="gray", label="piecewise: GTE1j")
  
  ax.set_ylim([0.0, 0.2])
  ax.legend()
  
  ax.set_title("MuTau QCD Fake Factor Comparison")
  
  ax.set_xlabel(r'Tau $p_{T}$ [GeV]')

  plt.show()



old_mvis_weights =  {
  "0j" : {
    "WJ" : [ 0.0, 0.44948888, 0.48709053, 0.67524474, 0.50798577,
    0.30572596, 0.26291757, 0.36291573, 0.45396447, 0.50760914,
    0.53213552, 0.51401822, 0.5389632 , 0.53212023, 0.55347546,
    0.49354312, 0.515111  , 0.45615758, 0.49706276, 0.47603629,
    0.46769062, 0.44418482, 0.48286102, 0.49221918, 0.28718744,
    0.40759256, 0.41038405, 0.4246403 , 0.42892607, 0.43369386],
    "QCD" : [ 0.0, 0.48555111, 0.40381454, 0.24558666, 0.44135018,
    0.66983689, 0.7161351 , 0.60970037, 0.51340257, 0.4578388 ,
    0.43213226, 0.45274492, 0.42562643, 0.43326491, 0.41175053,
    0.4689472 , 0.45429154, 0.51459492, 0.47215746, 0.49262575,
    0.49750084, 0.52590951, 0.48976589, 0.4807537 , 0.68528547,
    0.5689376 , 0.55795585, 0.55183232, 0.54333193, 0.54326978]
  },
  "GTE1j" : {
    "WJ" : [ 0.0, 0.35919842, 0.38588244, 0.43133431, 0.46609478,
    0.44423222, 0.40049161, 0.5140259 , 0.52309118, 0.54781008,
    0.56394086, 0.55453245, 0.56247195, 0.58533491, 0.54955494,
    0.49514224, 0.51411567, 0.47518111, 0.54872597, 0.49554874,
    0.47824467, 0.56399762, 0.51112266, 0.40956644, 0.40627854,
    0.45590943, 0.62126431, 0.57938354, 0.54590267, 0.42468222],
    "QCD" : [ 0.0, 0.5847488 , 0.54892652, 0.49746483, 0.46449129,
    0.49109413, 0.53835243, 0.40700889, 0.40053684, 0.369567  ,
    0.3540422 , 0.36201419, 0.35628948, 0.32944536, 0.37317331,
    0.43688905, 0.41442001, 0.45780746, 0.36813702, 0.42727713,
    0.4407349 , 0.34620719, 0.4180995 , 0.53518967, 0.51442426,
    0.4677225 , 0.28729954, 0.34340028, 0.39564531, 0.50200358]
  }
}

new_mvis_weights = {
  "0j" : { # made with HLepV2_newest
    "WJ" : [0.0, 0.71538272, 1.06462079, 1.17247763, 1.02534395,
    0.54390647, 0.53964404, 0.67686797, 0.77841908, 0.81707889,
    0.83967321, 0.83835022, 0.84320176, 0.90783081, 0.90161174,
    0.83237565, 0.88284674, 0.89184053, 0.84764886, 0.79320424,
    0.79774694, 0.85747927, 0.84319427, 0.79206026, 0.89528191,
    1.04120407, 0.86560451, 0.61764421, 0.87040562, 0.93020992], 
    "QCD" : [0.0,  0.28148969, 0.0, 0.0, 0.0,
     0.45497711,  0.45931101,  0.3218637 ,  0.22014255,  0.18116472,
     0.15835837,  0.15956006,  0.15440077,  0.08959185,  0.09555377,
     0.16500584,  0.11409682,  0.1052419 ,  0.1490675 ,  0.2033017 ,
     0.19900504,  0.13844839,  0.15227524,  0.20487331,  0.10097511,
     0.0,  0.13135428,  0.37805484,  0.12670006,  0.06408287] # values that are zero were once negative
  },
  "GTE1j" : {
    "WJ" : [ 0.0, 0.46181945, 0.64202312, 0.75214224, 0.81176301,
    0.70107077, 0.7451056 , 0.78477506, 0.83926879, 0.80423772,
    0.88332264, 0.89419591, 0.85547569, 0.91639891, 0.87821256,
    0.81862261, 0.8309619 , 0.8412575 , 0.78721782, 0.82031588,
    0.92411063, 0.84911878, 0.98391069, 0.80942164, 0.75585508,
    1.10627624, 0.94616639, 0.77182417, 0.7659672 , 0.84079994],
    "QCD" : [ 0.0,  0.51547452,  0.31929283,  0.20169761,  0.13859365,
    0.25635163,  0.2098122 ,  0.16501192,  0.10652101,  0.13864619,
    0.0575849 ,  0.04782454,  0.08768241,  0.02632051,  0.0637605 ,
    0.12657579,  0.10866128,  0.09984524,  0.15298744,  0.1233599 ,
    0.02064292,  0.09614293, 0.0,  0.13643187,  0.18954452,
    0.0, 0.0,  0.17068736,  0.17456418,  0.10691182] # values that are zero were once negative...
  }
}

WJInc_mvis_weights = {
  "0j" : {
    "QCD" : [0.0, 0.90240502, 0.95711925, 0.97984576, 0.79030026,
       0.41284612, 0.42564479, 0.5259534 , 0.60142661, 0.60630673,
       0.61714677, 0.59945244, 0.59177937, 0.60742979, 0.62551451,
       0.54598044, 0.54047414, 0.59005824, 0.56255325, 0.5429397 ,
       0.52637423, 0.55291422, 0.47373551, 0.38224014, 0.5447145 ,
       0.52762971, 0.48771847, 0.45083388, 0.55488791, 0.47888701], 
    "WJ" : [0.0, 0.09446739, 0.03683559, 0.014415  , 0.20695783,
       0.58603747, 0.57331027, 0.47277826, 0.39713502, 0.39193688,
       0.3808848 , 0.39845784, 0.40582316, 0.38999287, 0.37165099,
       0.45140105, 0.45646942, 0.40702418, 0.43416311, 0.45356625,
       0.47037775, 0.44301344, 0.52173399, 0.61469343, 0.45154252,
       0.46838492, 0.50924032, 0.54486518, 0.44221777, 0.51540578]
  },
  "GTE1j" : {
    "QCD" : [0.0, 0.43194625, 0.52239113, 0.65379285, 0.6362445 ,
       0.50849078, 0.54820784, 0.56001724, 0.60012838, 0.59139207,
       0.6337386 , 0.62920203, 0.59336641, 0.59698624, 0.59892467,
       0.53268682, 0.57149565, 0.56144091, 0.625905  , 0.58109993,
       0.49298562, 0.52148421, 0.52381374, 0.56444252, 0.54424407,
       0.74251108, 0.51639336, 0.45829914, 0.62294257, 0.58014667],
    "WJ" : [0.0, 0.54534772, 0.43892482, 0.300047  , 0.31411215,
       0.44893162, 0.40670995, 0.38976974, 0.34566142, 0.35149185,
       0.30716893, 0.31281841, 0.34979169, 0.34573318, 0.3430484 ,
       0.41251158, 0.36812753, 0.37966183, 0.31430026, 0.36257584,
       0.45176793, 0.4237775 , 0.41593903, 0.38141099, 0.40115553,
       0.19685949, 0.42765033, 0.48421239, 0.31758881, 0.36756509]
  }
}

fig, ax_new = plt.subplots()

do_frac_weights = False
if do_frac_weights:
  #diff_0j_QCD = np.array(old_mvis_weights["0j"]["QCD"]) - np.array(new_mvis_weights["0j"]["QCD"])
  #ax_new.plot(np.linspace(0,300, 30), diff_0j_QCD, label="0j QCD", color="red")
  
  #diff_GTE1j_QCD = np.array(old_mvis_weights["GTE1j"]["QCD"]) - np.array(new_mvis_weights["GTE1j"]["QCD"])
  #ax_new.plot(np.linspace(0,300, 30), diff_GTE1j_QCD, label="GTE1j QCD", color="red", linestyle="--")
  
  diff2_0j_QCD = np.array(old_mvis_weights["0j"]["QCD"]) - np.array(WJInc_mvis_weights["0j"]["QCD"])
  ax_new.plot(np.linspace(0,300, 30), diff2_0j_QCD, label="0j QCD", color="green")
  
  diff2_GTE1j_QCD = np.array(old_mvis_weights["GTE1j"]["QCD"]) - np.array(WJInc_mvis_weights["GTE1j"]["QCD"])
  ax_new.plot(np.linspace(0,300, 30), diff2_GTE1j_QCD, label="GTE1j QCD", color="green", linestyle="--")
  
  
  #diff_0j_WJ = np.array(old_mvis_weights["0j"]["WJ"]) - np.array(new_mvis_weights["0j"]["WJ"])
  #ax_new.plot(np.linspace(0,300, 30), diff_0j_WJ, label="0j WJ", color="blue")
  
  #diff_GTE1j_WJ = np.array(old_mvis_weights["GTE1j"]["WJ"]) - np.array(new_mvis_weights["GTE1j"]["WJ"])
  #ax_new.plot(np.linspace(0,300, 30), diff_GTE1j_WJ, label="GTE1j WJ", color="blue", linestyle="--")
  
  diff2_0j_WJ = np.array(old_mvis_weights["0j"]["WJ"]) - np.array(WJInc_mvis_weights["0j"]["WJ"])
  ax_new.plot(np.linspace(0,300, 30), diff2_0j_WJ, label="0j WJ", color="brown")
  
  diff2_GTE1j_WJ = np.array(old_mvis_weights["GTE1j"]["WJ"]) - np.array(WJInc_mvis_weights["GTE1j"]["WJ"])
  ax_new.plot(np.linspace(0,300, 30), diff2_GTE1j_WJ, label="GTE1j WJ", color="brown", linestyle="--")
  
  ax_new.set_title("fractional weight of background (old - new)")
  
  ax_new.set_xlabel(r'$m_{vis}$ [GeV]')

  ax_new.legend()

  plt.show()






