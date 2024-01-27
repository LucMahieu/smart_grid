
import matplotlib.pyplot as plt
import time
import random
from classes.district import District
from classes.house import House

class HillClimber():
    def __init__(self, district):
        self.district = district


    def run(self, houses):    
        shortest_connections = self.calculate_shortest_connections(houses)
        sorted_connections = self.sort_dict(shortest_connections)
        
        # Lay cable routes between houses and batteries
        layed_cables = {}
        for connection in sorted_connections:
            cable_route = self.lay_cable_route(connection)
            # Add cable route to dictionary of cable routes per connection
            layed_cables[connection] = cable_route
        # print(layed_cables)
        clusters = self.cluster_connections(layed_cables)
        # self.plot_clusters(clusters)
        connection_points = self.find_shortest_connections_between_clusters(clusters) #TODO: remove connection points part
        print(connection_points)
        self.plot_clusters(clusters, custom_color="red")
        self.plot_clusters(connection_points) #TODO: remove connection points part
        # Show plot
        plt.show()
    

    def find_shortest_connections_between_clusters(self, clusters):
        """Finds shortest connection to other cluster for each cluster."""
        shortest_connections = {}
        connection_points = [set()]
        for cluster in clusters:
            shortest_connection = float("inf")
            for other_cluster in clusters:
                if cluster != other_cluster:
                    for point1 in cluster:
                        for point2 in other_cluster:
                            manhatten_distance = self.manhatten_distance(point1, point2)
                            if manhatten_distance < shortest_connection:
                                shortest_connection = manhatten_distance
                                begin_point = point1
                                end_point = point2

            # Add shortest connection to dictionary
            connection_points[0].update([begin_point, end_point])
            shortest_connections[(begin_point, end_point)] = shortest_connection
        
        return connection_points
    

    def plot_clusters(self, clusters, custom_color=None):
        """Plot all the clusters as points in a different color on a grid."""

        # Create a list of colors for each cluster
        colors = ['green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black', 'grey', 'brown']

        # Iterate over each cluster and assign a color
        for i, cluster in enumerate(clusters):
            # Extract x and y coordinates of each point in the cluster
            x = [point[0] for point in cluster]
            y = [point[1] for point in cluster]
            
            # Determines if the clusters are plotted in different colors or not
            if custom_color == None:
                # Plot the cluster as points on a grid with the assigned color
                plt.scatter(x, y, color=colors[i % len(colors)])
            else:
                plt.scatter(x, y, color=custom_color)

        # Set labels and title
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Cluster Plot')


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
        clusters = []

        for connection, cables in connections.items():
            start_point = connection[0]
            end_point = connection[1]
            found_clusters = []

            # Zoek de clusters waarin de begin- en eindpunten zich bevinden
            for cluster in clusters:
                if start_point in cluster or end_point in cluster:
                    found_clusters.append(cluster)

            # Voeg de gevonden clusters samen, als er meerdere zijn
            if found_clusters:
                merged_cluster = set.union(*found_clusters)
                # Add starting and end point to merged cluster
                merged_cluster.update([start_point, end_point])
                # Add cable route to merged cluster
                merged_cluster.update(cables)
                clusters = [cluster for cluster in clusters if cluster not in found_clusters]
                clusters.append(merged_cluster)
            else:
                # Maak een nieuw cluster als geen van de punten in een bestaand cluster zit
                new_cluster = {start_point, end_point, *cables}
                clusters.append(new_cluster)


        return clusters


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
    

class cable():
    def __init__(self, connection, cable_route):
        self.connection = connection
        self.cable_route = cable_route
        self.cluster = None

if __name__ == "__main__":
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    hill_climber = HillClimber(district1)
    # house1 = ((30, 4), (30, 2))
    # house2 = ((4, 38), (5, 37))
    # cable_route = hill_climber.lay_cable_route(house2)
    
    # Create list of house objects with random coordinates
    # houses = []
    # for i in range(10):
    #     hill_climber.houses.append(House(random.randint(0, 50), random.randint(0, 50), 1))

    hill_climber.run(district1.houses)
    # for i in range(3):
    #     # Run hill climber algorithm
    #     hill_climber.run(district1.houses)
    
    
    

    
# ----------------- OLD CODE ----------------- #


                        # # Check all clusters to see if one of them contains the begin_point and add if not so
                        # found_cluster = False
                        # for cluster in clusters:
                        #     print(f"Current cluster: {cluster}")
                        #     if cluster == set():
                        #         # Print new points added to empty cluster
                        #         print(f"Start the first cluster with points {begin_point} and {end_point}")
                        #         cluster.add(begin_point)
                        #         cluster.add(end_point)
                        #         found_cluster = True
                        #         break
                            
                        #     if begin_point in cluster:
                        #         # Print new begin_point added to existing cluster
                        #         print(f"New begin_point: {begin_point}")
                        #         cluster.add(end_point)
                        #         found_cluster = True
                        #         break # break out of the for loop to prevent from adding the same point over and over again
                            
                        #     if end_point in cluster:
                        #         # Print new end_point added to existing cluster
                        #         print(f"New end_point: {end_point}")
                        #         cluster.add(begin_point)
                        #         found_cluster = True
                        #         break

                        #     # Merge clusters if they have a shared point
                        #     for cluster2 in clusters:
                        #         if begin_point in cluster and end_point in cluster2:
                        #             # Print merge clusters
                        #             print(f"Merge clusters {cluster} and {cluster2}")
                        #             cluster.add(cluster2)
                        #             clusters.remove(cluster2)
                        #             break
                        
                        # if found_cluster == False:
                        #     print(f"Found new cluster with points {begin_point} and {end_point}")
                        #     clusters.append({begin_point, end_point})                           

    # def cluster_connections(self, connections):
    #     clusters = []

    #     for start_point, end_point in connections:
    #         found_clusters = []

    #         # Zoek de clusters waarin de begin- en eindpunten zich bevinden
    #         for cluster in clusters:
    #             if start_point in cluster or end_point in cluster:
    #                 found_clusters.append(cluster)

    #         # Voeg de gevonden clusters samen, als er meerdere zijn
    #         if found_clusters:
    #             merged_cluster = set.union(*found_clusters)
    #             merged_cluster.update([start_point, end_point])
    #             clusters = [cluster for cluster in clusters if cluster not in found_clusters]
    #             clusters.append(merged_cluster)
    #         else:
    #             # Maak een nieuw cluster als geen van de punten in een bestaand cluster zit
    #             clusters.append({start_point, end_point})

    #     return clusters