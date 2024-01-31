import seaborn as sns
import matplotlib.pyplot as plt
from code.algorithms.algorithm import Greedy, Baseline
from code.classes.district import District
import time
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


def plot_smoothed_histogram(district, *data):
    """
    Plots a smoothed histogram of cost distribution for a specific district.
    """
    plt.figure(figsize=(10, 6))
    for costs, label in data:
        sns.kdeplot(costs, label=label, bw_adjust=1)
    
    plt.title(f'Cost Distribution in District {district.name}')
    plt.xlabel('Cost')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    plt.savefig(f'smoothed_histogram_district{district.name}.png')







def run_experiment_and_measure_time(district, algorithm_class, num_experiments):
    """
    Runs experiment and measures the duration and the cost.
    """
    costs = []
    times = []

    for _ in range(num_experiments):
        # Reset the district to its initial state before each experiment
        district.reset_state()

        # Measure start time
        start_time = time.time()

        # Create an instance of the algorithm and run it
        algorithm_instance = algorithm_class()
        algorithm_instance.run(district)

        # Measure end time
        end_time = time.time()

        # Calculate the shared cost for this iteration
        current_cost = district.shared_costs()

        # Store the cost and time
        costs.append(current_cost if current_cost is not None else 0)
        times.append(end_time - start_time)

    return costs, times


def plot_time_and_cost(costs_data, times_data):
    """
    Plots a comparison of the duration and the cost of the algorithms.
    """
    n_groups = len(costs_data)
    fig, ax = plt.subplots()

    # Calculate bar positions
    index = np.arange(n_groups)
    bar_width = 0.35

    # Plotting costs
    costs = [data[0] for data in costs_data]
    ax.bar(index, costs, bar_width, label='Cost', alpha=0.7)

    # Plotting times
    times = [data[0] for data in times_data]
    ax.bar(index + bar_width, times, bar_width, label='Time', alpha=0.7)

    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Values')
    ax.set_title('Cost and Time Comparison of Algorithms')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels([data[1] for data in costs_data])
    ax.legend()

    # Set y-axis to logarithmic scale
    ax.set_yscale('log')

    plt.tight_layout()
    plt.show()
    plt.savefig('timeandcost.png')
