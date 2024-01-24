import random

class Greedy2_algo():
    def __init__(self):
        self.prev_pos = ()
        self.lookahead = 4

    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''
        # Random order of houses
        random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to closest battery with capacity
            self.closest_connection(house, district)
            
            # If no battery available with enough capacity
            if house.battery == None:
                print("Invalid solution")

                return False 
            
            else:
                # Lays cable route based on steps that minimize distance
                self.lay_cable_route(house, self.lookahead)

        return district
    
    def manhattan_distance(self, beginning, end):
        '''
        Calculates Manhattan distance between two points.
        '''
        x1, y1 = beginning[0], beginning[1]
        x2, y2 = end[0], end[1]

        distance = abs(x1 - x2) + abs(y1 - y2)
        
        return distance
    
    def min_distance(self, selected_batteries, house):
        '''
        Selects the battery closest to the selected house with enough capacity left.
        '''
        distance_dict = {}
        beginning = house.pos_x, house.pos_y

        # Calculate manhattan distance for all batteries with enough capacity
        for option in selected_batteries:
            end = option.pos_x, option.pos_y
            distance = self.manhattan_distance(beginning, end)
            distance_dict[option] = distance

        # Check if there are any batteries left with enough capacity
        if distance_dict:
            # Saving closest battery 
            best_battery = min(distance_dict, key = distance_dict.get)

            return best_battery
        
        else:
            # Invalid solution; no batteries left
            print("No valid batteries found")
            
            return None

    def closest_connection(self, house, district):
        '''
        Connects a house to the closest battery with enough capacity left.
        '''
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

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[selected_battery].append(house)

            # Update battery capacity
            house.battery.update_capacity(house)

    def options_within_lookahead(self, current_pos, look_ahead):
        """
        Returns a list of options within the lookahead range from the current position.
        """
        options = set([(current_pos[0], current_pos[1])])

        for _ in range(look_ahead):
            new_options = set()
            
            for option in options:
                x, y = option
                new_options.add((x + 1, y))
                new_options.add((x - 1, y))
                new_options.add((x, y + 1))
                new_options.add((x, y - 1))
            
            options = new_options 

        return options

    def choose_step_greedily(self, options, cable_end_pos):
        """
        Calculates Manhattan distance for each cablesegment option, selects the option that minimizes .
        """
        distances = {}

        for option in options:
            distance = self.manhattan_distance(option, cable_end_pos)

            distances[option] = distance

        self.new_pos = min(distances, key = distances.get)


    def lay_cable_route(self, house, look_ahead):
        '''
        Lays cable route from house to selected battery.
        '''
        # Starting position of current pos and cable route is the house position
        self.current_pos = (house.pos_x, house.pos_y)
        house.cables = [self.current_pos]

        # end position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # keep generating and adding cable segments untill battery is reached
        while self.current_pos != cable_end_pos:
            # Determine possible steps with look ahead feature
            possible_options = self.options_within_lookahead(self.current_pos, look_ahead)

            # Choose step from options
            self.choose_step_greedily(possible_options, cable_end_pos)

            # add new step (cable point coordinates) to cable route
            house.cables.append(self.new_pos)
            
            # after the step, the current position becomes the previous position
            self.prev_pos = self.current_pos

            # after the step, the new position becomes the current position
            self.current_pos = self.new_pos