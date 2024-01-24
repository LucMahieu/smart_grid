import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import json 

# import json


# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # load house and battery icons
#     house_icon = Image.open('house.png')  # from: https://iconduck.com/icons/96056/house
#     battery_icon = Image.open('battery.png')  # from: https://www.iconfinder.com/icons/172578/battery_car_battery_icon

#     district = output.get("district")
#     batteries = output.get("batteries", [])

#     for battery in batteries[:2]:
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False,
#                                      pad=0)
#         ax.add_artist(battery_box)

#         houses = battery.get("houses", [])
#         for house in houses[:10]:
#             house_location = house.get("location")
#             x, y = map(float, house_location.split(','))

#             # display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
#             ax.add_artist(house_box)

#             # connect houses to batteries with cables
#             cables = house.get("cables", [])
#             for cable_point in cables[:10]:
#                 cable_x, cable_y = map(float, cable_point)
#                 ax.plot([x, cable_x], [y, y], 'k-', alpha=0.5)
#                 ax.plot([cable_x, cable_x], [y, cable_y], 'k-', alpha=0.5)

#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50) 
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.grid(True)
#     plt.savefig('figure.png')
#     # plt.show()

# if __name__ == '__main__':
#     # Load data from output.json in the parent directory
#     file_path = '../output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     # Call visualize_grid with the loaded data
# #     visualize_grid(output_data)
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json


# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # load house and battery icons
#     house_icon = Image.open('house.png')  # from: https://iconduck.com/icons/96056/house
#     battery_icon = Image.open('battery.png')  # from: https://www.iconfinder.com/icons/172578/battery_car_battery_icon

#     district = output.get("district")
#     batteries = output.get("batteries", [])

#     for battery in batteries[:2]:
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False,
#                                      pad=0)
#         ax.add_artist(battery_box)

#         houses = battery.get("houses", [])
#         for house in houses[:10]:
#             house_location = house.get("location")
#             x, y = map(float, house_location.split(','))

#             # display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
#             ax.add_artist(house_box)

#             # connect houses to batteries with one cable
#             cables = house.get("cables", [])
#             if cables:
#                 cable_x, cable_y = map(float, cables[0])

#                 # Draw horizontal and vertical cables
#                 ax.plot([x, cable_x], [y, y], 'k-', alpha=0.5)
#                 ax.plot([cable_x, x_battery], [y, y], 'k-', alpha=0.5)
#                 ax.plot([x_battery, x_battery], [y, y_battery], 'k-', alpha=0.5)

#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.grid(True)
#     plt.savefig('figure.png')
#     plt.show()

# if __name__ == '__main__':
#     # Load data from output.json in the parent directory
#     file_path = 'output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     # Call visualize_grid with the loaded data
#     visualize_grid(output_data)
# #almost correct but somehow all the cables are connected

# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json


# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # load house and battery icons
#     house_icon = Image.open('house.png')  # from: https://iconduck.com/icons/96056/house
#     battery_icon = Image.open('battery.png')  # from: https://www.iconfinder.com/icons/172578/battery_car_battery_icon

#     district = output.get("district")
#     batteries = output.get("batteries", [])

#     for battery in batteries[:2]:
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False,
#                                      pad=0)
#         ax.add_artist(battery_box)

#         houses = battery.get("houses", [])
#         for house in houses[:10]:
#             house_location = house.get("location")
#             x, y = map(float, house_location.split(','))

#             # display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
#             ax.add_artist(house_box)

#             # connect house to its battery with one cable
#             cables = house.get("cables", [])
#             for cable_point in cables[:10]:
#                 cable_x, cable_y = map(float, cable_point)

#                 # Draw horizontal and vertical cables only to the battery
#                 ax.plot([x, x_battery], [y, y], 'k-', alpha=0.5)
#                 ax.plot([x_battery, x_battery], [y, y_battery], 'k-', alpha=0.5)

#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.grid(True)
#     plt.savefig('figure.png')
#     # plt.show()

# if __name__ == '__main__':
#     
#     file_path = '../output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     # Call visualize_grid with the loaded data
#     visualize_grid(output_data)

# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json

# def visualize_grid(output):
#     fig, ax = plt.subplots(figsize=(8, 8))
#     # load house and battery icons
#     house_icon = Image.open('house.png')
#     battery_icon = Image.open('battery.png')

#     district = output.get("district")
#     batteries = output.get("batteries", [])

#     # Plot each battery and connected houses
#     for battery in batteries[:2]:
#         battery_location = battery.get("location")
#         x_battery, y_battery = map(float, battery_location.split(','))

#         # Display battery icon
#         battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.05), (x_battery, y_battery), frameon=False)
#         ax.add_artist(battery_box)

#         # Plot each house connected to the battery
#         houses = battery.get("houses", [])
#         for house in houses[:10]:
#             house_location = house.get("location")
#             x_house, y_house = map(float, house_location.split(','))

#             # Display house icon
#             house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.05), (x_house, y_house), frameon=False)
#             ax.add_artist(house_box)

#             # Draw cable from the house to the battery
#             ax.plot([x_house, x_house, x_battery], [y_house, y_battery, y_battery], 'k-', alpha=0.7)

#     # Set the axis limits and labels
#     ax.set_xlim(0, 50)
#     ax.set_ylim(0, 50)
#     ax.set_title(f'SmartGrid Visualization - District {district}')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')

#     ax.grid(True)
#     plt.axis('on')

#     # Save the figure
#     # plt.savefig('corrected_figure.png', bbox_inches='tight')
#     plt.show()

# if __name__ == '__main__':
  
#     file_path = '../output.json'
#     with open(file_path, 'r') as file:
#         output_data = json.load(file)
#     visualize_grid(output_data)


import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import json

def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))
    # load house and battery icons
    house_icon = Image.open('house.png')  # Make sure the path to house.png is correct
    battery_icon = Image.open('battery.png')  # Make sure the path to battery.png is correct

    district = output.get("district")
    batteries = output.get("batteries", [])

    # Ensure the icons do not overlap by adjusting the zoom if necessary
    

    # Iterate over the batteries
    for battery in batteries[:2]:
        battery_location = battery.get("location")
        x_battery, y_battery = map(float, battery_location.split(','))

        # Display battery icon
        battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.05), (x_battery, y_battery), frameon=False)
        ax.add_artist(battery_box)

        # Iterate over the houses for each battery
        houses = battery.get("houses", [])
        for house in houses[:10]:
            house_location = house.get("location")
            x_house, y_house = map(float, house_location.split(','))

            # Display house icon
            house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.05), (x_house, y_house), frameon=False)
            ax.add_artist(house_box)

            # Connect house to its battery with a unique cable path
            # Draw the cable path for the house as determined by the algorithm
            for i in range(1, len(house['cables'])):
                start_point = house['cables'][i - 1]
                end_point = house['cables'][i]
                ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'k-', alpha=0.7)

    # Set the axis limits and labels
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title(f'SmartGrid Visualization - District {district}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Remove the grid or make it very light
    ax.grid(False)
    plt.axis('on')  # Turn off the axis if not needed

    # Save the figure or show interactively
    #plt.savefig('corrected_figure.png', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    # Load data from output.json in the current directory
    file_path = '../output.json'  # Update this path to where your output.json is located
    with open(file_path, 'r') as file:
        output_data = json.load(file)
    visualize_grid(output_data)
