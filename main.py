from typing import Any
from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from archive.export_json import export_json
from code.visualization.visualizegrid import visualize_grid as vg
from code.visualization import visualizecost as vc
from experiments.experiment import save_experiment_results_to_csv
from code.visualization.visualize_results import load_scores_from_csv, plot_score_distribution
from code.algorithms.hill_climber import HillClimber
from code.visualization.hill_climber_visualizer import plot_hillclimber_solution
from experiments.experiment import run_timed_experiments
import random
import matplotlib.pyplot as plt
import csv


if __name__ == "__main__":
    # Create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    districts = [district1, district2, district3]
    
    max_duration = 10

    # Looping through districts
    for district in districts:
        # Looping through algorithms
        for algorithm_class in [HillClimber, Greedy, Baseline]:
            algorithm_name = algorithm_class.__name__
            print(f"Run {algorithm_name} in district {district.name}")

            if algorithm_class == HillClimber:
                algorithm_instance = algorithm_class(district)
            else:
                algorithm_instance = algorithm_class()

            # Runs the experiments   
            experiment_results, total_duration, all_scores, best_score = run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration)

            #Saves results of each algorithm in each district in a CSV file
            csv_filename = f"results/resultaten_{algorithm_name}_district{district.name}.csv"
            save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename)

            # retrieving the costs
            scores = []
            with open(csv_filename, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader, None)
                for row in csv_reader:
                    try:
                        score = float(row[4])
                        scores.append(score)
                    except ValueError:
                        continue

            # Pick name of algoritm from file
            algorithm_name = csv_filename.split("_")[1].split(".")[0]  
            district_name = csv_filename.split("_")[2].split(".")[0]


            scores = load_scores_from_csv(csv_filename)

            # Plots cost distribution of each algorithm
            plot_score_distribution(scores, algorithm_name, district_name)

    # visualizes the grid of Greedy and Baseline
    for district in districts:
        for algorithm_class in [Greedy, Baseline]:
            R = algorithm_class()
            R.run(district)
            output = export_json(district)
            vg(output)

    # visualizes the grid of Hillclimber
    for district in districts:
        R = HillClimber(district)
        R.run()
        output = export_json(district)
        plot_hillclimber_solution(district, R)
            

                    

