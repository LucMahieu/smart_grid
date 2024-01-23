import random
from Classes.district import District
from randomize import Random_algo
from euclidean_distance import Greedy_algo
from Classes.battery import Battery 

def run_experiment(district, algorithm_class, num_experiments):
    best_solution_cost = float('inf')
    worst_solution_cost = float('-inf')
    experiment_scores = []

    for _ in range(num_experiments):
        # Shuffle the order of houses
        random.shuffle(district.houses)

        # Reset the district state before running the algorithm
        for house in district.houses:
            house.cables = []
            house.battery = None
        for battery in district.batteries:
            battery.reset_capacity()

        # Create an instance of the algorithm class (Random_algo or Greedy_algo)
        algorithm_instance = algorithm_class()

        # Run the algorithm to connect houses with batteries and lay cable routes
        algorithm_instance.run(district)

        # Calculate  shared cost for this iteration
        district.shared_costs()
        current_cost = district.district_cost_shared

        # Update best and worst solutions
        best_solution_cost = min(best_solution_cost, current_cost)
        worst_solution_cost = max(worst_solution_cost, current_cost)

        # Add  current cost to  list of experiment scores
        experiment_scores.append(current_cost)


    return best_solution_cost, worst_solution_cost, experiment_scores

# Example usage:
best_cost, worst_cost, scores = run_experiment(district1, Greedy_algo, 10)
print(f"Best solution cost: {best_cost}")
print(f"Worst solution cost: {worst_cost}")
print(f"All experiment scores: {scores}")
