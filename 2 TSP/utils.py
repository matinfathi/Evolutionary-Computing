# TSP
import numpy as np
import random
import matplotlib.pyplot as plt
from typing import List, Tuple

with open("", "r") as f:
    data = f.readlines()

for idx, line in enumerate(data):
    if idx == 0:
        lentgh = int(line.strip())
        distance_matrix = np.empty((lentgh, lentgh))
    elif idx == 1:
        penalty = int(line.strip())
    else:
        if line.strip():
            distance_matrix[idx-2, :] = [int(item) for item in line.strip().split("\t")]
            
            
def calculate_distance(route: List[int]) -> List[int]:
    return sum(distance_matrix[route[i-1]][route[i]] for i in range(1, len(route)))

def inversion_mutation(route: List[int]) -> List[int]:
    i, j = sorted(random.sample(range(len(route)), 2))
    return route[:i] + route[i:j+1][::-1] + route[j+1:]

def scramble_mutation(route: List[int]) -> List[int]:
    i, j = sorted(random.sample(range(len(route)), 2))
    middle = route[i:j+1]
    random.shuffle(middle)
    return route[:i] + middle + route[j+1:]

def partially_mapped_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    size = len(parent1)
    # Randomly select crossover points
    point1, point2 = sorted(random.sample(range(size), 2))

    def pmx(parent1, parent2):
        child = [None]*size
        # Copy the segment from parent1 to child
        child[point1:point2+1] = parent1[point1:point2+1]

        # Map the remaining elements from parent2 to child
        for i in range(point1, point2+1):
            if parent2[i] not in child:
                x = parent2[i]
                j = i
                while child[j] is not None:
                    j = parent2.index(parent1[j])
                child[j] = x

        # Fill in the remaining positions with parent2's elements
        for i in range(size):
            if child[i] is None:
                child[i] = parent2[i]
        return child

    # Generate two children
    child1 = pmx(parent1, parent2)
    child2 = pmx(parent2, parent1)

    return child1, child2

def edge_crossover(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    size = len(parent1)
    # Build the edge map
    edge_map = {i: set() for i in range(size)}
    for p in [parent1, parent2]:
        for i in range(size):
            left = p[i - 1]
            right = p[(i + 1) % size]
            edge_map[p[i]].update([left, right])

    def construct_offspring(edge_map):
        # Start with a random element
        current = random.choice(list(edge_map.keys()))
        offspring = [current]
        while len(offspring) < size:
            # Remove the current node from edge_map and remove edges to the current node
            for edges in edge_map.values():
                edges.discard(current)
            current_edges = edge_map.pop(current)
            if current_edges:
                # Pick the next node with the fewest edges, break ties randomly
                current = min(current_edges, key=lambda x: (len(edge_map.get(x, [])), random.random()))
            else:
                # Pick randomly if there are no edges left
                current = random.choice(list(edge_map.keys()))
            offspring.append(current)
        return offspring

    # Construct two offspring using the edge map
    child1 = construct_offspring(edge_map.copy())
    child2 = construct_offspring(edge_map.copy())

    return child1, child2

def tournament_selection(population: List[List[int]], fitness_scores: List[float], tournament_size: int = 3) -> List[int]:
    # Randomly select tournament_size individuals for the tournament
    tournament_individuals = random.sample(list(enumerate(fitness_scores)), tournament_size)

    # Select the individual with the best fitness score
    winner_idx = min(tournament_individuals, key=lambda x: x[1])[0]

    return population[winner_idx]


# Example usage
population_size = 200
fitness_evaluations = 2000
