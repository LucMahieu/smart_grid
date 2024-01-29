import random
from classes.district import District
from algorithms.randomize import Random_algo
from algorithms.greedy import Greedy_algo
from classes.battery import Battery 
import matplotlib.pyplot as plt
import time 
import subprocess


def run_experiment(district, algorithm_class, num_experiments):
    best_solution_cost = float('inf')
    worst_solution_cost = float('-inf')
    experiment_scores = []
    valid_solutions_count = 0
    invalid_solutions_count = 0

    for _ in range(num_experiments):
        # Reset the district to its initial state before each experiment
        print(f"Before reset: {district.district_cost_shared}")
        district.reset_state()
        print(f"After reset: {district.district_cost_shared}")
        # Create an instance of the algorithm and run it
        algorithm_instance = algorithm_class()
        valid_solution = algorithm_instance.run(district)

        # Calculate the shared cost for this iteration
        current_cost = district.shared_costs()
        print(f"Current cost for this run: {current_cost}")

        if current_cost is not None:
            best_solution_cost = min(best_solution_cost, current_cost)
            worst_solution_cost = max(worst_solution_cost, current_cost)
            valid_solutions_count += 1
        else:
            invalid_solutions_count += 1

        # Append the current cost to the experiment_scores list
        experiment_scores.append(current_cost if current_cost is not None else 0)

    return best_solution_cost, worst_solution_cost, experiment_scores, valid_solutions_count, invalid_solutions_count


def plot_histogram(experiment_scores, valid_solutions_count, invalid_solutions_count, num_experiments):
    # Create histogram
    plt.hist(experiment_scores, bins=30, color='blue', alpha=0.7)
    
    
    plt.title('Distribution of Solution Costs')
    plt.xlabel('Cost')
    plt.ylabel('Frequency')
    plt.ylim(0, num_experiments) 

    # displaying counts of valid and invalid solutions
    plt.text(0.95, 0.95, f'Valid solutions: {valid_solutions_count}\nInvalid solutions: {invalid_solutions_count}',
             horizontalalignment='right',
             verticalalignment='top',
             transform = plt.gca().transAxes)

    # Show the plot
    plt.show()


# run and time the experiments
def run_timed_experiments(script_name, max_duration, max_run_time):
    start = time.time()
    n_runs = 0

    while time.time() - start < max_duration:
        print(f"Run {n_runs+1} in progress...")
        subprocess.call(["timeout", str(max_run_time), "python3", script_name, str(n_runs)])
        n_runs += 1
        print(f"Run {n_runs} completed.")



# parameter tuning
def grid_search(parameter_combinations, district, num_runs):
    
    best_cost = float('inf')
    best_parameters = None  """Beste parameter combinatie bijhouden"""

    """
    Doorloopt elke parametercombinatie in de lijst
    """
    for parameters in parameter_combinations:
        print(f"Testing parameters: {parameters}")

        cost = run_experiment_with_parameters(district, parameters, num_runs)

        """Controleert of de kosten van deze run lager zijn dan de beste kosten die we tot nu toe hebben gevonden"""
        if cost < best_cost:
            best_cost = cost
            best_parameters = parameters

    """ Geeft beste parameters en hun kosten terug """
    return best_parameters, best_cost



### functie voor run experiment with parameters en functie set_parameters nog nodig ###
def set_parameters(algorithm_instance, parameters):
    for parameter, value in parameters.items():
        if hasattr(algorithm_instance, parameter):
            setattr(algorithm_instance, parameter, value)


def run_experiment_with_parameters(district, algorithm_class, parameters, num_runs):
    best_solution_cost = float('inf')
    total_cost = 0

    for _ in range(num_runs):
        district.reset_state()
        algorithm_instance = algorithm_class(*parameters)
        algorithm_instance.run(district)
        current_cost = district.shared_costs()

        if current_cost is not None:
            best_solution_cost = min(best_solution_cost, current_cost)
            total_cost += current_cost

    average_cost = total_cost / num_runs if num_runs > 0 else None
    return best_solution_cost, average_cost



# run experiments and save results
def run_experiments_and_save_results(algorithms, district, num_runs, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['algorithm', 'run', 'cost'])

        for algo_name, algorithm in algorithms.items():
            for run in range(num_runs):
                print(f"Running {algo_name}, run {run+1}/{num_runs}")
                district.reset_state()
                algorithm.run(district)
                cost = district.shared_costs()
                writer.writerow([algo_name, run+1, cost])





