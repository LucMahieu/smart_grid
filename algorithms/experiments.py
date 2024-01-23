import random
from classes.district import District
from algorithms.randomize import Random_algo
from algorithms.greedy import Greedy_algo
from classes.battery import Battery 

# def run_experiment(district, algorithm_class, num_experiments):
#     best_solution_cost = float('inf')
#     worst_solution_cost = float('-inf')
#     experiment_scores = []

#     for _ in range(num_experiments):
#         # Reset the district to its initial state before each experiment
#         district.reset_state()

#         # Create an instance of the algorithm and run it
#         algorithm_instance = algorithm_class()
#         valid_solution = algorithm_instance.run(district)

#         if not valid_solution:
#             print("Invalid solution encountered, skipping this iteration.")
#             continue

#         # Calculate the shared cost for this iteration
#         current_cost = district.shared_costs()
#         if current_cost is not None:
#             best_solution_cost = min(best_solution_cost, current_cost)
#             worst_solution_cost = max(worst_solution_cost, current_cost)
#             experiment_scores.append(current_cost)
#         else:
#             print("Incomplete solution, skipping this iteration.")

#     return best_solution_cost, worst_solution_cost, experiment_scores

def run_experiment(district, algorithm_class, num_experiments):
    best_solution_cost = float('inf')
    worst_solution_cost = float('-inf')
    experiment_scores = []

    for _ in range(num_experiments):
        # Reset the district to its initial state before each experiment
        district.reset_state()

        # Create an instance of the algorithm and run it
        algorithm_instance = algorithm_class()
        valid_solution = algorithm_instance.run(district)

        # Calculate the shared cost for this iteration
        current_cost = district.shared_costs()
        if current_cost is not None:
            best_solution_cost = min(best_solution_cost, current_cost)
            worst_solution_cost = max(worst_solution_cost, current_cost)
        else:
            print("Incomplete solution encountered.")

        # Append the current cost to the experiment_scores list
        experiment_scores.append(current_cost)

    return best_solution_cost, worst_solution_cost, experiment_scores
# # Example usage:
# best_cost, worst_cost, scores = run_experiment(district1, Greedy_algo, 10)
# print(f"Best solution cost: {best_cost}")
# print(f"Worst solution cost: {worst_cost}")
# print(f"All experiment scores: {scores}")
