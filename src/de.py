import numpy as np
from tqdm import tqdm


def de(population, objective_func, iterations=100):
    population = population.copy()
    popsize = len(population)

    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    best_score = objective_func(best_individual)
    F = 0.5
    results = []

    for _ in range(iterations):
        for individual in range(popsize):
            indices = np.random.choice(popsize, 3, replace=False)
            while individual in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]
            mutant = r1 + F * (r2 - r3)

            mutant_result = objective_func(mutant)

            if mutant_result >= fitness[individual]:
                continue
            fitness[individual] = mutant_result
            population[individual] = mutant
            if mutant_result < fitness[best_index]:
                best_index = individual
                best_individual = mutant

        results.append((best_individual, fitness[best_index]))
    return results


def msr_de(population, objective_func, iterations=100):
    population = population.copy()
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_individual = population[best_index]
    F = 0.8  # Początkowy zasięg mutacji

    success_rates = []
    results = []
    for _ in range(iterations):
        successes = 0  # Liczba mutacji zakończonych sukcesem

        for i in range(popsize):
            indices = np.random.choice(popsize, 3, replace=False)
            while i in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]

            mutant = r1 + F * (r2 - r3)
            mutant_result = objective_func(mutant)

            # Selekcja
            if mutant_result < fitness[i]:
                population[i] = mutant
                fitness[i] = mutant_result
                successes += 1

                if mutant_result < fitness[best_index]:
                    best_index = i
                    best_individual = mutant

        # Wskaźnik sukcesu dla generacji
        success_rate = successes / popsize
        success_rates.append(success_rate)

        # Median Success Rule dopasowująca parametr F
        if len(success_rates) > 1:  # Sprawdzenie czy jest wystarczjąco danych do policzenia mediany
            median_success = np.median(success_rates[-10:])
            # Aktualizacja parametru F
            if median_success > 0.5:
                F *= 1.1
            else:
                F *= 0.9

        results.append((best_individual.copy(), fitness[best_index]))

    return results


def tpa_de(population, objective_func, iterations=100):
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])
    best_index = np.argmin(fitness)

    # Inicjalizacja dwóch parametrów F
    F1, F2 = 0.5, 0.8
    # Śledzenie jakości dla każdego z parametrów
    performance_F1, performance_F2 = [], []

    results = []
    for _ in tqdm(range(iterations)):
        # Wybór F na podstawie performance'u
        if (
            np.mean(performance_F1[-10:]) > np.mean(performance_F2[-10:])
            if len(performance_F1) >= 10
            else True
        ):
            F = F1
            current_F = "F1"
        else:
            F = F2
            current_F = "F2"

        for i in range(popsize):
            indices = np.random.choice(popsize, 3, replace=False)
            while i in indices:
                indices = np.random.choice(popsize, 3, replace=False)
            r1, r2, r3 = population[indices]

            mutant = r1 + F * (r2 - r3)
            mutant_result = objective_func(mutant)

            if mutant_result < fitness[i]:
                population[i] = mutant
                fitness[i] = mutant_result

                if mutant_result < fitness[best_index]:
                    best_index = i

                if current_F == "F1":
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
