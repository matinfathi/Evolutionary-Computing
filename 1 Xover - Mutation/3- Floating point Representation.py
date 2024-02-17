# Floating point Representation
from typing import List, Tuple
import random
import numpy as np

def crossover(a: List[float], b: List[float], kind: str, **kwargs) -> Tuple[List[float], List[float]]:
    if kind == 'simple_arithmetic':
        pt = random.randint(1, len(a)-2)
        alpha = kwargs.get('alpha', 0.5)
        child1 = a[:pt] + [round(alpha * x + (1 - alpha) * y, 3) for x, y in zip(a[pt:], b[pt:])]
        child2 = b[:pt] + [round(alpha * y + (1 - alpha) * x, 3) for x, y in zip(a[pt:], b[pt:])]
        return (child1, child2)

    elif kind == 'whole_arithmetic':
        alpha = kwargs.get('alpha', 0.5)
        child1 = [round(alpha * x + (1 - alpha) * y, 3) for x, y in zip(a, b)]
        child2 = [round(alpha * y + (1 - alpha) * x, 3) for x, y in zip(a, b)]
        return (child1, child2)

    elif kind == 'blend':
        alpha = kwargs.get('alpha', 0.5)
        child1 = [round(random.uniform(min(x, y) - alpha * (max(x, y) - min(x, y)), max(x, y) + alpha * (max(x, y) - min(x, y))), 3) for x, y in zip(a, b)]
        child2 = [round(random.uniform(min(x, y) - alpha * (max(x, y) - min(x, y)), max(x, y) + alpha * (max(x, y) - min(x, y))), 3) for x, y in zip(a, b)]
        return (child1, child2)

    else:
        return a, b


def mutation(a: List[float], kind: str, **kwargs) -> List[float]:
    if kind == 'uncorrelated_one_sigma':
        sigma = kwargs.get('sigma', 0.1)
        vector = np.array(a)
        n = len(vector)
        tau = 1 / np.sqrt(n)
        epsilon = 1e-5

        sigma_prime = sigma * np.exp(tau * np.random.normal(0, 1))
        sigma_prime = max(sigma_prime, epsilon)

        mutated_vector = vector + sigma_prime * np.random.normal(0, 1, n)

        return mutated_vector.tolist()

    elif kind == 'uncorrelated_n_sigmas':
        sigmas = np.array(kwargs.get('sigmas', [0.01 for _ in a]))
        vector = np.array(a)
        n = len(vector)
        tau_prime = 1 / np.sqrt(2 * np.sqrt(n))
        tau = 1 / np.sqrt(2 * n)
        epsilon = 1e-5

        sigmas_prime = sigmas * np.exp(tau_prime * np.random.normal(0, 1) + tau * np.random.normal(0, 1, n))
        sigmas_prime = np.maximum(sigmas_prime, epsilon)

        mutated_vector = vector + sigmas_prime * np.random.normal(0, 1, n)

        return mutated_vector.tolist()

    else:
        return a

# Example vectors for floating-point representation
v1 = [0.1, 0.2, 0.3, 0.4, 0.5]
v2 = [0.5, 0.1, 0.2, 0.4, 0.3]

# Perform Simple Arithmetic Crossover
print("Simple Arithmetic Crossover:")
print(crossover(v1, v2, kind='simple_arithmetic'))

# Perform Whole Arithmetic Crossover
print("\nWhole Arithmetic Crossover:")
print(crossover(v1, v2, kind='whole_arithmetic'))

# Perform Blend Crossover
print("\nBlend Crossover:")
print(crossover(v1, v2, kind='blend', alpha=0.5))

# Uncorrelated mutation with 1 sigmas
print("\n\nAfter uncorrelated mutation with one sigma:")
print(mutation(v1, kind='uncorrelated_one_sigma', sigma=0.01))

# Uncorrelated mutation with n sigmas
print("\nAfter uncorrelated mutation with n sigmas:")
print(mutation(v1, kind='uncorrelated_n_sigmas'))


"""
Parent 1: [0.1, 0.2, 0.3, 0.4, 0.5]
Parent 2: [0.5, 0.1, 0.2, 0.4, 0.3]

Simple Arithmetic Crossover:
([0.1, 0.2, 0.3, 0.4, 0.4], [0.5, 0.1, 0.2, 0.4, 0.4])

Whole Arithmetic Crossover:
([0.3, 0.15, 0.25, 0.4, 0.4], [0.3, 0.15, 0.25, 0.4, 0.4])

Blend Crossover:
([0.321, 0.053, 0.178, 0.4, 0.532], [0.026, 0.086, 0.152, 0.4, 0.358])


After uncorrelated mutation with one sigma:
[0.11009958550183029, 0.19592268430431847, 0.2873691809275631, 0.4198605922296408, 0.4931679161751738]

After uncorrelated mutation with n sigmas:
[0.09548341833239948, 0.20048816219736196, 0.3019497485944225, 0.3992967418756751, 0.4947715604941096]
"""