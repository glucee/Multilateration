# Multilateration Python Script

This script computes the location of a source given its distance to several stations.


## Requirements

* Python 3.6
* Scipy
* Numpy

## Description

This script implements a multilateration algorithm that, given the coordinates of a finite number of radio stations,
and given their distances to the source (derived from the intensities of the signal they received in a previous step)
computes the most probable coordinates of the source. Even if the distances computed for each station do not match
(in terms of pointing to a single optimal solution) the algorithm finds the coordinates that minimize the error function
and returns the most optimal solution possible.

The task: Given the implementation in Python folder in Python 3.6, replicate this sample script in C++ in CPP folder, implementing the
optimization algorithm that lies at the core of this script (The Nelder-Mead simplex algorithm) from scratch. The CPP files should work in an embedded system such as Arduino.

## Resources

* https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
* https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html#optimize-minimize-neldermead
* https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method
* https://en.wikipedia.org/wiki/Simplex_algorithm
