#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random, json, struct, geopy.distance, math, copy
from operator import itemgetter
import numpy
from numpy import array_split
from pmx import pmx

N_GENERATION = 1
N_POPULATION = 200
CROSSOVER_RATE = 0.8
# Mutation rate rate in percents
MUTATION_RATE = 0,5

data = json.load(open('cities.json', 'r'))

def rand_population(nb_individuals):
    """
    Generate a list of solutions
    Return format: rand_population[row][column]
    """
    initial_population = []
    for line in range(nb_individuals):
        rand = random.sample(range(15), 15)
        initial_population.append(rand)
    return list(initial_population)

def cities_distance(city1, city2):
    """
    Get distance between two cities, take the row number as arguments
    Usage: cities_distance(0,4)
    """
    coords_1 = ( float( data[city1]['lan'] ), float( data[city1]['lng'] ) )
    coords_2 = ( float( data[city2]['lan'] ), float( data[city2]['lng'] ) )
    return geopy.distance.geodesic(coords_1, coords_2).km

def get_chromosome(a_list, row):
    """Return only one individual from rand_population"""
    individual = []
    for cities in range( len( a_list[row] ) ):
        individual.append(a_list[row][cities])
    return individual

def individual_fitness(individual):
    """Evaluate the fitness of one individual"""
    pass_value = []
    individual.append(individual[0]) # Add starting point at the end of the pass
    for i in range( len( individual ) -1):
        pass_value.append( cities_distance( individual[i], individual[i+1] ) )
    individual.append(sum(pass_value)) # Add fitness to the end of the list
    return individual

def population_fitness(population):
    """Evaluate the fitness of a complete population"""
    list_with_fitness = []
    for members in range(len(population)):
        list_with_fitness.append(individual_fitness(get_chromosome(population, members)))
    return list_with_fitness

def sort_a_list(a_list):
    """Sort population by fitness, best on top, twss"""
    sorted_list = sorted(a_list, key=itemgetter(16))
    return sorted_list

def clean_list(a_list_of_lists):
    """
    Remove the last two elements of the individual
    (as return point and the total distance are not used for crossover)
    Ex: [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2, 10, 6955.305315636573]
    is transformed into:
    [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2]
    """
    new_cleaned_list = copy.deepcopy(a_list_of_lists) # Complete replicate to left the older list intact
    for individuals in new_cleaned_list:
        del individuals[-2:]
    return new_cleaned_list

def cut_by_four(a_list):
    """Return list cutted in four"""
    return numpy.array_split(a_list, 4)

def random_pick(percents, a_list):
    """Randomly pick x percent of elements from a list/dict, and return the modified list"""
    nb_elements = int( len(a_list) * percents) # Number of elements to pick
    random.shuffle(a_list) # Randomize list
    return a_list[:nb_elements]

def select_individuals(population):
    """Randomly select individuals"""
    very_good_fit = random_pick(0.5, population[0]).tolist()
    good_fit = random_pick(0.3, population[1]).tolist()
    bad_fit = random_pick(0.15, population[2]).tolist()
    very_bad_fit = random_pick(0.05, population[3]).tolist()
    return very_good_fit + good_fit + bad_fit + very_bad_fit

def crossover(selected_population):
    childs_list = []
    for individual in range( len( selected_population ) -1):
        childs_list.append( pmx( selected_population[individual], selected_population[individual+1] ) )
    return childs_list

def new_population(selected_individuals):
    """Generate a list composed of random individuals and of the childs from crossover"""
    childs = crossover(selected_individuals)
    childs = list(map(lambda x: x[0], childs)) # Childs is a list of tuples, here we convert it in a list of lists
    nb_to_generate =  N_POPULATION - len(selected_individuals + childs)
    nb_to_generate = int(nb_to_generate)
    random_individuals = rand_population(nb_to_generate)
    new_pop = selected_individuals + childs + random_individuals
    return new_pop

def generate(nb_of_generations):
    random_population_list = rand_population(N_POPULATION)
    population_with_fitness = population_fitness(random_population_list)
    sorted_list = sort_a_list(population_with_fitness)

    cleaned_list = clean_list(sorted_list)
    cutted_list = cut_by_four(cleaned_list) # Here we got a list of lists of lists

    selection = select_individuals(cutted_list)
    random.shuffle(selection) # Tu use or not to use ? Enough entropy ?

    new_generation = new_population(selection)
    a = population_fitness(new_generation)
    b = sort_a_list(a)
    c = clean_list(b)
    d = cut_by_four(c)
    e = select_individuals(d)
    return e

print(generate(N_GENERATION))
