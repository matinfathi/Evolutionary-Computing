# Integer Representation
import random
from typing import List, Tuple

def crossover(a: List[int], b: List[int], kind: str, **kwargs) -> Tuple[List[int], List[int]]:
    if kind == 'n-point':
        n_point = kwargs.get('n_point', 2)
        points = sorted(random.sample(range(1, len(a)), n_point))
        new_a, new_b = a[:], b[:]

        for i in range(len(points)):
            start = points[i]
            end = points[i + 1] if i + 1 < len(points) else len(a)
            if i % 2 != 0:
                new_a[start:end], new_b[start:end] = new_b[start:end], new_a[start:end]

        return new_a, new_b
    else:
        return a, b


def mutation(a: List[int], kind: str, **kwargs) -> List[int]:
    mutated_vector = a[:]

    if kind == 'creep':
        for i in range(len(mutated_vector)):
            if random.random() < kwargs.get('p_creep', 0.1):
                if mutated_vector[i] == max(mutated_vector):
                    mutated_vector[i] += -1
                elif mutated_vector[i] == min(mutated_vector):
                    mutated_vector[i] += 1
                else:
                    mutated_vector[i] += random.choice([-1, 1])

        return mutated_vector

    elif kind == 'reset':
        for i in range(len(mutated_vector)):
            if random.random() < kwargs.get('p_reset', 0.1):
                mutated_vector[i] = random.choice(range(min(a), max(a)))

        return mutated_vector

    else:
        return a

# Example usage
v1 = [1, 2, 3, 4, 5, 6, 7, 8]
v2 = [7, 3, 6, 8, 2, 1, 0, 4]
n_point=3

print("Parents:\nParent 1: {}\nParent 2: {}".format(v1, v2))

c1, c2 = crossover(v1, v2, kind='n-point', n_point=n_point)
print("\n{}-point Crossover:\nChild 1: {}\nChild 2: {}".format(n_point, c1, c2))

creep_mutated = mutation(v1, kind='creep', p_creep=0.2)
print("\nAfter creep mutation:", creep_mutated)

# Perform reset mutation
reset_mutated = mutation(v1, kind='reset', p_reset=0.2)
print("\nAfter reset mutation:", reset_mutated)



"""
Parents:
Parent 1: [1, 2, 3, 4, 5, 6, 7, 8]
Parent 2: [7, 3, 6, 8, 2, 1, 0, 4]

3-point Crossover:
Child 1: [1, 2, 3, 8, 2, 1, 0, 8]
Child 2: [7, 3, 6, 4, 5, 6, 7, 4]

After creep mutation: [2, 2, 3, 5, 6, 6, 7, 8]

After reset mutation: [1, 2, 3, 4, 5, 1, 7, 8]
"""