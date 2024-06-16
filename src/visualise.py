import matplotlib.pyplot as plt
import warnings
import numpy as np

FONTSIZE = 18


def plot(scores_list: list, global_minimum: float, title: str):
    # Number of iterations is assumed to be consistent across all score lists
    iterations = list(range(1, len(scores_list[0]) + 1))

    average_scores = np.mean(scores_list, axis=0)

    # Create the plot for linear scale
    plt.figure(figsize=(12, 6))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Extend colors if more than 7 lists
    for scores, color in zip(scores_list, colors):
        plt.plot(iterations, scores, marker="o", linestyle="-", linewidth=0.8, color=color, label=f"Scores {colors.index(color)+1}")

    plt.plot(iterations, average_scores, marker="o", linestyle="--", linewidth=0.8, color="orange", label="Average Scores")
    plt.axhline(y=global_minimum, color="k", linestyle="--", linewidth=0.8, label="Global Minimum ({})".format(global_minimum))

    # Adding labels and title
    plt.xlabel("Iteration", fontsize=FONTSIZE)
    plt.ylabel("Score", fontsize=FONTSIZE)
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)
    # plt.title(title)
    plt.legend()

    # Show the grid
    plt.grid(True)
    plt.savefig(f"./img/{title}.png")
    plt.close()

    # Create the plot for log scale
    plt.figure(figsize=(12, 6))
    for scores, color in zip(scores_list, colors):
        plt.plot(iterations, scores, marker="o", linestyle="-", linewidth=0.8, color=color, label=f"Experiment {colors.index(color)+1}")

    plt.plot(iterations, average_scores, marker="o", linestyle="--", linewidth=0.8, color="orange", label="Average Scores")
    plt.axhline(y=global_minimum, color="k", linestyle="--", linewidth=0.8, label="Global Minimum ({})".format(global_minimum))

    # Adding labels and title
    plt.xlabel("Iteration", fontsize=FONTSIZE)
    plt.ylabel("Score", fontsize=FONTSIZE)
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)
    plt.title(title + " (Log Scale)")
    plt.legend()

    # Show the grid and set log scale
    plt.grid(True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        plt.yscale("log")
    plt.savefig(f"./img/{title}_log.png")
    plt.close()


def plot_average_scores(scores_list, obj_function, title):
    plt.figure(figsize=(10, 6))
    markers = ['o', 'v', 's', 'P', '*', 'D', 'X', 'd']
    for i, (de_type, avg_scores) in enumerate(scores_list):
        plt.plot(avg_scores, marker=markers[i % len(markers)], label=de_type)

    plt.title(f"Average Scores of DE Algorithms on {obj_function}")
    plt.xlabel('Iteration')
    plt.ylabel('Average Score')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./img/{title}_avg.png")
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./img/{title}_avg_log.png")
    plt.close()


def plot_best_scores(best_scores_list, obj_function, title):
    labels, values = zip(*best_scores_list)
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')

    plt.title(f"Best Minimal Scores of DE Algorithms on {obj_function}")
    plt.xlabel('DE Type')
    plt.ylabel('Best Minimal Score')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.savefig(f"./img/{title}_best.png")
    plt.yscale('log')
    plt.savefig(f"./img/{title}_best_log.png")
    plt.close()


def plot_execution_times(exec_time_list, obj_function, title):
    de_types = [item[0] for item in exec_time_list]
    avg_exec_times = [item[1] for item in exec_time_list]

    plt.figure(figsize=(10, 6))
    plt.bar(de_types, avg_exec_times, color='skyblue')

    plt.title(f"Average Execution Time of DE Algorithms on {obj_function}")
    plt.xlabel('DE Type')
    plt.ylabel('Average Execution Time (seconds)')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.savefig(f"./img/{title}_times.png")
    plt.close()


def plot_best_scores_each_iteration(scores_list, obj_function, title):
    plt.figure(figsize=(10, 6))
    markers = ['o', 'v', 's', 'P', '*', 'D', 'X', 'd']
    for i, (de_type, best_scores) in enumerate(scores_list):
        plt.plot(best_scores, marker=markers[i % len(markers)], label=de_type)

    plt.title(f"Best Scores per Iteration of DE Algorithms on {obj_function}")
    plt.xlabel('Iteration')
    plt.ylabel('Best Score')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./img/{title}_best_each_iteration.png")
    plt.yscale('log')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./img/{title}_best_each_iteration_log.png")
    plt.close()


if __name__ == "__main__":
    # Example usage with dummy data
    scores_list = [
        [-0.3, -0.5, -0.7, -0.9, -1.0],
        [-0.1, -0.2, -0.6, -0.8, -0.95],
        [-0.4, -0.4, -0.4, -0.5, -0.6]
    ]
    global_minimum = -1
    plot(scores_list, global_minimum, "Convergence Plot")
