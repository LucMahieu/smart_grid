import random 

class Algorithm():
    def __init__(self):
        self.crossed_battery = False
    
    
    def run(self, district):
        """
        Makes connections between batteries and houses and lays cable routes between them based on Manhattan distance. 
        Tries again when no battery with enough capacity is left, or if batteries are connected to eachother whilst laying the cable.
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
                
                # If batteries are connected, solution is not valid
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
            # Select battery from the list of batteries with enough capacity and connect to house
            house.battery = self.select_battery(batteries_with_capacity, house)

            # Update battery capacity
            house.battery.update_capacity(house)

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[house.battery].append(house)


    def lay_cable_route(self, district, house):
        """
        Lays cable route from current house to selected battery.
        """
        # Starting of the current position at the house coordinates
        current_pos = [house.pos_x, house.pos_y]
        house.cables = [tuple(current_pos)]
        self.crossed_battery = False

        # End position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # Coordinates of other batteries to avoid
        avoid_coordinates = [(battery.pos_x, battery.pos_y) for battery in district.batteries if battery != house.battery]
        
        # X an y-coordinate of position
        x_and_y = [0, 1]
        for x_or_y in x_and_y: 
        
            # Adding cable segments 
            self.add_segments(current_pos, cable_end_pos, x_or_y, avoid_coordinates, house)


    def add_segments(self, current_pos, cable_end_pos, x_or_y, avoid_coordinates, house):
        """
        Adds cable segments from starting until end position based on Manhattan Distance. Breaks when cable crosses another battery than 
        the one the house is connected to.
        """
        # Keep adding cable segments until the end position is reached
        while current_pos[x_or_y] != cable_end_pos[x_or_y]:

            # Y-coordinate: if current position is below the end, move up
            # X-coordinate: if current position is left from the end, move right
            if current_pos[x_or_y] - cable_end_pos[x_or_y] < 0:
                current_pos[x_or_y] += 1

            # Y-coordinate: if current position is above the end, move down
            # X-coordinate: if current position is right from the end, move left
            else:
                current_pos[x_or_y] -= 1
            
            # If incorrect battery is crossed by cable, break
            if tuple(current_pos) in avoid_coordinates:
                self.crossed_battery = True
                return

            # Add coordinate to cablecoordinate list
            house.cables.append(tuple(current_pos))


class Greedy(Algorithm):
    def manhattan_distance(self, house, battery):
        """
        Calculates Manhattan distance between a house and a battery.
        """
        return abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)


    def select_battery(self, batteries_with_capacity, house):
        """
        Selects the battery closest to the selected house with enough capacity left.
        """
        # Create dictionary to store distances 
        distance_dict = {}

        # Calculate Manhattan distance for all batteries with enough capacity
        for battery in batteries_with_capacity:
            distance = self.manhattan_distance(house, battery)
            
            # Add calculated distance to dictionary
            distance_dict[battery] = distance

        # Return battery from dictionary that is closest to house
        return min(distance_dict, key = distance_dict.get)
    

class Baseline(Algorithm):
    def select_battery(self, batteries_with_capacity, _):
        """
        Assigns random battery to current house.
        """
        return random.choice(batteries_with_capacity)