from iminuit import Minuit
from iminuit.cost import LeastSquares

import numpy as np
import matplotlib.pyplot as plt

def user_line_p_const(x, a, b, c): # line + const y = a*x + b if x < c, else y = a*c + b
    return np.piecewise(x, [x < c], [lambda x: a * x + b, lambda x: a * c + b])

def user_line(x, a, b):
    # y = mx + b # par[0]*x^1 + par[1]*x^0
    #return np.polyval([a, b], x)  # for len(par) == 2, this is a line
    return a*x + b

def get_midpoints(input_bins):
  '''
  From an input array of increasing values, return the values halfway between each value.
  The input array is size N, and the output array is size N-1
  '''
  midpoints = []
  for i, ibin in enumerate(input_bins):
    if (i+1 != len(input_bins)):
      midpoints.append( ibin + (input_bins[i+1] - ibin)/2 )
  midpoints = np.array(midpoints)
  return midpoints

def mask_zeros(input_list, mask_all=False):
  '''
  remove entry if val or error is zero (and is next to another zero)
  or, return mask for all zeros if mask_all is set to true
  '''
  adjacent_zeros = []
  for i, val in enumerate(input_list):
    if (val == 0):
      # first value in list, only check for adjacenet zero to the right
      if (i == 0):
        if (input_list[i+1] == 0): adjacent_zeros.append(True)
        else: adjacent_zeros.append(False)
      # last value in list, only check for adjacent zero to the left
      elif (i == len(input_list)-1):
        if (input_list[i-1] == 0): adjacent_zeros.append(True)
        else: adjacent_zeros.append(False)
      # all other values in the list, check both sides for another zero
      elif ((input_list[i+1] == 0) or (input_list[i-1] == 0)): adjacent_zeros.append(True)
      # not adjacent to another zero
      else: adjacent_zeros.append(False) 
    # not zero
    else: adjacent_zeros.append(False)
  all_zeros = np.array([(input_list[i] <= 0) for i in range(len(input_list))])
  adjacent_zeros = all_zeros if mask_all else np.array(adjacent_zeros) 
  return adjacent_zeros


bins = np.linspace(0, 300, 30+1)

# OLD METHOD
#RAW RATIO OF DRsr / (AR*FF)
#vals = np.array([ 0.0, 0.0, 0.0, -1.38795271e+04,
#  1.45417099e+00, -2.97488960e+01,  1.86764912e+00,  2.67921840e+00,
#  1.51646879e+00,  1.39831617e+00,  1.43627599e+00,  1.41202495e+00,
#  1.37464856e+00,  1.43003193e+00,  1.54858933e+00,  1.47132847e+00,
#  1.61432031e+00,  1.18680366e+00,  1.30460555e+00,  1.52069756e+00,
#  1.27021510e+00,  1.39723202e+00,  1.28916594e+00,  1.23265051e+00,
#  1.06791991e+00,  9.79626826e-01,  1.30867288e+00,  1.94337228e+00,
#  1.49126057e+00,  1.15200478e+00])
#RAW ERROR
#vals_err = np.array([0., 0., 0., 0., 1.89212661, 0.,
# 1.47894989, 1.1162601,  0.10151756, 0.0601275,  0.05983117, 0.06422517,
# 0.06838078, 0.07958705, 0.09899084, 0.10500871, 0.1315629,  0.10115593,
# 0.12539214, 0.1735626,  0.14163486, 0.18154919, 0.18895621, 0.19844782,
# 0.1824747,  0.17696183, 0.28932915, 0.50125683, 0.42467954, 0.12020447])

# NEW METHOD
#RAW RATIO OF DRsr / (AR_star*FF)
vals = np.array([ 0.00, 0.00, 0.00, -1.43620011e+04,
  1.44248981e+00, -2.87292597e+01,  1.12309387e+00,  1.64363883e+00,
  1.32553622e+00,  1.29536253e+00,  1.32422565e+00,  1.35661720e+00,
  1.29924601e+00,  1.31517287e+00,  1.38667179e+00,  1.34332983e+00,
  1.42300848e+00,  1.10231855e+00,  1.14310728e+00,  1.40595646e+00,
  1.03590255e+00,  1.17523820e+00,  1.16462919e+00,  1.12713709e+00,
  1.00060067e+00,  8.48425396e-01,  1.24032512e+00,  1.65862689e+00,
  1.49363096e+00,  1.01928517e+00])

