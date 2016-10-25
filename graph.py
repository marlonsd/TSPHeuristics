import math, sys
import numpy as np

from mpmath import nint
from scipy.sparse.csgraph import minimum_spanning_tree

class Graph:

	def __init__(self, points, size = 0, edge = 'EUC_2D'):
		self.__matrix = np.zeros((size, size))
		self.__size = len(points)

		for i,a in enumerate(points):
			for j,b in enumerate(points):
				if self.__matrix[i][j] == 0.0:
					dist = self.__distance(a,b,edge)
					if dist is None:
						self.__size = 0
						break
					self.__matrix[i][j] = dist
					self.__matrix[j][i] = dist

	def __distance(self, a, b, type):

		if a == b:
			return 0

		xd = a[0] - b[0]
		yd = a[1] - b[1]

		dij = None

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

	def size(self):
		return self.__size

	def get_distance(self, i, j):
		if i > self.__size or j > self.__size:
			return None

		return self.__matrix[i][j]

	def mst(self):
		temp_matrix = self.__matrix.copy()

		for i in range(self.__size):
			for j in range(self.__size):
				if i >= j:
					temp_matrix[i][j] = 0

		mst = minimum_spanning_tree(temp_matrix)

		mst = mst.toarray().astype(int)

		return mst
