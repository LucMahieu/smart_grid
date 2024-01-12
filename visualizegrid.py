import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))

    # load house and battery icons
    house_icon = Image.open('house.png') #from:https://iconduck.com/icons/96056/house
    battery_icon = Image.open('battery.png') #from:https://www.iconfinder.com/icons/172578/battery_car_battery_icon

    for index, entry in enumerate(output):
        if index == 0:
            # skip first entry if it doesnt contain "district" key
            continue
            
        if 'location' in entry and 'houses' in entry:
            connected_houses = []

            # plot houses
            for house_info in entry['houses']:
                house_location = house_info['location']
                x, y = map(float, house_location.split(','))

                # display house icon
                # from https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html
                house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
                ax.add_artist(house_box)

                connected_houses.append((x, y))


            # plot battery
            battery_location = entry['location']
            x_battery, y_battery = map(float, battery_location.split(','))

            #display battery icon
            # from https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html
            battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
            ax.add_artist(battery_box)

            # connect houses to batteriesy with cables
            for house_x, house_y in connected_houses:
                ax.plot([house_x, x_battery], [house_y, house_y], 'k-', alpha=0.5)
                ax.plot([x_battery, x_battery], [house_y, y_battery], 'k-', alpha=0.5)

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 25)
    ax.set_title('SmartGrid Visualization')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)

    plt.show()
    


# example usage with dummy data (from the output example of SmartGrid)
dummy_output = [
    {
        "district": 1,
        "costs-shared": 10198
    },
    {
        "location": "38,12",
        "capacity": 1507.0,
        "houses": [
            {
                "location": "33,7",
                "output": 39.45690812,
                "cables": [
                    "33,7", "33,8", "33,9", "33,10", "33,11", "33,12", "34,12", "35,12", "36,12", "37,12", "38,12"
                ]
            },
            {
                "location": "30,12",
                "output": 66.05341632,
                "cables": ["30,12", "31,12", "32,12", "33,12", "34,12"]
            }
        ]
    },
    {
        "location": "42,3",
        "capacity": 1507.0,
        "houses": [
            {
                "location": "48,4",
                "output": 58.90934923,
                "cables": ["48,4", "48,3", "47,3", "46,3", "45,3", "44,3", "43,3", "42,3"]
            }
        ]
    }
]
visualize_grid(dummy_output)

