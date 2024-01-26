import random
from classes.district import District
from algorithms.randomize import Random_algo
from algorithms.greedy import Greedy_algo
from classes.battery import Battery 
import matplotlib.pyplot as plt
import time 


def run_experiment(district, algorithm_class, num_experiments):
    best_solution_cost = float('inf')
    worst_solution_cost = float('-inf')
    experiment_scores = []
    valid_solutions_count = 0
    invalid_solutions_count = 0

    for _ in range(num_experiments):
        # Reset the district to its initial state before each experiment
        print(f"Before reset: {district.district_cost_shared}")
        district.reset_state()
        print(f"After reset: {district.district_cost_shared}")
        # Create an instance of the algorithm and run it
        algorithm_instance = algorithm_class()
        valid_solution = algorithm_instance.run(district)

        # Calculate the shared cost for this iteration
        current_cost = district.shared_costs()
        print(f"Current cost for this run: {current_cost}")

        if current_cost is not None:
            best_solution_cost = min(best_solution_cost, current_cost)
            worst_solution_cost = max(worst_solution_cost, current_cost)
            valid_solutions_count += 1
        else:
            invalid_solutions_count += 1

        # Append the current cost to the experiment_scores list
        experiment_scores.append(current_cost if current_cost is not None else 0)

    return best_solution_cost, worst_solution_cost, experiment_scores, valid_solutions_count, invalid_solutions_count


def plot_histogram(experiment_scores, valid_solutions_count, invalid_solutions_count, num_experiments):
    # Create histogram
    plt.hist(experiment_scores, bins=30, color='blue', alpha=0.7)
    
    
    plt.title('Distribution of Solution Costs')
    plt.xlabel('Cost')
    plt.ylabel('Frequency')
    plt.ylim(0, num_experiments) 

    # displaying counts of valid and invalid solutions
    plt.text(0.95, 0.95, f'Valid solutions: {valid_solutions_count}\nInvalid solutions: {invalid_solutions_count}',
             horizontalalignment='right',
             verticalalignment='top',
             transform = plt.gca().transAxes)

    # Show the plot
    plt.show()



