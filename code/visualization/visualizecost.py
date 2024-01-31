import seaborn as sns
import matplotlib.pyplot as plt
# from ..algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from code.visualization.visualize_results import load_scores_from_csv
import numpy as np

def plot_cost_range(costs, label):
    """
    Plots highest and lowest cost of an algorithm.
    """
    highest_cost = max(costs)
    lowest_cost = min(costs)
    
    # Set plot properties
    plt.figure(figsize=(10, 6))
    plt.bar([0, 1], [highest_cost, lowest_cost], color=['red', 'green'], alpha=0.7)
    plt.xticks([0, 1], ['Highest Cost', 'Lowest Cost'])
    plt.ylabel('Cost')
    plt.title(f'Cost Range for {label}')
    plt.ylim(0, highest_cost * 1.1)

    # Show plot
    plt.show()


def collect_experiment_scores(district, algorithm):
    """
    Collects experiment results for each algorithm and district.
    """
    csv_filename = f"./results_of_{algorithm}_district{district.name}.csv"
    scores = load_scores_from_csv(csv_filename)

    return scores


def plot_smoothed_histogram(district, data):
    """
    Plots a smoothed histogram of cost distribution for a specific district.
    """
    plt.figure(figsize=(10, 6))
    for costs, label in data:
        sns.kdeplot(costs, label=label)
    
    # Set plot properties
    plt.title(f'Cost Distribution in District {district.name}')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()

    # Show and save plot
    plt.show()
    plt.savefig(f'smoothed_histogram_district{district.name}.png')


