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
from export_json import export_json

if __name__ == "__main__":
    # Create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    districts = [district1, district2, district3]


max_duration = 10



# for algorithm in [HillClimber]:
#     algorithm_name = algorithm.__class__.__name__
#     print(f"Uitvoeren van {algorithm_name}")

#     experiment_results, total_duration, all_scores, best_score = run_timed_experiments([algorithm], district1, max_duration)   
#     csv_filename = f"resultaten_{algorithm_name}.csv"
#     save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename)

#     # Lees de scores in vanuit het CSV-bestand
#     scores = []
#     with open(csv_filename, mode='r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader, None)

#         for row in csv_reader:
#             try:
#                 score = float(row[4])
#                 scores.append(score)
#             except ValueError:
#                 continue

#     csv_filename = f"resultaten_{algorithm_name}.csv"


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
    #plot_score_distribution(scores, algorithm_name)


    #vg.visualize_grid(output)



#     # # connect houses with batteries in a district

#     # for battery in district1.batteries:
#     #     print(battery.capacity)


#     # export the results to a json file
    # output = export_json(district1)


    #output = export_json(district1)
    
    #vg(output)
    #vg(output)
    # district1.shared_costs()
    # print(district1.district_cost_shared)

    # for battery in district1.batteries:
    #     print(battery.capacity)

    # print(district1.houses[-1].max_output)

#     # num_experiments = 1000

#     # best_cost, worst_cost, scores, valid_count, invalid_count = run_experiment(district1, Greedy_algo, num_experiments)
#     # plot_histogram(scores, valid_count, invalid_count, num_experiments)


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #ARCHIVE

#     #print(district1.battery_houses_connections)

#     # district1.own_costs()
#     # print(district1.district_cost_seperate)

#     # for house in district1.houses:
#     #     if house.battery is None:
#     #         print(f"house at ({house.pos_x}, {house.pos_y}) does not have a battery assigned")
#     #     if not house.cables:
#     #         print(f"house at ({house.pos_x}, {house.pos_y}) does not have proper cable routes")
#     # # Run experiments
#     # num_experiments = 30
#     # best_cost, worst_cost, experiment_costs = run_experiment(district3, Greedy_algo, num_experiments)

#     # # Print the results from experiments
#     # print(f"Best solution cost: {best_cost}")
#     # print(f"Worst solution cost: {worst_cost}")
#     # print(f"All experiment scores: {scores}")

#     # plot for baseline
#     # plot_experiment_costs(experiment_costs)

    # num_experiments = 1000

    # Run experiments for each algorithm
    #costs_greedy = [cost for cost in run_experiment(district3, Greedy_algo, num_experiments)[2] if cost > 0]
    #costs_baseline = [cost for cost in run_experiment(district1, Baseline, num_experiments)[2] if cost > 0]

#     # plot_smoothed_histogram(
#     #     (costs_greedy, "Greedy Algo"),
#     #     (costs_greedy2, "Greedy Algo 2"),
#     #     (costs_baseline, "Baseline"),
#     #     (costs_baseline2, "Baseline 2")
#     # )

    # best_cost, worst_cost, scores, valid_count, invalid_count = run_experiment(district1, Baseline, num_experiments)
    # plot_histogram(scores, valid_count, invalid_count, num_experiments)

# #     visualize_grid(output)

# # #     #print(District.own_costs())

# #     visualize_costs(output)


# # if __name__ == "__main__":
# #     # Create districts
# #     districts = [
# #         District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv"),
# #         District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv"),
# #         District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")
# #     ]

# #     total_cost = 0
# #     for district in districts:
# #         # Run algorithm for each district
# #         R = Greedy_algo()
# #         R.run(district)

# #         # Calculate shared costs
# #         district.shared_costs()
# #         print(f"Cost for District {district.id}: {district.district_cost_shared}")
# #         total_cost += district.district_cost_shared

# #         # Export results to JSON
# #         export_json(district)

# #         # Run experiments
# #         best_cost, worst_cost, experiment_costs = run_experiment(district, Random_algo, num_experiments)
# #         print(f"Best solution cost for District {district.id}: {best_cost}")
# #         print(f"Worst solution cost for District {district.id}: {worst_cost}")

# #         # Plot experiment costs
# #         plot_experiment_costs(experiment_costs)

# #     print(f"Total cost for all districts: {total_cost}")
    
    #from visualization.visualizegrid import visualize_grid
# from algorithms.experiments import run_experiment
# from algorithms.experiments import plot_histogram
# from visualization.visualizecost import plot_smoothed_histogram
# from visualization.visualizecost import run_experiment_and_measure_time
# import time
# from visualization.visualizecost import plot_time_and_cost
# from visualization.visualizecost import plot_cost_range
#from algorithms.hill_climber_test import HillClimber
# from algorithms.experiments import run_experiments_and_save_results
# from algorithms.experiments import run_timed_experiments
    #from code.algorithms import greedy as gr
#from code.algorithms.hill_climber import HillClimber as hc