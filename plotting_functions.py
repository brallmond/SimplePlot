# libraries
import numpy as np
import matplotlib.pyplot as plt

### README
# this file contains functions to setup plotting interfaces and draw the plots themselves

from MC_dictionary        import MC_dictionary
from binning_dictionary   import binning_dictionary, label_dictionary
from triggers_dictionary  import triggers_dictionary

from luminosity_dictionary import luminosities_with_normtag as luminosities
from calculate_functions  import yields_for_CSV, calculate_underoverflow


def make_pie_chart(data_hist, MC_dictionary, use_data=False, use_fakes=False):
      sums, labels, colors = [], [], []
      for process in MC_dictionary:
        if (use_fakes == False) and (("Fakes" in process) or (process=="QCD")): pass
        else:
          sums.append(np.sum(MC_dictionary[process]["BinnedEvents"]))
          color, label, _ = set_MC_process_info(process, luminosity=-1)
          labels.append(label)
          colors.append(color)
      # add Data - MC
      total_sum = np.sum(sums)
      disagreement = np.sum(data_hist) - total_sum
      if (disagreement > 0):
        sums.append(disagreement)
        labels.append("Data-MC")
        colors.append("Grey")
      if (use_data == True):
        sums = [np.sum(data_hist)]
        labels = ["Data"]
        colors = ["White"]
      fig, ax = plt.subplots()
      ax.pie(sums, labels=labels, colors=colors, autopct='%1.1f%%')


def make_fraction_all_events(axis, xbins, h_data, h_backgrounds):
  color_array, label_array, percent_stack_array = [], [], []
  percent_QCD = np.ones(np.shape(h_data))
  for process in h_backgrounds.keys():
    color, label, _ = set_MC_process_info(process, luminosity=-1)
    color_array.append(color)
    label_array.append(label)
    h_bkgd = h_backgrounds[process]["BinnedEvents"]
    h_diff = h_data - h_bkgd
    h_percent = h_bkgd / h_data
    percent_stack_array.append(h_percent)
    percent_QCD -= h_percent
  percent_stack_array.append(percent_QCD)
  QCD_color, QCD_label, _ = set_MC_process_info("QCD", luminosity=-1)
  color_array.append(QCD_color)
  label_array.append(QCD_label)
  axis.stackplot(xbins[0:-1], percent_stack_array, step="post", edgecolor="black", colors=color_array, labels=label_array)


def make_fraction_fakes(axis, xbins, h_data, h_backgrounds, fake_processes=["TT", "WJ", "DYJet"]):
  color_array, label_array = [], []
  fakes_percent = []
  h_fakes_total = np.zeros(np.shape(h_data))
  h_bkgd_total = np.zeros(np.shape(h_data))
  for process in h_backgrounds.keys():
    h_bkgd = h_backgrounds[process]["BinnedEvents"]
    h_bkgd_total += h_bkgd
    if (process in fake_processes):
      color, label, _ = set_MC_process_info(process, luminosity=-1)
      color_array.append(color)
      label_array.append(label)
      h_fakes_total += h_bkgd
  h_QCD = h_data - h_bkgd_total
  h_fakes_total += h_QCD
  for process in fake_processes:
    h_bkgd = h_backgrounds[process]["BinnedEvents"]
    fakes_percent.append(h_bkgd / h_fakes_total)
  fakes_percent.append(h_QCD / h_fakes_total)
  QCD_color, QCD_label, _ = set_MC_process_info("QCD", luminosity=-1)
  QCD_label += " (Data-MC)"
  color_array.append(QCD_color)
  label_array.append(QCD_label)
  print(fake_processes, "QCD")
  print(fakes_percent)
  axis.stackplot(xbins[0:-1], fakes_percent, step="post", edgecolor="black", colors=color_array, labels=label_array)
 

def make_two_dimensional_plot(input_dictionary, final_state, x_var, y_var, 
                              add_to_title="", alt_x_bins=[], alt_y_bins=[]):
  fig, axis = plt.subplots()
  x_array = input_dictionary[x_var]
  y_array = input_dictionary[y_var]
  x_bins  = binning_dictionary[final_state][x_var] if len(alt_x_bins) == 0 else alt_x_bins
  y_bins  = binning_dictionary[final_state][y_var] if len(alt_y_bins) == 0 else alt_y_bins
  h2d, xbins, ybins = np.histogram2d(x_array, y_array, bins=(x_bins, y_bins))
  h2d = h2d.T # transpose from image coordinates to data coordinates
  cmesh = axis.pcolormesh(xbins, ybins, h2d) #pcolormesh uses data coordinates by default, imshow uses array of 1x1 squares
  axis.set_title(f"{final_state} :" + f" {add_to_title}")
  axis.set_xlabel(label_dictionary[x_var])
  axis.set_ylabel(label_dictionary[y_var])
  plt.colorbar(cmesh)

