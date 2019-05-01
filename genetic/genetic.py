#! /usr/bin/env python3

import random, json
from math import sqrt as sqrt

# Crossover rate in percents
CROSSOVER_RATE = 80

# Mutation rate rate in percents
MUTATION_RATE = 0,5

data = json.load(open('cities.json', 'r'))

class City(object):
    def __init__(self):
        self.name = name
        self.lan = lan
        self.lng = lng

def rand_population():
    """Generate a list of solutions"""
    initial_population = []
    for line in range(200):
        rand = random.sample(range(10), 10)
        initial_population.append(rand)
    return initial_population

def square_root_distance(object1, object2):
    """Calculate the square root distance between two objects"""
    x = object1.x - object2.x
    y = object1.y - object2.y
    distance = sqrt(x*x + y*y)

def individual_fitness(solution):
    """Evaluate the fitness of one individual"""
