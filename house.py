class House:
    def __init__(self, x_position, y_position, max_output):
        self.x_position = x_position
        self.y_position = y_position
        self.max_output = max_output
        self.battery = None

    # calculates mmanhattan distance between this house and another house
    def calculate_distance(self, other_house):
        return abs(self.x_position - other_house.x_position) + abs(self.y_position - other_house.y_position)
