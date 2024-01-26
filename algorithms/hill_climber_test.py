import math

class HillClimber():
    def __init__(self, district):
        self.district = district

    def manhatten_distance(self, point1, point2):
        """Calculate manhatten distance between two points."""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        

    def calculate_shortest_distances(self, points):
        """Calculate distances between coordinates (points on grid)."""
        distances = {}

        for i in points:
            shortest_distance = float("inf")
            for j in points:
                if j != i:
                    point1 = (i.pos_x, i.pos_y)
                    point2 = (j.pos_x, j.pos_y)
                    distance = self.manhatten_distance(point1, point2)
            
                    # Keep track of shortest distance
                    if distance < shortest_distance:
                        shortest_distance = distance
            
            distances[(point1, point2)] = shortest_distance
        
        print(distances)


    