def make_two_dimensional_ratio_plot(numerator_dictionary, denominator_dictionary,
                                    final_state, x_var, y_var,
                                    add_to_title="", alt_x_bins=[], alt_y_bins=[]):
  fig, axis = plt.subplots()

  from matplotlib.colors import ListedColormap
  cmap = ListedColormap(["#f9f954", "#f7e752", "#f6d453", "#edc756", "#ddc15f", "#cdbc67", "#b5bc70", 
                         "#9dbd7a", "#85bb86", "#6eb894", "#5cb4a4", "#52adb3", "#4da5bf", "#479bc8", 
                         "#408cca", "#3c7fcf", "#3470d2", "#2d62d4", "#2951c5", "#2b3da2"][::-1]) # ROOT 2D default

  x_bins  = make_bins(x_var, final_state) if len(alt_x_bins) == 0 else alt_x_bins
  y_bins  = make_bins(y_var, final_state) if len(alt_y_bins) == 0 else alt_y_bins
  # TODO: remove all exposed calls to binning dictionary in preference of the helper function :)
  #x_bins  = binning_dictionary[final_state][x_var] if len(alt_x_bins) == 0 else alt_x_bins
  #y_bins  = binning_dictionary[final_state][y_var] if len(alt_y_bins) == 0 else alt_y_bins

  num_keys = [*numerator_dictionary.keys()] # python for 1) put in a list [], 2) unpack *, 3) dict keys .keys
  num1_x_array = numerator_dictionary[num_keys[0]]["PlotEvents"][x_var]
  num1_y_array = numerator_dictionary[num_keys[0]]["PlotEvents"][y_var]
  num1_h2d, xbins, ybins = np.histogram2d(num1_x_array, num1_y_array, bins=(x_bins, y_bins))
  num1_h2d = num1_h2d/100. # unscale signal
  num2_x_array = numerator_dictionary[num_keys[1]]["PlotEvents"][x_var]
  num2_y_array = numerator_dictionary[num_keys[1]]["PlotEvents"][y_var]
  num2_h2d, xbins, ybins = np.histogram2d(num2_x_array, num2_y_array, bins=(x_bins, y_bins))
  num2_h2d = num2_h2d/100. # unscale signal
  num_h2d = num1_h2d + num2_h2d

  den_keys = [*denominator_dictionary.keys()]
  den_x_array = denominator_dictionary[den_keys[0]]["PlotEvents"][x_var]
  den_y_array = denominator_dictionary[den_keys[0]]["PlotEvents"][y_var]
  den_h2d, xbins, ybins = np.histogram2d(den_x_array, den_y_array, bins=(x_bins, y_bins))

  #ratio_h2d = num_h2d / den_h2d
  ratio_h2d = num_h2d / np.sqrt(den_h2d)
  ratio_h2d = ratio_h2d.T # transpose from image coordinates to data coordinates
  ratio_h2d[np.isnan(ratio_h2d)] = 0 # zero over zero 
  ratio_h2d[np.isinf(ratio_h2d)] = np.min(ratio_h2d[np.nonzero(ratio_h2d)]) # div by zero, assume there's data there and use the lowest signal value
  cmesh = axis.pcolormesh(xbins, ybins, ratio_h2d, cmap=cmap) #pcolormesh uses data coordinates by default, imshow uses array of 1x1 squares
  axis.set_title(f"{final_state} :" + f" {add_to_title}")
  axis.set_xlabel(label_dictionary[x_var])
  axis.set_ylabel(label_dictionary[y_var])

  plt.colorbar(cmesh)

  #print("shape and xbins")
  #print(ratio_h2d.shape[0])
  #print(ybins)
  #print()
  #print(ratio_h2d.shape[1])
  #print(xbins)
  #for i in range(ratio_h2d.shape[0] - 1):
  #  for j in range(ratio_h2d.shape[1] - 1):
  #    plt.text(ybins[i], xbins[j], f"{ratio_h2d[i,j]:.2f}", ha='center', va='center')

def make_eta_phi_plot(process_dictionary, process_name, final_state_mode, jet_mode, label_suffix):
  eta_phi_by_FS_dict = {"ditau"  : ["FS_t1_eta", "FS_t1_phi", "FS_t2_eta", "FS_t2_phi"],
                        "mutau"  : ["FS_mu_eta", "FS_mu_phi", "FS_tau_eta", "FS_tau_phi"],
                        "etau"   : ["FS_el_eta", "FS_el_phi", "FS_tau_eta", "FS_tau_phi"],
                        "emu"    : ["FS_el_eta", "FS_el_phi", "FS_mu_eta", "FS_mu_phi"],
                        "dimuon" : ["FS_m1_eta", "FS_m1_phi", "FS_m2_eta", "FS_m2_phi"]}
  eta_phi_by_FS = eta_phi_by_FS_dict[final_state_mode]
  make_two_dimensional_plot(process_dictionary[process_name]["PlotEvents"], final_state_mode,
                            eta_phi_by_FS[0], eta_phi_by_FS[1], add_to_title=label_suffix)
  make_two_dimensional_plot(process_dictionary[process_name]["PlotEvents"], final_state_mode,
                            eta_phi_by_FS[2], eta_phi_by_FS[3], add_to_title=label_suffix)
  if (jet_mode == "1j"):
    make_two_dimensional_plot(process_dictionary[process_name]["PlotEvents"], final_state_mode,
                             "CleanJetGT30_eta_1", "CleanJetGT30_phi_1", add_to_title=label_suffix)

def plot_raw(histogram_axis, xbins, input_vals, luminosity,
             color="black", label="Data", marker="o", fillstyle="full"):
  '''
  Plotting function for raw values, usually made by pre-processing data/background
  '''
  stat_error = np.sqrt(input_vals) # TODO: this isn't necessarily correct
  midpoints   = get_midpoints(xbins)
  bin_width  = abs(xbins[0:-1]-xbins[1:])/2 # only works for uniform bin widths
  histogram_axis.errorbar(midpoints, input_vals, xerr=bin_width, yerr=stat_error,
                          color=color, marker=marker, fillstyle=fillstyle, label=label,
                          linestyle='none', markersize=3)

def blind_region(input_array, allbins, blind_range):
  # zero-out anything in the blind range
  output_array = input_array
  blind_idx = np.where((allbins >= blind_range[0]) & (allbins <= blind_range[1])) # get indices greater/less than range
  output_array[blind_idx] = 0
  return output_array
  

def plot_data(histogram_axis, xbins, data_dictionary, luminosity, presentation_mode=False,
              blind_var=False, blind_range=[],
              color="black", label="Data", marker="o", fillstyle="full"):
  '''
  Add the data histogram to the existing histogram axis, computing errors in a simple way.
  For data, since points and error bars are used, they are shifted to the center of the bins.
  TODO: The error calculation should be followed up and separated to another function. 
  '''
  data_info = data_dictionary["Data"]["BinnedEvents"]
  stat_error = np.sqrt(data_dictionary["Data"]["BinnedErrors"])
  sum_of_data = np.sum(data_info)
  midpoints   = get_midpoints(xbins)
  bin_width  = abs(xbins[0:-1]-xbins[1:])/2 # only works for uniform bin widths
  label += "" if presentation_mode else f" [{sum_of_data:>.0f}]"
  if (blind_var): data_info = blind_region(data_info, xbins, blind_range)
  histogram_axis.errorbar(midpoints, data_info, xerr=bin_width, yerr=stat_error, 
                          color=color, marker=marker, fillstyle=fillstyle, label=label,
                          linestyle='none', markersize=3)
  #below plots without error bars
  #histogram_axis.plot(midpoints, data_info, color="black", marker=marker, linestyle='none', markersize=3, label=label)


