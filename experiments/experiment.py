from code.algorithms.algorithm import Baseline, Greedy
from code.algorithms.hill_climber import HillClimber
from code.classes.district import District
from code.classes.battery import Battery
import subprocess
import csv


def run_experiments(algorithm_instance, algorithm_name, district, iterations):
    """
    Run experiments with algorithms and limit the total duration of experiments to 'max_duration'.
    """
    experiment_results = []
    all_scores = []

    # Continue until max duration is reached 
    for _ in range(iterations):

        # HillClimber
        if isinstance(algorithm_instance, HillClimber):
            algorithm_instance.run()
            cost = district.district_cost_shared
            # Reset state of district after each run
            district.reset_state()
            # Reset HillClimber attributes
            algorithm_instance.__init__(district)

        # Greedy and Baseline
        else:
            algorithm_instance.run(district) 
            cost = district.shared_costs()
        
        all_scores.append(cost)

        experiment_results.append({
            'algorithm': algorithm_name,
            'iterations': iterations,
            'cost': cost
        })

    best_score = min(all_scores) if all_scores else None

    return experiment_results, all_scores, best_score


def save_experiment_results_to_csv(experiment_results, csv_filename):
    """
    Save experiment results to a CSV file.
    """
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['algorithm', 'iterations', 'cost']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for result in experiment_results:
            writer.writerow(result)
    
    print(f"Results saved in {csv_filename}")