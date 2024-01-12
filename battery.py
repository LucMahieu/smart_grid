class Battery():
        
    def __init__(self, position_x, position_y, capacity):
        self.position_x = position_x
        self.position_y = position_y
        self.capacity = capacity
        # list that keeps track of connected housess
        self.connected_houses = []
        self.connected_cables = []

            
    def capacity_limit(self):
        """
        Calculates the output the battery recieves from the houses,
        and checks if the capacity limit of the battery is exceeded.
        """
        total_output = sum(house.max_output for house in self.connected_houses)
        return total_output > self.capacity
            
