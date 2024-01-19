from collections import OrderedDict
import json

def house_to_dict(house):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(house.pos_x) + "," + str(house.pos_y)
    output["output"] = house.max_output
    output["cables"] = [cable for cable in house.cables]
    return output

def battery_to_dict(battery, district):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(battery.pos_x) + "," + str(battery.pos_y)
    output["capacity"] = battery.capacity
    output["houses"] = [house_to_dict(house) for house in district.houses]
    return output

def district_to_dict(district):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["district"] = district.name
    output["costs-separate"] = district.district_price_seperate
    output["costs-shared"] = district.district_price_shared
    output["batteries"] = [battery_to_dict(battery, district) for battery in district.batteries]
    return output

def export_json(district):
    """Exports the districts to a json file."""
    output = district_to_dict(district)
    with open("output.json", "w") as outfile:
        json.dump(output, outfile, indent=4, sort_keys=False)

    return output