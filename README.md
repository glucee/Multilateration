# Multilateration Python Script

This script computes the location of a source given its distance to several stations.


## Current Stage
The repo has implemented a Python version of multilateration, which is located in Python\example.py, the requirement for that is:

* Python 3.6
* Scipy
* Numpy

## Algorithm Description

This script implements a multilateration algorithm that, given the coordinates of a finite number of radio stations,
and given their distances to the source (derived from the intensities of the signal they received in a previous step)
computes the most probable coordinates of the source. Even if the distances computed for each station do not match
(in terms of pointing to a single optimal solution) the algorithm finds the coordinates that minimize the error function
and returns the most optimal solution possible.

### Task

Given the implementation in Python folder in Python 3.6, replicate this sample script in C++ in CPP folder, implementing the
optimization algorithm that lies at the core of this script (The Nelder-Mead simplex algorithm) from scratch. The CPP files should work in an embedded system such as Arduino.

### Evaluation

* The final CPP script, should achieve exactly the same estimated source coordinates as the Python example script.

* The final CPP script should be able to run on an Arduino board.

* The final CPP script should be able to compute the estimated location of the source in real time for a subset of <=4 stations.

## Resources

* https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
* https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html#optimize-minimize-neldermead
* https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method
* https://en.wikipedia.org/wiki/Simplex_algorithm
