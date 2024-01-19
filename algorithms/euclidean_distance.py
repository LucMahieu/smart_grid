import math
import random
import copy

class Greedy_algo():
    def __init__(self, grid_size=50):
        self.grid_size = grid_size
        self.create_outer_grid()
        self.prev_pos = ()

    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''

        # houses_copy = copy.deepcopy(district.houses)
        # random.shuffle(houses_copy)
        # random_house_order = houses_copy
        # print(random_house_order)

        for house in district.houses:
            
            # connect house to closest battery with capacity
            self.closest_connection(house, district)

            #self.lay_cable_route(house)

        print(district.battery_houses_connections)

        return district
    
    def euclidean_distance(self, house, battery):
        '''
        Calculates Euclidean distance between battery and house.
        '''
        x1, y1 = house.pos_x, house.pos_y
        x2, y2 = battery.pos_x, battery.pos_y

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        return distance
    
    def min_distance(self, selected_batteries, house):
        '''
        Saves dictionary with closest battery with capacity leftfor selected house.
        '''
        distance_dict = {}
        for option in selected_batteries:
            distance = self.euclidean_distance(house, option)
            distance_dict[option] = distance

        # Check if there are batteries left with enough capacity
        if distance_dict:

            # Saving battery with the shortest distance to selected house
            best_battery = min(distance_dict, key = distance_dict.get)

            return best_battery
        
        else:
            print("No valid batteries found")
            
            return None

    def closest_connection(self, house, district):
        '''
        Connects a house to the closest battery with enough capacity left.
        '''
        # create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # check if battery has enough capacity
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

            # Updating capacity
            house.battery.update_capacity(house)

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

        # print(f'all options: {self.options}')
        # print(f'current pos: {self.current_pos}')

        # remove step options that are in outer grid or that go back to previous position
        for option in self.options.copy():
            if option in self.outer_grid or option == self.prev_pos:
                if option in self.options:
                    self.options.remove(option)

        # check if there are still options left
        if not self.options:
            print(f'no netto options left at current position: {self.options}')


    def choose_step_randomly(self):
        """
        Chooses randomly where to lay a single new cablesegment within 50 x 50 grid.
        """
        self.new_pos = random.choice(list(self.options))


    def lay_cable_route(self, house):
        '''
        Lays cable route from house to selected battery.
        '''
        if house.battery is None:
            print(f"Error: No valid battery found for house {house}. Cable route cannot be laid.")
            return
        # starting position of current pos and cable route is the house position
        self.current_pos = (house.pos_x, house.pos_y)
        house.cables = [self.current_pos]

        # end position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # keep generating and adding cable segments untill battery is reached
        while self.current_pos != cable_end_pos:
            # determine possible steps
            self.determine_possible_steps()

            # choose step from options
            self.choose_step_randomly()

            # print the log if the new pos exceeds the grid size
            if self.new_pos[0] > self.grid_size or self.new_pos[1] > self.grid_size or self.new_pos[0] < 0 or self.new_pos[1] < 0:
                print(f'new pos: {self.new_pos}')
                print(f'prev pos: {self.prev_pos}')
                print(f'current pos: {self.current_pos}')
                print(f'cable route: {house.cables}')
                print(f'options: {self.options}')
                print(f'outer grid: {self.outer_grid}')
                print('-----------------------------------')

            # add new step (cable point coordinates) to cable route
            house.cables.append(self.new_pos)
            
            # after the step, the current position becomes the previous position
            self.prev_pos = self.current_pos

            # after the step, the new position becomes the current position
            self.current_pos = self.new_pos