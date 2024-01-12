class House:
    def __init__(self, pos_x_house, pos_y_house, max_output):
        self.pos_x_house = pos_x_house
        self.pos_y_house = pos_y_house
        self.max_output = max_output
        self.battery = None

    # calculates mmanhattan distance between this house and another house
    def calculate_distance(self, other_house):
        return abs(self.pos_x_house - other_house.pos_x_house) + abs(self.pos_y_house - other_house.pos_y_house)
