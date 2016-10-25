import math, sys
import numpy as np

from collections import defaultdict

# https://github.com/feynmanliang/Euler-Tour/blob/master/FindEulerTour.py
def find_euler_tour(graph):
	tour = []
	E = graph

	numEdges = defaultdict(int)

	def find_tour(u):
		for e in E:
			if u == e[0]:
				u,v = e
				E.remove(e)
				find_tour(v)
			elif u == e[1]:
				v,u = e
				E.remove(e)
				find_tour(v)
		tour.insert(0,u)

	for i,j in graph:
		numEdges[i] += 1
		numEdges[j] += 1

	start = graph[0][0]
	for i,j in numEdges.iteritems():
		if j % 2 > 0:
			start = i
			break

	current = start
	find_tour(current)

	if tour[0] != tour[-1]:
		return None
	return tour

# https://web.tuke.sk/fei-cit/butka/hop/htsp.pdf
def christofides(graph):
	mst = graph.mst()

	vertice_list = []

	# Duplicating edges
	for i in range(len(mst)):
		for j in range(len(mst)):
			if (mst[i][j] > 0):
				vertice_list += [(i,j)]
				vertice_list += [(i,j)]

	tour = find_euler_tour(vertice_list)

	cost = 0.
	for i in range(len(tour)-1):
		cost += graph.get_distance(tour[i], tour[i+1])

	return cost, tour