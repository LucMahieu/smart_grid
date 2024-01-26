import math
import random

class HillClimber():
    def __init__(self): #TODO: readd district as parameter
        # self.district = district
        pass

    def run(self):
        calculate_shortest_distances = self.calculate_shortest_distances(self.district.houses)
        sorted_distances = self.sort_dict(calculate_shortest_distances)
        layed_cables = self.lay_cables(sorted_distances)

    def manhatten_distance(self, point1, point2):
        """Calculate manhatten distance between two points."""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        

    def calculate_shortest_distances(self, points):
        """Calculate distances between coordinates (points on grid)."""
        distances = {}

        # Make combinations of all points and calculate distances
        for i in points:
            shortest_distance = float("inf")
            for j in points:
                if j != i:
                    # Make tuples of coordinates
                    point1 = (i.pos_x, i.pos_y)
                    point2 = (j.pos_x, j.pos_y)

                    distance = self.manhatten_distance(point1, point2)
            
                    # Keep track of shortest distance
                    if distance < shortest_distance:
                        shortest_distance = distance
                        begin_point = point1
                        end_point = point2
            
            distances[(begin_point, end_point)] = shortest_distance
        
        return distances
    
    def lay_cables(self, distances):
        for cable in distances:
            self.lay_cable_route(cable)


    def sort_dict(self, dictionary):
        """Sort dictionary by value."""
        return dict(sorted(dictionary.items(), key=lambda x: x[1]))
    
    def choose_x_y_lines(self, cable):
        """Determine what will be the y-line and x-line of cable route between points.
        These are the outer lines of the manhatten distance domain between the points.
        Its value is either the x or y coordinate of the begin or end point."""
        
        begin_point = cable[0]
        end_point = cable[1]

        y_line = random.choice((begin_point[1], end_point[1]))
        # After the y_line is choosen, the x_line is always the other coordinate
        if y_line == begin_point[1]:
            x_line = end_point[0]
        else:
            x_line = begin_point[0]
        
        return y_line, x_line


    def lay_cable_route(self, cable):
        """Lay cable routes between points."""
        begin_point = cable[0]
        end_point = cable[1]

        y_line, x_line = self.choose_x_y_lines(cable)
        
        # Initialize horizontal cable route between points
        horizontal_cable = set()

        # Initialize vertical cable route between points
        delta_x = end_point[0] - begin_point[0]
        for x in range(delta_x + 1):
            if delta_x < 0:
                horizontal_cable.add((begin_point[0] - x, y_line))
            else:
                horizontal_cable.add((begin_point[0] + x, y_line))

        # Initialize vertical cable route between points
        vertical_cable = set()

        # Determine relative position of end point to begin point
        delta_y = end_point[1] - begin_point[1]
        for y in range(delta_y + 1):
            if delta_y < 0:
                vertical_cable.add((x_line, begin_point[1] - y))
            else:
                vertical_cable.add((x_line, begin_point[1] + y))

        # Merge vertical and horizontal cable routes
        cable_route = horizontal_cable.union(vertical_cable)

        return cable_route
            

if __name__ == "__main__":
    hill_climber = HillClimber()
    hill_climber.lay_cable_route(((1, 2), (3, 4)))
