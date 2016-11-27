import math, sys, random
import numpy as np

from collections import defaultdict
from copy import copy

from local_search import hill_climbing_best_fitting as hill_climbing
from local_search import two_opt, nearest_neighbour_algorithm

def random_greedy(graph, n = 5):

	def get_smallest(values, n = 5):
		smallest_values = np.argsort(values)[:n]

		np.random.shuffle(smallest_values)

		return smallest_values[0]

	def initial_city(graph, n):
		possible_values = []
		for i, line in enumerate(range(graph.size())):
			possible_cities = range(graph.size())
			possible_cities.remove(i)

			smallest = graph.get_distance(i,possible_cities[0])

			for j in possible_cities:
				value = graph.get_distance(i,j)

				if value < smallest:
					smallest = value

			possible_values.append(smallest)

		return get_smallest(possible_values, n)

	if graph.size() == 0:
		return -1, []

	initial_point = initial_city(graph, n)
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

def calc_cost(tour, graph):
	cost = 0.
	for i in range(len(tour)-1):
		cost += graph.get_distance(tour[i], tour[i+1])

	return cost

def grasp(graph, num_neighboors = 5, max_iteration = 100, alpha = 0.5):
	# current_best = [cost, tour]
	error = np.inf
	it = 0

	best = [np.inf, []]

	while (error > alpha and it < max_iteration):
		solution = random_greedy(graph, num_neighboors)
		new_solution = hill_climbing(graph, solution[1])

		if new_solution[0] < solution[0]:
			current_best = new_solution
		else:
			current_best = solution

		if current_best[0] < best[0]:
			best = current_best
			error = float(np.abs(error - best[0])/best[0])*100.

		it += 1

	return best, it

def perturb(tour, prob_perturbation = 0.5):
	if np.random.random() < prob_perturbation:
		return tour
	else:
		first_pos = np.random.randint(1, len(tour)-1)
		second_pos = np.random.randint(1, len(tour)-1)
		while (second_pos == first_pos):
			second_pos = np.random.randint(1, len(tour)-1)

		aux = tour[second_pos]
		tour[second_pos] = tour[first_pos]
		tour[first_pos] = aux

		return tour

def iterated_local_search(graph, max_iteration = 250, alpha = 0.5):
	cost, tour = nearest_neighbour_algorithm(graph)

	best_tour = tour
	best_cost = cost

	error = np.inf
	it = 0

	while (error > alpha and it < max_iteration):
		it += 1

		tour = perturb(tour)
		new_cost, new_tour = hill_climbing(graph, tour)


		if new_cost < best_cost:

			error = float(np.abs(best_cost-new_cost)/best_cost)*100.

			best_tour = new_tour
			best_cost = new_cost
		else:
			break

		tour = new_tour

	return best_cost, best_tour, it