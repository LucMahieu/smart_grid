import seaborn as sns
import matplotlib.pyplot as plt
# from ..algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
from code.visualization.visualize_results import load_scores_from_csv
import numpy as np


def collect_experiment_results(district, algorithm):
    """
    Collects experiment results for each algorithm and district.
    """
    data = []
    csv_filename = f"./resultaten_{algorithm}_district{district.name}.csv"
    scores = load_scores_from_csv(csv_filename)
    data.append((scores, algorithm))

    return data

def plot_smoothed_histogram(*data):
    """ 
    Plots a smoothed histogram of cost distribution of each algorithm in one plot.
    """
    for costs, label in data:
        sns.kdeplot(costs, label=label, bw_adjust=0.5)

    plt.title('Cost Distribution of Different Algorithms')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    plt.ylim(0, 8)
    plt.savefig('results/smoothedhistogram.png')

    # Show and save plot
    plt.show()
    plt.savefig(f'smoothed_histogram_district{district.name}.png')

