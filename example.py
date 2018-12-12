
"""

This script implements a multilateration algorithm that, given the coordinates of a finite number of radio stations,
and given their distances to the source (derived from the intensities of the signal they received in a previous step)
computes the most probable coordinates of the source. Even if the distances computed for each station do not match
(in terms of pointing to a single optimal solution) the algorithm finds the coordinates that minimize the error function
and returns the most optimal solution possible.

The task: Given the implementation below in Python 3.6, replicate this sample script in C++, implementing the
optimization algorithm that lies at the core of this script (The Nelder-Mead simplex algorithm) from scratch.


https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html#optimize-minimize-neldermead

"""

from scipy.optimize import minimize
import numpy as np

def gps_solve(distances_to_source, stations_coordinates):
	def error(x, c, r):
		return sum([(np.linalg.norm(x - c[i]) - r[i]) ** 2 for i in range(len(c))])

	l = len(stations_coordinates)
	S = sum(distances_to_source)
	# compute weight vector for initial guess
	W = [((l - 1) * S) / (S - w) for w in distances_to_source]
	# get initial guess of point location
	x0 = sum([W[i] * stations_coordinates[i] for i in range(l)])
	# optimize distance from signal origin to border of spheres
	return minimize(error, x0, args=(stations_coordinates, distances_to_source), method='Nelder-Mead').x


if __name__ == "__main__":
	stations = list(np.array([[1,1], [0,1], [1,0], [0,0]]))
	distances_to_source = [0.1, 0.5, 0.5, 1.3]
	print(gps_solve(distances_to_source, stations))