# libraries
import numpy as np
import matplotlib.pyplot as plt

# for plotting errors in MC
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

### README
# this file contains functions to setup plotting interfaces and draw the plots themselves

from MC_dictionary        import MC_dictionary
from binning_dictionary   import binning_dictionary, label_dictionary
from triggers_dictionary  import triggers_dictionary

from calculate_functions  import yields_for_CSV, calculate_underoverflow


def make_pie_chart(data_hist, MC_dictionary, use_data=False, use_fakes=False):
      sums, labels, colors = [], [], []
      for process in MC_dictionary:
        if ( (use_fakes == False) and (process=="QCD") ): pass
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


def plot_data(histogram_axis, xbins, data_info, luminosity, 
              color="black", label="Data", marker="o", fillstyle="full"):
  '''
  Add the data histogram to the existing histogram axis, computing errors in a simple way.
  For data, since points and error bars are used, they are shifted to the center of the bins.
  TODO: The error calculation should be followed up and separated to another function. 
  '''
  sum_of_data = np.sum(data_info)
  stat_error = np.array([np.sqrt(entry) if entry > 0 else 0 for entry in data_info]) #error = √N
  midpoints   = get_midpoints(xbins)
  bin_width  = abs(xbins[0:-1]-xbins[1:])/2 # only works for uniform bin widths
  label = f"Data [{sum_of_data:>.0f}]" if label == "Data" else label
  histogram_axis.errorbar(midpoints, data_info, xerr=bin_width, yerr=stat_error, 
                          color=color, marker=marker, fillstyle=fillstyle, label=label,
                          linestyle='none', markersize=3)
  #below plots without error bars
  #histogram_axis.plot(midpoints, data_info, color="black", marker="o", linestyle='none', markersize=2, label="Data")


def plot_MC(histogram_axis, xbins, stack_dictionary, luminosity,
            custom=False, color="default", label="MC", fill=True):
  # TODO handle variable binning with list of differences
  '''
  TODO update this
  Add background MC histograms to the existing histogram axis. The input 'stack_dictionary'
  contains a list of backgrounds (which should be pre-grouped, normally), the name of which
  determines colors and labels of the stacked output. 

  Since the 'bar' method of matplotlib doesn't necessarily expect histogram data, 
  the final bin edge is omitted so that the size of the xaxis array and the plotted 
  data array are equal. To stack the plots, the 'bottom'  keyword argument is 
  adjusted each iteration of the loop such that it is the top of the previous histogram. 
  '''
  weight_per_bin_squared = 0
  color_array, label_array, stack_array = [], [], []
  for MC_process in stack_dictionary:
    if custom == True:
      pass
    else:
      color, label, _ = set_MC_process_info(MC_process, luminosity)
    current_hist = stack_dictionary[MC_process]["BinnedEvents"]
    label += f" [{np.sum(current_hist):>.0f}]"
    current_hist = np.append(current_hist, 0)
    color_array.append(color)
    label_array.append(label)
    stack_array.append(current_hist)
    #print(MC_process) # DEBUG
    #print("weight per bin squared")
    #print(weight_per_bin_squared)
    #weight_per_bin_squared += np.array([entry*entry if entry > 0 else 0 for entry in current_hist])

  xbins = np.append(xbins, xbins[-1]+(xbins[1]-xbins[0]))
  histogram_axis.stackplot(xbins[0:-1], stack_array, step="post", edgecolor="black", colors=color_array, labels=label_array)

  summed_squared_weights = weight_per_bin_squared
  #print("summed_squared_weights")
  #print(summed_squared_weights)
  # error = √sum(weights_i**2)
  #stat_error = np.array([np.sqrt(squared_weight) if squared_weight > 0 else 0 for squared_weight in summed_squared_weights])
  #print("stat_error")
  #print(stat_error)
  #histogram_axis.errorbar(xbins[0:-1], previous_histogram_tops, yerr=stat_error, fmt="o")
  # error boxes not quite working yet
  #histogram_axis.errorbar(xbins[0:-1], previous_histogram_tops, yerr=5, fmt="o", markersize=3) # faked
  #_ = make_error_boxes(histogram_axis, xbins[0:-1], previous_histogram_tops, # fake
  #                     abs(xbins[1:]-xbins[0:-1])/2, 10*np.ones(previous_histogram_tops.shape),
  #                     facecolor='grey', edgecolor='none', alpha=0.1)


  #histogram_axis.errorbar(xbins[0:-1], previous_histogram_tops, yerr=5, fmt="o", markersize=3) # faked
  # actually, check if stairs has an error method
  # TODO : it would be easier to store errors when binning events? probably
  # USE fill_between axis method for shaded errors
  # https://stackoverflow.com/questions/60697625/error-bars-as-a-shaded-area-on-matplotlib-pyplot-step

