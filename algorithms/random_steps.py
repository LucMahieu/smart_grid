import random

def determine_next_step(prev_x, prev_y, x, y, grid_size=50):
    # determine the possible movements
    options = []

    # determine current direction with delta x and delta y
    delta_x = x - prev_x
    delta_y = y - prev_y

    # if on left edge
    if x == 0:
        if y == grid_size:
            print("upper left corner")
            if delta_x == -1:
                options += [('down', (0, -1))]
                print("direction: left")
            elif delta_y == 1:
                options += [('right', (1, 0))]
                print("direction: up")
        elif y == 0:
            print("lower left corner")
            if delta_x == -1:
                options += [('up', (0, 1))]
                print("direction: left")
            elif delta_y == -1:
                options += [('right', (1, 0))]
                print("direction: down")
        # if on left edge, but not in a corner
        else:
            if delta_x == -1:
                options += [('up', (0, 1)), ('down', (0, -1))]
                print("direction: up or down")

    # if on right edge
    if x == grid_size:
        # if in upper right corner
        if y == grid_size:
            print("upper right corner")
            if delta_x == 1:
                options += [('down', (0, -1))]
                print("direction: right")
            elif delta_y == 1:
                options += [('left', (-1, 0))]
                print("direction: up")
        # if in lower right corner
        elif y == 0:
            print("lower right corner")
            if delta_x == 1:
                options += [('up', (0, 1))]
                print("direction: right")
            elif delta_y == -1:
                options += [('left', (-1, 0))]
                print("direction: down")
        # if on right edge, but not in a corner
        else:
            print("right edge")
            if delta_x == 1:
                options += [('up', (0, 1)), ('down', (0, -1))]
                print("direction: right")

    if not options:
        # if on top edge
        if y == grid_size:
            if delta_y == 1:
                options += [('left', (-1, 0)), ('right', (1, 0))]
                print("direction: up")
            else:
                options += [('down', (0, -1))]
                print("direction: left or right")

        # if on bottom edge
        if y == 0:
            if delta_y == -1:
                options += [('left', (-1, 0)), ('right', (1, 0))]
                print("direction: down")
            else:
                options += [('up', (0, 1))]
                print("direction: left or right")

    # if segment is not in a corner or border determine possible movements
    if not options:
        if delta_y == 0:
            # if moving right
            if delta_x == 1:
                options += [('down', (0, -1)), ('right', (1, 0)), ('up', (0, 1))]
                print("direction: right")
            # if moving left
            else:
                options += [('left', (-1, 0)), ('up', (0, 1)), ('down', (0, -1))]
                print("direction: left")   
        # if moving up
        elif delta_y == 1:
            options += [('left', (-1, 0)), ('up', (0, 1)), ('right', (1, 0))]
            print("direction: up")
        # if moving down
        else:
            options += [('left', (-1, 0)), ('down', (0, -1)), ('right', (1, 0))]
            print("direction: down")

    # choose a random option for a step
    chosen_direction, (new_x, new_y) = random.choice(options)

    return new_x, new_y

# prev_x, prev_y = 44, 25
# x, y = 44, 24

# for i in range(20):
#     print(determine_next_step(prev_x, prev_y, x, y))



# ---------------------------------------------------------------------------------------------
#     new version of random_cables in class Cable


import random

class Cable:
    def __init__(self, x, y, grid_size=50):
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.grid_size = grid_size

    def determine_possible_movements(self):
        options = []
        delta_x = self.x - self.prev_x
        delta_y = self.y - self.prev_y

        # determine possible movements based on cable's position and direction
        # if on left edge
        if self.x == 0:
            if self.y == self.grid_size:
                if delta_x == -1:
                    options += [('down', (0, -1))]
                elif delta_y == 1:
                    options += [('right', (1, 0))]
            elif self.y == 0:
                if delta_x == -1:
                    options += [('up', (0, 1))]
                elif delta_y == -1:
                    options += [('right', (1, 0))]
            else:
                if delta_x == -1:
                    options += [('up', (0, 1)), ('down', (0, -1))]

        # if on right edge
        if self.x == self.grid_size:
            if self.y == self.grid_size:
                if delta_x == 1:
                    options += [('down', (0, -1))]
                elif delta_y == 1:
                    options += [('left', (-1, 0))]
            elif self.y == 0:
                if delta_x == 1:
                    options += [('up', (0, 1))]
                elif delta_y == -1:
                    options += [('left', (-1, 0))]
            else:
                if delta_x == 1:
                    options += [('up', (0, 1)), ('down', (0, -1))]

        if not options:
            # if on top edge
            if self.y == self.grid_size:
                if delta_y == 1:
                    options += [('left', (-1, 0)), ('right', (1, 0))]
                else:
                    options += [('down', (0, -1))]

            # if on bottom edge
            if self.y == 0:
                if delta_y == -1:
                    options += [('left', (-1, 0)), ('right', (1, 0))]
                else:
                    options += [('up', (0, 1))]

        # if segment is not in a corner or border determine possible movements
        if not options:
            if delta_y == 0:
                # if moving right
                if delta_x == 1:
                    options += [('down', (0, -1)), ('right', (1, 0)), ('up', (0, 1))]
                # if moving left
                else:
                    options += [('left', (-1, 0)), ('up', (0, 1)), ('down', (0, -1))]
            # if moving up
            elif delta_y == 1:
                options += [('left', (-1, 0)), ('up', (0, 1)), ('right', (1, 0))]
            # if moving down
            else:
                options += [('left', (-1, 0)), ('down', (0, -1)), ('right', (1, 0))]

        return options
    

    def move(self):
        options = self.determine_possible_movements()
        if options:
            chosen_direction, (delta_x, delta_y) = random.choice(options)
            self.x = max(0, min(self.grid_size, self.x + delta_x))
            self.y = max(0, min(self.grid_size, self.y + delta_y))
            print(chosen_direction)
            return self.x, self.y
        else:
            return None

# usage
cable = Cable(44, 24)
for i in range(20):
    print(cable.move())