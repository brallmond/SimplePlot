
## How to Use the FF Scripts

First, I'm assuming you're quite familiar with how the library works already. If not, good luck anyways.

There are three scripts currently and each has its own purpose.

`FF_plot_set1.py` `FF_plot_set1p5_ratios.py` `FF_plot_set2.py`

`FF_plot_set1.py` should be used to make Data+MC graphs in various non-signal regions.
(link an image)
The region produced can be changed via the "region" variable, but the default is make all 7 for ditau.
As input, the file just needs your data.
The output is simply the plots.

`FF_plot_set1p5_ratios.py` should be used to make comparisons and ratios of different regions.
It is written such that any two regions can be compared with the same variable on the same plot, and then a
fit is performed on the ratio of the lines.
As input, the file needs two input valid regions.
The output is simply the plots, and one would use the fit values from terminal or the plots themselves in the next step.

`FF_plot_set2.py` should be used to make validations.
It is written such that any two regions can be used, although not every combination is sensible.
As input, the file needs two input regions, and the fit information (coefficients) from `FF_plot_set1p5_ratios.py`.
The output is simply the plots.

