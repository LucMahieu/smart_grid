# import matplotlib.pyplot as plt
# import json

# def visualize_costs(output):
#     """
#     Visualize and save the costs for different random scenarios.

#     Parameters:
#     - output: Output dictionary containing information about districts.
#     """
#     costs = []

#     if 'batteries' in output and isinstance(output['batteries'], list):
#         for battery_entry in output['batteries']:
#             if 'costs-shared' in battery_entry:
#                 costs.append(battery_entry['costs-shared'])

#     print("Costs:", costs)

#     plt.bar(range(1, len(costs) + 1), costs, color='blue')
#     plt.xlabel('Battery')
#     plt.ylabel('Cost')
#     plt.title(f'District {output["district"]} Cost Comparison')
#     plt.savefig('district_costs_visualization.png')
#     plt.show()

# # Example usage:
# # Load the output from the generated "output.json" file
# with open('output.json', 'r') as infile:
#     output_data = json.load(infile)

# visualize_costs(output_data)

import seaborn as sns
import matplotlib.pyplot as plt
from algorithms.randomize import Random_algo
from algorithms.greedy import Greedy_algo
from algorithms.greedy2 import Greedy_algo2
from algorithms.baseline import Baseline
from algorithms.baseline2 import Baseline2
from classes.district import District
from algorithms.experiments import run_experiment

def plot_smoothed_histogram(*data):
    for costs, label in data:
        sns.kdeplot(costs, label=label, bw_adjust=0.5)
    plt.title('Cost Distribution of Different Algorithms')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    plt.ylim(0, 8)

if __name__ == "__main__":
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    num_experiments = 10

    # Run experiments for each algorithm and collect costs
   
    _, _, costs_greedy, _, _ = run_experiment(district1, Greedy_algo, num_experiments)
    _, _, costs_greedy2, _, _ = run_experiment(district1, Greedy_algo2, num_experiments)
    _, _, costs_baseline, _, _ = run_experiment(district1, Baseline, num_experiments)
    _, _, costs_baseline2, _, _ = run_experiment(district1, Baseline2, num_experiments)

    # Plot all results in one smoothed histogram
    plot_smoothed_histogram(
        (costs_greedy, "Greedy Algo"),
        (costs_greedy2, "Greedy Algo 2"),
        (costs_baseline, "Baseline"),
        (costs_baseline2, "Baseline 2")
    )
