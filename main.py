from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.commons import initialize_population

# wrapper na czas
def run(population: tuple, objective_function, de_function) -> tuple:
    results = de_function(population, objective_function)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    return individuals, scores

def main():
    # parametry dla wszystkich
    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 2
    OBJECTIVE_FUNCTION = lambda x: sum(x**2)/len(x)
    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)

    # execution
    individuals, scores = run(
        denorm_population,
        OBJECTIVE_FUNCTION,
        de
    )

    # evaluation
    print(scores)

    

if __name__ == "__main__":
    main()