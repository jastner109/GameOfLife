Conways's Game Of Life

Author: Digvijay Singh

Some notes:
Code in python2.
All imported modules in native python.
Use anaconda to run it, color scheme is much better.
Results stored as gif files in "gifs" subfolder. Some examples have been provided.
Gifs file name format: -gridsize-number_of_seeds-epochs-timestamp

* imagemagick required to greate the gifs/ for mac installation command is "brew install imagemagick"
(other OS users kindly figure it out)

Defaults:
gridsize = 25
number of seeds = 100
epochs = 100
backoff = 10 (this is a parameter to check till the how far back in previous generations, whether the current generation is being repeated or not)

Ranges:
gridsize = [10, 100]
number of seeds = [gridsize, gridsize^2/2]
epochs = [10, 999]

Algorithm notes:
Larger grid sizes will take more time.
If invalid values provided, will revert to defaults.
For good game, provide at least gridsize^2/4 number of seeds.
Even with large seed amount, convergence is usually achieved after 100 epochs.
