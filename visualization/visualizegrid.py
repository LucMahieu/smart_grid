# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from PIL import Image
# import json 

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
#almost correct but somehow all the cables are connected

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
#     #plt.savefig('figure.png')
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

def draw_cables(ax, house_x, house_y, cable_points):
    """
    Draw cables with horizontal and vertical lines only.
    """
    prev_x, prev_y = house_x, house_y

    for point in cable_points:
        cable_x, cable_y = point
        # Draw horizontal line
        ax.plot([prev_x, cable_x], [prev_y, prev_y], 'k-', alpha=0.5)

        # Draw vertical line
        ax.plot([cable_x, cable_x], [prev_y, cable_y], 'k-', alpha=0.5)

        prev_x, prev_y = cable_x, cable_y


def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))
    house_icon = Image.open('house.png')
    battery_icon = Image.open('battery.png')

    district = output.get("district")
    batteries = output.get("batteries", [])

    for battery in batteries[:2]:
        battery_location = battery.get("location", "0,0")
        x_battery, y_battery = map(float, battery_location.split(','))

        battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
        ax.add_artist(battery_box)

        houses = battery.get("houses", [])
        for house in houses[:10]:
            house_location = house.get("location", "0,0")
            x, y = map(float, house_location.split(','))

            house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
            ax.add_artist(house_box)

            cables = house.get("cables", [])
            draw_cables(ax, x, y, cables)

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title(f'SmartGrid Visualization - District {district}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)
    plt.show()
    plt.savefig('visualize.png')


if __name__ == '__main__':
    file_path = '../output.json'
    with open(file_path, 'r') as file:
        output_data = json.load(file)
    visualize_grid(output_data)