def plot_MC(histogram_axis, xbins, stack_dictionary, luminosity, presentation_mode=False,
            custom=False, color="default", label="MC", fill=True):
  '''
  Add background MC histograms to the existing histogram axis. The input 'stack_dictionary'
  contains a list of backgrounds (which should be pre-grouped, normally), the name of which
  determines colors and labels of the stacked output. 
  '''
  color_array, label_array, stack_array = [], [], []
  total_error = 0
  stack_top   = 0
  for MC_process in stack_dictionary:
    #print(MC_process) # DEBUG
    if custom == True:  pass
    else:               color, label, _ = set_MC_process_info(MC_process, luminosity)
    current_hist = stack_dictionary[MC_process]["BinnedEvents"]
    current_hist = np.append(current_hist, 0) # adding empty element to get around step="post" in stackplot
    stack_top   += current_hist
    total_error += stack_dictionary[MC_process]["BinnedErrors"]
    label += "" if presentation_mode else f" [{np.sum(current_hist):>.0f}]"
    color_array.append(color)
    label_array.append(label)
    stack_array.append(current_hist)

  total_error = np.append(total_error, 0) # same as nearest above comment 
  total_error = np.sqrt(total_error)
  error_up    = stack_top + total_error
  error_down  = stack_top - total_error

  histogram_axis.stackplot(xbins, stack_array, step="post", edgecolor="black", colors=color_array, labels=label_array)
  histogram_axis.fill_between(xbins, error_down, error_up, step="post", 
                              color="grey", alpha=0.50, edgecolor="none", hatch="/////") # no hatchcolor option :(


def plot_signal(histogram_axis, xbins, signal_dictionary, luminosity, presentation_mode=False,
            custom=False, color="default", label="MC", fill=False):
  '''
  Similar to plot_MC, except signals are not stacked, and the 'stair' method
  of matplotlib DOES expect histogram data, so no adjustment to xbins is necessary.
  '''
  for signal in signal_dictionary:
    if custom == True:
      pass
    else:
      color, label, _ = set_MC_process_info(signal, luminosity, scaling=True, signal=True)
    current_hist = signal_dictionary[signal]["BinnedEvents"]
    label += "" if presentation_mode else f" [{np.sum(current_hist):>.0f}]"
    stairs = histogram_axis.stairs(current_hist, xbins, color=color, label=label, fill=False)


def set_MC_process_info(process, luminosity, scaling=False, signal=False):
  '''
  Obtain process-specific styling and scaling information.
  MC_dictionary is maintained in a separate file.
  '''
  if "alt" in process: process = process.replace("_alt","")
  color = MC_dictionary[process]["color"]
  label = MC_dictionary[process]["label"]
  lumi_key = "" if "QCD" in process else [key for key in luminosities.items() if key[1] == luminosity][0][0]
  if scaling:
    if ("Fakes" in process) or (process=="myQCD"): scaling = 1
    else: scaling = MC_dictionary[process]["XSecMCweight"] * MC_dictionary[process]["plot_scaling"]
    #if process.startswith("WJets"): scaling = MC_dictionary[process]["plot_scaling"] # Removing XSecMCweight if Stitchweight used instead
    # TODO: can i remove these lines? do i care if testing still works like that? 
    # hacky unscaling and rescaling so that "testing" still works
    if ("C" in lumi_key) or ("D" in lumi_key):
      scaling *= 1 / luminosities["2022 CD"]
    elif ("E" in lumi_key) or ("F" in lumi_key) or ("G" in lumi_key):
      scaling *= 1 / luminosities["2022 EFG"]
    elif (lumi_key == "2022"):
      scaling *= 1 / luminosities["2022"]
    elif (lumi_key == ""):
      print(f"custom luminosity set to {luminosity} for {process} process")
    else:
      print(f"unrecognized lumi_key: {lumi_key}")
    scaling *= luminosity
  if signal:
    #label += " x" + str(MC_dictionary[process]["plot_scaling"])
    label += " x100"
  return (color, label, scaling)


def setup_ratio_plot():
  '''
  Define a standard plot format with a plotting area on top, and a ratio area below.
  The plots share the x-axis, and other functions should handle cosmetic additions/subtractions.
  '''
  gs = gridspec_kw = {'height_ratios': [4, 1], 'hspace': 0.09}
  fig, (upper_ax, lower_ax) = plt.subplots(nrows=2, sharex=True, gridspec_kw=gridspec_kw)
  return (upper_ax, lower_ax)


def setup_single_plot():
  fig, ax = plt.subplots()
  return ax


def setup_unrolled_plot(n_ax):
  gridspec_kw = {'height_ratios': [3, 1], 'hspace': 0.09, 'wspace': 0} # used to be 4:1
  fig, (upper_n_ax, lower_n_ax) = plt.subplots(ncols=n_ax, nrows=2, sharex='col', sharey='row', figsize=(16, 6),
                                               gridspec_kw=gridspec_kw)
  return fig, upper_n_ax, lower_n_ax


def add_CMS_preliminary(axis):
  '''
  Add text to plot following CMS plotting guidelines
  https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/FigGuidelines#Example_ROOT_macro_python
  '''
  CMS_text = "CMS"
  axis.text(0.01, 1.02, CMS_text, transform=axis.transAxes, fontsize=16, weight='bold')
  preliminary_text = "Preliminary"
  axis.text(0.12, 1.02, preliminary_text, transform=axis.transAxes, fontsize=16, style='italic')

