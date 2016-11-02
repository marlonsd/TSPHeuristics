import math, sys, copy
import numpy as np

from collections import defaultdict

def minimum_spanning_tree(graph):
	mst = graph.mst()

	return np.sum(np.sum(mst))


def one_tree(graph):
	if graph.size() <= 0:
		return None

	short_graph = copy.deepcopy(graph)

	short_graph.remove_node(0)

	mst = short_graph.mst()

	cost = np.sum(np.sum(mst))

	min_cost = graph.get_distance(0,1)
	second_min = min_cost
	s = 1
	s_ = 1

	for j in range(1,graph.size()):
		dist = graph.get_distance(0,j)
		if dist < min_cost:
			second_min = min_cost
			min_cost = dist
			s_ = s
			s = j

	cost += min_cost + second_min

	return cost, mst, (s, s_)

def held_karp_bound(graph, epson = 0.05, iteration = 5000):
	if graph.size() <= 0:
		return None

	pi = [0 for i in range(graph.size())]
	step_size = 0.5

	g_line = copy.deepcopy(graph)

	condition = True
	it = 0

	hk = 0

	while condition:
		it += 1
		for i in range(graph.size()):
			for j in range(graph.size()):
				o = g_line.get_distance(i,j)
				g_line.set_distance(o + pi[i] + pi[j], i, j)

		cost, mst, pair = one_tree(g_line)

		w = cost - 2*np.sum(pi)

		if w > hk:
			hk = w

		degree = [0 for i in range(graph.size())]

		for i,line in enumerate(mst):
			for j,c in enumerate(line):
					if c > 0:
						degree[i+1] += 1
						degree[j+1] += 1

		degree[0] = 2
		degree[pair[0]] += 1
		degree[pair[1]] += 1

		variation = 0.
		for i in range(len(pi)):
			change = pi[i] + (step_size * (degree[i]-2))
			variation += np.abs(change - pi[i])
			pi[i] = change

		variation /= len(pi)

		condition = ((not (variation <= epson)) and it < iteration)

	# cost = 0.

	# min_cost = graph.get_distance(0,1)
	# second_min = min_cost

	# v = np.nonzero(mst)
	# for i in range(len(v[0])):
	# 	cost += graph.get_distance(v[0][i]+1, v[1][i]+1)

	# for i,line in enumerate(mst):
	# 	dist = graph.get_distance(0,i+1)
	# 	if dist < min_cost:
	# 		second_min = min_cost
	# 		min_cost = dist

	# return (cost + min_cost + second_min)
	return hk
