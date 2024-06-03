from time import perf_counter

from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.commons import initialize_population
from src.commons import timeit
from src.cost_functions import *
from src.visualise import plot


@timeit()
def run(population: tuple, objective_function, de_function, iterations) -> tuple:
    start = perf_counter()
    results = de_function(population, objective_function, iterations)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    end = perf_counter()
    return individuals, scores, round(end - start, 2)


def main():
    # parametry dla wszystkich
    POPULATION_SIZE = 10  # max
    BOUNDS = [(-10, 10)] * 2
    objective_function = rosenbrock
    normalized_population, denorm_population = initialize_population(
        POPULATION_SIZE, BOUNDS
    )
    iterations = 100  # max

    # execution
    individuals, scores, exec_time = run(
        denorm_population, objective_function, de, iterations
    )
    # evaluation
    # print(f"{sum(scores) / len(scores)}")
    # print(scores)
    plot(scores, len(scores), -1, "testujemy-pzdr")


if __name__ == "__main__":
    main()