#RAW ERROR
vals_err = np.array([0., 0., 0., 0., 1.88002144, 0.,
 0.98681431, 0.74111878, 0.09124016, 0.05661592, 0.05611325, 0.06222521,
 0.06541494, 0.07449836, 0.0906484,  0.09770422, 0.11891603, 0.09558722,
 0.11318734, 0.16304376, 0.1211256,  0.15860665, 0.17464402, 0.18522606,
 0.1737309,  0.15913488, 0.27747173, 0.44011154, 0.42521908, 0.10952633])


print(bins)
print(vals)
print(vals_err)

#silly_zeros = mask_zeros(vals)
midpoints = get_midpoints(bins)

# cludging for non-fit variable
#use_FF_ratio     = vals[~silly_zeros]
#use_FF_ratio_err = vals_err[~silly_zeros]
#use_midpoints    = midpoints[~silly_zeros]

print(bins)
valid_range = np.where(bins > 70)
valid_range = valid_range[0][:-1] # drop last idx
print(valid_range)

use_FF_ratio     = vals[valid_range]
use_FF_ratio_err = vals_err[valid_range]
use_midpoints    = midpoints[valid_range]

print(use_FF_ratio)
print(use_FF_ratio_err)

#least_squares_pw  = LeastSquares(use_midpoints, use_FF_ratio, use_FF_ratio_err, user_line_p_const) 
least_squares_pw  = LeastSquares(use_midpoints, use_FF_ratio, use_FF_ratio_err, user_line) 

# piecewise fit
#pw_fit = Minuit(least_squares_pw, a=-0.0003, b=0.06, c=100) # Initial vals for DiTau DRar_star
pw_fit = Minuit(least_squares_pw, a=-0.005, b=1) # Initial vals for DiTau DRar_star
pw_fit.migrad()
FoPW_values = pw_fit.values

# check reduced chi2, goodness-of-fit estimate, should be around 1 # from Minuit manual
print("PIECEWISE FIT INFO")
print(pw_fit)
chi_squared = pw_fit.fval
ndof = len(use_FF_ratio) - len(pw_fit.values)
RX2 = chi_squared / ndof
print(f"RX2: {RX2}")
print(FoPW_values)
pw_func_params = {}
for i, val in enumerate(FoPW_values):
  pw_func_params["ab"[i]] = val
  #pw_func_params["abc"[i]] = val
print(f"vals for dictionary: [{pw_func_params['a']:.4f}, {pw_func_params['b']:.4f}]")
#print(f"vals for dictionary: [{pw_func_params['a']:.4f}, {pw_func_params['b']:.4f}, {pw_func_params['c']:.4f}]")

#pw_label = f"pw func = a*x + b if x < c, else y = a*c + b \n\
pw_label = f"func = a*x + b\n\
             a = {pw_func_params['a']:.4f} \n\
             b = {pw_func_params['b']:.4f} \n\
             RX2 = {chi_squared:.2f} / {ndof:.2f} = {RX2:.2f}"
#             c = {pw_func_params['c']:.4f}"

more_xvals = np.linspace(0, 400, 800)

fig, ax = plt.subplots()
#ax.plot(midpoints, vals, marker="o", markersize=8, color="black", linestyle="None")
bin_width  = abs(bins[0:-1]-bins[1:])/2
ax.errorbar(midpoints, vals, xerr=bin_width, yerr=vals_err, marker="o", markersize=4, color="black", linestyle="None")
ax.plot(more_xvals, user_line(more_xvals, *FoPW_values), color="purple", label=pw_label)
#ax.plot(more_xvals, user_line_p_const(more_xvals, *FoPW_values), color="purple", label=pw_label)
ax.vlines(80, -1, 4)
ax.set_ylim(-1, 4)
ax.set_title("SS-->OS Bias Correction")
ax.set_ylabel("Ratio (Expected / Actual)")
ax.set_xlabel(r'$m_{vis}$ [GeV]')
plt.legend()

plt.show()
