import matplotlib.pyplot as plt
import csv
import numpy as np


def load_scores_from_csv(csv_filename):
    """
    Read given csv file and save cost.
    """
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

    return scores


def plot_score_distribution(scores, algorithm_name):
    """
    Plots the distribution of costs of each algorithm.
    """
    if scores:
        print(f"Number of experiments: {len(scores)}")
        print(f"Mean score: {np.mean(scores)}")
        print(f"Standard deviation: {np.std(scores)}")
        print(f"Min score: {np.min(scores)}")
        print(f"Max score: {np.max(scores)}")

        # Maak een histogram van de scores
        plt.hist(scores, bins=30, color='blue', alpha=0.7)
        plt.title(f'Distribution of costs {algorithm_name}')
        plt.xlabel('Cost')
        plt.ylabel('Frequency')
        plt.show()
        plt.savefig(f'Cost distribution_of_{algorithm_name}')

    else:
        print("No valid solution")
