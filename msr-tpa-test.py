import numpy as np

def objective_function(x):
    return x**2

def median_success_rule(initial_step_size, iterations, success_threshold=0.5):
    current_position = np.random.randn()
    step_size = initial_step_size

    for _ in range(iterations):
        new_position = current_position + np.random.randn() * step_size
        if objective_function(new_position) < objective_function(current_position):
            current_position = new_position
            success = True
        else:
            success = False

        # Adapt step size based on success
        if success > success_threshold:
            step_size *= 1.1  # Increase step size
        else:
            step_size *= 0.9  # Decrease step size

        print(f"Current position: {current_position}, Step size: {step_size}")

def two_point_adaptation(initial_step_size, iterations):
    current_position = np.random.randn()
    step_sizes = [initial_step_size, initial_step_size * 1.2]
    best_step_size = step_sizes[0]

    for _ in range(iterations):
        positions = [current_position + np.random.randn() * s for s in step_sizes]
        best_index = np.argmin([objective_function(p) for p in positions])

        current_position = positions[best_index]
        best_step_size = step_sizes[best_index]

        # Adapt the losing step size to be closer to the winning one
        step_sizes[1 - best_index] *= 0.9

        print(f"Current position: {current_position}, Best step size: {best_step_size}")

median_success_rule(0.1, 20)
two_point_adaptation(0.1, 20)
