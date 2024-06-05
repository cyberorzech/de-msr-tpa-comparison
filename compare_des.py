import pandas as pd
from time import perf_counter
from math import pi

from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.hybrid_de import hybrid_msr, hybrid_tpa
from src.commons import initialize_population
from src.cost_functions import *
from src.visualise import *


ITERATIONS = 20
REPEATS = 20
DIMENSIONS = 2
bounds = {
    "rosenbrock": [(-5, 10)] * DIMENSIONS,
    "levy": [(-10, 10)] * DIMENSIONS,
    "michalewicz": [(0, pi)] * DIMENSIONS,
    "bonachevsky": [(-100, 100)] * DIMENSIONS,
    "eason": [(-100, 100)] * 2
}

DE_types = [de, msr_de, tpa_de, bbde, hybrid_msr, hybrid_tpa]


def compare_de_algorithms(population_size, obj_function, function_bounds):
    print("Performing comparison tests for all DE types")
    initial_normalized_population, initial_denorm_population = initialize_population(
        population_size,
        function_bounds
    )

    if obj_function == levy:
        function_name = "levy"
    elif obj_function == rosenbrock:
        function_name = "rosenbrock"
    elif obj_function == michalewicz:
        function_name = "michalewicz"
    elif obj_function == eason:
        function_name = "eason"
    else:
        function_name = "bonachevsky"

    title = f"all_DEs_{function_name}"
    data_fragments = list()
    scores_list = list()
    exec_time_list = list()
    best_scores_list = list()

    for de_type in DE_types:
        de_type_name = de_type.__name__
        all_scores = []
        exec_times = []
        for repetition in range(REPEATS):
            denorm_population = np.copy(initial_denorm_population)

            individuals, scores, exec_time = run(
                population=denorm_population,
                objective_function=obj_function,
                de_function=de_type,
                iterations=200
            )

            all_scores.append(scores)
            exec_times.append(exec_time)

            repetition_data = pd.DataFrame({
                "DE_type": [de_type_name] * len(scores),
                "repetition": [repetition] * len(scores),
                "scores": scores,
                "exec_time": [exec_time] * len(scores)
            })

            data_fragments.append(repetition_data)

        best_score = np.min(all_scores)
        avg_scores = np.mean(all_scores, axis=0)
        avg_exec_time = np.mean(exec_times)
        best_scores_list.append((de_type_name, best_score))
        scores_list.append((de_type_name, avg_scores))
        exec_time_list.append((de_type_name, avg_exec_time))

    all_data = pd.concat(data_fragments, ignore_index=True)

    all_data.to_csv(f"./csv/{function_name}_results.csv", index=False)

    plot_average_scores(scores_list, function_name, title)
    plot_best_scores(best_scores_list, function_name, title)
    plot_execution_times(exec_time_list, function_name, title)


def run(population: tuple, objective_function, de_function, iterations) -> tuple:
    start = perf_counter()
    results = de_function(population, objective_function, iterations)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    end = perf_counter()
    return individuals, scores, round(end - start, 2)


compare_de_algorithms(20, eason, bounds["eason"])
# compare_de_algorithms(20, levy, bounds["levy"])
# compare_de_algorithms(20, rosenbrock, bounds["rosenbrock"])
# compare_de_algorithms(20, michalewicz, bounds["michalewicz"])
# compare_de_algorithms(20, bonachevsky, bounds["bonachevsky"])
