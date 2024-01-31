from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from archive.export_json import export_json
from code.visualization.visualizegrid import visualize_grid as vg
from code.visualization import visualizecost as vc
from experiments.experiment import run_timed_experiments, save_experiment_results_to_csv
from code.visualization.visualize_results import load_scores_from_csv, plot_score_distribution, plot_histogram_valid_solutions
from code.algorithms.hill_climber import HillClimber
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

    R = Greedy()
    R.run(district1)
    output = export_json(district1)
    vg(output)


    max_duration = 10





<<<<<<< HEAD
    for district in districts:
        for algorithm_class in [Baseline, Greedy, HillClimber]:
            algorithm_name = algorithm_class.__name__
            print(f"Uitvoeren van {algorithm_name} op district {district.name}")

            if algorithm_class == HillClimber:
                algorithm_instance = algorithm_class(district)
            else:
                algorithm_instance = algorithm_class()
                
            experiment_results, total_duration, all_scores, best_score = run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration)

            csv_filename = f"resultaten_{algorithm_name}_district{district.name}.csv"
            save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename)

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


        algorithm_name = csv_filename.split("_")[1].split(".")[0]  # Haal de naam van het algoritme uit het bestand

        scores = load_scores_from_csv(csv_filename)
        plot_score_distribution(scores, algorithm_name)
=======
# for district in districts:
#     for algorithm_class in [Greedy, Baseline]:
#         algorithm_name = algorithm_class.__name__
#         print(f"Uitvoeren van {algorithm_name} op district {district.name}")

#         if algorithm_class == HillClimber:
#             algorithm_instance = algorithm_class(district)
#         else:
#             algorithm_instance = algorithm_class()
            
#         experiment_results, total_duration, all_scores, best_score = run_timed_experiments(algorithm_instance, algorithm_name, district, max_duration)

#         csv_filename = f"resultaten_{algorithm_name}_district{district.name}.csv"
#         save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename)

#         scores = []
#         with open(csv_filename, mode='r') as csv_file:
#             csv_reader = csv.reader(csv_file)
#             next(csv_reader, None)
#             for row in csv_reader:
#                 try:
#                     score = float(row[4])
#                     scores.append(score)
#                 except ValueError:
#                     continue


#     algorithm_name = csv_filename.split("_")[1].split(".")[0]  # Haal de naam van het algoritme uit het bestand

#     scores = load_scores_from_csv(csv_filename)
    #plot_score_distribution(scores, algorithm_name)

for district in districts:
    for algorithm_name in ["Greedy", "Baseline", "HillClimber"]:
        csv_filename = f"resultaten_{algorithm_name}_district{district.name}.csv"

        try:
            scores = load_scores_from_csv(csv_filename)
            plot_score_distribution(scores, algorithm_name)
        except FileNotFoundError:
            print(f"Bestand {csv_filename} niet gevonden, overslaan van dit bestand.")



    #vg.visualize_grid(output)
>>>>>>> c4a278a (update)




#    






    
   
    # district1.shared_costs()
    # print(district1.district_cost_shared)

    # for battery in district1.batteries:
    #     print(battery.capacity)

    # print(district1.houses[-1].max_output)

#     # num_experiments = 1000

#     # best_cost, worst_cost, scores, valid_count, invalid_count = run_experiment(district1, Greedy, num_experiments)
#     # plot_histogram(scores, valid_count, invalid_count, num_experiments)

