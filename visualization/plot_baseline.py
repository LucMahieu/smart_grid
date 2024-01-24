# import matplotlib.pyplot as plt

# def plot_experiment_costs(experiment_costs):
#     plt.figure(figsize=(12, 6))
    
#     # Create a list of experiment indices for the x-axis
#     experiment_indices = range(1, len(experiment_costs) + 1)
    
#     plt.bar(experiment_indices, experiment_costs, color='skyblue', edgecolor='black')
    
#     plt.title('Costs of Each Experiment')
#     plt.xlabel('Experiment Index')
#     plt.ylabel('Costs')
    
#     plt.show()

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_experiment_costs(experiment_costs):
    plt.figure(figsize=(10, 6))
    
    # Count the frequency of each unique cost
    from collections import Counter
    cost_counts = Counter(experiment_costs)
    
    # Extract unique costs and their frequencies
    unique_costs = list(cost_counts.keys())
    frequencies = list(cost_counts.values())
    
    # Create the histogram
    plt.bar(unique_costs, frequencies, color='skyblue', edgecolor='black')
    
    plt.title('Histogram of Experiment Costs')
    plt.xlabel('Costs')
    plt.ylabel('Frequency')
    
    plt.show()