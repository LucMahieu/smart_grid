from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from experiments.experiment import run_experiments, save_experiment_results_to_csv
from code.visualization.visualize_results import plot_score_distribution
from code.algorithms.hill_climber import HillClimber
from code.visualization.hill_climber_visualizer import plot_hillclimber_solution
from code.visualization.visualizecost import plot_smoothed_histogram
import random
import matplotlib.pyplot as plt

# Create districts from files with batteries and houses
district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

districts = [district1, district2, district3]

hill = HillClimber(district1)
hill.run()

# plot_hillclimber_solution(vars(district1), vars(hill))

# iterations = 10

# for district in districts:
#     saved_best_hill_climber_solutions = []
#     data = [] # Reset data for each district
#     for algorithm_class in [HillClimber, Greedy, Baseline]: #Greedy, Baseline, 
#         algorithm_name = algorithm_class.__name__
#         print(f"Uitvoeren van {algorithm_name} op district {district.name}")

#         # Create an instance of the algorithm
#         if algorithm_class == HillClimber:
#             algorithm_instance = algorithm_class(district)
#         else:
#             algorithm_instance = algorithm_class()
        
#         experiment_results, scores, best_hill_climber_solution, best_district_solution \
#             = run_experiments(algorithm_instance, algorithm_name, district, iterations)
        
#         csv_filename = f"results_of_{algorithm_name}_district{district.name}.csv"
#         save_experiment_results_to_csv(experiment_results, csv_filename)
        
#         data.append((scores, algorithm_name))

#         # Checks if it is a hill climber run and saves the solution attributes
#         if best_hill_climber_solution != None:
#             print(f"Saving best hill climber solution: {best_hill_climber_solution}")
#             saved_best_hill_climber_solution = best_hill_climber_solution
#             saved_district = best_district_solution

#             # Plot the end result of the hill climber
#             plot_hillclimber_solution(saved_district, saved_best_hill_climber_solution)
        
#         # Plot the distribution of costs for each algorithm
#         plot_score_distribution(scores, algorithm_name)

#     plot_smoothed_histogram(district, data)
    



