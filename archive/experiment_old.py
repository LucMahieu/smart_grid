# def run_experiment(district, algorithm_class, num_experiments):
#     best_solution_cost = float('inf')
#     worst_solution_cost = float('-inf')
#     experiment_scores = []

#     for _ in range(num_experiments):
#         # Reset the district to its initial state before each experiment
#         district.reset_state()

#         # Create an instance of the algorithm and run it
#         algorithm_instance = algorithm_class()
#         valid_solution = algorithm_instance.run(district)

#         if not valid_solution:
#             print("Invalid solution encountered, skipping this iteration.")
#             continue

#         # Calculate the shared cost for this iteration
#         current_cost = district.shared_costs()
#         if current_cost is not None:
#             best_solution_cost = min(best_solution_cost, current_cost)
#             worst_solution_cost = max(worst_solution_cost, current_cost)
#             experiment_scores.append(current_cost)
#         else:
#             print("Incomplete solution, skipping this iteration.")

#     return best_solution_cost, worst_solution_cost, experiment_scores

def run_experiment(district, algorithm_class, num_experiments):
    best_solution_cost = float('inf')
    worst_solution_cost = float('-inf')
    experiment_scores = []

    for _ in range(num_experiments):
        # Reset the district to its initial state before each experiment
        district.reset_state()

        # Create an instance of the algorithm and run it
        algorithm_instance = algorithm_class()
        valid_solution = algorithm_instance.run(district)

        # Calculate the shared cost for this iteration
        current_cost = district.shared_costs()
        if current_cost is not None:
            best_solution_cost = min(best_solution_cost, current_cost)
            worst_solution_cost = max(worst_solution_cost, current_cost)
        else:
            print("Incomplete solution encountered.")

        # Append the current cost to the experiment_scores list
        experiment_scores.append(current_cost)

    return best_solution_cost, worst_solution_cost, experiment_scores
# # Example usage:
# best_cost, worst_cost, scores = run_experiment(district1, Greedy_algo, 10)
# print(f"Best solution cost: {best_cost}")
# print(f"Worst solution cost: {worst_cost}")
# print(f"All experiment scores: {scores}")

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


def run_timed_experiments(algorithm_classes, district, max_duration, num_experiments):
    start = time.time()
    total_experiment_duration = 0
    experiment_results = []

    for n_runs in range(num_experiments):
        if total_experiment_duration >= max_duration:
            break

        for algorithm_class in algorithm_classes:
            algorithm_instance = algorithm_class()
            run_start_time = time.time()
            algo_iterations = algorithm_instance.run(district)
            run_end_time = time.time()

            run_duration = run_end_time - run_start_time
            total_experiment_duration += run_duration

            experiment_results.append({
                'algorithm': algorithm_class.__name__,
                'run_number': n_runs + 1,
                'run_duration': run_duration,
                'iterations': algo_iterations,
                'cost': district.shared_costs()
            })

            if total_experiment_duration >= max_duration:
                break

    total_duration = time.time() - start
    return experiment_results, total_duration




# # parameter tuning
# def grid_search(parameter_combinations, district, num_runs):
    
#     best_cost = float('inf')
#     best_parameters = None  """Beste parameter combinatie bijhouden"""

#     """
#     Doorloopt elke parametercombinatie in de lijst
#     """
#     for parameters in parameter_combinations:
#         print(f"Testing parameters: {parameters}")

#         cost = run_experiment_with_parameters(district, parameters, num_runs)

#         """Controleert of de kosten van deze run lager zijn dan de beste kosten die we tot nu toe hebben gevonden"""
#         if cost < best_cost:
#             best_cost = cost
#             best_parameters = parameters

#     """ Geeft beste parameters en hun kosten terug """
#     return best_parameters, best_cost



# ### functie voor run experiment with parameters en functie set_parameters nog nodig ###
# def set_parameters(algorithm_instance, parameters):
#     for parameter, value in parameters.items():
#         if hasattr(algorithm_instance, parameter):
#             setattr(algorithm_instance, parameter, value)


# def run_experiment_with_parameters(district, algorithm_class, parameters, num_runs):
#     best_solution_cost = float('inf')
#     total_cost = 0

#     for _ in range(num_runs):
#         district.reset_state()
#         algorithm_instance = algorithm_class(*parameters)
#         algorithm_instance.run(district)
#         current_cost = district.shared_costs()

#         if current_cost is not None:
#             best_solution_cost = min(best_solution_cost, current_cost)
#             total_cost += current_cost

#     average_cost = total_cost / num_runs if num_runs > 0 else None
#     return best_solution_cost, average_cost



# run experiments and save results
def save_experiment_results_to_csv(experiment_results, total_duration, csv_filename):
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['algorithm', 'run_number', 'run_duration', 'iterations', 'cost']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for result in experiment_results:
            writer.writerow(result)

    print(f"Totaal experiment duurde: {total_duration} seconden")






#############
    



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
