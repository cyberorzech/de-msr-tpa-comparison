import pandas as pd
from time import perf_counter, sleep
from tqdm import tqdm
from datetime import datetime
from math import pi

from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.hybrid_de import hybrid_msr, hybrid_tpa
from src.commons import initialize_population
from src.commons import timeit
from src.cost_functions import *
from src.visualise import plot


def run(population: tuple, objective_function, de_function, iterations) -> tuple:
    start = perf_counter()
    results = de_function(population, objective_function, iterations)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    end = perf_counter()
    return individuals, scores, round(end - start, 2)


def main():
    # # parametry dla wszystkich
    # POPULATION_SIZE = 10  # max
    # BOUNDS = [(-10, 10)] * 2
    # objective_function = rosenbrock
    # normalized_population, denorm_population = initialize_population(
    #     POPULATION_SIZE, BOUNDS
    # )
    # iterations = 100  # max
    # # execution
    # individuals, scores, exec_time = run(
    #     denorm_population, objective_function, de, iterations
    # )
    # # evaluation
    # # print(f"{sum(scores) / len(scores)}")
    # # print(scores)
    # plot(scores, len(scores), -1, "testujemy-pzdr")


    # CASE 1
    MINIMAL_POPULATION = 10
    MAXIMAL_POPULATION = 131
    POPULATION_INTERVAL = 30
    ITERATIONS = 20
    REPEATS = 20
    DIMENSIONS = 10
    bounds = {
        "rosenbrock": [(-5, 10)] * DIMENSIONS,
        "levy": [(-10, 10)] * DIMENSIONS,
        "michalewicz": [(0, pi)] * DIMENSIONS,
        "bonachevsky": [(-100, 100)] * DIMENSIONS
    }

    print(f"Case 1: {datetime.now().__str__()}")
    for population_size in tqdm(range(MINIMAL_POPULATION, MAXIMAL_POPULATION, POPULATION_INTERVAL), desc="Population size", leave=False):
    #for population_size in range(MINIMAL_POPULATION, MAXIMAL_POPULATION, POPULATION_INTERVAL):
        # rosenbrock
        print(f"Iteration for population size: f'{population_size}'")
        initial_normalized_population, initial_denorm_population = initialize_population(
            population_size, 
            bounds["rosenbrock"]
        )
        title = f"case1_{population_size}_rosenbrock"
        data_fragments = list()
        scores_list = list()
        for repetition in range(REPEATS):
            denorm_population = np.copy(initial_denorm_population)

            individuals, scores, exec_time = run(
                population=denorm_population,
                objective_function=levy,
                de_function=hybrid_msr,
                iterations=100
            )
            repetition_data = pd.DataFrame({
                "repetition": [repetition] * len(scores),
                "scores": scores,
                "exec_time": [exec_time] * len(scores)
            })
            data_fragments.append(repetition_data)
            scores_list.append(scores)
        results = pd.concat(data_fragments, ignore_index=True)

        results.to_csv(f"./csv/{title}.csv")
        plot(
            scores_list=scores_list,
            global_minimum=0,
            title=title
        )

        all_scores = np.concatenate(scores_list)
        min_value = np.min(all_scores)
        avg_value = np.mean(all_scores)

        print('Average score = ', avg_value, 'Minimum score = ', min_value)


        

        # levy
        # michalewicz
        # bonachevsky
        
        

    # CASE 2


    # CASE 3


    # CASE 4


    # CASE 5


    # CASE 6


    # CASE 7


if __name__ == "__main__":
    main()
