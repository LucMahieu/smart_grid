import district
import house

def house_to_dict(house):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["location"] = str(house.x_position) + "," + str(house.y_position)
    output["output"] = house.max_output
    output["cables"] = house.cables
    return output

def battery_to_dict(battery):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["location"] = str(battery.position_x) + "," + str(battery.position_y)
    output["capacity"] = battery.capacity
    output["houses"] = [house_to_dict(house) for house in battery.connected_houses]
    return output

def district_to_dict(district):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["district"] = district.name
    output["costs-shared"] = district.costs_shared
    output["batteries"] = [battery_to_dict(battery) for battery in district.batteries]