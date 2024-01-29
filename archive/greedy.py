import random

class Greedy():
    def __init__(self):
        pass


    def run(self, district):
        """
        Greedily makes connections between batteries and houses and lays cable routes between them based on Manhattan distance.
        """
        # Random order of houses
        random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to closest battery with capacity
            self.closest_connection(house, district)
            
            # If no battery available with enough capacity
            if house.battery == None:
                print("Invalid solution")
                break
            
            # Lays cable route based on steps that minimize distance
            self.lay_cable_route(house)

        return district
    

    def manhattan_distance(self, beginning, end):
        """
        Calculates Manhattan distance between two points.
        """
        x1, y1 = beginning[0], beginning[1]
        x2, y2 = end[0], end[1]

        distance = abs(x1 - x2) + abs(y1 - y2)
        
        return distance
    

    def min_distance(self, selected_batteries, house):
        """
        Selects the battery closest to the selected house with enough capacity left.
        """
        # Create dictionary to store distance between house and each battery with sufficient capacity left
        distance_dict = {}

        # Calculate manhattan distance for all batteries with enough capacity
        for option in selected_batteries:
            beginning = house.pos_x, house.pos_y
            end = option.pos_x, option.pos_y
            distance = self.manhattan_distance(beginning, end)
            
            # Add calculated distance to dictionary
            distance_dict[option] = distance

        # Saving closest battery 
        best_battery = min(distance_dict, key = distance_dict.get)

        return best_battery


    def closest_connection(self, house, district):
        """
        Connects a house to the closest battery with enough capacity left.
        """
        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # Check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:
            # Connecting to closest battery with capacity
            selected_battery = self.min_distance(batteries_with_capacity, house)

            # Update the house's battery attribute
            house.battery = selected_battery

            # Update battery capacity
            house.battery.update_capacity(house)

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[selected_battery].append(house)


    def determine_possible_steps(self):
        """
        Determines possible positions for the next step.
        """
        # Possible absolute steps
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # Define step options based on current position
        self.options = set()
        for position in [right, left, up, down]:
            self.options.add((self.current_pos[0] + position[0], self.current_pos[1] + position[1]))


    def choose_step_greedily(self, options, cable_end_pos):
        """
        Calculates Manhattan distance for each cablesegment option, selects the option that minimizes Manhattan distance.
        """
        # Create dictionary to store distance for each cablesegment option
        distances = {}

        # Calculate Manhattan distance for each segment
        for option in options:
            distance = self.manhattan_distance(option, cable_end_pos)
            distances[option] = distance

        # Select position that minimizes the distance
        self.new_pos = min(distances, key = distances.get)


    def lay_cable_route(self, house):
        """
        Lays cable route from house to selected battery.
        """
        # Starting position of current pos and cable route is the house position
        self.current_pos = (house.pos_x, house.pos_y)
        house.cables = [self.current_pos]

        # End position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # Keep generating and adding cable segments untill battery is reached
        while self.current_pos != cable_end_pos:
            # Determine possible steps
            self.determine_possible_steps()

            # Choose step from options
            self.choose_step_greedily(self.options, cable_end_pos)

            # Add new step (cable point coordinates) to cable route
            house.cables.append(self.new_pos)

            # After the step, the new position becomes the current position
            self.current_pos = self.new_pos