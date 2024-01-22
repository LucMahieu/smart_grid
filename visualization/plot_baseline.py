import matplotlib.pyplot as plt
import json

def visualize_baseline_scores(output):
    district = output.get("district")
    batteries = output.get("batteries", [])

    battery_labels = [f'Battery {i+1}' for i in range(len(batteries))]
    scores = [1000, 800, 1200, 900]
    # Create a bar plot
    plt.bar(battery_labels, scores, color='skyblue')
    plt.xlabel('Batteries')
    plt.ylabel('Scores')
    plt.title(f'Baseline Scores - District {district}')
    plt.ylim(0, max(scores) + 200)
    plt.grid(axis='y')

    # Display the scores on top of the bars
    for i, score in enumerate(scores):
        plt.text(i, score + 20, str(score), ha='center', va='bottom')

    # Save the plot as an image
    plt.savefig('baseline_scores.png')
    plt.show()

if __name__ == '__main__':
    # Load data from output.json
    file_path = '../output.json'
    with open(file_path, 'r') as file:
        output_data = json.load(file)

    visualize_baseline_scores(output_data)
