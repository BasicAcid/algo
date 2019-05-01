#! /usr/bin/env python3

import random, json, struct, geopy.distance
from math import sin, cos, sqrt, atan2, radians

# Crossover rate in percents
CROSSOVER_RATE = 80

# Mutation rate rate in percents
MUTATION_RATE = 0,5

data = json.load(open('cities.json', 'r'))

for each in data:
    print(each)

class City(object):
    def __init__(self):
        self.name = name
        self.lan = lan
        self.lng = lng

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def rand_population():
    """Generate a list of solutions"""
    initial_population = []
    for line in range(200):
        rand = random.sample(range(10), 10)
        initial_population.append(rand)
    return initial_population

def cities_distance(city1, city2):
    coords_1 = (52.2296756, 21.0122287)
    coords_2 = (52.406374, 16.9251681)
    return geopy.distance.geodesic(coords_1, coords_2).km

def individual_fitness(solution):
    """Evaluate the fitness of one individual"""
    pass
