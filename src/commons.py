import numpy as np
from time import perf_counter

SEED = 123


def initialize_population(population_size, bounds):
    np.random.seed(seed=SEED)
    dimensions = len(bounds)
    normalized_population = np.random.rand(population_size, dimensions)
    # check if bounds are given in proper order
    min_bound, max_bound = np.asarray(bounds).T
    bounds_difference = np.fabs(min_bound - max_bound)
    denorm_population = max_bound - bounds_difference * normalized_population
    return normalized_population, denorm_population


def timeit():
    def measure_time(func):
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            stop = perf_counter()
            print(f"Function: {func.__name__}, {(stop - start):.2f} seconds")
            return result

        return wrapper

    return measure_time


if __name__ == "__main__":
    raise NotImplementedError("Use as package")
