import math, sys, random
import numpy as np

from collections import defaultdict
from copy import copy

from constructive_heuristics import nearest_neighbour_algorithm

def hill_climbing_best_fitting(graph, initial_solution = None):

	def init_random_tour(tour_length):
		tour = range(tour_length)
		random.shuffle(tour)
		tour.append(tour[0])
		return tour

	def cost_calculation(graph, tour):
		cost = 0.
		for i in range(len(tour)-1):
			cost += graph.get_distance(tour[i], tour[i+1])

		return cost

	def get_neighborhood(tour):
		neighborhood = []

		for j in range(1,len(tour)-1):
			for i in range(j+1,len(tour)-1):
				possible_solution = copy(tour)
				possible_solution[j], possible_solution[i] = tour[i], tour[j]
				neighborhood.append(possible_solution)

		return neighborhood


	if initial_solution is None:
		e_cost, initial_solution = nearest_neighbour_algorithm(graph)

	tour = initial_solution
	min_cost = cost_calculation(graph, tour)

	condition = True

	while(condition):
		condition = False
		temp_solution = copy(tour)


		for j in range(1,len(tour)-1):
			for i in range(j+1,len(tour)-1):
				possible_solution = copy(tour)
				possible_solution[j], possible_solution[i] = tour[i], tour[j]

				local_cost = cost_calculation(graph, possible_solution)

				if local_cost < min_cost:
					condition = True
					min_cost = local_cost
					temp_solution = possible_solution

		tour = temp_solution
			

	return min_cost, tour


def hill_climbing_first_fitting(graph, initial_solution = None):

	def init_random_tour(tour_length):
		tour = range(tour_length)
		random.shuffle(tour)
		tour.append(tour[0])
		return tour

	def cost_calculation(graph, tour):
		cost = 0.
		for i in range(len(tour)-1):
			cost += graph.get_distance(tour[i], tour[i+1])

		return cost

	def get_neighborhood(tour):
		neighborhood = []

		for j in range(1,len(tour)-1):
			for i in range(j+1,len(tour)-1):
				possible_solution = copy(tour)
				possible_solution[j], possible_solution[i] = tour[i], tour[j]
				neighborhood.append(possible_solution)

		return neighborhood


	if initial_solution is None:
		e_cost, initial_solution = nearest_neighbour_algorithm(graph)

	tour = initial_solution
	min_cost = cost_calculation(graph, tour)

	condition = True

	while(condition):
		condition = False
		temp_solution = copy(tour)


		for j in range(1,len(tour)-1):
			for i in range(j+1,len(tour)-1):
				possible_solution = copy(tour)
				possible_solution[j], possible_solution[i] = tour[i], tour[j]

				local_cost = cost_calculation(graph, possible_solution)

				if local_cost < min_cost:
					condition = True
					min_cost = local_cost
					temp_solution = possible_solution
					break
			if condition:
				break

		tour = temp_solution
			

	return min_cost, tour


