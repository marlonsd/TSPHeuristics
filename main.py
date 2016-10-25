import argparse, math, sys

from time import time

import glob


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

	files = glob.glob(path+"/*."+file_format)

	for file in files:
		print file		
		f = open(file, 'r')

		data = f.read().splitlines()

		problem_name = data[0].split(" ")[-1]
		size = int(data[3].split(" ")[-1])
		edge_type = data[4].split(" ")[-1]

		data = data[6:]

		points = []

		for i in range(size):
			point = " ".join(data[i].strip().split()).split()
			points.append([float(point[-2]), float(point[-1])])


		f.close()