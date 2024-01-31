import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import json
import numpy as np


def visualize_grid(output):
    """
    Visualizes the grid, containing batteries, houses and cablesegments.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    house_icon = Image.open('code/visualization/house1.png')
    battery_icon = Image.open('code/visualization/battery1.png')

    district = output.get("district")
    batteries = output.get("batteries", [])
    
    
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']

    # Visualizing batteries
    for i, battery in enumerate(batteries):
        
        color = colors[i % len(colors)]
        battery_location = battery.get("location")
        x_battery, y_battery = map(float, battery_location.split(','))

        
        battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
        ax.add_artist(battery_box)

        houses = battery.get("houses", [])

        # Visualizing houses
        for house in houses:
            house_location = house.get("location")
            x, y = map(float, house_location.split(','))

            
            house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
            ax.add_artist(house_box)

            
            cables = house.get("cables", [])
            prev_x, prev_y = x, y

            # Visualizing cables
            for cable_point in cables:
                cable_x, cable_y = cable_point
                ax.plot([prev_x, cable_x], [prev_y, cable_y], color=color, alpha=0.5)
                prev_x, prev_y = cable_x, cable_y

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title(f'SmartGrid Visualization - District {district}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)
    plt.show()
    plt.savefig('grid.png')

if __name__ == '__main__':
    
    file_path = '../output.json'
    with open(file_path, 'r') as file:
        output_data = json.load(file)

    visualize_grid(output_data)