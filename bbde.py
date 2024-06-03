import numpy as np
from random import random, choice


def initialize_population(population_size, bounds):
    dimensions = len(bounds)
    normalized_population = np.random.rand(population_size, dimensions)
    # check if bounds are given in proper order
    min_bound, max_bound = np.asarray(bounds).T
    bounds_difference = np.fabs(min_bound - max_bound)
    denorm_population = max_bound - bounds_difference * normalized_population
    return normalized_population, denorm_population


def adaptive_bbde(fobj, pop, its=1000):
    popsize = len(pop)
    population = np.copy(pop)
    # Ensure fitness is calculated as a list of scalar values
    fitness = np.array([fobj(ind) for ind in population])
    best_index = np.argmin(fitness)
    best = population[best_index]
    results = []

    F1, F2 = 0.5, 0.8  # Initial scale factors
    success_rates = []

    for i in range(its):
        successes = 0
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = population[np.random.choice(idxs, 3, replace=False)]
            
            F = F1 if random() > 0.5 else F2  # Two-point adaptation
            
            mutant = a + F * (b - c)
            trial = np.array([mutant[k] if random() < 0.9 else population[j][k] for k in range(len(mutant))])
            
            new_fitness = fobj(trial)
            # Ensure scalar comparisons for fitness
            if new_fitness < fitness[j]:
                fitness[j] = new_fitness
                population[j] = trial
                if new_fitness < fitness[best_index]:
                    best_index = j
                    best = trial
                successes += 1

        success_rates.append(successes / popsize)
        results.append((best.copy(), fitness[best_index]))

        # Median Success Rule for scale factor adaptation
        median_success = np.median(success_rates)
        if median_success > 0.5:
            F1 *= 1.1
            F2 *= 1.1
        else:
            F1 *= 0.9
            F2 *= 0.9

    return results





def main():
    population_size = 20
    bounds = [(-10, 10)] * 10
    normalized_population, denorm_population = initialize_population(population_size, bounds)
    fobj = lambda x: x**2
    results = adaptive_bbde(fobj, normalized_population)
    print(results)

if __name__ == "__main__":
    main()