
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json

# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # Load house and battery icons
#     house_icon = Image.open('visualization/house1.png')
#     battery_icon = Image.open('visualization/battery1.png')

#     # Define a list of colors for the batteries
#     colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']

#     district = output.get("district")
#     batteries = output.get("batteries", [])

#     for i, battery in enumerate(batteries):
#         color = colors[i % len(colors)]  # Cycle through colors list
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # Display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
#         ax.add_artist(battery_box)

#         houses = battery.get("houses", [])
#         for house in houses:
#             house_location = house.get("location")
#             x, y = map(float, house_location.split(','))

#             # Display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
#             ax.add_artist(house_box)

#             # Connect houses to batteries with colored cables
#             cables = house.get("cables", [])
#             prev_x, prev_y = x, y
#             for cable_point in cables:
#                 cable_x, cable_y = cable_point
#                 ax.plot([prev_x, cable_x], [prev_y, cable_y], color=color, alpha=0.5)
#                 prev_x, prev_y = cable_x, cable_y

#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.grid(True)
#     plt.show()

# if __name__ == '__main__':
#     # Load data from output.json in the parent directory
#     file_path = '../output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     # Call visualize_grid with the loaded data
#     visualize_grid(output_data)

# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json
# import matplotlib.colors as mcolors

# def generate_unique_colors(num_colors):
#     colors = list(mcolors.TABLEAU_COLORS.values())  # Get a set of unique colors
#     if num_colors > len(colors):
#         additional_colors_needed = num_colors - len(colors)
#         for _ in range(additional_colors_needed):
#             # Generate a random color
#             colors.append((np.random.rand(), np.random.rand(), np.random.rand()))
#     return colors

# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # Load house and battery icons
#     house_icon = Image.open('visualization/house1.png')
#     battery_icon = Image.open('visualization/battery1.png')

#     district = output.get("district")
#     batteries = output.get("batteries", [])
#     colors = generate_unique_colors(len(batteries))  # Generate unique colors for each battery

#     for i, battery in enumerate(batteries):
#         color = colors[i]  # Assign a unique color to each battery
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # Display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
#         ax.add_artist(battery_box)

#         houses = battery.get("houses", [])
#         for house in houses:
#             house_location = house.get("location")
#             x, y = map(float, house_location.split(','))

#             # Display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
#             ax.add_artist(house_box)

#             # Connect houses to batteries with colored cables
#             cables = house.get("cables", [])
#             prev_x, prev_y = x, y
#             for cable_point in cables:
#                 cable_x, cable_y = cable_point
#                 ax.plot([prev_x, cable_x], [prev_y, cable_y], color=color, alpha=0.5)  # Use the battery's unique color
#                 prev_x, prev_y = cable_x, cable_y

#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.grid(True)
#     plt.show()

# if __name__ == '__main__':
#     # Load data from output.json in the parent directory
#     file_path = '../output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     # Call visualize_grid with the loaded data
#     visualize_grid(output_data)

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import json
import numpy as np

def generate_unique_colors(num_colors):
    # Generate a list of unique colors using a simple method to cycle through the colormap
    colors = plt.cm.get_cmap('hsv', num_colors)
    return colors(range(num_colors))

def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))
    # Load house and battery icons
    house_icon = Image.open('visualization/house1.png')
    battery_icon = Image.open('visualization/battery1.png')

    district = output.get("district")
    batteries = output.get("batteries", [])
    colors = generate_unique_colors(len(batteries))  # Generate unique colors for each battery

    for i, battery in enumerate(batteries):
        color = colors[i]  # Assign a unique color to each battery
        battery_location = battery.get("location")
        x_battery, y_battery = map(float, battery_location.split(','))

        # Display battery icon
        battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
        ax.add_artist(battery_box)

        houses = battery.get("houses", [])
        for house in houses:
            house_location = house.get("location")
            x, y = map(float, house_location.split(','))

            # Display house icon
            house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
            ax.add_artist(house_box)

            # Connect houses to batteries with colored cables
            cables = house.get("cables", [])
            prev_x, prev_y = x, y
            for cable_point in cables:
                cable_x, cable_y = cable_point
                ax.plot([prev_x, cable_x], [prev_y, cable_y], color=color, alpha=0.5)  # Use the battery's unique color
                prev_x, prev_y = cable_x, cable_y

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title(f'SmartGrid Visualization - District {district}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)
    plt.show()

if __name__ == '__main__':
    # Load data from output.json in the parent directory
    file_path = '../output.json'
    with open(file_path, 'r') as file:
        output_data = json.load(file)
    # Call visualize_grid with the loaded data
    visualize_grid(output_data)
