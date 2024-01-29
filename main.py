from archive import baseline as bs
#from code.algorithms import greedy as gr
from code.algorithms import hill_climber as hc
from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from export_json import export_json
#from code.visualization import visualizegrid as vg
#from code.visualization import visualizecost as vc
from experiments.experiments import run_timed_experiments, save_experiment_results_to_csv
import random
import matplotlib.pyplot as plt
import time 
import subprocess
import csv
from visualization.visualizegrid import visualize_grid
from algorithms.baseline import Baseline
# from algorithms.experiments import run_experiment
# from algorithms.experiments import plot_histogram
# from visualization.visualizecost import plot_smoothed_histogram
# from visualization.visualizecost import run_experiment_and_measure_time
# import time
# from visualization.visualizecost import plot_time_and_cost
# from visualization.visualizecost import plot_cost_range
from algorithms.hill_climber_test import HillClimber
# from algorithms.experiments import run_experiments_and_save_results
# from algorithms.experiments import run_timed_experiments
from check50_export_json import export_json

if __name__ == "__main__":
    # Create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    # Create hill climber algorithm object
    #hill_climber = hc.HillClimber(district1)

    # Run hill climber algorithm
    #hill_climber.run(district1.houses)

 

    # Maximale duur van de experimenten in seconden
    # algorithms = [gr.Greedy, bs.Baseline]

    # # Maximum duration of the experiments in seconds
    # max_duration = 10

    # # Run experiments and save the results to a CSV file
    # experiment_results, total_duration, all_scores, best_score = run_timed_experiments(algorithms, district1, max_duration)
    # csv_filename = "scores.csv"
    # save_experiment_results_to_csv('Greedy', greedy_results, total_duration_greedy, all_scores_greedy)
    # save_experiment_results_to_csv('Baseline', baseline_results, total_duration_baseline, all_scores_baseline)
    max_duration = 20
    
    for algorithm in [gr.Greedy, bs.Baseline]:
        algorithm_name = algorithm.__name__
        
        # Voer experimenten uit
        experiment_results, total_duration, all_scores, best_score = run_timed_experiments([algorithm], district1, max_duration)
        
        # Sla resultaten op in een CSV-bestand
        csv_filename = f"resultaten_{algorithm_name}.csv"
        save_experiment_results_to_csv(algorithm_name, experiment_results, total_duration, all_scores, csv_filename)
    # # check if the cable routes indeed connect the houses with the batteries and if the cable stays on the grid
    # for battery in district1.batteries:
    #     for house in district1.battery_houses_connections[battery]:
    #         # print house and battery positions and the cable route between them
    #         print('\n\n\n')
    #         # xprint(f'House: {house.pos_x, house.pos_y} \nCable route: {house.cables}')
    #         #print(f'Battery: {battery.pos_x, battery.pos_y}')

    # # connect houses with batteries in a district

    # for battery in district1.batteries:
    #     print(battery.capacity)

    R = Baseline()
    R.run(district1)
    # R = bs.Baseline()
    # R.run(district1)
    print(district1.shared_costs())

    # # Create hill climber algorithm object
    # hill_climber = hc.HillClimber(district1)

    # # Run hill climber algorithm
    # hill_climber.run(district1.houses)

    # algorithms = {
    #     'Greedy': gr.Greedy(),
    #     'Baseline': bs.Baseline(),
    #     'HillClimber': hc.HillClimber()
    # }

#     max_duration = 3600  
#     max_run_time = 60    

#     experiment_results, total_duration = run_timed_experiments(algorithms.values(), district1, max_duration, num_experiments)

#     csv_filename = "experiment_results.csv"
#     save_experiment_results_to_csv(experiment_results, total_duration, csv_filename)    # connect houses with batteries in a district
    
#     # # check if the cable routes indeed connect the houses with the batteries and if the cable stays on the grid
#     # for battery in district1.batteries:
#     #     for house in district1.battery_houses_connections[battery]:
#     #         # print house and battery positions and the cable route between them
#     #         print('\n\n\n')
#     #         # xprint(f'House: {house.pos_x, house.pos_y} \nCable route: {house.cables}')
#     #         #print(f'Battery: {battery.pos_x, battery.pos_y}')

#     # # connect houses with batteries in a district

#     # for battery in district1.batteries:
#     #     print(battery.capacity)


#     # export the results to a json file
    # output = export_json(district1)


    output = export_json(district1)
    
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
    costs_baseline = [cost for cost in run_experiment(district1, Baseline, num_experiments)[2] if cost > 0]

#     # plot_smoothed_histogram(
#     #     (costs_greedy, "Greedy Algo"),
#     #     (costs_greedy2, "Greedy Algo 2"),
#     #     (costs_baseline, "Baseline"),
#     #     (costs_baseline2, "Baseline 2")
#     # )

    best_cost, worst_cost, scores, valid_count, invalid_count = run_experiment(district1, Baseline, num_experiments)
    plot_histogram(scores, valid_count, invalid_count, num_experiments)

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
