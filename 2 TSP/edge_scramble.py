from utils import *


def evolve_edge_scramble(population_size: int, fitness_evaluations: int):
    population = [random.sample(range(30), 30) for _ in range(population_size)]
    fitness = [calculate_distance(route) for route in population]

    best_fitness_progress = []
    worst_fitness_progress = []

    for _ in range(fitness_evaluations // population_size):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, fitness, tournament_size=10)
            parent2 = tournament_selection(population, fitness, tournament_size=10)
            child1, child2 = edge_crossover(parent1, parent2)

            child1 = scramble_mutation(child1)
            child2 = scramble_mutation(child2)

            new_population.extend([child1, child2])

        population = new_population
        fitness = [calculate_distance(route) for route in population]

        best_fitness_progress.append(min(fitness))
        worst_fitness_progress.append(max(fitness))

    best_route_index = fitness.index(min(fitness))

    # Plotting the progress
    plt.plot(best_fitness_progress, label='Best Fitness')
    plt.plot(worst_fitness_progress, label='Worst Fitness', color='r')
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.title('Evolutionary Algorithm Progress')
    plt.legend()
    plt.show()

    return population[best_route_index], fitness[best_route_index]

best_route, best_distance = evolve_edge_scramble(population_size, fitness_evaluations)
print(f"Best Route: {best_route}\nBest Distance: {best_distance}")