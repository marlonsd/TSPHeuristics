import argparse, math, sys, glob

from time import time
from graph import Graph

import numpy as np

from constructive_heuristics import nearest_neighbour_algorithm, nearthest_insertion_algorithm
from lower_bound import one_tree, held_karp_bound, minimum_spanning_tree

if (__name__ == '__main__'):

	### Arguments Treatment ###
	parser = argparse.ArgumentParser()

	parser.add_argument("-p","--folder_path", type=str, default='instances',
						help="Folder where TSP instances are located (Default: instances).")

	parser.add_argument("-f","--file_format", type=str, default='txt',
						help="Format of file where TSP instances are stored (Default: txt).")

	# Parsing args
	args = parser.parse_args()

	path = args.folder_path
	file_format = args.file_format

	files = sorted(glob.glob(path+"/*."+file_format))

	for file in files:
		f = open(file, 'r')

		data = f.read().splitlines()

		problem_name = file.split(".")[0]
		size = int(data[0].split(" ")[-1])
		edge_type = data[4].split(" ")[-1]

		data = data[2:]

		points = []

		for i in range(size):
			point = " ".join(data[i].strip().split()) # Remove duplicate spaces in between line
			point = point.split() # Separete line by space

			points.append([float(point[-2]), float(point[-1])])

		graph = Graph(points=points, size=size, edge=edge_type)

		t0 = time()
		cost_nn, temp = nearest_neighbour_algorithm(graph)
		nn_time = time()-t0

		t0 = time()
		cost_i, temp = nearthest_insertion_algorithm(graph)
		it_time = time()-t0
		# cost, temp = compute(graph.triangular_sup_matrix())

		lb, _, _ = one_tree(graph)
		lb2 = held_karp_bound(graph)

		print problem_name + "," + str(graph.size()) + "," + str(cost_nn) + "," + str(nn_time) + "," + str(cost_i) + "," + str(it_time),
		print str(lb)+","+str(lb2)
		# print problem_name + "," + str(graph.size()) + "," + str(temp['Travel_Cost']) + "," + str(len(np.unique(temp)))

		f.close()