final_state_str = {
    "ditau"  : r"${\tau_h}{\tau_h}$",
    "mutau"  : r"${\tau_{\mu}}{\tau_h}$",
    "etau"   : r"${\tau_e}{\tau_h}$",
    "dimuon" : r"${\mu}{\mu}$",
    "emu"    : r"${e}{\mu}$",
}
jet_mode_str = {
    "Inclusive" : "≥0j",
    "0j"    : "0j",
    "1j"    : "1j",
    "GTE1j" : "≥1j",
    "GTE2j" : "≥2j",
}
def add_final_state_and_jet_mode(axis, final_state_mode, jet_mode):
  axis.text(0.05, 0.92, 
  #axis.text(0.45, -0.045, 
            final_state_str[final_state_mode] + " : " + jet_mode_str[jet_mode], 
            transform=axis.transAxes, fontsize=10)

def add_text(axis, text_to_add, loc=[0.05, 0.85], rotation=0, ha="left", va="baseline"):
  axis.text(loc[0], loc[1], text_to_add,
            transform=axis.transAxes, fontsize=10, 
            rotation=rotation, ha=ha, va=va)


def spruce_up_single_plot(axis, variable_name, ylabel, title, final_state_mode, jet_mode, yrange=None,
                           leg_on=True, leg_loc ="upper right",):
  add_CMS_preliminary(axis)
  add_final_state_and_jet_mode(axis, final_state_mode, jet_mode)
  axis.set_title(title, loc='right', y=0.98)
  axis.set_ylabel("Events")
  axis.minorticks_on()
  axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  axis.set_xlabel(variable_name)
  axis.set_ylabel(ylabel)
  if (yrange != None): axis.set_ylim(yrange)
  if (leg_on):
    leg = axis.legend(loc=leg_loc, frameon=True, bbox_to_anchor=[0.6, 0.4, 0.4, 0.6],
                      labelspacing=0.35, handlelength=0.8, handleheight=0.8, handletextpad=0.4)


def spruce_up_plot(histogram_axis, ratio_plot_axis, variable_name, title, final_state_mode, jet_mode,
                   set_x_log = False, set_y_log = False):
  '''
  Add title and axes labels
  Additionally:
    - hide a zero that overlaps with the upper plot.
    - add a horizontal line at y=1 to the ratio plot
  '''
  add_CMS_preliminary(histogram_axis)
  add_final_state_and_jet_mode(histogram_axis, final_state_mode, jet_mode)
  histogram_axis.set_title(title, loc='right', y=0.98)
  histogram_axis.set_ylabel("Events")
  histogram_axis.minorticks_on()
  histogram_axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  #yticks = histogram_axis.yaxis.get_major_ticks()
  #yticks[0].label1.set_visible(false) # hides a zero that overlaps with the upper plot

  ylimmin, ylimmax = histogram_axis.get_ylim()
  # posisble to make multicol, consider part of presentation_mode?
  # https://www.geeksforgeeks.org/use-multiple-columns-in-a-matplotlib-legend/
  histogram_axis.set_ylim(ylimmin, ylimmax*1.75) # scale up graph so legend fits without crazy overlap

  ratio_plot_axis.set_ylim([0.45, 1.55]) # 0.0, 2.0 also make sense
  ratio_plot_axis.set_xlabel(variable_name) # shared axis label
  if variable_name == "Trigger Indices":
    ratio_plot_axis.set_xlabel("") # shared axis label
    trig_labels = ["DiTau", "DiTau+Jet", "VBFRun3", "VBFRun2"]
    xpos  = 0.26
    xstep = 0.18
    ypos  = -0.35
    for i,nlabel in enumerate(trig_labels):
      add_text(ratio_plot_axis, nlabel, loc=[xpos+xstep*i, ypos], rotation=35, ha="center", va="center")
  if ("Decay Mode" in variable_name) and ("Pair" not in variable_name):
    flat_map = ["","0","","1","","10","","11",""]
    flat_map = [0, 1, 10, 11]
    ratio_plot_axis.set_xticks(np.arange(len(flat_map)), labels=flat_map, fontsize=10, ha="center")
  if "Tau Pair Decay Mode" in variable_name:
    pair_DM_decoder = { 0: 0,   1:  100, 2:  1000, 3:  1100, # 16 unique DM pairs from t1_DM*100 + t2_DM
                        4: 1,   5:  101, 6:  1001, 7:  1101,
                        8: 10,  9:  110, 10: 1010, 11: 1110,
                       12: 11,  13: 111, 14: 1011, 15: 1111 }
    flat_map = [0, 100, 1000, 1100, 1, 101, 1001, 1101, 10, 110, 1010, 1110, 11, 111, 1011, 1111]
    ratio_plot_axis.set_xticks(np.arange(len(flat_map)), labels=flat_map, rotation=45, ha="left", fontsize=8)

  ratio_plot_axis.set_ylabel("Obs. / Exp.")
  ratio_plot_axis.axhline(y=1, color='grey', linestyle='--')
  ratio_plot_axis.minorticks_on()
  ratio_plot_axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  ratio_plot_axis.yaxis.set_major_locator(plt.FixedLocator([0.6, 0.8, 1.0, 1.2, 1.4]))
  ratio_plot_axis.yaxis.set_major_formatter('{x:.1f}')
  ratio_plot_axis.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

  if (set_x_log == True):
    # does not work how you think it should, need custom redefine
    #ax.set_xscale('function', functions=(1-log, inverse))
    histogram_axis.set_xscale('log')
    ratio_plot_axis.set_xscale('log')
  if (set_y_log == True):
    histogram_axis.set_yscale('log')
    ratio_plot_axis.set_yscale('log')

