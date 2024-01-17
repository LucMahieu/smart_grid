import random

class Random_algo():
    def __init__(self, grid_size=50):
        self.grid_size = grid_size
        self.create_outer_grid()
        self.prev_pos = ()


    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''
        # connect houses with batteries
        for house in district.houses:
            district.battery_houses_connections
            self.assign_battery_to_house(district, house)
            self.lay_cable_route(house)
    
        return district
    

    def create_outer_grid(self):
        """
        Creates a set of points that are just outside the grid. These points are used to 
        check if a step is within the grid or not.
        """
        self.outer_grid = set()

        for x in range(1, self.grid_size + 1):
            self.outer_grid.add((x, 0))  # points just above the top row
            self.outer_grid.add((x, self.grid_size + 1))  # points just below the bottom row
        
        for y in range(1, self.grid_size + 1):
            self.outer_grid.add((0, y))  # points just left of the leftmost column
            self.outer_grid.add((self.grid_size + 1, y))  # points just right of the rightmost column


    def assign_battery_to_house(self, district, house):
        '''
        Assigns battery to current house and adds them to the list of connected houses.
        '''
        # make copy of batteries list to keep track of batteries that have been tried
        batteries = district.batteries.copy()

        for battery in batteries:
            # check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            # remove battery from list of batteries if it doesn't have enough capacity
            if not enough_capacity:
                batteries.remove(battery)
            else:
                # add current house to the list of houses that are connected to the selected battery
                district.battery_houses_connections[battery].append(house)
                house.battery = battery


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


    def choose_step_randomly(self):
        """
        Chooses randomly where to lay a single new cablesegment within 50 x 50 grid.
        """
        self.new_pos = random.choice(list(self.options))


    def lay_cable_route(self, house):
        '''
        Lays cable route from house to selected battery.
        '''
        # starting position of current pos and cable route is the house position
        self.current_pos = (house.pos_x, house.pos_y)
        cable_route = [self.current_pos]

        # end position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # keep generating and adding cable segments untill battery is reached
        while self.current_pos != cable_end_pos:
            # determine possible steps
            self.determine_possible_steps()

            # choose step from options
            self.choose_step_randomly()

            # add new step (cable point coordinates) to cable route
            cable_route.append(self.new_pos)
            
            # after the step, the current position becomes the previous position
            self.prev_pos = self.current_pos

            # after the step, the new position becomes the current position
            self.current_pos = self.new_pos
            
        return cable_route


#---------------------------------------------------------------------------------------------

# ARCHIVED CODE
    
    # def random_cables(self, house):
    #     '''
    #     Lay cable from house to selected battery.
    #     '''
    #     # Cable starts at house and ends at battery
    #     cable_start_x = house.pos_x
    #     cable_start_y = house.pos_y
    #     cable_end_x = house.battery.pos_x
    #     cable_end_y = house.battery.pos_y
    #     cable_route = [(cable_start_x, cable_start_y)]

    #     # starting position of cable
    #     cable_x = cable_start_x
    #     cable_y = cable_start_y

    #     # Keep generating and adding cable segments untill battery is reached
    #     while (cable_x, cable_y) != (cable_end_x, cable_end_y):
    #         # Generate random segment (step)
    #         cable_x += self.random_segment(cable_x, cable_end_x)
    #         cable_y += self.random_segment(cable_y, cable_end_y)

    #         # Add segment to cable route
    #         cable_route.append((cable_x, cable_y))
            
    #     return cable_route

    # def random_segment(self, current, end):
    #     '''
    #     Chooses randomly where to lay a single new cablesegment within 50 x 50 grid.
    #     '''
    #     # Stay in same position if battery is reached
    #     if current == end:
    #         return 0
        
    #     # Go forward or stay in same position at start of grid
    #     elif current == 0:
    #         return random.choice([0, 1])
        
    #     # Go backward or stay in same position at end of grid
    #     elif current == 50: 
    #         return random.choice([0, -1])
        
    #     # Move in any direction
    #     else:
    #         return random.choice([-1, 0, 1])


    # def random_assignment(self, district, house):
    #     '''
    #     Randomly assigns each house to a battery that meets the requirements (e.g. enough capacity).
    #     '''
    #     # make copy of batteries list to keep track of batteries that have been tried
    #     batteries = district.batteries.copy()

    #     # set enough_capacity to False to start while loop
    #     enough_capacity = False

    #     # keep selecting random battery until a battery with enough capacity is found
    #     while enough_capacity == False:

    #         # stop if no battery has enough capacity
    #         if len(batteries) == 0:
    #             print("No battery has enough capacity")
    #             break

    #         # select random battery from shrinking list of batteries
    #         selected_battery = random.choice(batteries)
    #         # selected_battery = randint(0, len(batteries) - 1)

    #         # check if battery has enough capacity and update capacity
    #         enough_capacity = selected_battery.check_capacity(house)
    #         selected_battery.update_capacity(house)
            
    #         # remove battery from list of batteries if it doesn't have enough capacity
    #         if not enough_capacity:
    #             batteries.remove(selected_battery)

    #     # add current house to the list of houses that are connected to the selected battery
    #     district.battery_houses_connections[selected_battery].append(house)

    #     return selected_battery
    