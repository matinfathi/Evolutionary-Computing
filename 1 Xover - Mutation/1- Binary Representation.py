# Binary Representation
import random
from typing import List, Tuple, Dict


def crossover(a:List[int], b:List[int], kind:str='one_point', **kwargs:Dict[str, str]) -> Tuple[List[int], List[int]]:

    if kind == 'one_point':
        pt = random.randint(1, len(a)-2)
        c = a[:pt] + b[pt:]
        d = b[:pt] + a[pt:]
        return c, d, pt

    elif kind == 'uniform':
        c, d = [], []
        for i in range(len(a)):
            if random.random() < 0.5:
                c.append(a[i])
                d.append(b[i])
            else:
                c.append(b[i])
                d.append(a[i])
        return c, d

def mutation(a:List[int], **kwargs:Dict[str, str]) -> List[int]:
    for i in range(len(a)):
        if random.random() < kwargs.get('mutation_rate', 0.2):
            a[i] = 1 - a[i]
    return a


v1 = [1, 1, 1, 1, 1, 1, 1, 1]
v2 = [0, 0, 0, 0, 0, 0, 0, 0]

print("Parents:\nParent 1: {}\nParent 2: {}".format(v1, v2))

c1, c2, pt = crossover(v1, v2, 'one_point')
print("\nOne-point Crossover:\nChild 1: {} {}\nChild 2: {} {}".format(c1[:pt], c1[pt:], c2[:pt], c2[pt:]))

c1, c2 = crossover(v1, v2, 'uniform')
print("\nUniform Crossover:\nChild 1: {}\nChild 2: {}".format(c1, c2))

m1 = mutation(v1)
print("\nMutation:\nMutated Child: {}".format(m1))


"""
Parents:
Parent 1: [1, 1, 1, 1, 1, 1, 1, 1]
Parent 2: [0, 0, 0, 0, 0, 0, 0, 0]

One-point Crossover:
Child 1: [1, 1, 1, 1] [0, 0, 0, 0]
Child 2: [0, 0, 0, 0] [1, 1, 1, 1]

Uniform Crossover:
Child 1: [0, 1, 1, 1, 1, 1, 1, 0]
Child 2: [1, 0, 0, 0, 0, 0, 0, 1]

Mutation:
Mutated Child: [1, 1, 1, 1, 1, 1, 1, 0]
"""