import matplotlib.pyplot as plt
import csv
import numpy as np

def load_scores_from_csv(csv_filename):
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
    if scores:
        print(f"Aantal experimenten: {len(scores)}")
        print(f"Gemiddelde score: {np.mean(scores)}")
        print(f"Standaarddeviatie van scores: {np.std(scores)}")
        print(f"Minimale score: {np.min(scores)}")
        print(f"Maximale score: {np.max(scores)}")

        # Maak een histogram van de scores
        plt.hist(scores, bins=30, color='blue', alpha=0.7)
        plt.title(f'Distributie van behaalde scores {algorithm_name}')
        plt.xlabel('Score')
        plt.ylabel('Frequentie')
        plt.show()
        plt.savefig(f'Distributie_van_{algorithm_name}')

    else:
        print("Geen geldige scores")



import matplotlib.pyplot as plt

def plot_histogram_valid_solutions(algorithm_instance, num_experiments):
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