def spruce_up_unrolled_plot(fig, histogram_axes, ratio_axes, variable_name, title, final_state_mode, jet_mode, tau_pt_cut,
                            set_x_log = False, set_y_log = False):

  vals = {
   "ditau" : { "None" : [], "Low" : [25, 50],  "Mid" : [50, 70],  "High" : [70, 10000]  },
   "mutau" : { "None" : [], "Low" : [30, 50],  "Mid" : [50, 70],  "High" : [70, 10000]  },
   "etau"  : { "None" : [], "Low" : [30, 50],  "Mid" : [50, 70],  "High" : [70, 10000]  },
  }
  midax = int(len(histogram_axes)/2)
  use_vals = vals[final_state_mode][tau_pt_cut]
  if   tau_pt_cut == "None": valstring = "- Inclusive"; tau_pt_cut = ""
  elif tau_pt_cut == "High": valstring = f"> {use_vals[0]}"
  else:                      valstring = f"[{use_vals[0]}, {use_vals[1]}]"
  histogram_axes[midax].set_title(f"{final_state_str[final_state_mode]} : {tau_pt_cut} Tau pT Category {valstring}")
  histogram_axes[0].text(0.01, 1.02, "CMS Preliminary", transform=histogram_axes[0].transAxes, fontsize=16, weight='bold')
  histogram_axes[-1].set_title(title, loc='right', y=0.98)
  histogram_axes[0].set_ylabel("Events")
  for histogram_axis in histogram_axes:
    histogram_axis.minorticks_on()
    histogram_axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")

  #ylimmin, ylimmax = histogram_axes[0].get_ylim()
  #for histogram_axis in histogram_axes: # don't do this, it will break
  #  histogram_axis.set_ylim(ylimmin, ylimmax*1.25) # scale up graph

  ratio_axes[0].set_ylabel("Obs. / Exp.")
  ratio_axes[midax].set_xlabel(variable_name) # shared axis label on middle-ish plot
  for ratio_axis in ratio_axes:
    ratio_axis.set_ylim([0.45, 1.55]) # 0.0, 2.0 also make sense
    ratio_axis.axhline(y=1, color='grey', linestyle='--')
    ratio_axis.minorticks_on()
    ratio_axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
    ratio_axis.yaxis.set_major_locator(plt.FixedLocator([0.6, 0.8, 1.0, 1.2, 1.4]))
    ratio_axis.yaxis.set_major_formatter('{x:.1f}')
    ratio_axis.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

  if (set_y_log == True): # put in loop if you want to use...
    for histogram_axis in histogram_axes:
      histogram_axis.set_yscale('log')
    #for ratio_axis in ratio_axes: # almost never will want this
    #  ratio_axis.set_yscale('log')
  
  handles, labels = histogram_axes[0].get_legend_handles_labels()
  leg = fig.legend(handles, labels, loc="upper center", frameon=False, ncol=len(labels),
                   labelspacing=0.35, handlelength=0.8, handleheight=0.8, handletextpad=0.4)
 

def spruce_up_legend(histogram_axis, final_state_mode):
  # this post has good advice about moving the legend off the plot
  # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
  # defaults are here, but using these to mimic ROOT defaults 
  # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
  leg = histogram_axis.legend(loc="upper right", frameon=False,
                        labelspacing=0.35, handlelength=0.8, handleheight=0.8, handletextpad=0.4)

  if final_state_mode == "dimuon":
    handles, original_labels = histogram_axis.get_legend_handles_labels()
    labels, yields = yields_for_CSV(histogram_axis)
    save_entry = [i for i,yield_ in enumerate(yields) if yield_ != 0]
    save_handles = [handles[entry] for entry in save_entry]
    save_labels  = [labels[entry] for entry in save_entry]
    histogram_axis.legend(save_handles, save_labels)
    print(f"Legend lables were previously {original_labels}")
    print("Removed samples with yield=0 from legend!")


def make_ratio_plot(ratio_axis, xbins, 
                    numerator_data, numerator_type, numerator_weight,
                    denominator_data, denominator_type, denominator_weight, 
                    no_plot = False,
                    label=None, color="black"):
  '''
  Uses provided numerator and denominator info to make a ratio to add to given plotting axis.
  Errors are also calculated using the same matplotlib function as used in plot_data.
  '''
  ratio = numerator_data/denominator_data
  ratio[np.isnan(ratio)] = 0 # numpy idiom to set "nan" values to 0
  # TODO : technically errors from stack should be individually calculated, not one stack
  
  # the error bars on a ratio plot of a histogram A divided by a histogram B is:
  # (A/B) * √[ (errA / A)^2 + (errB / B)^2 ]
  # for data, error = √ [N] \ where A and B are simply N events in a bin
  # for MC  , error = √ [ Σ (w)^2] \ where w is "event weights" in a bin
  #if (numerator_type=="MC") and (denominator_type=="MC"):
    # ratio error = (A/B) * √ [ ( √ [Σ (w_A)^2] / A)^2 + ( √ [Σ (w_B)^2] / B)^2 ] \
  #if (numerator_type=="Data") and (denominator_type=="MC"):
    # ratio error = (A/B) * √ [ (1/A) + ( √ [Σ (w_B)^2] / B)^2 ] \
  if (numerator_type=="Data") and (denominator_type=="Data"):
    # ratio error = (A/B) * √ [ (1/A) + (1/B) ] \
    statistical_error = np.array([ ratio[i] * np.sqrt( (1/numerator_data[i]) + (1/denominator_data[i]))
                        if ((denominator_data[i] > 0) and (numerator_data[i] > 0)) else 0
                        for i,_ in enumerate(denominator_data)]) 
  statistical_error[np.isnan(statistical_error)] = 0
  if no_plot == True:
    pass
  else:
    midpoints = get_midpoints(xbins)
    bin_width  = abs(xbins[0:-1]-xbins[1:])/2
    ratio_axis.errorbar(midpoints, ratio, xerr=bin_width, yerr=statistical_error,
                      color=color, marker="o", linestyle='none', markersize=2, label=label)

  return ratio, statistical_error


def make_bins(variable_name, final_state_mode):
  '''
  Information for binning is referenced from a python dictionary in a separate file.
  '''
  try: 
    xbins = binning_dictionary[final_state_mode][variable_name]
  except KeyError:
    xbins = binning_dictionary["common"][variable_name]
  return xbins


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


