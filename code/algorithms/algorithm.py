import random 

class Algorithm():
    def __init__(self):
        self.crossed_battery = False
    
    def run(self, district):
        """
        Makes connections between batteries and houses and lays cable routes between them based on Manhattan distance.
        """
        # Keep trying until valid solution is found
        while True:

            # Resetting district if solution is not found
            district.reset_state()
            valid_solution = True

            # Random order of houses
            random.shuffle(district.houses)

            for house in district.houses:
                # Connect house to battery
                self.assign_battery_to_house(district, house)
                
                # If no battery available with enough capacity, solution is not valid
                if house.battery == None:
                    valid_solution = False
                    break
                
                # Lays cable route based on steps that minimize distance
                self.lay_cable_route(district, house)
                if self.crossed_battery == True:
                    valid_solution = False
                    break

            # If a valid solution is found, exit while loop
            if valid_solution:
                break

        return district

    def assign_battery_to_house(self, district, house):
        """
        Assigns battery to house with enough capacity and adds it to the connections dictionary.
        """
        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # Check if battery has enough capacity to connect to house
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:
            # Select battery from the list of batteries with enough capacity
            selected_battery = self.select_battery(batteries_with_capacity, house)

            # Connect selected battery to the current house
            house.battery = selected_battery

            # Update battery capacity
            house.battery.update_capacity(house)

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[selected_battery].append(house)


    def lay_cable_route(self, district, house):
        """
        Lays cable route from current house to randomly selected battery, breaks if batteries are accidentally connected.
        """
        self.crossed_battery = False
        # Starting of the current position at the house coordinates
        current_pos = [house.pos_x, house.pos_y]
        house.cables = [tuple(current_pos)]

        # End position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # Coordinates of other batteries to avoid
        avoid_coordinates = [(battery.pos_x, battery.pos_y) for battery in district.batteries if battery != house.battery]

        # Keep adding cable segments until the x-coordinate of the end position is reached
        while current_pos[0] != cable_end_pos[0]:

            # If current position is to the left of the end, move right
            if current_pos[0] - cable_end_pos[0] < 0:
                current_pos[0] += 1

            # If current position is to the right of the end, move left
            else:
                current_pos[0] -= 1
            
            # If incorrect battery is reached, break
            if tuple(current_pos) in avoid_coordinates:
                self.crossed_battery = True
                return

            house.cables.append(tuple(current_pos))

        # Keep adding cable segments until the y-coordinate of the end position is reached
        while current_pos[1] != cable_end_pos[1]:

            # If current position is below the end, move up
            if current_pos[1] - cable_end_pos[1] < 0:
                current_pos[1] += 1

            # If current position is above the end, move down
            else:
                current_pos[1] -= 1
            
            # If incorrect battery is reached, break
            if tuple(current_pos) in avoid_coordinates:
                self.crossed_battery = True
                return

            house.cables.append(tuple(current_pos))


class Greedy(Algorithm):
    def manhattan_distance(self, beginning, end):
        """
        Calculates Manhattan distance between two points.
        """
        x1, y1 = beginning[0], beginning[1]
        x2, y2 = end[0], end[1]

        distance = abs(x1 - x2) + abs(y1 - y2)
        
        return distance


    def select_battery(self, batteries_with_capacity, house):
        """
        Selects the battery closest to the selected house with enough capacity left.
        """
        # Create dictionary to store distance between house and each battery with sufficient capacity left
        distance_dict = {}

        # Calculate manhattan distance for all batteries with enough capacity
        for option in batteries_with_capacity:
            beginning = house.pos_x, house.pos_y
            end = option.pos_x, option.pos_y
            distance = self.manhattan_distance(beginning, end)
            
            # Add calculated distance to dictionary
            distance_dict[option] = distance

        # Saving closest battery 
        best_battery = min(distance_dict, key = distance_dict.get)

        return best_battery
    

class Baseline(Algorithm):
    def select_battery(self, batteries_with_capacity, house):
        """
        Assigns random battery to current house.
        """
        return random.choice(batteries_with_capacity)