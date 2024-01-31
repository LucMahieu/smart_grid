from typing import Any
from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from archive.export_json import export_json
from code.visualization.visualizegrid import visualize_grid as vg
from code.visualization import visualizecost as vc
from experiments.experiment import run_timed_experiments, save_experiment_results_to_csv
from code.visualization.visualize_results import load_scores_from_csv, plot_score_distribution, plot_histogram_valid_solutions
from code.algorithms.hill_climber import HillClimber
from code.visualization.hill_climber_visualizer import plot_hillclimber_solution
from code.visualization.visualizecost import plot_smoothed_histogram
import random

import matplotlib.pyplot as plt
import time 
import subprocess
import csv


if __name__ == "__main__":
    # Create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    districts = [district1, district2, district3]

    max_duration = 10
    num_experiments = 100
    algorithms = ['Greedy', 'Baseline', 'HillClimber']

    run_timed_experiments(districts, algorithms, num_experiments, max_duration)

    save_experiment_results_to_csv(districts, algorithms, num_experiments)
    load_scores_from_csv("resultaten_Greedy_district1.csv")
    plot_histogram_valid_solutions(districts, algorithms, num_experiments)
    plot_score_distribution(districts, algorithms, num_experiments)
    plot_smoothed_histogram(districts, algorithms, num_experiments) #TODO: 
    plot_hillclimber_solution(districts, algorithms, num_experiments)
        



