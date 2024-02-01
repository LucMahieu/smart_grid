from code.algorithms.algorithm import Baseline, Greedy
from code.algorithms.hill_climber import HillClimber
from code.classes.district import District
from code.classes.battery import Battery
import time
import subprocess
import csv


def run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration):
    """
    Run experiments with algorithms for X iterations.
    """
    start = time.time()
    total_experiment_duration = 0
    experiment_results = []
    all_costs = []
    lowest_cost = float('inf')
    best_hill_climber_solution = None
    best_district_solution = None

    # Continue until max duration is reached
    for _ in range(iterations):
        print(f"iterations: {_}")

        if isinstance(algorithm_instance, HillClimber):
            algorithm_instance.run()
            cost = district.district_cost_shared
            
            # Saves the best solution in the form of an object with attributes
            if cost <= lowest_cost:
                # Copy the attributes of the best solution
                best_hill_climber_solution = vars(algorithm_instance).copy()
                best_district_solution = vars(district).copy()
                lowest_cost = cost
                print(f'district_cost: {district.district_cost_shared}')
                district.district_cost_shared = 0
                print(f'district_cost na op nul zetten: {district.district_cost_shared}')
            
            # Reset state of district after each run
            district.reset_state()
            # Reset HillClimber attributes
            algorithm_instance.__init__(district)

        # Greedy and Baseline
        else:
            algorithm_instance.run(district)
            cost = district.shared_costs()
        
        all_costs.append(cost)

        experiment_results.append({
            'algorithm': algorithm_name,
            'run_number': run_number,
            'run_duration': run_duration,
            'cost': cost
        })

    return experiment_results, all_costs, best_hill_climber_solution, best_district_solution


def save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename):
    """
    Saves algorithm, run_number, run_duration, iterations, cost to a CSV file for each algorithm.
    """

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['algorithm', 'run_number', 'run_duration', 'iterations', 'cost']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in experiment_results:
            writer.writerow(result)

    print(f"Results saved in {csv_filename}")