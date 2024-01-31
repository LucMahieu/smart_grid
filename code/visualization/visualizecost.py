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
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar([0, 1], [highest_cost, lowest_cost], color=['red', 'green'], alpha=0.7)
    plt.xticks([0, 1], ['Highest Cost', 'Lowest Cost'])
    plt.ylabel('Cost')
    plt.title(f'Cost Range for {label}')
    plt.ylim(0, highest_cost * 1.1)
    plt.show()


def collect_experiment_results(district, algorithm):
    """
    Collects experiment results for each algorithm and district.
    """
    data = []
    csv_filename = f"./resultaten_{algorithm}_district{district.name}.csv"
    scores = load_scores_from_csv(csv_filename)
    data.append((scores, algorithm))

    return data


def plot_smoothed_histogram(district, algorithm):
    """
    Plots a smoothed histogram of cost distribution for a specific district.
    """
    data = collect_experiment_results(district, algorithm)
    plt.figure(figsize=(10, 6))
    for costs, algorithm in data:
        sns.kdeplot(costs, label=algorithm, bw_adjust=1)
    
    plt.title(f'Cost Distribution in District {district.name}')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    plt.savefig(f'smoothed_histogram_district{district.name}.png')


district1 = District(1, "./data/district_1/district-1_batteries.csv", "./data/district_1/district-1_houses.csv")
plot_smoothed_histogram(district1, 'Greedy')


def plot_histogram_valid_solutions(algorithm_instance, num_experiments):
    """ 
    Creates two plots, one showing the cost distribution for valid solutions, 
    and one showing the count of valid and invalid solutions.
    """
    # Run the algorithm and collect the experiment scores
    experiment_scores = []
    valid_solutions_count = 0
    invalid_solutions_count = 0

    for _ in range(num_experiments):
        algorithm_instance.run()
        cost = algorithm_instance.district.shared_costs()
        experiment_scores.append(cost)

        if algorithm_instance.district.is_valid_solution():
            valid_solutions_count += 1
        else:
            invalid_solutions_count += 1

    # Create histogram
    plt.hist(experiment_scores, bins=30, color='blue', alpha=0.7)

    plt.title('Distribution of Solution Costs')
    plt.xlabel('Cost')
    plt.ylabel('Frequency')
    plt.ylim(0, num_experiments)

    # Display counts of valid and invalid solutions
    plt.text(0.95, 0.95, f'Valid solutions: {valid_solutions_count}\nInvalid solutions: {invalid_solutions_count}',
             horizontalalignment='right',
             verticalalignment='top',
             transform=plt.gca().transAxes)

    # Show the plot
    plt.show()
    plt.savefig('validsolutions.png')

