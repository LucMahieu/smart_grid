from code.algorithms.algorithm import Baseline, Greedy
from code.algorithms.hill_climber import HillClimber
from code.classes.district import District
from code.classes.battery import Battery
import time
import subprocess
import csv


def run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration):
    """
    Run experiments with algorithms and limit the total duration of experiments to 'max_duration'.
    """
    start = time.time()
    total_experiment_duration = 0
    experiment_results = []
    all_scores = []
    run_number = 0

    # Continue until max duration is reached 
    while total_experiment_duration < max_duration:
        run_start_time = time.time()

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

        run_end_time = time.time()
        run_duration = run_end_time - run_start_time
        total_experiment_duration += run_duration

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