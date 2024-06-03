import numpy as np
from random import random, choice
from scipy.stats import truncnorm
from tqdm import tqdm
from math import exp

from src.gauss import sample_multivariate_truncated_gaussian

def initialize_population(population_size, bounds):
    dimensions = len(bounds)
    normalized_population = np.random.rand(population_size, dimensions)
    # check if bounds are given in proper order
    min_bound, max_bound = np.asarray(bounds).T
    bounds_difference = np.fabs(min_bound - max_bound)
    denorm_population = max_bound - bounds_difference * normalized_population
    return normalized_population, denorm_population

# problem minimalizacji (argmin)
def bbde(population, objective_func, iterations=100, alternative_exp_offset = True):
    exp_offset = 0.5 if alternative_exp_offset else 0.0
    population = population.copy()
    popsize = len(population)

    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    best_score = objective_func(best_individual)
    F = 0.8
    results = []

    # for i in tqdm(range(iterations), leave=False, desc=f'BBDE alt - {alternative_exp_offset}'):
    for _ in range(iterations): # i to?
        for individual in range(len(population)):
            # WYBIERA DWOCH LOSOWYCH OSOBNIKOW
            available_population_indexes = [idx for idx in range(popsize)]  # r1 != r2
            r1, r2 = population[np.random.choice(available_population_indexes, 2, replace=False)] # get two random individuals

            # TUTAJ ROZNE WARIANTY TEGO MUTANTA
            # TODO zwykly DE
            # indices = np.random.choice(popsize, 3, replace=False)
            # while individual in indices:
            #     indices = np.random.choice(popsize, 3, replace=False)
            # r1, r2, r3 = population[indices]
            # mutant_classic = r1 + F * (r2 - r3)
            
            # TODO zwykly BBDE
            # HERE
            #direction = r1 - r2
            sigma = abs(best_individual - individual)
            # sigma = np.std(direction)  # Standard deviation of the difference for Gaussian noise scaling
            
            #mutant_bbde = best_individual + np.random.normal(0, sigma, size=best_individual.shape)
            midpoint = (best_individual + individual) / 2
            mutant_bbde = np.random.normal(midpoint, sigma)  

            #if random.uniform(0, 1) < 0.5:
            #    mutant = mutant_classic
            #else:
            #    mutant = mutant_bbde                    

            # TODO z MSR

            # TODO z TPA

            # opcjonalnie: z exp (papier strona 130)
            # rand = random()                             # random real number between (0, 1)
            # mutant = population[j] + exp(rand - exp_offset) * (r1 - r2)     # (2) local selection, exp(od -0.5 do 0.5), TUTAJ CHYBA WCHODZI MSR I TPA
            # calkowicie nowy punkt, stworzony wg powyzszej reguly

            mutant = mutant_bbde# dummy, delete later
            
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


def main():
    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 2
    OBJECTIVE_FUNCTION = lambda x: sum(x**2)/len(x)

    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)
    results = bbde(denorm_population, OBJECTIVE_FUNCTION)
    # evaluation
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    
    print(f"{sum(scores) / len(scores)}")
    
    

if __name__ == "__main__":
    main()