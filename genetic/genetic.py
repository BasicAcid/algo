#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Genetic approach to TSP
"""

import random
import json
import copy
import argparse
import sys
from operator import itemgetter
import geopy.distance
import numpy
from pmx import pmx

sys.setrecursionlimit(1500)

parser = argparse.ArgumentParser(description='TSP GA')
parser.add_argument('-i', help='number of individuals in one generation',
                    action='store', dest='n_individuals', default=200,
                    type=int, required=True)
parser.add_argument('-g', help='number of generations', action='store',
                    dest='n_generations', default=0, type=int, required=True)
args = parser.parse_args()

N_GENERATION = args.n_generations
N_POPULATION = args.n_individuals
# CROSSOVER_RATE = 0.8
# MUTATION_RATE = 0,5

data = json.load(open('cities.json', 'r'))


def rand_population(nb_individuals):
    """
    Generate a list of solutions
    Return format: rand_population[row][column]
    """
    initial_population = []
    for _line in range(nb_individuals):
        rand = random.sample(range(15), 15)
        initial_population.append(rand)
    return list(initial_population)


def cities_distance(city1, city2):
    """
    Get distance between two cities, take the row number as arguments
    Usage: cities_distance(0,4)
    """
    coords_1 = (float(data[city1]['lan']), float(data[city1]['lng']))
    coords_2 = (float(data[city2]['lan']), float(data[city2]['lng']))
    return geopy.distance.geodesic(coords_1, coords_2).km


def get_chromosome(a_list, row):
    """Return only one individual from rand_population"""
    individual = []
    for cities in range(len(a_list[row])):
        individual.append(a_list[row][cities])
    return individual


def individual_fitness(individual):
    """Evaluate the fitness of one individual"""
    pass_value = []
    individual.append(individual[0])  # Add starting point at the end of pass
    for i in range(len(individual)-1):
        pass_value.append(cities_distance(individual[i], individual[i+1]))
    individual.append(sum(pass_value))  # Add fitness to the end of the list
    return individual


def population_fitness(population):
    """Evaluate the fitness of a complete population"""
    list_with_fitness = []
    for members in range(len(population)):
        list_with_fitness.append(
            individual_fitness(get_chromosome(population, members)))
    return list_with_fitness


def sort_a_list(a_list):
    """Sort population by fitness, best on top, twss"""
    sorted_list = sorted(a_list, key=itemgetter(16))
    return sorted_list


def clean_list(a_list_of_lists):
    """
    Remove the last two elements of the individual
    (as return point and the total distance are not used for crossover)
    Ex: [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2, 10, 6955.30]
    is transformed into:
    [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2]
    """
    # Complete replicate to left the older list intact
    new_cleaned_list = copy.deepcopy(a_list_of_lists)
    for individuals in new_cleaned_list:
        del individuals[-2:]
    return new_cleaned_list


def random_pick(percents, a_list):
    """
    Randomly pick x percent of elements from a list/dict,
    and return the modified list
    """
    nb_elements = int(len(a_list)*percents)  # Number of elements to pick
    random.shuffle(a_list)  # Randomize list
    return a_list[:nb_elements]


def select_individuals(population):
    """Randomly select individuals"""
    very_good_fit = random_pick(0.5, population[0]).tolist()
    good_fit = random_pick(0.3, population[1]).tolist()
    bad_fit = random_pick(0.15, population[2]).tolist()
    very_bad_fit = random_pick(0.05, population[3]).tolist()
    return very_good_fit + good_fit + bad_fit + very_bad_fit


def crossover(selected_population):
    """Partially Matched Crossover"""
    childs_list = []
    for individual in range(len(selected_population)-1):
        childs_list.append(pmx(selected_population[individual],
                               selected_population[individual+1]))
    return childs_list


def new_population(selected_individuals):
    """
    Generate a list composed of random individuals
    and of the childs from crossover
    """
    childs = crossover(selected_individuals)
    # Childs is a list of tuples, here we convert it in a list of lists
    childs = list(map(lambda x: x[0], childs))
    nb_to_generate = N_POPULATION - len(selected_individuals + childs)
    nb_to_generate = int(nb_to_generate)
    random_individuals = rand_population(nb_to_generate)
    new_pop = selected_individuals + childs + random_individuals
    return new_pop


def generate(input_population):
    """Generate a new population from the one inputed"""
    population_with_fitness = population_fitness(input_population)
    sorted_list = sort_a_list(population_with_fitness)

    cleaned_list = clean_list(sorted_list)
    cutted_list = numpy.array_split(cleaned_list, 4)

    selection = select_individuals(cutted_list)
    random.shuffle(selection)  # Tu use or not to use ? Enough entropy ?

    new_generation = new_population(selection)
    return new_generation


def evolve(input_population, _n):
    """Evolve n times a given population"""
    print(_n)
    _n = _n - 1
    pop = generate(input_population)
    if _n > 0:
        pop = evolve(pop, _n)
    return pop


# Init a population
random_population_list = rand_population(N_POPULATION)

print(sort_a_list(population_fitness(evolve(random_population_list,
                                            N_GENERATION)))[0])


def assign_cities(a_list):
    """Assign cities to a list of integers"""
    route = []
    for cities in a_list:
        route.append(data[cities]['city'])
    return route
