import matplotlib.pyplot as plt
import warnings

FONTSIZE = 18


def plot(scores: list, iterations: list, global_minimum: int, title: str):
    # Known global minimum for the problem
    global_minimum = -1

    # Number of iterations
    iterations = list(range(1, len(scores) + 1))

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(iterations, scores, marker="o", linestyle="-", color="b", label="Scores")
    plt.axhline(
        y=global_minimum, color="r", linestyle="--", label="Global Minimum (-1)"
    )

    # Adding labels and title
    plt.xlabel("Iteration", fontsize=FONTSIZE)
    plt.ylabel("Score", fontsize=FONTSIZE)
    plt.xticks(fontsize=FONTSIZE)
    plt.yticks(fontsize=FONTSIZE)
    # plt.title('Convergence of Scores to Global Minimum')
    plt.legend()

    # Show the grid
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Linear Y axe
        plt.grid(True)
        plt.savefig(f"./img/{title}.png")
        plt.close()
        # Log Y axe
        plt.yscale("log")
        plt.savefig(f"./img/{title}_log.png")
        plt.close()


if __name__ == "__main__":
    raise NotImplementedError()
