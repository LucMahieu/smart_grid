
import matplotlib.pyplot as plt
import time
import random
from classes.district import District
from classes.house import House

class HillClimber():
    def __init__(self, district):
        self.district = district
        self.layed_cables = {}
        self.clusters = []
        self.all_cables = set()


    def run(self, houses):    
        # Connect houses with shortest connections first
        shortest_connections = self.calculate_shortest_connections(houses)
        sorted_connections = self.sort_dict(shortest_connections)
        
        for connection in sorted_connections:
            self.layed_cables[connection] = self.lay_cable_route(connection)

        self.collect_all_cables()
        self.plot_clusters([self.all_cables])

        # Make clusters of connected houses
        self.cluster_connections(self.layed_cables)
        print(self.clusters)
        connections = self.find_shortest_connections_between_clusters() #TODO: The connections are not sorted in how big the distance is between the clusters. Maybe use a different data structure for the connections?
        
        # Lay cable routes between clusters
        for connection in connections:
            self.layed_cables[connection] = self.lay_cable_route(connection)

        
        while len(self.clusters) > 1:
            self.cluster_connections(self.layed_cables)
            connections = self.find_shortest_connections_between_clusters()
            
            for connection in connections:
                self.layed_cables[connection] = self.lay_cable_route(connection)

            self.collect_all_cables()
            self.plot_clusters([self.all_cables])
    

    def collect_all_cables(self):
        """Adds new cables to set with all cables and plots them"""
        for cable_route in self.layed_cables.values():
            self.all_cables.update(cable_route)


    def find_shortest_connections_between_clusters(self):
        """Finds shortest connection to other cluster for each cluster."""
        shortest_connections = {}
        # For each cluster, calculate the shortest connection to another cluster
        for cluster in self.clusters:
            shortest_connection = float("inf")
            for other_cluster in self.clusters:
                if cluster != other_cluster:
                    for point1 in cluster:
                        for point2 in other_cluster:
                            manhatten_distance = self.manhatten_distance(point1, point2)
                            if manhatten_distance < shortest_connection:
                                shortest_connection = manhatten_distance
                                begin_point = point1
                                end_point = point2

            # Add shortest connection to dictionary
            if shortest_connection != float("inf"):
                shortest_connections[(begin_point, end_point)] = shortest_connection
            else:
                print("No shortest connection found")
                break
        
        return shortest_connections


    def plot_clusters(self, clusters, custom_color=None):
        """Plot all the clusters as points in a different color on a grid."""

        colors = ['green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black', 'grey', 'brown']

        # Iterate over each cluster and assign a color
        for i, cluster in enumerate(clusters):
            # Extract x and y coordinates of each point in the cluster
            x = [point[0] for point in cluster]
            y = [point[1] for point in cluster]
            
            # Determines if the clusters are plotted in different colors or not
            if custom_color == None:
                # Plot the cluster as points on a grid with the assigned color
                plt.scatter(x, y, color=colors[i % len(colors)], marker='.')
            else:
                plt.scatter(x, y, color=custom_color)

        # Set labels and title
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Cluster Plot')

        plt.show()


    def manhatten_distance(self, point1, point2):
        """Calculate manhatten distance between two points."""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        

    def calculate_shortest_connections(self, points):
        """Calculate distances between coordinates (points on grid) and save."""
        connections = {}

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

            connections[(begin_point, end_point)] = shortest_distance
        
        return connections


    def cluster_connections(self, connections):
        for connection, cables in connections.items():
            start_point = connection[0]
            end_point = connection[1]
            found_clusters = []

            # Find clusters where start and end point are in
            for cluster in self.clusters:
                if start_point in cluster or end_point in cluster: #TODO: check if cables are in cluster instead of start and end point only by using set.issubset() oid
                    found_clusters.append(cluster)

            # Merge clusters if they have a shared point
            if found_clusters:
                # Asterisk unpacks the list of found clusters and set.unions them into a set
                merged_cluster = set.union(*found_clusters)
                # Add starting and end point to merged cluster
                merged_cluster.update([start_point, end_point])
                # Add cable route to merged cluster
                merged_cluster.update(cables)
                # Only keep clusters that are not merged
                self.clusters = [cluster for cluster in self.clusters if cluster not in found_clusters]
                # Add merged cluster to list of clusters
                self.clusters.append(merged_cluster)
            else:
                # Make new cluster if start and end point are not in any cluster. Asterisk again unpacks the set of cables
                new_cluster = {start_point, end_point, *cables}
                self.clusters.append(new_cluster)


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


    def lay_cable_route(self, connection):
        """Lays cable route between two points."""
        begin_point = connection[0]
        end_point = connection[1]

        y_line, x_line = self.choose_x_y_lines(connection)
        
        # Initialize horizontal cable route between points
        horizontal_cable = set()

        # Initialize vertical cable route between points
        delta_x = end_point[0] - begin_point[0]
        for x in range(abs(delta_x) + 1):
            if delta_x < 0:
                horizontal_cable.add((begin_point[0] - x, y_line))
            else:
                horizontal_cable.add((begin_point[0] + x, y_line))

        # Initialize vertical cable route between points
        vertical_cable = set()

        # Determine relative position of end point to begin point
        delta_y = end_point[1] - begin_point[1]
        for y in range(abs(delta_y) + 1):
            if delta_y < 0:
                vertical_cable.add((x_line, begin_point[1] - y))
            else:
                vertical_cable.add((x_line, begin_point[1] + y))

        # Merge vertical and horizontal cable routes
        cable_route = horizontal_cable.union(vertical_cable)

        return cable_route


if __name__ == "__main__":
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    hill_climber = HillClimber(district1)
    hill_climber.run(district1.houses)