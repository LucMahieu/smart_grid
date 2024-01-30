import matplotlib.pyplot as plt
import random
from ..classes.district import District
from .algorithm import Greedy
from export_json import export_json
from ..visualization.visualizegrid import visualize_grid

class HillClimber():
    def __init__(self, district):
        self.district = district
        self.layed_cables = {battery: {} for battery in self.district.batteries}
        self.clusters = {battery: [] for battery in self.district.batteries}
        self.current_battery = None
        self.all_cables = set()


    def run(self):
        """Runs all steps involved in the hill climber algorithm."""
        
        # Assign houses to batteries with the greedy algorithm
        for house in self.district.houses:
            greedy = Greedy()
            greedy.assign_battery_to_house(self.district, house)

        # Setup plot so it can be updated while running
        self.setup_plot()

        # Lay cable routes between houses for each battery
        for battery in self.district.batteries:
            # Save current battery for later use
            self.current_battery = battery
  
            # Select houses assigned to current battery
            self.current_houses = self.district.battery_houses_connections[battery]

            # Connect houses with shortest connections first
            shortest_connections = self.calculate_shortest_connections(self.current_houses)
            sorted_connections = self.sort_dict(shortest_connections)
            
            for connection in sorted_connections:
                self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(connection)


            # Make clusters of connected houses
            self.cluster_connections()
            self.find_shortest_connections_between_clusters()
            
            # Lay cable routes between clusters
            for connection in self.connections:
                self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(connection)

            
            while len(self.clusters[self.current_battery]) > 1:
                self.cluster_connections()
                self.find_shortest_connections_between_clusters()
                
                for connection in self.connections:
                    self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(connection)
        

            shortest_connection = self.calculate_shortest_distance_to_battery()
            self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(shortest_connection)

            # Collect and save all cable routes for this battery in one set
            self.collect_all_cables()
            # Add all cable routes to first house of battery (for export_json to work)
            self.current_houses[0].cables = self.all_cables

            # Update de plot
            self.plot_network()

        # Show plot after it is finished
        plt.show()

        # # Calculate cost of shared cables
        self.calculate_cost_shared()
        print(self.district.district_cost_shared)


    def calculate_shortest_distance_to_battery(self):
        """Calculates shortest way to connect a battery and then lay cable from cable to battery."""
        shortest_distance = float("inf")
        connection = {}
        for cable_point in self.layed_cables[self.current_battery]:
            battery_point = (self.current_battery.pos_x, self.current_battery.pos_y)

            distance = self.manhatten_distance(cable_point[0], battery_point)

            if distance < shortest_distance:
                shortest_distance = distance
                begin_point = cable_point[0]
                end_point = battery_point

        return (begin_point, end_point)


    def calculate_cost_shared(self):
        """Calculates the cost of the shared cables."""
        self.district.district_cost_shared = (len(self.all_cables) - 1) * 9 + 5000 * len(self.district.batteries)
            

    def setup_plot(self):
        """Initialise the plot out of loop so plot gets updated."""
        plt.figure(figsize=(6, 6))
        self.ax = plt.gca()

        # Fill in grid
        self.ax.set_xticks(range(50))
        self.ax.set_yticks(range(50))
        self.ax.grid(True)
    

    def plot_network(self):
        """Plots all cables, houses and batteries on the grid and is used to update it while running."""
        # Extract x and y coordinates of each point in the whole cable route
        x = [point[0] for point in self.all_cables]
        y = [point[1] for point in self.all_cables]

        self.ax.plot(x, y, marker='o', linestyle='None', color='black', markersize=4)
        # plt.scatter(x, y, color='black', marker='.')

        colors = ['orange', 'purple', 'grey', 'red', 'green']
        
        # Plot each battery with its assigned houses in a different color
        for i, battery in enumerate(self.district.batteries):
            houses = self.district.battery_houses_connections[battery]
            
            # Extract x and y coordinates of each point in the cluster
            x = [house.pos_x for house in houses]
            y = [house.pos_y for house in houses]

            chosen_color = colors[i]

            # Plot the cluster as points on a grid with the assigned color
            self.ax.plot(x, y, color=chosen_color, marker='o', linestyle='None')

            # Also plot the batteries in corresponding color
            self.ax.plot(battery.pos_x, battery.pos_y, color=chosen_color, marker='s', markersize=12)

        plt.draw()
        plt.pause(3)


    def collect_all_cables(self):
        """Adds new cables to set with all cables and plots them"""
        for cable_route in self.layed_cables[self.current_battery].values():
            self.all_cables.update(cable_route)


    def find_shortest_connections_between_clusters(self):
        """Finds shortest connection to other cluster for each cluster."""
        # For convenience, store clusters in variable
        clusters = self.clusters[self.current_battery]
        self.connections = {}
        # For each cluster, calculate the shortest connection to another cluster
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

            # For each cluster add shortest connection to dictionary
            if shortest_connection != float("inf"):
                self.connections[(begin_point, end_point)] = shortest_connection
            else:
                print("No shortest connection found")
                break


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


    def cluster_connections(self):
        """Connects cables with eachother to make a bigger cluster if possible."""
        for connection, cables in self.layed_cables[self.current_battery].items():
            start_point = connection[0]
            end_point = connection[1]
            found_clusters = []
            # For convenience, store clusters in variable
            clusters = self.clusters[self.current_battery]

            # Find clusters where start and end point are in
            for cluster in clusters:
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
                self.clusters[self.current_battery] = [cluster for cluster in clusters if cluster not in found_clusters]
                # Add merged cluster to list of clusters
                self.clusters[self.current_battery].append(merged_cluster)
            else:
                # Make new cluster if start and end point are not in any cluster. Asterisk again unpacks the set of cables
                new_cluster = {start_point, end_point, *cables}
                self.clusters[self.current_battery].append(new_cluster)


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


    def lay_cable_connection(self, connection):
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
    hill_climber.run()