#from https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html#sphx-glr-gallery-statistics-errorbars-and-boxes-py
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):
    # Loop over data points; create box from errors at each point
    #errorboxes = [Rectangle((x - xe, y - ye), xe.sum(), ye.sum())
    errorboxes = [Rectangle((x, y), xe, ye)
                  for x, y, xe, ye in zip(xdata, ydata, xerror, yerror)]
    # Create patch collection with specified colour/alpha
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)
    # Add collection to axes
    ax.add_collection(pc)
    # Plot errorbars
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')
    return artists
  

def plot_signal(histogram_axis, xbins, signal_dictionary, luminosity):
  '''
  Similar to plot_MC, except signals are not stacked, and the 'stair' method
  of matplotlib DOES expect histogram data, so no adjustment to xbins is necessary.
  '''
  for signal in signal_dictionary:
    color, label, _ = set_MC_process_info(signal, luminosity, scaling=True, signal=True)
    current_hist = signal_dictionary[signal]["BinnedEvents"]
    label += f" [{np.sum(current_hist):>.0f}]"
    stairs = histogram_axis.stairs(current_hist, xbins, color=color, label=label, fill=False)


def set_MC_process_info(process, luminosity, scaling=False, signal=False):
  '''
  Obtain process-specific styling and scaling information.
  MC_dictionary is maintained in a separate file.
  '''
  color = MC_dictionary[process]["color"]
  label = MC_dictionary[process]["label"]
  if scaling:
  # factor of 1000 comes from lumi and XSec units of fb^-1 = 10E15 b^-1 and pb = 10E-12 b respectively
    plot_scaling = MC_dictionary[process]["plot_scaling"] # 1 for all non-signal processes by default
    scaling = 1000. * plot_scaling * luminosity * MC_dictionary[process]["XSec"] / MC_dictionary[process]["NWEvents"]
    if process=="myQCD": scaling = 1
    # TODO pass "testing" boolean through here too
    if process=="TTTo2L2Nu": scaling *= 15 # scale up by n*ignored files
    if process=="TTToSemiLeptonic": scaling *= 27 # scale up by n*ignored files
    #if process=="DYInc": scaling *=6.482345 # scale up factor for New Dimuon DY
  if signal:
    label += " x" + str(plot_scaling)
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


def setup_TnP_plot():
  fig, ax = plt.subplots() #subplot?
  return ax


def add_CMS_preliminary(axis):
  '''
  Add text to plot following CMS plotting guidelines
  https://twiki.cern.ch/twiki/bin/viewauth/CMS/Internal/FigGuidelines#Example_ROOT_macro_python
  '''
  CMS_text = "CMS"
  axis.text(0.01, 1.02, CMS_text, transform=axis.transAxes, fontsize=16, weight='bold')
  preliminary_text = "Preliminary"
  axis.text(0.12, 1.02, preliminary_text, transform=axis.transAxes, fontsize=16, style='italic')


def add_final_state_and_jet_mode(axis, final_state_mode, jet_mode):
  final_state_str = {
    "ditau"  : r"${\tau_h}{\tau_h}$",
    "mutau"  : r"${\mu}{\tau_h}$",
    "mutau_TnP"  : r"$Z{\rightarrow}{\tau_\mu}{\tau_h}$",
    "etau"   : r"$e{\tau_h}$",
    "dimuon" : r"${\mu}{\mu}$",
  }
  jet_mode_str = {
    "Inclusive" : "≥0j",
    "0j"    : "0j",
    "1j"    : "1j",
    "GTE1j" : "≥1j",
    "GTE2j" : "≥2j",
  }
  axis.text(0.05, 0.92, 
  #axis.text(0.45, -0.045, 
            final_state_str[final_state_mode] + " : " + jet_mode_str[jet_mode], 
            transform=axis.transAxes, fontsize=10)


