import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
from district import District

def visualize_grid(output):
    fig, ax = plt.subplots(figsize=(8, 8))

    # load house and battery icons
    house_icon = Image.open('house.png')
    battery_icon = Image.open('battery.png')

    for entry in output:
        if 'location' in entry and 'houses' in entry:
            connected_houses = []

            # plot houses
            for house_info in entry['houses']:
                house_location = house_info['location']
                x, y = map(float, house_location.split(','))

                # display house icon
                house_box = AnnotationBbox(OffsetImage(house_icon, zoom=0.04), (x, y), frameon=False, pad=0)
                ax.add_artist(house_box)

                connected_houses.append((x, y))

            # plot battery
            battery_location = entry['location']
            x_battery, y_battery = map(float, battery_location.split(','))

            # display battery icon
            battery_box = AnnotationBbox(OffsetImage(battery_icon, zoom=0.04), (x_battery, y_battery), frameon=False, pad=0)
            ax.add_artist(battery_box)

            # connect houses to batteries with cables
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

from export_json import export_json

if __name__ == "__main__":
    districts = [District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv"),
                 District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv"),
                 District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")]

    # call export_json function to get output
    output = export_json(districts)

    visualize_grid(output)

