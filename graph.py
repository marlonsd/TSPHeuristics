import argparse, math, sys

import numpy as np

from mpmath import nint

class Graph:

	def __init__(self, points, size, edge):
		self.matrix = np.zeros((size, size))

		for i,a in enumerate(points):
			for j,b in enumerate(points):
				if self.matrix[i][j] == 0.0:
					dist = self.distance(a,b,edge)
					self.matrix[i][j] = dist
					self.matrix[j][i] = dist

	def distance(self, a, b, type):

		if a == b:
			return 0

		xd = a[0] - b[0]
		yd = a[1] - b[1]

		dij = -1

		if type == "EUC_2D":
			"""
				xd= x[i]-x[j];
				yd= y[i]-y[j];
				dij= nint( sqrt( xd*xd + yd*yd));
			"""
			dij = nint(math.sqrt(pow(xd,2)+(pow(yd,2))))
		else:
			if type == "ATT":
				"""
					xd= x[i]-x[j];
					yd= y[i]-y[j];
					rij= sqrt( (xd*xd + yd*yd)/10.0 );
					tij= nint( rij );

					if(tij<rij)
						dij= tij+1;
					else
						dij= tij;
				"""
				rij = math.sqrt((pow(xd,2)+(pow(yd,2))) / 10.0)
				tij = nint(rij)

				if (tij < rij):
					dij = tij + 1
				else:
					dij = tij

		return dij