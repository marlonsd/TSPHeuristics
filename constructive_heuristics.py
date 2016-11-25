import math, sys
import numpy as np

from collections import defaultdict

def nearest_neighbour_algorithm(graph):
	if graph.size == 0:
		return -1, []

	points = range(graph.size())

	current = points[0]
	tour = [current]

	points.remove(current)

	while len(points) > 0:
		next = points[0]
		for point in points:
			if graph.get_distance(current, point) < graph.get_distance(current, next):
				next = point      
		tour.append(next)
		points.remove(next)
		current = next

	tour.append(tour[0])

	cost = 0
	for i in range(len(tour)-1):
		cost += graph.get_distance(tour[i], tour[i+1])

	# cost += graph.get_distance(tour[i+1], tour[0])

	return cost, tour


def nearthest_insertion_algorithm(graph):
	if graph.size == 0:
		return -1, []

	points = range(graph.size())

	current = points[0]

	points.remove(current)

	i = current
	j = points[0]
	cij = graph.get_distance(i,j)
	for point in points:
		if graph.get_distance(i, point) < cij:
			cij = graph.get_distance(i, point)
			j = point

	points.remove(j)
	
	edges = [(i,j)]

	visited = []
	visited.append(i)
	visited.append(j)

	while len(points) > 0:
		i = visited[0]
		k = points[0]
		crj = graph.get_distance(k,i)

		for point in points:
			for c in visited:
				dist = graph.get_distance(point,c)
				if dist < crj:
					k = point

		i = edges[0][0]
		j = edges[0][1]
		c_min = graph.get_distance(i,k) + graph.get_distance(k,j) - graph.get_distance(i,j)

		for e in edges:
			aux_i = e[0]
			aux_j = e[1]
			dist = graph.get_distance(aux_i,k) + graph.get_distance(k,aux_j) - graph.get_distance(aux_i,aux_j)
			if dist < c_min:
				c_min = dist
				i = aux_i
				j = aux_j

		edges.remove((i,j))
		edges.append((i,k))
		edges.append((k,j))

		visited.append(k)
		points.remove(k)


	cost = 0
	for e in edges:
		i = e[0]
		j = e[1]
		cost += graph.get_distance(i, j)

	return cost, edges

def greedy(graph, initial_point = 0):
	if graph.size == 0:
		return -1, []

	tour = [initial_point]
	cost = 0.
	local_point = initial_point

	possible_cities = range(graph.size())

	possible_cities.remove(local_point)

	while(len(possible_cities) > 0):
		smallest = graph.get_distance(local_point,possible_cities[0])
		city = possible_cities[0]

		for i in possible_cities:
			value = graph.get_distance(local_point,i)

			if value < smallest:
				smallest = value
				city = i

		if not (city is None):
			tour.append(city)
			local_point = city
			cost += smallest
			possible_cities.remove(local_point)
		else:
			print "Something is not quite right!"
			print "An illusion?! What are you hiding?"
			sys.exit()

	cost += graph.get_distance(tour[-1],tour[0])
	tour.append(initial_point)

	return cost, tour