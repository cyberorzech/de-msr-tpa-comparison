import numpy as np
from random import random, choice
from scipy.stats import truncnorm
from tqdm import tqdm
from math import exp


# problem minimalizacji (argmin)
def de(population, objective_func, iterations=100):
    population = population.copy()
    popsize = len(population)

    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    best_score = objective_func(best_individual)
    F = 0.8
    results = []

    for _ in range(iterations): # i to?
        for individual in range(len(population)):
            # WYBIERA DWOCH LOSOWYCH OSOBNIKOW
            available_population_indexes = [idx for idx in range(popsize)]  # r1 != r2
            r1, r2 = population[np.random.choice(available_population_indexes, 2, replace=False)] # get two random individuals

            indices = np.random.choice(popsize, 3, replace=False)
            while individual in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]
            mutant = r1 + F * (r2 - r3)
            
            mutant_result = objective_func(mutant)
            # jesli wartosc funkcji celu dla mutanta jest lepsza (mniejsza) niz aktualnie rozpatrywany punkt: podmiana punktow i aktualizacja wartosci w fitness 
            # dodatkowo jesli jest najlepszy jak dotad to best index tez aktualizowany
            if mutant_result >= fitness[individual]:
                continue
            fitness[individual] = mutant_result
            population[individual] = mutant
            if mutant_result < fitness[best_index]:
                best_index = individual
                best_individual = mutant
        # na koniec z tej calej populacji i podmianek mutantow lub braku podmianek wylania sie najlepszy punkt, ktory trafia do results
        results.append((best_individual, fitness[best_index]))    
    return results

def msr_de(population, objective_func, iterations=100):
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    F = 0.8  # Initial mutation factor

    # Track the success of each mutation
    success_rates = []

    results = []
    for _ in tqdm(range(iterations)):
        successes = 0  # Number of successful mutations in this iteration

        for i in range(popsize):
            # Select three random individuals, different from the target individual
            indices = np.random.choice(popsize, 3, replace=False)
            while i in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]

            # Perform mutation using DE formula
            mutant = r1 + F * (r2 - r3)
            mutant_result = objective_func(mutant)
            
            # Selection step
            if mutant_result < fitness[i]:
                population[i] = mutant
                fitness[i] = mutant_result
                successes += 1

                # Update best solution found
                if mutant_result < fitness[best_index]:
                    best_index = i
                    best_individual = mutant

        # Track the success rate of this generation
        success_rate = successes / popsize
        success_rates.append(success_rate)

        # Median Success Rule to adjust F
        if len(success_rates) > 1:  # Ensure there's enough data to calculate median
            median_success = np.median(success_rates)
            if median_success > 0.5:
                F *= 1.1  # Increase F if more than half the mutations are successful
            else:
                F *= 0.9  # Decrease F otherwise

        results.append((best_individual.copy(), fitness[best_index]))

    return results

def tpa_de(population, objective_func, iterations=100):
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    
    # Initialize two different mutation factors for TPA
    F1, F2 = 0.5, 0.8
    # Track performance history for each F
    performance_F1, performance_F2 = [], []
    
    results = []
    for _ in tqdm(range(iterations)):
        # For each generation, select which F to use based on past performance
        if np.mean(performance_F1[-10:]) > np.mean(performance_F2[-10:]) if len(performance_F1) >= 10 else True:
            F = F1
            current_F = 'F1'
        else:
            F = F2
            current_F = 'F2'

        for i in range(popsize):
            indices = np.random.choice(popsize, 3, replace=False)
            while i in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]

            # Mutation
            mutant = r1 + F * (r2 - r3)
            mutant_result = objective_func(mutant)
            
            # Selection
            if mutant_result < fitness[i]:
                population[i] = mutant
                fitness[i] = mutant_result

                # Update best solution found
                if mutant_result < fitness[best_index]:
                    best_index = i

                # Track successful application of F
                if current_F == 'F1':
                    performance_F1.append(mutant_result)
                else:
                    performance_F2.append(mutant_result)

        results.append((population[best_index].copy(), fitness[best_index]))

    return results

def main():
    """
    Example usage:

    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 100
    OBJECTIVE_FUNCTION = lambda x: sum(x**2)/len(x)

    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)
    results = bbde(denorm_population, OBJECTIVE_FUNCTION)
    # evaluation
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    
    print(f"{sum(scores) / len(scores)}")
    """
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()