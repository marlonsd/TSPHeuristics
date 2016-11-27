import argparse, math, sys, glob

from time import time
from graph import Graph

import numpy as np

from local_search import hill_climbing_best_fitting, hill_climbing_first_fitting

from metaheuristics import grasp, iterated_local_search

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

	print "name,size,hcbf cost,hcbf time,hcff cost, hcff time, grasp cost, grasp time, grasp iteration, ils cost, ils time, ils iteration"

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

		t0 = time()
		cost_hcbf, temp = hill_climbing_best_fitting(graph)
		hcbf_time = time()-t0

		t0 = time()
		cost_hcff, temp = hill_climbing_first_fitting(graph)
		hcff_time = time()-t0

		t0 = time()
		cost_grasp, temp, it_grasp = iterated_local_search(graph)
		grasp_time = time()-t0

		t0 = time()
		cost_ils, temp, it_ils = iterated_local_search(graph)
		ils_time = time()-t0

		print problem_name + "," + str(graph.size()) + "," + str(cost_hcbf) + "," + str(hcbf_time) + "," + str(cost_hcff) + "," + str(hcff_time),
		print "," + str(cost_grasp) + "," + str(grasp_time) + "," + str(it_grasp),
		print "," + str(cost_ils) + "," + str(ils_time) + "," + str(it_ils),

		f.close()