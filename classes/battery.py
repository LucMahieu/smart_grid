class Battery():
        
    def __init__(self, pos_x_batt, pos_y_batt, capacity):
        self.pos_x_batt = pos_x_batt
        self.pos_y_batt = pos_y_batt
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
            