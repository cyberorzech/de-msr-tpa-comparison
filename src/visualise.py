# import matplotlib.pyplot as plt
# import warnings

# FONTSIZE = 18


# def plot(scores: list, iterations: list, global_minimum: int, title: str):
#     # Known global minimum for the problem
#     global_minimum = -1

#     # Number of iterations
#     iterations = list(range(1, len(scores) + 1))

#     # Create the plot
#     plt.figure(figsize=(12, 6))
#     plt.plot(iterations, scores, marker="o", linestyle="-", color="b", label="Scores")
#     plt.axhline(
#         y=global_minimum, color="r", linestyle="--", label="Global Minimum (-1)"
#     )

#     # Adding labels and title
#     plt.xlabel("Iteration", fontsize=FONTSIZE)
#     plt.ylabel("Score", fontsize=FONTSIZE)
#     plt.xticks(fontsize=FONTSIZE)
#     plt.yticks(fontsize=FONTSIZE)
#     # plt.title('Convergence of Scores to Global Minimum')
#     plt.legend()

#     # Show the grid
#     with warnings.catch_warnings():
#         warnings.simplefilter("ignore")
#         # Linear Y axe
#         plt.grid(True)
#         plt.savefig(f"./img/{title}.png")
#         plt.close()
#         # Log Y axe
#         plt.yscale("log")
#         plt.savefig(f"./img/{title}_log.png")
#         plt.close()


# if __name__ == "__main__":
#     raise NotImplementedError()



import matplotlib.pyplot as plt
import warnings

FONTSIZE = 18

def plot(scores_list: list, global_minimum: float, title: str):
    # Number of iterations is assumed to be consistent across all score lists
    iterations = list(range(1, len(scores_list[0]) + 1))

    # Create the plot for linear scale
    plt.figure(figsize=(12, 6))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Extend colors if more than 7 lists
    for scores, color in zip(scores_list, colors):
        plt.plot(iterations, scores, marker="o", linestyle="-", color=color, label=f"Scores {colors.index(color)+1}")
    
    plt.axhline(y=global_minimum, color="k", linestyle="--", label="Global Minimum ({})".format(global_minimum))

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
        plt.plot(iterations, scores, marker="o", linestyle="-", color=color, label=f"Experiment {colors.index(color)+1}")
    
    plt.axhline(y=global_minimum, color="k", linestyle="--", label="Global Minimum ({})".format(global_minimum))

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

if __name__ == "__main__":
    # Example usage with dummy data
    scores_list = [
        [-0.3, -0.5, -0.7, -0.9, -1.0],
        [-0.1, -0.2, -0.6, -0.8, -0.95],
        [-0.4, -0.4, -0.4, -0.5, -0.6]
    ]
    global_minimum = -1
    plot(scores_list, global_minimum, "Convergence Plot")
