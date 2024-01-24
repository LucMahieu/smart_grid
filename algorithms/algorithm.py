import random 

class BaseAlgorithm():
    def __init__(self):
        self.prev_pos = ()

    def run(self, district):

        for house in district.houses:

            self.assign_battery_to_house(district, house)
            self.lay_cable_route(house)

        return district

    def assign_battery_to_house(self, district, house):

        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # Check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:

            selected_battery = self.select_battery(batteries_with_capacity)
            house.battery = selected_battery

    
    def select_battery(self, batteries_with_capacity):

        # Default implementation: Select the first battery with capacity

        if batteries_with_capacity:

            return batteries_with_capacity[0]
        
        else:
            return None

    def determine_possible_steps(self):
        '''
        Determines possible positions for the next step.
        '''
        # possible absolute steps
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # define step options based on current position
        self.options = set()
        for position in [right, left, up, down]:
            self.options.add((self.current_pos[0] + position[0], self.current_pos[1] + position[1]))

        # remove step options that are in outer grid or that go back to previous position
        for option in self.options.copy():
            if option in self.outer_grid or option == self.prev_pos:
                if option in self.options:
                    self.options.remove(option)

        # check if there are still options left
        if not self.options:
            print(f'no netto options left at current position: {self.options}')

    def lay_cable_route(self, house):
        self.current_pos = (house.pos_x, house.pos_y)
        house.cables = [self.current_pos]

        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        while self.current_pos != cable_end_pos:
            self.determine_possible_steps()
            self.choose_step(house, cable_end_pos)
            house.cables.append(self.new_pos)
            self.prev_pos = self.current_pos
            self.current_pos = self.new_pos


class GreedyAlgorithm(BaseAlgorithm):
    
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

    def select_battery(self, house, district):
        '''
        Connects a house to the closest battery with enough capacity left.
        '''
        # Connecting to closest battery with capacity
        selected_battery = self.min_distance(batteries_with_capacity, house)

        # Update the house's battery attribute
        house.battery = selected_battery

        # Add current house to the list of houses that are connected to the selected battery
        district.battery_houses_connections[selected_battery].append(house)

        # Update battery capacity
        house.battery.update_capacity(house)
    
    def choose_step(self, options, cable_end_pos):
        """
        Calculates Manhattan distance for each cablesegment option, selects the option that minimizes .
        """
        distances = {}

        for option in options:
            distance = self.manhattan_distance(option, cable_end_pos)

            distances[option] = distance

        self.new_pos = min(distances, key = distances.get)


class RandomAlgorithm(BaseAlgorithm):
    def __init__(self, grid_size=50):
        self.grid_size = grid_size
        self.create_outer_grid()
        
    def select_battery(self):
        random_battery = random.choice(batteries_with_capacity)
        house.battery = random_battery

    def choose_step(self):
        """
        Chooses randomly where to lay a single new cablesegment within 50 x 50 grid.
        """
        self.new_pos = random.choice(list(self.options))

    def create_outer_grid(self):
        """
        Creates a set of points that are just outside the grid. These points are used to 
        check if a step is within the grid or not.
        """
        self.outer_grid = set()

        for x in range(-1, self.grid_size + 1):
            self.outer_grid.add((x, -1))  # points just below the bottom row
            self.outer_grid.add((x, self.grid_size + 1))  # points just above the top row
        
        for y in range(-1, self.grid_size + 1):
            self.outer_grid.add((-1, y))  # points just left of the leftmost column
            self.outer_grid.add((self.grid_size + 1, y))  # points just right of the rightmost column