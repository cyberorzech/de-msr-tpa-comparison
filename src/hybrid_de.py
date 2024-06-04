import numpy as np


def hybrid_tpa(population, objective_func, iterations=100):
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])

    best_index = np.argmin(fitness)
    best_individual = population[best_index]

    F1, F2 = 0.5, 0.8
    performance_F1, performance_F2 = [], []

    results = []

    for iteration in range(iterations):
        for individual in range(popsize):
            if iteration % 2 == 0:
                sigma = abs(best_individual - individual)
                midpoint = (best_individual + individual) / 2
                mutant = np.random.normal(midpoint, sigma)
                mutant_result = objective_func(mutant)
                if mutant_result >= fitness[individual]:
                    continue
                fitness[individual] = mutant_result
                population[individual] = mutant
                if mutant_result < fitness[best_index]:
                    best_index = individual
                    best_individual = mutant

            else:
                if len(performance_F1) >= 10:
                    mean_F1_last_10 = np.mean(performance_F1[-10:])
                    mean_F2_last_10 = np.mean(performance_F2[-10:])

                    if mean_F1_last_10 > mean_F2_last_10:
                        F = F1
                        current_F = "F1"
                    else:
                        F = F2
                        current_F = "F2"
                else:
                    F = F1
                    current_F = "F1"

                indices = np.random.choice(popsize, 3, replace=False)
                while individual in indices:
                    indices = np.random.choice(popsize, 3, replace=False)
                r1, r2, r3 = population[indices]

                mutant = r1 + F * (r2 - r3)
                mutant_result = objective_func(mutant)

                if mutant_result < fitness[individual]:
                    population[individual] = mutant
                    fitness[individual] = mutant_result

                    if mutant_result < fitness[best_index]:
                        best_index = individual
                        best_individual = mutant

                    if current_F == "F1":
                        performance_F1.append(mutant_result)
                    else:
                        performance_F2.append(mutant_result)

        results.append((best_individual.copy(), fitness[best_index]))

    return results


def hybrid_msr(population, objective_func, iterations=100):
    popsize = len(population)
    fitness = np.asarray([objective_func(ind) for ind in population])

    best_index = np.argmin(fitness)
    best_individual = population[best_index]

    F = 0.5
    success_rates = []
    results = []

    for iteration in range(iterations):
        successes = 0

        for individual in range(popsize):
            if iteration % 2 == 0:
                sigma = abs(best_individual - individual)
                midpoint = (best_individual + individual) / 2
                mutant = np.random.normal(midpoint, sigma)
                mutant_result = objective_func(mutant)
                if mutant_result >= fitness[individual]:
                    continue
                fitness[individual] = mutant_result
                population[individual] = mutant
                if mutant_result < fitness[best_index]:
                    best_index = individual
                    best_individual = mutant

            else:
                indices = np.random.choice(popsize, 3, replace=False)
                while individual in indices:
                    indices = np.random.choice(popsize, 3, replace=False)
                r1, r2, r3 = population[indices]

                mutant = r1 + F * (r2 - r3)
                mutant_result = objective_func(mutant)

                if mutant_result < fitness[individual]:
                    population[individual] = mutant
                    fitness[individual] = mutant_result
                    successes += 1

                    if mutant_result < fitness[best_index]:
                        best_index = individual
                        best_individual = mutant

            success_rate = successes / popsize * 0.5
            success_rates.append(success_rate)

            if len(success_rates) > 1:
                median_success = np.median(success_rates)
                if median_success > 0.5:
                    F *= 1.1  # Increase F if more than half the mutations are successful
                else:
                    F *= 0.9  # Decrease F otherwise

        results.append((best_individual.copy(), fitness[best_index]))

    return results
