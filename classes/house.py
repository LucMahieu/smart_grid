class House():
    def __init__(self, pos_x, pos_y, max_output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cables = []
        self.max_output = max_output
        self.battery = None