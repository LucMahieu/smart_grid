import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))

    result = []

    # load house and battery icons
    house_icon = Image.open('house.png') #from:https://iconduck.com/icons/96056/house
    battery_icon = Image.open('battery.png') #from:https://www.iconfinder.com/icons/172578/battery_car_battery_icon

    for index, entry in enumerate(output):
        if index == 0:
            # skip first entry if it doesnt contain "district" key
            continue

        district = entry.get("district", 1)  # default to 1 if "district" not present
        costs_type = "shared-costs" if "costs-shared" in entry else "own-costs"
        total_costs = entry.get("costs-shared", 0) + entry.get("costs-own", 0)

        result.append({
            "district": district,
            "type": costs_type,
            "total-costs": total_costs
        })

        # store locations of connected houses for each battery
        if 'location' in entry and 'houses' in entry:
            connected_houses = set()

            # plot houses
            for house_info in entry['houses']:
                house_location = house_info['location']
                x, y = map(int, house_location.split(','))

                # display house icon
                #from:https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html
                house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.05), (x, y), frameon=False, pad=0)
                ax.add_artist(house_box)

                # record  location of the connected house
                connected_houses.add((x, y))

            # plot battery
            battery_location = entry['location']
            x_battery, y_battery = map(int, battery_location.split(','))

            # display battery icon
            #from:https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html
            battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.05), (x_battery, y_battery), frameon=False, pad=0)
            ax.add_artist(battery_box)

            # plot single cable connecting battery to houses
            for house_x, house_y in connected_houses:
                ax.plot([x_battery, house_x], [y_battery, house_y], 'k-', alpha=0.5)

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_title('Smart Grid Visualization')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)

    plt.show()

    return result

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
            },
            {
                "location": "30,12",
                "output": 66.05341632,
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
            }
        ]
    }
]

formatted_output = visualize_grid(dummy_output)
print(formatted_output)