def adjust_scaling(final_state, process, scaling):
  '''
  Try to read a dictionary of factors to scale up processes, changing with final state.
  If it doesn't exist, don't adjust the factor (multiply by one and send it back).
  Scaling is N ignored files (only ignored during testing)
  '''
  adjustment_dictionary = {
    "mutau" : {
      "TTTo2L2Nu" : 15,
      "TTToSemiLeptonic" : 27,
    },
    "etau"  : {
      "TTTo2L2Nu" : 9,
      "TTToSemiLeptonic" : 19,
    },
    "dimuon" : {
      "DYInc" : 6.482345 # for "New DiMuon DY", whatever that means :)
    },
    "emu" : {
      "TTTo2L2Nu" : 68,
    },
  }
  try:
    adjustment_factor = adjustment_dictionary[final_state][process]
  except KeyError:
    adjustment_factor = 1
  return scaling * adjustment_factor


def get_binned_info(final_state, testing, process_name, process_variable, xbins, process_weights, luminosity, mask=[]):
  '''
  Take in a list of events and produce a histogram (values binned in a numpy array).
  'scaling' is either set to 1 for data (no scaling) or retrieved from the MC_dictionary.
  Underflows and overflows are included in the first and final bins of the output histogram by default.
  Note: 'process_variable' is a list of events
  '''
  scaling = 1 if "Data" in process_name else set_MC_process_info(process_name, luminosity, scaling=True)[2]
  if testing == True: scaling = adjust_scaling(final_state, process_name, scaling)
  weights = scaling * process_weights
  if (len(mask) != 0): 
    process_variable = process_variable[mask]
    weights = weights[mask]
  underflow, overflow, underflow_error, overflow_error = calculate_underoverflow(process_variable, xbins, weights)
  binned_values, _    = np.histogram(process_variable, xbins, weights=weights)
  binned_values[0]   += underflow
  binned_values[-1]  += overflow
  binned_weight_2, _  = np.histogram(process_variable, xbins, weights=weights*weights)
  binned_weight_2[0]  += underflow_error
  binned_weight_2[-1] += overflow_error
  return binned_values, binned_weight_2

def get_weight_stats(process_name, process_weights):
  ''' to be used in get_binned_info as a quick way to quantify process_weights'''
  from scipy import stats
  print(f"Average process weight for {process_name}")
  print(np.average(process_weights))
  print(stats.describe(process_weights))
  

def get_binned_process(final_state, testing, process_dictionary, variable, xbins_, lumi_, mask={}, mask_n=999):
  '''
  Standard loop to get only the plotted variable from a dictionary containing info and multiple variables.
  This is written to only get on process at a time. Other functions combine the processes when necessary.
  '''
  h_processes = {}

  for process in process_dictionary:
    process_variable = process_dictionary[process]["PlotEvents"][variable]
    process_mask = mask[process][mask_n] if mask_n != 999 else []
    if len(process_variable) == 0: continue
    if "Data" in process:
      process_weights = np.ones(np.shape(process_variable)) # weights of one for data
    elif ("Fakes" in process) or (process == "myQCD"):
      process_weights = process_dictionary[process]["FF_weight"]
    else:
      process_weights = get_MC_weights(process_dictionary, process)
    h_processes[process] = {}
    #print("process, variable, process_variable, process_weights, process_mask, lengths(var, weights, mask)") # DEBUG
    #print(process)  # DEBUG
    #print(variable) # DEBUG
    #print(process_variable) # DEBUG
    #print(process_weights)  # DEBUG
    #print(process_mask) # DEBUG
    #print(len(process_variable), len(process_weights), len(process_mask)) # DEBUG
    binned_values, binned_errors = get_binned_info(final_state, testing, process, process_variable, 
                                                   xbins_, process_weights, lumi_, process_mask)
    h_processes[process]["BinnedEvents"] = binned_values
    h_processes[process]["BinnedErrors"] = binned_errors
  return h_processes


def get_binned_data(final_state, testing, data_dictionary, variable, xbins_, lumi_, mask={}, mask_n=999):
  h_data_by_dataset = get_binned_process(final_state, testing, data_dictionary, variable, xbins_, lumi_, mask, mask_n)
  h_data = {}
  h_data["Data"] = {}
  first_key = list(h_data_by_dataset)[0]
  h_data["Data"]["BinnedEvents"] = np.zeros(len(h_data_by_dataset[first_key]["BinnedEvents"]))
  h_data["Data"]["BinnedErrors"] = np.zeros(len(h_data_by_dataset[first_key]["BinnedErrors"]))
  for dataset in h_data_by_dataset:
    h_data["Data"]["BinnedEvents"] += h_data_by_dataset[dataset]["BinnedEvents"]
    h_data["Data"]["BinnedErrors"] += h_data_by_dataset[dataset]["BinnedErrors"] #still squared errors
  return h_data