def spruce_up_single_plot(axis, variable_name, ylabel, title, final_state_mode, jet_mode, yrange=None):
  add_CMS_preliminary(axis)
  add_final_state_and_jet_mode(axis, final_state_mode, jet_mode)
  axis.set_title(title, loc='right', y=0.98)
  axis.set_ylabel("Events / bin")
  axis.minorticks_on()
  axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  axis.set_xlabel(variable_name)
  axis.set_ylabel(ylabel)
  if (yrange != None): axis.set_ylim(yrange)
  leg = axis.legend(loc="upper right", frameon=True, bbox_to_anchor=[0.6, 0.4, 0.4, 0.6],
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
  #histogram_axis.set_ylim([0, histogram_axis.get_ylim()[1]*1.2]) # scale top of graph up by 20%
  histogram_axis.set_title(title, loc='right', y=0.98)
  histogram_axis.set_ylabel("Events / bin")
  histogram_axis.minorticks_on()
  histogram_axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  #yticks = histogram_axis.yaxis.get_major_ticks()
  #yticks[0].label1.set_visible(false) # hides a zero that overlaps with the upper plot

  ratio_plot_axis.set_ylim([0.45, 1.55]) # 0.0, 2.0 also make sense
  ratio_plot_axis.set_xlabel(variable_name) # shared axis label
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


def spruce_up_TnP_plot(axis, variable_name, title):
  add_CMS_preliminary(axis)
  axis.set_title(title, loc='right', y=0.98)
  axis.set_ylabel("Efficiency (Probe/Tag)")
  axis.set_ylim([0.0, 1.1])
  axis.minorticks_on()
  axis.tick_params(which="both", top=True, bottom=True, right=True, direction="in")
  axis.set_xlabel(variable_name) # shared axis label
  axis.grid(True)


def spruce_up_legend(histogram_axis, final_state_mode, data_hists):
  # this post has good advice about moving the legend off the plot
  # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
  # defaults are here, but using these to mimic ROOT defaults 
  # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
  leg = histogram_axis.legend(loc="upper right", frameon=True, bbox_to_anchor=[0.6, 0.4, 0.4, 0.6],
                        labelspacing=0.35, handlelength=0.8, handleheight=0.8, handletextpad=0.4)

  # some matplotlib documentation about transforming plotting coordinate systems
  # https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html
  # DEBUG
  #print(leg.get_bbox_to_anchor())
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transAxes.inverted()))
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transData))
  #plt.draw()
  #print(leg.get_bbox_to_anchor())
  #print("transAxes, inverted, transData, inverted")
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transAxes))
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transAxes.inverted()))
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transData))
  #print(leg.get_bbox_to_anchor().transformed(histogram_axis.transData.inverted())) # this
  if final_state_mode == "dimuon":
    handles, original_labels = histogram_axis.get_legend_handles_labels()
    labels, yields = yields_for_CSV(histogram_axis)
    save_entry = [i for i,yield_ in enumerate(yields) if yield_ != 0]
    save_handles = [handles[entry] for entry in save_entry]
    save_labels  = [labels[entry] for entry in save_entry]
    histogram_axis.legend(save_handles, save_labels)
    print(f"Legend lables were previously {original_labels}")
    print("Removed samples with yield=0 from legend!")

def make_ratio_no_plot(numerator_data, numerator_type, numerator_weight,
                       denominator_data, denominator_type, denominator_weight):
  ratio = numerator_data/denominator_data
  ratio[np.isnan(ratio)] = 0 # numpy idiom to set "nan" values to 0
  if (numerator_type=="Data") and (denominator_type=="Data"):
    # ratio error = (A/B) * √ [ (1/A) + (1/B) ] \
    statistical_error = np.array([ ratio[i] * np.sqrt( (1/numerator_data[i]) + (1/denominator_data[i]))
                        if ((denominator_data[i] > 0) and (numerator_data[i] > 0)) else 0
                        for i,_ in enumerate(denominator_data)]) 
  statistical_error[np.isnan(statistical_error)] = 0
  return ratio, statistical_error
 
 
