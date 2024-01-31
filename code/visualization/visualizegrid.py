import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import json


def visualize_grid(output):
    """
    Visualizes the grid, containing batteries, houses and cablesegments.
    """
    # Initialize the plot 
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Load house and battery icons
    house_icon = Image.open('code/visualization/house1.png')
    battery_icon = Image.open('code/visualization/battery1.png')

    # Extract data from output
    district = output.get("district")
    batteries = output.get("batteries", [])
    
    # Define the colors
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']

    # Visualize batteries
    for i, battery in enumerate(batteries):
        
        # Selecting color
        color = colors[i % len(colors)]

        # Plotting battery at right location
        battery_location = battery.get("location")
        x_battery, y_battery = map(float, battery_location.split(','))

        # Add battery icon to grid
        battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
        ax.add_artist(battery_box)

        # Visualize houses
        houses = battery.get("houses", [])
        for house in houses:

            # Plotting house at right location
            house_location = house.get("location")
            x, y = map(float, house_location.split(','))

            # Add house icon to plot
            house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
            ax.add_artist(house_box)

            # Visualize cables
            cables = house.get("cables", [])
            prev_x, prev_y = x, y
            for cable_point in cables:

                # Plotting cable at right location
                cable_x, cable_y = cable_point

                # Plot cablesegments
                ax.plot([prev_x, cable_x], [prev_y, cable_y], color=color, alpha=0.5)
                prev_x, prev_y = cable_x, cable_y

    # Set plot properties
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title(f'SmartGrid Visualization - District {district}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)

    # Show and save plot
    plt.show()
    plt.savefig('grid.png')

if __name__ == '__main__':
    # Load output data from JSON file
    file_path = '../output.json'
    with open(file_path, 'r') as file:
        output_data = json.load(file)

    # Visualize the output data on the grid
    visualize_grid(output_data)