# 2 DIMENSIONS

# import numpy as np
# from scipy.stats import multivariate_normal

# def sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=1):
#     """
#     Sample from a multivariate Gaussian and manually truncate the results.
#     :param means: Array of means for each dimension.
#     :param cov_matrix: Covariance matrix for the dimensions.
#     :param lower_bounds: Array of lower bounds for each dimension.
#     :param upper_bounds: Array of upper bounds for each dimension.
#     :param size: Number of samples to generate.
#     :return: Array of truncated samples.
#     """
#     # Ensure bounds, means, and covariance matrix have compatible shapes
#     assert len(means) == len(lower_bounds) == len(upper_bounds) == len(cov_matrix), "Dimension mismatch"

#     # Sample from a multivariate normal distribution
#     samples = multivariate_normal.rvs(mean=means, cov=cov_matrix, size=size)
    
#     # Apply truncation
#     truncated_samples = np.clip(samples, lower_bounds, upper_bounds)
    
#     return truncated_samples

# # Example usage
# means = np.array([0.5, 0.5])  # Mean of each dimension
# cov_matrix = np.array([[0.1, 0], [0, 0.1]])  # Covariance matrix
# lower_bounds = np.array([0, 0])  # Lower bounds for each dimension
# upper_bounds = np.array([1, 1])  # Upper bounds for each dimension

# samples = sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=10)
# print("Truncated Multivariate Gaussian Samples:\n", samples)


# 3 DIMENSIONS

import numpy as np
from scipy.stats import multivariate_normal

def sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=1):
    """
    Sample from a multivariate Gaussian and manually truncate the results for 3 dimensions.
    :param means: Array of means for each dimension (length 3).
    :param cov_matrix: 3x3 covariance matrix for the dimensions.
    :param lower_bounds: Array of lower bounds for each dimension (length 3).
    :param upper_bounds: Array of upper bounds for each dimension (length 3).
    :param size: Number of samples to generate.
    :return: Array of truncated samples.
    """
    # Ensure bounds, means, and covariance matrix have compatible shapes
    assert len(means) == len(lower_bounds) == len(upper_bounds) == len(cov_matrix), "Dimension mismatch"

    # Sample from a multivariate normal distribution
    samples = multivariate_normal.rvs(mean=means, cov=cov_matrix, size=size)
    
    # Apply truncation
    truncated_samples = np.clip(samples, lower_bounds, upper_bounds)
    
    return truncated_samples

# Example usage
means = np.array([0.5, 0.5, 0.5])  # Mean of each dimension
cov_matrix = np.array([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]])  # Covariance matrix
lower_bounds = np.array([0, 0, 0])  # Lower bounds for each dimension
upper_bounds = np.array([1, 1, 1])  # Upper bounds for each dimension

samples = sample_multivariate_truncated_gaussian(means, cov_matrix, lower_bounds, upper_bounds, size=10)
print("Truncated Multivariate Gaussian Samples:\n", samples)
