import argparse, math, sys, glob

from time import time
from graph import Graph

from constructive_heuristics import christofides


if (__name__ == '__main__'):

	### Arguments Treatment ###
	parser = argparse.ArgumentParser()

	parser.add_argument("-p","--folder_path", type=str, default='EUC_2D',
						help="Folder where TSP instances are located (Default: EUC_2D).")

	parser.add_argument("-f","--file_format", type=str, default='tsp',
						help="Format of file where TSP instances are stored (Default: tsp).")

	# Parsing args
	args = parser.parse_args()

	path = args.folder_path
	file_format = args.file_format

	files = sorted(glob.glob(path+"/*."+file_format))

	for file in files:
		f = open(file, 'r')

		data = f.read().splitlines()

		problem_name = data[0].split(" ")[-1]
		size = int(data[3].split(" ")[-1])
		edge_type = data[4].split(" ")[-1]

		data = data[6:]

		points = []

		for i in range(size):
			point = " ".join(data[i].strip().split()) # Remove duplicate spaces in between line
			point = point.split() # Separete line by space

			points.append([float(point[-2]), float(point[-1])])

		graph = Graph(points=points, size=size, edge=edge_type)

		cost, _ = christofides(graph)

		print problem_name+','+str(cost)

		f.close()