def get_binned_backgrounds(final_state_mode, testing, background_dictionary, variable, xbins_, lumi_, 
                           presentation_mode=False, mask={}, mask_n=999):
  '''
  Treat each MC process, then group the output by family into flat dictionaries.
  Relies on all family names being mutually exclusive and no processes containing "Other" in their names :)

  Add up separate MC histograms for processes belonging to the same family.
  For example, with three given inputs of the same family, the output is the final line:
    WWToLNu2Q = [0.0, 1.0, 5.5, 0.5]
    WZTo2L2Nu = [0.0, 2.0, 7.5, 0.2]
    ZZTo4L    = [0.0, 3.0, 4.5, 0.1]
    --------------------------------
    VV        = [0.0, 6.0, 17.5, 0.8]
  Inputs without the specified 'parent_process_key' are ignored,
  therefore, this function is called once for each parent process
  '''
  skip_background_accumulation = False # DEBUG
  h_MC_by_process = get_binned_process(final_state_mode, testing, background_dictionary, variable, xbins_, lumi_, mask, mask_n)
  if (skip_background_accumulation): return h_MC_by_process

  # Note: Re-ordering of backgrounds in the stacked histogram can be done here by rearranging the processes in these lists
  if presentation_mode:
    keep_separate = { # order of these processes determines initial stack order on plot
      "ditau" : ["JetFakes", "Other", "DY"],
      "mutau" : ["JetFakes", "Other", "DY"],
      "etau"  : ["JetFakes", "Other", "DY"],
      "emu"   : ["JetFakes", "TT", "Other", "DY"],
    }
  else:
    default_families = ["JetFakes", "TT", "ST", "VV", "DY"] # Note no WJ by default !!
    default_families_WJ = ["JetFakes", "TT", "ST", "VV", "WJ", "DY"]
    keep_separate = {"ditau" : default_families, "mutau" : default_families, 
                     "etau"  : default_families_WJ, "emu"   : default_families}
  MC_by_family = keep_separate[final_state_mode]

  # initialize empty family entries here
  first_key = list(h_MC_by_process)[0]
  h_MC_by_family = {}
  for family_name in MC_by_family:
    h_MC_by_family[family_name] = {}
    h_MC_by_family[family_name]["BinnedEvents"] = np.zeros(len(h_MC_by_process[first_key]["BinnedEvents"]))
    h_MC_by_family[family_name]["BinnedErrors"] = np.zeros(len(h_MC_by_process[first_key]["BinnedErrors"]))
 
  background_is_processed = {}
  for MC_process in h_MC_by_process:
    background_is_processed[MC_process] = False
    if ("Other" in MC_by_family): MC_by_family.remove("Other") # remove so it's not looped over as a family name
    for family_name in MC_by_family:
      if   (not background_is_processed[MC_process]) and (family_name in MC_process):
        h_MC_by_family[family_name]["BinnedEvents"] += h_MC_by_process[MC_process]["BinnedEvents"]
        h_MC_by_family[family_name]["BinnedErrors"] += h_MC_by_process[MC_process]["BinnedErrors"]
        background_is_processed[MC_process] = True
      elif ( (not background_is_processed[MC_process]) 
            and (np.any([diboson_tag in MC_process for diboson_tag in ["WW", "WZ", "ZZ"]]))
            and (not presentation_mode) ): # special handling for VV when not in presentation mode
        h_MC_by_family["VV"]["BinnedEvents"] += h_MC_by_process[MC_process]["BinnedEvents"]
        h_MC_by_family["VV"]["BinnedErrors"] += h_MC_by_process[MC_process]["BinnedErrors"]
        background_is_processed[MC_process] = True
      # TODO: Need this below? Wasn't "Other" removed above?
      #elif (not background_is_processed[MC_process]) and (not np.any([family_name in MC_process for family_name in MC_by_family])):
      #  h_MC_by_family["Other"]["BinnedEvents"] += h_MC_by_process[MC_process]["BinnedEvents"]
      #  h_MC_by_family["Other"]["BinnedErrors"] += h_MC_by_process[MC_process]["BinnedErrors"] # TODO: add in quadrature
      #  background_is_processed[MC_process] = True
      else: pass
        # background_is_processed[MC_process] == True OR 
        # current family name doesn't match sample, but a later one does
        # for example, MC_process = DY0JNLO , but it has to go through families JetFakes, TT, ST, VV before DY
  for process_key, is_processed in background_is_processed.items():
    if (not is_processed): print(f"Warning! {process_key} wasn't processed! It's not part of the plot!")

  return h_MC_by_family

def get_summed_backgrounds(h_backgrounds):
  '''
  Return a dictionary of summed backgrounds
  Expecting h_backgrounds to be split and binned already
  '''
  accumulated_values = 0
  accumulated_errors = 0
  for background in h_backgrounds:
    accumulated_values += h_backgrounds[background]["BinnedEvents"]
    accumulated_errors += h_backgrounds[background]["BinnedErrors"]
  h_summed_backgrounds = {}
  h_summed_backgrounds["Bkgd"] = {}
  h_summed_backgrounds["Bkgd"]["BinnedEvents"] = accumulated_values
  h_summed_backgrounds["Bkgd"]["BinnedErrors"] = accumulated_errors #still squared errors
  return h_summed_backgrounds


def get_binned_signals(final_state, testing, signal_dictionary, variable, xbins_, lumi_, mask={}, mask_n=999):
  h_signals = get_binned_process(final_state, testing, signal_dictionary, variable, xbins_, lumi_, mask, mask_n)
  return h_signals


def get_MC_weights(MC_dictionary, process):
  gen     = MC_dictionary[process]["Generator_weight"]
  PU      = MC_dictionary[process]["PUweight"]
  TauSF   = MC_dictionary[process]["TauSFweight"]
  MuSF    = MC_dictionary[process]["MuSFweight"]
  ElSF    = MC_dictionary[process]["ElSFweight"]
  BTagSF  = MC_dictionary[process]["BTagSFfull"]
  DY_Zpt  = MC_dictionary[process]["Weight_DY_Zpt"]
  TT_NNLO = MC_dictionary[process]["Weight_TTbar_NNLO"]
  full_weights = gen * PU * TauSF * MuSF * ElSF *\
                 BTagSF * DY_Zpt * TT_NNLO

  # Additional weights per individual sample
  additional = 1.
  #if "WJets" in process: 
  #  additional = MC_dictionary[process]["StitchWeight_WJets_NLO"]
  full_weights *= additional

  # use this to achieve no SF weights, or no Gen Weights
  skip_SFs = False
  inclued_gen_weights = True
  if skip_SFs == True:
    print("  NO SFs APPLIED!  ")
    if include_gen_weights == False:
      print("  NO GEN WEIGHTS APPLIED EITHER!  ")
      return np.ones(np.shape(MC_dictionary[process]["Generator_weight"]))
    else:
      return MC_dictionary[process]["Generator_weight"]
  return full_weights


