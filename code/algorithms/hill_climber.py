
import matplotlib.pyplot as plt
import random

class HillClimber:
    def __init__(self) -> None:
        self.cost_results = []
        self.current_pos = ()
        self.prev_pos = ()


    def plot_results(self):
        """Plots the cost of each iteration of the hill climber algorithm in a histogram."""
        plt.hist(self.cost_results)
        plt.xlabel("Cost")
        plt.ylabel("Number of iterations")


    def run_experiment(self, district: object, number_of_iterations: int = 10000):
        """Runs the hill climber algorithm for each district."""
        for _ in range(number_of_iterations):
            self.create_outer_grid(district)
            self.connect_houses_to_batteries(district)
            self.lay_cable_routes(district)
            cost = district.shared_costs()
            self.cost_results.append(cost)
        print(self.cost_results)


    def create_outer_grid(self, district):
        """
        Creates a set of points that are just outside the grid. These points are used to 
        check if a step is within the grid or not.
        """
        self.outer_grid = set()

        for x in range(-1, district.grid_size + 1):
            self.outer_grid.add((x, -1))  # points just below the bottom row
            self.outer_grid.add((x, district.grid_size + 1))  # points just above the top row
        
        for y in range(-1, district.grid_size + 1):
            self.outer_grid.add((-1, y))  # points just left of the leftmost column
            self.outer_grid.add((district.grid_size + 1, y))  # points just right of the rightmost column


    def connect_houses_to_batteries(self, district):
        '''
        Assigns battery to current house and adds them to the list of connected houses.
        '''
        for house in district.houses:
            # make copy of batteries list to keep track of batteries that have been tried
            batteries = district.batteries

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

                # add current battery to house
                house.battery = random_battery


    def lay_cable_routes(self, district):
        """Lays the cables from the houses to the batteries."""
        for house in district.houses:
            # starting position of current pos and cable route is the house position
            self.current_pos = (house.pos_x, house.pos_y)
            house.cables = [self.current_pos] #TODO: cable_route is intuitever dan cables

            # end position of cable is the battery position
            cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

            # keep generating and adding cable segments untill battery is reached
            while self.current_pos != cable_end_pos:
                # determine possible positions
                possible_positions = self.determine_possible_positions()

                # determine the new position based on the option with lowest cost
                self.choose_best_position()

                # add new position (cable point coordinates) to cable route
                house.cables.append(self.new_pos)
                
                # after the position, the current position becomes the previous position
                self.prev_pos = self.current_pos

                # after the position, the new position becomes the current position
                self.current_pos = self.new_pos


    def determine_possible_positions(self):
        '''
        Determines possible positions for the next step.
        '''
        # possible absolute positions
        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # define new positions based on current position
        self.positions = set()
        for position in [right, left, up, down]:
            self.positions.add((self.current_pos[0] + position[0], self.current_pos[1] + position[1]))

        # remove positions that are in outer grid or that go back to previous position
        for option in self.positions.copy():
            if option in self.outer_grid or option == self.prev_pos:
                if option in self.positions:
                    self.positions.remove(option)

        # check if there are still positions left
        if not self.positions:
            print(f'no netto positions left at current position: {self.positions}')


    def choose_best_position(self):
        """Chooses the position with the lowest cost as the new position for the next cable segment."""
        lowest_cost = float("inf")
        for position in self.positions:
            cost = self.calculate_position_cost(position)
            if cost < lowest_cost:
                lowest_cost = cost
                best_position = position

        self.new_pos = best_position


    def calculate_position_cost(self, position):
        """Calculates the cost of laying a cable at a certain position."""
        return position[0] + random.randint(0, 20) #TODO: calculate actual cost. This is only a random placeholder


if __name__ == "__main__":
    pass