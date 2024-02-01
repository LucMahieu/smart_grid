import matplotlib.pyplot as plt
import csv
import numpy as np


def load_scores_from_csv(csv_filename):
    """
    Read given csv file and return list of cost values.
    """
    scores = []
    with open(csv_filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)

        for row in csv_reader:
            print(f"Row: {row}")
            score = float(row[2])
            scores.append(score)

    return scores


def plot_score_distribution(scores, algorithm_name, district_name):
    """
    Plots the distribution of costs of each algorithm.
    """
    if scores:
        # Print basic statistics
        print(f"Number of experiments: {len(scores)}")
        print(f"Mean score: {round(np.mean(scores), 1)}")
        print(f"Standard deviation: {round(np.std(scores), 1)}")
        print(f"Min score: {np.min(scores)}")
        print(f"Max score: {np.max(scores)}")

        # Make a histogram of the scores
        plt.hist(scores, bins=30, color='blue', alpha=0.7)
        plt.title(f'Distribution of costs {algorithm_name}')
        plt.xlabel('Cost')
        plt.ylabel('Frequency')
        #plt.show()


        # Save the plot
        #plt.figure()
        plt.savefig(f'results/Cost distribution_of_{algorithm_name}_of_{district_name}')
        plt.close()


    # If there is no cost, solution is not valid
    else:
        print("No valid solution")