final_state_vars = {
    # can't put nanoaod branches here because this dictionary is used to protect branches created internally
    "none"   : [],
    "ditau"  : ["FS_t1_pt", "FS_t1_eta", "FS_t1_phi", "FS_t1_dxy", "FS_t1_dz", "FS_t1_chg", "FS_t1_DM", "FS_t1_mass",
                "FS_t2_pt", "FS_t2_eta", "FS_t2_phi", "FS_t2_dxy", "FS_t2_dz", "FS_t2_chg", "FS_t2_DM", "FS_t2_mass",
                "FS_t1_flav", "FS_t2_flav", 
                #"FS_t1_rawPNetVSjet", "FS_t1_rawPNetVSmu", "FS_t1_rawPNetVSe",
                #"FS_t2_rawPNetVSjet", "FS_t2_rawPNetVSmu", "FS_t2_rawPNetVSe",
                "FS_t1_DeepTauVSjet", "FS_t1_DeepTauVSmu", "FS_t1_DeepTauVSe", 
                "FS_t2_DeepTauVSjet", "FS_t2_DeepTauVSmu", "FS_t2_DeepTauVSe", 
                "FS_trig_idx", "FS_pair_DM",
                "FS_mt_t1t2", "FS_mt_t1_MET", "FS_mt_t2_MET", "FS_mt_TOT", "FS_dphi_t1t2", "FS_deta_t1t2",
                "FS_t1_FLsig", "FS_t1_FLX", "FS_t1_FLY", "FS_t1_FLZ", "FS_t1_FLmag",
                "FS_t1_ipLsig", "FS_t1_ip3d", "FS_t1_tk_lambda", "FS_t1_tk_qoverp",
                "FS_t2_FLsig", "FS_t2_FLX", "FS_t2_FLY", "FS_t2_FLZ", "FS_t2_FLmag",
                "FS_t2_ipLsig", "FS_t2_ip3d", "FS_t2_tk_lambda", "FS_t2_tk_qoverp",
               ],

    "mutau"  : ["FS_mu_pt", "FS_mu_eta", "FS_mu_phi", "FS_mu_iso", "FS_mu_dxy", "FS_mu_dz", "FS_mu_chg", "FS_mu_mass",
                "FS_tau_pt", "FS_tau_eta", "FS_tau_phi", "FS_tau_dxy", "FS_tau_dz", "FS_tau_chg", "FS_tau_mass", "FS_tau_DM",
                "FS_mt", "FS_t1_flav", "FS_t2_flav", "FS_nbJet", "FS_acoplan",
                "FS_LeadTkPtOverTau",
                #"FS_tau_rawPNetVSjet", "FS_tau_rawPNetVSmu", "FS_tau_rawPNetVSe"
                "FS_dphi_mutau", "FS_deta_mutau",
               ],

    "etau"   : ["FS_el_pt", "FS_el_eta", "FS_el_phi", "FS_el_iso", "FS_el_dxy", "FS_el_dz", "FS_el_chg", "FS_el_mass",
                "FS_tau_pt", "FS_tau_eta", "FS_tau_phi", "FS_tau_dxy", "FS_tau_dz", "FS_tau_chg", "FS_tau_mass", "FS_tau_DM",
                "FS_mt", "FS_t1_flav", "FS_t2_flav", "FS_nbJet",
                "FS_dphi_etau", "FS_deta_etau",
               ],

    "dimuon" : ["FS_m1_pt", "FS_m1_eta", "FS_m1_phi", "FS_m1_iso", "FS_m1_dxy", "FS_m1_dz",
                "FS_m2_pt", "FS_m2_eta", "FS_m2_phi", "FS_m2_iso", "FS_m2_dxy", "FS_m2_dz",
               ],

    "emu"    : ["FS_el_pt", "FS_el_eta", "FS_el_phi", "FS_el_iso", "FS_el_dxy", "FS_el_dz", "FS_el_chg",
                "FS_mu_pt", "FS_mu_eta", "FS_mu_phi", "FS_mu_iso", "FS_mu_dxy", "FS_mu_dz", "FS_mu_chg",
                "FS_nbJet", "FS_PZeta",
               ],
}

# TODO this is ugly and bad and i am only doing this out of desperation
# need to make a jet cut function folder, where this would be more at home...
clean_jet_vars = {
    "Inclusive" : ["nCleanJetGT30",
      #"CleanJetGT30_pt_1", "CleanJetGT30_eta_1",
      #"CleanJetGT30_pt_2", "CleanJetGT30_eta_2",
      #"CleanJetGT30_pt_3", "CleanJetGT30_eta_3",
    ],

    "0j" : ["nCleanJetGT30"],
    "1j" : ["nCleanJetGT30", "CleanJetGT30_pt_1", "CleanJetGT30_eta_1", "CleanJetGT30_phi_1"],
    "2j" : ["nCleanJetGT30"],
    "3j" : ["nCleanJetGT30"],
    "4j" : ["nCleanJetGT30"],
    "GTE1j" : ["nCleanJetGT30", 
               "CleanJetGT30_pt_1", "CleanJetGT30_eta_1", "CleanJetGT30_phi_1",
               "CleanJetGT30_pt_2", "CleanJetGT30_eta_2", "CleanJetGT30_phi_2",
               "FS_mjj", "FS_detajj",
              ],
    "GTE2j" : ["nCleanJetGT30", 
               "CleanJetGT30_pt_1", "CleanJetGT30_eta_1", "CleanJetGT30_phi_1",
               "CleanJetGT30_pt_2", "CleanJetGT30_eta_2", "CleanJetGT30_phi_2",
               "FS_mjj", "FS_detajj", 
               "FS_j1index", "FS_j2index", 
               #"FS_dijet_pair_calc", "FS_dijet_pair_HTT",
              ],
}

def set_vars_to_plot(final_state_mode, jet_mode="none"):
  '''
  Helper function to keep plotting variables organized
  '''
  # common to all final states
  vars_to_plot = ["HTT_m_vis", "HTT_dR", "HTT_pT_l1l2", "FastMTT_mass",
                  "PuppiMET_pt", "PuppiMET_phi", "PV_npvs",
                 ]
  FS_vars_to_add = final_state_vars[final_state_mode]
  for var in FS_vars_to_add:
    vars_to_plot.append(var)

  jet_vars_to_add = clean_jet_vars[jet_mode]
  if (jet_mode=="Inclusive") or (jet_mode=="GTE2j"):
    pass
    #jet_vars_to_add += ["HTT_DiJet_dEta_fromHighestMjj", "HTT_DiJet_MassInv_fromHighestMjj",
    #                    "HTT_DiJet_dEta_fromLeadingJets", "HTT_DiJet_MassInv_fromLeadingJets",
    #                    "HTT_DiJet_j1index", "HTT_DiJet_j2index",
    #                   ]
  for jet_var in jet_vars_to_add:
    vars_to_plot.append(jet_var)

  return vars_to_plot


