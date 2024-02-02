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



def plot_smoothed_histogram(algorithms, districts):
    plt.figure(figsize=(10, 6))
    
    for algorithm in algorithms:
        all_scores = []
        for district in districts:
            csv_filename = f"results/resultaten_{algorithm}_district2.csv"
            scores = load_scores_from_csv(csv_filename)
            all_scores.extend(scores)
        
        sns.kdeplot(all_scores, bw_adjust=1, label=f"{algorithm}")
    
    plt.title(f'Cost Distribution Across Algorithms')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()
    #plt.show()
    plt.savefig('results/cost_distribution_all_algorithms')