import random

class Breath_first():
    def __init__(self, depth):
        self.prev_pos = ()
        self.depth = 3

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

    def child_cable(self, house, options):
        queue = queue.Queue()

        # Adding begin state to queue
        queue.put(house.pos_x, house.pos_y)

        while not queue.empty():
            state = queue.get()

            # stop when depth is reached
            if len(state) < depth:

                for i in self.options:
                    child = copy.deepcopy(state)
                    child += i
                    queue.put(child)

        def determine_possible_steps(self):

        right = (1, 0)
        left = (-1, 0)
        up = (0, 1)
        down = (0, -1)

        # Define step options based on current position
        self.options = set()
        for position in [right, left, up, down]:
            self.options.add((self.current_pos[0] + position[0], self.current_pos[1] + position[1]))