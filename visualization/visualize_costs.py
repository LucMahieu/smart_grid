# import matplotlib.pyplot as plt
# import json

# def visualize_costs(output):
#     """
#     Visualize and save the costs for different random scenarios.

#     Parameters:
#     - output: Output dictionary containing information about districts.
#     """
#     costs = []

#     if 'batteries' in output and isinstance(output['batteries'], list):
#         for battery_entry in output['batteries']:
#             if 'costs-shared' in battery_entry:
#                 costs.append(battery_entry['costs-shared'])

#     print("Costs:", costs)

#     plt.bar(range(1, len(costs) + 1), costs, color='blue')
#     plt.xlabel('Battery')
#     plt.ylabel('Cost')
#     plt.title(f'District {output["district"]} Cost Comparison')
#     plt.savefig('district_costs_visualization.png')
#     plt.show()

# # Example usage:
# # Load the output from the generated "output.json" file
# with open('output.json', 'r') as infile:
#     output_data = json.load(infile)

# visualize_costs(output_data)
