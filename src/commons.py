import numpy as np
from scipy.stats import multivariate_normal
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


def sample_multivariate_truncated_gaussian(
    means, cov_matrix, lower_bounds, upper_bounds, size=1
):
    """
    Sample from a multivariate Gaussian and manually truncate the results.
    :param means: Array of means for each dimension.
    :param cov_matrix: Covariance matrix for the dimensions.
    :param lower_bounds: Array of lower bounds for each dimension.
    :param upper_bounds: Array of upper bounds for each dimension.
    :param size: Number of samples to generate.
    :return: Array of truncated samples.
    """
    # Ensure bounds, means, and covariance matrix have compatible shapes
    assert (
        len(means) == len(lower_bounds) == len(upper_bounds) == len(cov_matrix)
    ), "Dimension mismatch"

    # Sample from a multivariate normal distribution
    samples = multivariate_normal.rvs(mean=means, cov=cov_matrix, size=size)

    # Apply truncation
    truncated_samples = np.clip(samples, lower_bounds, upper_bounds)

    return truncated_samples


if __name__ == "__main__":
    raise NotImplementedError("Use as package")

# Example usage
# 2 dimensions
# means = np.array([0.5, 0.5, 0.5])  # Mean of each dimension
# cov_matrix = np.array([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]])  # Covariance matrix
# lower_bounds = np.array([0, 0, 0])  # Lower bounds for each dimension
# upper_bounds = np.array([1, 1, 1])  # Upper bounds for each dimension

# samples = sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=10)
# print("Truncated Multivariate Gaussian Samples:\n", samples)

# 3 dimensions
# means = np.array([0.5, 0.5, 0.5])  # Mean of each dimension
# cov_matrix = np.array([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]])  # Covariance matrix
# lower_bounds = np.array([0, 0, 0])  # Lower bounds for each dimension
# upper_bounds = np.array([1, 1, 1])  # Upper bounds for each dimension

# samples = sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=10)
# print("Truncated Multivariate Gaussian Samples:\n", samples)
