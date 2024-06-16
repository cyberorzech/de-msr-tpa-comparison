import numpy as np


def bbde(population, objective_func, iterations=100, alternative_exp_offset=True):
    exp_offset = 0.5 if alternative_exp_offset else 0.0
    population = population.copy()
    popsize = len(population)

    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    results = []

    # for i in tqdm(range(iterations), leave=False, desc=f'BBDE alt - {alternative_exp_offset}'):
    for _ in range(iterations):
        for i in range(popsize):
            # Generowanie nowego punktu na podstawie obecnego i najlepszego punktu przy pomocy rozkładu normalnego
            sigma = abs(best_individual - population[i]) / 2
            midpoint = (best_individual + population[i]) / 2
            mutant = np.random.normal(midpoint, sigma)

            # Ocena nowego punktu
            mutant_result = objective_func(mutant)

            if mutant_result < fitness[i]:
                fitness[i] = mutant_result
                population[i] = mutant

                if mutant_result < fitness[best_index]:
                    best_index = i
                    best_individual = mutant

        results.append((best_individual, fitness[best_index]))
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
