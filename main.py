from time import perf_counter

from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.commons import initialize_population
from src.commons import timeit
from src.cost_functions import *


@timeit()
def run(population: tuple, objective_function, de_function) -> tuple:
    start = perf_counter()
    results = de_function(population, objective_function)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    end = perf_counter()
    return individuals, scores, round(end - start, 2)

def main():
    # parametry dla wszystkich
    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 2
    objective_function = x_squared
    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)

    # execution
    individuals, scores, exec_time = run(
        denorm_population,
        objective_function,
        de
    )
    # evaluation
    # print(scores)
    # print(f"{exec_time=}s")

    

if __name__ == "__main__":
    main()