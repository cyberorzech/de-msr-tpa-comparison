import numpy as np
import matplotlib.pyplot as plt


# Define the Sphere function
def sphere_function(x):
    return np.sum(x**2, axis=1)


# Generate random initial population
population_size = 100
dimensions = 10
population = np.random.randn(population_size, dimensions)

# Placeholder for BBDE implementation
# Here you would integrate the BBDE algorithm
# For now, let's assume we just evaluate the initial population
fitness = sphere_function(population)

# Plotting the fitness of the initial population
plt.figure(figsize=(10, 5))
plt.hist(fitness, bins=20, alpha=0.75)
plt.title("Initial Fitness Distribution of Population")
plt.xlabel("Fitness")
plt.ylabel("Frequency")
plt.show()
