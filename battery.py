class Battery():
        
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        # list that keeps track of connected houses
        self.connected_houses = []
        self.connected_cables = []

            
    def capacity_limit(self):
        """
        Calculates the output the battery recieves from the houses,
        and checks if the capacity limit of the battery is exceeded.
        """
        total_output = sum(house.max_output for house in self.connected_houses)
        return total_output > self.capacity
            
