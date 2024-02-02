from code.algorithms.algorithm import Baseline, Greedy
from code.algorithms.hill_climber import HillClimber
from code.classes.district import District
from code.classes.battery import Battery
import time
import subprocess
import csv


def run_experiments(algorithm_instance, algorithm_name, district, num_experiments):
    experiment_results = []
    all_scores = []

    for _ in range(num_experiments):
        district.reset_state()

        # Run the algorithm
        if isinstance(algorithm_instance, HillClimber):
            # For HillClimber, no district argument is needed
            algorithm_instance.run()
            # Use district_cost_shared for HillClimber
            cost = district.district_cost_shared
        else:
            # For Greedy and Baseline, use district as an argument
            algorithm_instance.run(district)
            # Use shared_costs for Greedy and Baseline
            cost = district.shared_costs()
        
        all_scores.append(cost)

        experiment_results.append({
            'algorithm': algorithm_name,
            'cost': cost
        })

    best_score = min(all_scores) if all_scores else None

    return experiment_results, all_scores, best_score



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