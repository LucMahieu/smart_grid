import random
from code.classes.district import District
from code.algorithms.algorithm import Baseline
from code.algorithms.algorithm import Greedy
from code.classes.battery import Battery 
import matplotlib.pyplot as plt
import time 
import subprocess
import csv
import numpy as np
import matplotlib.pyplot as plt


# def run_experiment(district, algorithm_class, num_experiments):
#     best_solution_cost = float('inf')
#     worst_solution_cost = float('-inf')
#     experiment_scores = []
#     valid_solutions_count = 0
#     invalid_solutions_count = 0

#     for _ in range(num_experiments):
#         # Reset the district to its initial state before each experiment
#         print(f"Before reset: {district.district_cost_shared}")
#         district.reset_state()
#         print(f"After reset: {district.district_cost_shared}")
#         # Create an instance of the algorithm and run it
#         algorithm_instance = algorithm_class()
#         valid_solution = algorithm_instance.run(district)

#         # Calculate the shared cost for this iteration
#         current_cost = district.shared_costs()
#         print(f"Current cost for this run: {current_cost}")

#         if current_cost is not None:
#             best_solution_cost = min(best_solution_cost, current_cost)
#             worst_solution_cost = max(worst_solution_cost, current_cost)
#             valid_solutions_count += 1
#         else:
#             invalid_solutions_count += 1

#         # Append the current cost to the experiment_scores list
#         experiment_scores.append(current_cost if current_cost is not None else 0)

#     return best_solution_cost, worst_solution_cost, experiment_scores, valid_solutions_count, invalid_solutions_count


from code.algorithms.hill_climber_test import HillClimber
from code.algorithms.algorithm import Greedy, Baseline





"""
Run experiments with algorithms and limit the total duration of experiments to 'max_duration'.
"""
def run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration):
    start = time.time()
    total_experiment_duration = 0
    experiment_results = []
    all_scores = []
    run_number = 0


    while total_experiment_duration < max_duration:
        run_start_time = time.time()

        if isinstance(algorithm_instance, HillClimber):
            algorithm_instance.run()
        else:
            algorithm_instance.run(district)
        run_end_time = time.time()
        run_duration = run_end_time - run_start_time
        total_experiment_duration += run_duration

        cost = district.shared_costs()
        all_scores.append(cost)

        experiment_results.append({
            'algorithm': algorithm_name,
            'run_number': run_number,
            'run_duration': run_duration,
            'cost': cost
        })

        if total_experiment_duration >= max_duration:
            break

    total_duration = time.time() - start
    best_score = min(all_scores) if all_scores else None

    return experiment_results, total_duration, all_scores, best_score


"""
Save experiment results to a CSV file.
"""
def save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename):
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['algorithm', 'run_number', 'run_duration', 'iterations', 'cost']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in experiment_results:
            writer.writerow(result)
    
    print(f"Resultaten opgeslagen in {csv_filename}")
