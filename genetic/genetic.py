#! /usr/bin/env python3

import random, json, struct, geopy.distance, math
from operator import itemgetter
import numpy
from numpy import array_split

# Currently not used
# N_GENERATION =
N_POPULATION = 200
# Crossover rate in percents
CROSSOVER_RATE = 80
# Mutation rate rate in percents
MUTATION_RATE = 0,5

data = json.load(open('cities.json', 'r'))

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def rand_population():
    """
    Generate a list of solutions
    Return format: rand_population[row][column]
    """
    initial_population = []
    for line in range(N_POPULATION):
        rand = random.sample(range(15), 15)
        initial_population.append(rand)
    return initial_population

rand_population = rand_population()

def cities_distance(city1, city2):
    """
    Get distance between two cities, take the row number as arguments
    Usage: cities_distance(0,4)
    """
    coords_1 = ( float( data[city1]['lan'] ), float( data[city1]['lng'] ) )
    coords_2 = ( float( data[city2]['lan'] ), float( data[city2]['lng'] ) )
    return geopy.distance.geodesic(coords_1, coords_2).km

def get_chromosome(row):
    """Return only one individual from rand_population"""
    individual = []
    for cities in range( len( rand_population[row] ) ):
        individual.append(rand_population[row][cities])
    return individual

def individual_fitness(individual):
    """Evaluate the fitness of one individual"""
    pass_value = []
    # Add starting point at the end of the pass
    individual.append(individual[0])
    for i in range( len( individual ) -1):
        pass_value.append( cities_distance( individual[i], individual[i+1] ) )
    # Add fitness to the end of the list
    individual.append(sum(pass_value))
    return individual

def population_fitness(population):
    """Evaluate the fitness of a complete population"""
    population_with_fitness = []
    for members in range(len(population)):
        population_with_fitness.append(individual_fitness(get_chromosome(members)))
    return population_with_fitness

population = population_fitness(rand_population)

# Sort population by fitness, best on top, twss
sorted_list = sorted(population, key=itemgetter(16))

def clean_list(a_list_of_lists):
    """
    Remove the last two elements of the individual
    (as return point and the total distance are not used for crossover)
    Ex: [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2, 10, 6955.305315636573]
    is transformed into:
    [10, 1, 11, 4, 5, 13, 12, 0, 9, 3, 8, 7, 6, 14, 2]
    """
    for individuals in a_list_of_lists:
        del individuals[-2:]
    return a_list_of_lists

clean_list(sorted_list)

def cut_by_four(a_list):
    """Return list cutted in four"""
    return numpy.array_split(a_list, 4)

cutted_list = cut_by_four(sorted_list) # Here we got a list of lists of lists

def random_pick(percents, a_list):
    """Randomly pick x percent of elements from a list/dict, and return the modified list"""
    # Number of elements to pick
    nb_elements = int( len(a_list) * percents)
    # Randomize list
    random.shuffle(a_list)
    return a_list[:nb_elements]

def darwin_curse(population):
    """Remove unwanted individuals"""
    very_good_fit = random_pick(0.5, population[0])
    good_fit = random_pick(0.3, population[1])
    bad_fit = random_pick(0.15, population[2])
    very_bad_fit = random_pick(0.05, population[3])
    return len(very_good_fit), len(good_fit), len(bad_fit), len(very_bad_fit)

darwin_curse(cutted_list)

def new_generation(parents):
    pass
