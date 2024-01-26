import random

class Baseline_old():
    def __init__(self):
        self.prev_pos = ()

    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''
        # # Random order of houses
        # random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to random battery with capacity
            self.random_connection(house, district)
            
            # If no battery available with enough capacity
            if house.battery == None:
                print("Invalid solution")
                break 
                return False 
            
            else:
                # Lays cable route based on steps that minimize distance
                self.lay_cable_route(house)

        return district
    
    def manhattan_distance(self, beginning, end):
        '''
        Calculates Manhattan distance between two points.
        '''
        x1, y1 = beginning[0], beginning[1]
        x2, y2 = end[0], end[1]

        distance = abs(x1 - x2) + abs(y1 - y2)
        
        return distance
    
    def random_connection(self, house, district):
        '''
        Assigns battery to current house and adds them to the list of connected houses.
        '''
        # make copy of batteries list to keep track of batteries that have been tried
        batteries = district.batteries.copy()

        # create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in batteries:
            # check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:
            # select random battery from the list of batteries with enough capacity
            random_battery = random.choice(batteries_with_capacity)

            # add current battery to the house
            house.battery = random_battery

            # Update battery capacity
            house.battery.update_capacity(house)

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[random_battery].append(house)

    def determine_possible_steps(self):
        '''
        Determines possible positions for the next step.
        '''
        # Possible absolute steps
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # Define step options based on current position
        self.options = set()
        for position in [right, left, up, down]:
            self.options.add((self.current_pos[0] + position[0], self.current_pos[1] + position[1]))


    def choose_step(self, options, cable_end_pos):
        """
        Calculates Manhattan distance for each cablesegment option, selects the option that minimizes .
        """
        distances = {}

        for option in options:
            distance = self.manhattan_distance(option, cable_end_pos)

            distances[option] = distance

        self.new_pos = min(distances, key = distances.get)

    def lay_cable_route(self, house):
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
            # determine possible steps
            self.determine_possible_steps()

            # choose step from options
            self.choose_step(self.options, cable_end_pos)

            # add new step (cable point coordinates) to cable route
            house.cables.append(self.new_pos)
            
            # after the step, the current position becomes the previous position
            self.prev_pos = self.current_pos

            # after the step, the new position becomes the current position
            self.current_pos = self.new_pos