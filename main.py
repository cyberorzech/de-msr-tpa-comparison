from src.bbde import bbde
from src.de import de, msr_de, tpa_de
from src.commons import initialize_population

def main():
    POPULATION_SIZE = 20 # dwadziescia osobnikow, czyli par x y
    BOUNDS = [(-10, 10)] * 2
    OBJECTIVE_FUNCTION = lambda x: sum(x**2)/len(x)

    normalized_population, denorm_population = initialize_population(POPULATION_SIZE, BOUNDS)
    # evaluation
    results = tpa_de(denorm_population, OBJECTIVE_FUNCTION)
    individuals = [result[0] for result in results]
    scores = [result[1] for result in results]
    
    print(f"{sum(scores) / len(scores)}")

if __name__ == "__main__":
    main()