def make_ratio_plot(ratio_axis, xbins, 
                    numerator_data, numerator_type, numerator_weight,
                    denominator_data, denominator_type, denominator_weight,
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
  midpoints = get_midpoints(xbins)
  bin_width  = abs(xbins[0:-1]-xbins[1:])/2
  #print(bin_width, len(bin_width)) # TODO COME BACK HERE soon
  #print(statistical_error, len(statistical_error))
  #bin_width = []
  #bin_width.extend([xbins[i+1] - xbins[i] for i in range(len(xbins)-1)])
  #print(bin_width)
  #bin_width.append(xbins[-1] - xbins[-2]) 
  #print(bin_width)
  ratio_axis.errorbar(midpoints, ratio, xerr=bin_width, yerr=statistical_error,
                    color=color, marker="o", linestyle='none', markersize=2, label=label)

  return ratio, statistical_error


def get_trimmed_Generator_weight_copy(variable, single_background_dictionary, jet_mode):
  '''
  Only to be used with Inclusive jet mode

  When plotting inclusively, we would like to show j1_pt, j2_pt, j3_pt, etc.
  However, these branches are not available for every event, and to plot them we
  also need the Generator_weight branch. So, what we do is make copies of the Generator_weight
  branch for only the events also found in the variable we want to plot. This is
  possible because the jet_mode cut branch is defined and stored in our dictionary
  '''
  Gen_weight = single_background_dictionary["Generator_weight"]
  Cuts       = single_background_dictionary["Cuts"]
  if   ("_1" in variable) and (jet_mode=="Inclusive"):
    # events with ≥1 j
    pass_jet_cut = sorted(np.concatenate([Cuts["pass_1j_cuts"], Cuts["pass_2j_cuts"], Cuts["pass_3j_cuts"]]))
  elif (("_2" in variable) or ("fromHighestMjj" in variable)) and (jet_mode=="Inclusive"):
    # events with ≥2 j
    pass_jet_cut = sorted(np.concatenate([Cuts["pass_2j_cuts"], Cuts["pass_3j_cuts"]]))
  elif ("_3" in variable) and ((jet_mode=="Inclusive") or (jet_mode=="GTE2j")):
    pass_jet_cut = Cuts["pass_3j_cuts"]

    print("gen weight, pass jet cut, and temp weight shapes") # DEBUG
    print(Gen_weight.shape, pass_jet_cut.shape) # DEBUG
  temp_weight = np.take(Gen_weight, pass_jet_cut)
  print("temp_weight.shape")
  print(temp_weight.shape) # DEBUG

  return temp_weight


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


def get_binned_info(process_name, process_variable, xbins, process_weights, luminosity, underflow=True):
  '''
  Take in a list of events and produce a histogram (values binned in a numpy array).
  'scaling' is either set to 1 for data (no scaling) or retrieved from the MC_dictionary.
  Underflows and overflows are included in the first and final bins of the output histogram by default.
  Note: 'process_variable' is a list of events
  '''
  scaling = 1 if "Data" in process_name else set_MC_process_info(process_name, luminosity, scaling=True)[2]
  weights = scaling*process_weights
  underflow, overflow = calculate_underoverflow(process_variable, xbins, weights)
  binned_values, _    = np.histogram(process_variable, xbins, weights=weights)
  if underflow:  binned_values[0]   += underflow
  binned_values[-1]  += overflow
  binned_weight_2, _  = np.histogram(weights, xbins, weights=weights*weights)
  binned_errors       = np.array([np.sqrt(value) for value in binned_weight_2])
  return binned_values, binned_errors


def get_binned_data(data_dictionary, variable, xbins_, lumi_, underflow=True):
  '''
  Standard loop to get only the plotted variable from a dictionary containing data.

  This is written so that it can be extended to use multiple datasets, but the default
  usage is only one dataset at a time. 
  '''
  h_data_by_dataset = {}
  for dataset in data_dictionary:
    data_variable = data_dictionary[dataset]["PlotEvents"][variable]
    data_weights  = np.ones(np.shape(data_variable)) # weights of one for data
    # normalized to Era D, Era E for some reason is still larger than it should be
    if dataset == "DataMuonEraC":
      data_weights = (2.922/4.953)*data_weights
    if dataset == "DataMuonEraD":
      data_weights = (2.922/2.922)*data_weights
    if dataset == "DataMuonEraE":
      data_weights = (2.922/5.672)*data_weights
    if dataset == "DataMuonEraF":
      data_weights = (2.922/17.61)*data_weights
    if (dataset == "DataMuonEraG") or (dataset=="DataMuonEraGPrompt"):
      data_weights = (2.922/3.06)*data_weights
    #print(f"For {dataset} using weights:") # DEBUG
    #print(data_weights) # DEBUG
    h_data_by_dataset[dataset] = {}
    binned_values, binned_errors = get_binned_info(dataset, data_variable, xbins_, data_weights, lumi_, underflow)
    h_data_by_dataset[dataset]["BinnedEvents"] = binned_values
    h_data_by_dataset[dataset]["BinnedErrors"] = binned_errors
  h_data = accumulate_datasets(h_data_by_dataset)
  return h_data


def accumulate_datasets(dataset_dictionary):
  '''
  Very similar to accumulate_MC_subproceses
  Written to add datasets (Muon, Tau, EGamma, MuonEG) together
  '''
  accumulated_values = 0
  for dataset in dataset_dictionary:
    accumulated_values += dataset_dictionary[dataset]["BinnedEvents"]

  return accumulated_values


def accumulate_MC_subprocesses(parent_process, process_dictionary):
  '''
  Add up separate MC histograms for processes belonging to the same family.
  For example, with three given inputs of the same family, the output is the final line:
    WWToLNu2Q = [0.0, 1.0, 5.5, 0.5]
    WZTo2L2Nu = [0.0, 2.0, 7.5, 0.2]
    ZZTo4L    = [0.0, 3.0, 4.5, 0.1]
    --------------------------------
    VV        = [0.0, 6.0, 17.5, 0.8]
  Inputs not belonging to the specified 'parent_process' are ignored,
  therefore, this function is called once for each parent process
  '''
  accumulated_values = 0
  for MC_process in process_dictionary:
    skip_process = False
    if (MC_process == "DYGen") or (MC_process == "DYGenNLO"):
      skip_process = True
    if (MC_process == "DYLep") or (MC_process == "DYLepNLO"):
      skip_process = True
    if (MC_process == "DYJet") or (MC_process == "DYJetNLO"):
      skip_process = True
    if get_parent_process(MC_process, skip_process=skip_process) == parent_process:
      accumulated_values += process_dictionary[MC_process]["BinnedEvents"]
  return accumulated_values


def get_parent_process(MC_process, skip_process=False):
  '''
  Given some process, return a corresponding parent_process, effectively grouping
  related processes (i.e. DYInclusive, DY1, DY2, DY3, and DY4 all belong to DY).
  TODO: simplify this code, it is currently written in a brain-dead way
  '''
  parent_process = ""
  # TODO
  # pass through for no parent process
  # this parent process is most helpful for VV, but for the rest...
  # it would be useful to have a mode where no automatic combining takes place
  #if   "JetFakes" in MC_process:  parent_process = "DYJetFakes" # DEBUG
  #elif "LepFakes" in MC_process:  parent_process = "DYLepFakes" # DEBUG
  #elif "Genuine"  in MC_process:  parent_process = "DY" # DEBUG
  if skip_process: parent_process = MC_process
  #if "DY" in MC_process: parent_process = "DY"
  elif ("QCD" in MC_process) and (MC_process != "myQCD"): parent_process = "QCD"
  elif "WJets" in MC_process:  parent_process = "WJ"
  elif "TT"    in MC_process:  parent_process = "TT"
  elif "ST"    in MC_process:  parent_process = "ST"
  elif ("WW"   in MC_process or 
        "WZ"   in MC_process or 
        "ZZ"   in MC_process): parent_process = "VV"
  else:
    if MC_process == "QCD":
      pass
    else:
      print(f"No matching parent process for {MC_process}, continuing as individual process...")
  return parent_process


# TODO: jetmode not actually used here
def get_binned_backgrounds(background_dictionary, variable, xbins_, lumi_, jet_mode, underflow=True):
  '''
  Treat each MC process, then group the output by family into flat dictionaries.
  Also, sum all backgrounds into h_summed_backgrounds to use in ratio plot.
  '''
  h_MC_by_process = {}
  for process in background_dictionary:
    process_variable = background_dictionary[process]["PlotEvents"][variable]
    if len(process_variable) == 0: continue
    if process == "myQCD":  
      process_weights = background_dictionary[process]["FF_weight"]
    #if ( (("JetGT30_" in variable or "fromHighestMjj" in variable) and (jet_mode=="Inclusive")) or 
    #     ((variable == "CleanJetGT30_pt_3" or variable == "CleanJetGT30_eta3") and (jet_mode=="GTE2j")) ):
    ##if ("JetGT30_" in variable) and (jet_mode=="Inclusive"):
    #  process_weights = get_trimmed_Generator_weight_copy(variable, background_dictionary[process], jet_mode)
    else:
      process_weights = get_MC_weights(background_dictionary, process)
    #print("process, variable, variable and weight shapes") # DEBUG 
    #print(process, variable, process_variable.shape, process_weights.shape) # DEBUG
    h_MC_by_process[process] = {}
    binned_values, binned_errors = get_binned_info(process, process_variable, xbins_, process_weights, lumi_, underflow)
    h_MC_by_process[process]["BinnedEvents"] = binned_values
    h_MC_by_process[process]["BinnedErrors"] = binned_errors
  # add together subprocesses of each MC family
  h_MC_by_family = {}
  # see what processes exist in the dictionary
  if "myQCD" in background_dictionary.keys(): # QCD is on bottom of stack since it is first called
    h_MC_by_family["myQCD"] = {}
    h_MC_by_family["myQCD"]["BinnedEvents"] = h_MC_by_process["myQCD"]["BinnedEvents"]
    all_MC_families  = ["TT", "ST", "WJ", "VV", "DYJet", "DYLep", "DYGen"] # far left is bottom of stack
  else:
    all_MC_families  = ["QCD", "TT", "ST", "WJ", "VV", "DYJet", "DYLep", "DYGen"] # far left is bottom of stack
  used_MC_families = []
  for family in all_MC_families:
    for process in h_MC_by_process:
      if (("WW" in process) or ("WZ" in process) or ("ZZ" in process)) and ("VV" not in used_MC_families):
        used_MC_families.append("VV")
      elif (family in process) and (family not in used_MC_families):
        used_MC_families.append(family)

  for family in used_MC_families:
    h_MC_by_family[family] = {}
    h_MC_by_family[family]["BinnedEvents"] = accumulate_MC_subprocesses(family, h_MC_by_process)
  h_backgrounds = h_MC_by_family
  #print(h_MC_by_family) # DEBUG
  # used for ratio plot
  h_summed_backgrounds = 0
  for background in h_backgrounds:
    h_summed_backgrounds += h_backgrounds[background]["BinnedEvents"]

  return h_backgrounds, h_summed_backgrounds


def get_binned_signals(signal_dictionary, variable, xbins_, lumi_, jet_mode):
  #TODO : bundle with background above
  '''
  Signal is put in a separate dictionary from MC, but they are processed identically 
  '''
  h_signals = {}
  for process in signal_dictionary:
    signal_variable = signal_dictionary[process]["PlotEvents"][variable]
    if len(signal_variable) == 0: continue
    #if ("JetGT30_" in variable or "fromHighestMjj" in variable) and (jet_mode=="Inclusive" or jet_mode=="GTE2j"):
    if ( (("JetGT30_" in variable or "fromHighestMjj" in variable) and (jet_mode=="Inclusive")) or 
         ((variable == "CleanJetGT30_pt_3" or variable == "CleanJetGT30_eta3") and (jet_mode=="GTE2j")) ):
    #if ("JetGT30_" in variable) and (jet_mode=="Inclusive"):
      signal_weights = get_trimmed_Generator_weight_copy(variable, signal_dictionary[process], jet_mode)
    else:
      signal_weights = get_MC_weights(signal_dictionary, process)
    h_signals[process] = {}
    binned_values, binned_errors = get_binned_info(process, signal_variable, xbins_, signal_weights, lumi_)
    h_signals[process]["BinnedEvents"] = binned_values
    h_signals[process]["BinnedErrors"] = binned_errors
  return h_signals


def get_MC_weights(MC_dictionary, process):
  gen     = MC_dictionary[process]["Generator_weight"]
  PU      = MC_dictionary[process]["PUweight"]
  TauSF   = MC_dictionary[process]["TauSFweight"]
  MuSF    = MC_dictionary[process]["MuSFweight"]
  ElSF    = MC_dictionary[process]["ElSFweight"]
  BTagSF  = MC_dictionary[process]["BTagSFfull"]
  DY_Zpt  = MC_dictionary[process]["Weight_DY_Zpt"] # bugged in V12 samples, always 1
  TT_NNLO = MC_dictionary[process]["Weight_TTbar_NNLO"]
  full_weights = gen * PU * TauSF * MuSF * ElSF *\
                 BTagSF * DY_Zpt * TT_NNLO
  return full_weights
