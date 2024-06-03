import numpy as np
from random import random, choice
from tqdm import tqdm
from math import exp


def initialize_population(population_size, bounds):
    dimensions = len(bounds)
    normalized_population = np.random.rand(population_size, dimensions)
    # check if bounds are given in proper order
    min_bound, max_bound = np.asarray(bounds).T
    bounds_difference = np.fabs(min_bound - max_bound)
    denorm_population = max_bound - bounds_difference * normalized_population
    return normalized_population, denorm_population

# problem minimalizacji (argmin)
def bbde(population, fobj, iterations=100, alternative_exp_offset = True):
    exp_offset = 0.5 if alternative_exp_offset else 0.0
    population = population.copy()
    popsize = len(population)

    fitness = np.asarray([fobj(ind) for ind in population])
    best_index = np.argmin(fitness)
    best = population[best_index]
    results = []

    # for i in tqdm(range(iterations), leave=False, desc=f'BBDE alt - {alternative_exp_offset}'):
    for _ in range(iterations): # i to?



        # ========
        for j in range(len(population)): # j to osobnik?

            # WYBIERA DWOCH LOSOWYCH OSOBNIKOW
            random_indexes = [idx for idx in range(popsize)]  # r1 != r2   # czy to jest zle? nei ma losowosci
            r1, r2 = population[np.random.choice(random_indexes, 2, replace=False)]

            rand = random()                             # random real number between (0, 1)
            mutant = population[j] + exp(rand - exp_offset) * (r1 - r2)     # (2) local selection, exp(od -0.5 do 0.5), TUTAJ CHYBA WCHODZI MSR I TPA
            # calkowicie nowy punkt, stworzony wg powyzszej reguly


            trial = mutant                              # CR = 1 (1)

            f = fobj(trial)

            # jesli wartosc funkcji celu dla mutanta jest lepsza (mniejsza) niz aktualnie rozpatrywany punkt: podmiana punktow i aktualizacja wartosci w fitness 
            # dodatkowo jesli jest najlepszy jak dotad to best index tez aktualizowany
            if f < fitness[j]:
                fitness[j] = f
                population[j] = trial
                if f < fitness[best_index]:
                    best_index = j
                    best = trial
        # na koniec z tej calej populacji i podmianek mutantow lub braku podmianek wylania sie najlepszy punkt, ktory trafia do results
        results.append((best, fitness[best_index]))

    
    
    
    return results


def main():
    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 2
    OBJECTIVE_FUNCTION = lambda x: sum(x**2)/len(x)

    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)
    results = bbde(denorm_population, OBJECTIVE_FUNCTION)
    print(results)
    
    

if __name__ == "__main__":
    main()