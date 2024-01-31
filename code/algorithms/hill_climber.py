import matplotlib.pyplot as plt
import random
from ..classes.district import District
from .algorithm import Greedy
from archive.export_json import export_json
#from visualization.visualizegrid import visualize_grid
import json

class HillClimber():
    def __init__(self, district):
        self.district = district
        self.layed_cables = {battery: {} for battery in self.district.batteries}
        self.clusters = {battery: [] for battery in self.district.batteries}
        self.current_battery = None
        self.all_cables = set()
        self.cable_networks = {battery: set() for battery in self.district.batteries}


    def run(self, plot_results=False):
        """
        Runs all steps involved in the hill climber algorithm.
        """
        # Assign houses to batteries with the greedy algorithm
        for house in self.district.houses:
            greedy = Greedy()
            greedy.assign_battery_to_house(self.district, house)

        # Lay cable network for each battery
        for battery in self.district.batteries:

            # Save current battery as attribute for later use
            self.current_battery = battery
  
            # Select houses assigned to current battery
            current_houses = self.district.battery_houses_connections[battery]

            # Connect houses with shortest connections first
            shortest_connections = self.calculate_shortest_connections(current_houses)
            sorted_connections = self.sort_dict(shortest_connections)
            
            for connection in sorted_connections:
                self.hill_climber(connection)

            # Make clusters of connected houses
            self.cluster_connections()
            self.find_shortest_connections_between_clusters()
            
            # Lay cable routes between clusters
            for connection in self.connections:
                # self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(connection)
                self.hill_climber(connection)
            
            while len(self.clusters[self.current_battery]) > 1:
                self.cluster_connections()
                self.find_shortest_connections_between_clusters()
                
                for connection in self.connections:
                    # self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(connection)
                    self.hill_climber(connection)

            shortest_connection = self.calculate_shortest_distance_to_battery()
            self.layed_cables[self.current_battery][connection] = self.lay_cable_connection(shortest_connection)

            # Add all cable routes for this battery to first house of battery (for export_json to work)
            current_houses[0].cables = self.layed_cables[self.current_battery]

            # Collect all cables for this battery
            self.collect_network_cables()

            # Calculate cost of cable routes for this battery and add to total
            self.district.district_cost_shared += self.calculate_network_cost(self.cable_networks[self.current_battery])
        
        if plot_results == True:
            self.setup_plot()
            self.plot_network()
        
        # Reset state of district after each run
        self.district.reset_state()


    def collect_all_cables(self):
        """
        Collects all cables from all battery networks in order to plot function.
        """
        for battery in self.district.batteries:
            self.all_cables.update(self.cable_networks[battery])


    def hill_climber(self, connection):
        """
        Tries to lay two possible cable routes between houses, clusters or batteries 
        and chooses the best one in terms of lowest costs.
        """
        # Lay two possible cable routes between entities
        cable_route1 = self.lay_cable_connection(connection, "beginpoint_y_route")
        cable_route2 = self.lay_cable_connection(connection, "endpoint_y_route")

        possible_cable_network1 = self.cable_networks[self.current_battery].copy()
        possible_cable_network1.update(cable_route1)

        possible_cable_network2 = self.cable_networks[self.current_battery].copy()
        possible_cable_network2.update(cable_route2)

        # Calculate cost of both cable networks
        cost_network1 = self.calculate_network_cost(possible_cable_network1)
        cost_network2 = self.calculate_network_cost(possible_cable_network2)

        # Choose cable route that results in lowest cable network cost
        if cost_network1 < cost_network2:
            self.layed_cables[self.current_battery][connection] = cable_route1
        else:
            self.layed_cables[self.current_battery][connection] = cable_route2


    def calculate_shortest_distance_to_battery(self):
        """
        Calculates shortest way to connect a battery and then lay cable from 
        cable to battery.
        """
        shortest_distance = float("inf")
        connection = {}
        for cable_point in self.layed_cables[self.current_battery]:
            battery_point = (self.current_battery.pos_x, self.current_battery.pos_y)

            distance = self.manhattan_distance(cable_point[0], battery_point)

            if distance < shortest_distance:
                shortest_distance = distance
                begin_point = cable_point[0]
                end_point = battery_point

        return (begin_point, end_point)


    def calculate_network_cost(self, cable_route):
        """
        Calculates the cost of the shared cables.
        """
        return (len(cable_route) - 1) * 9 + 5000
            

    def setup_plot(self, max_x_value=50, max_y_value=50):
        """
        Initialise the plot out of loop so plot gets updated.
        """
        plt.figure(figsize=(6, 6))
        self.ax = plt.gca()

        # Create grid lines with 5 interval spacing
        self.ax.set_xticks(range(0, max_x_value + 1, 5)) # major
        self.ax.set_xticks(range(0, max_x_value + 1, 5)) # major

        # Create gridlines with 1 interval spacing
        self.ax.set_xticks(range(0, max_x_value + 1), minor=True)
        self.ax.set_yticks(range(0, max_y_value + 1), minor=True)
        self.ax.grid(True)
        
        # Adjust transparancy of gridlines with alpha
        self.ax.grid(which='major', alpha=0.5) # the gridlines with interval of 5
        self.ax.grid(which='minor', alpha=0.2)
    

    def plot_network(self):
        """
        Plots end result of the algorithm including all cables, houses, and 
        batteries on the grid.
        """
        # Collect all cables from all battery networks to plot
        self.collect_all_cables()

        # Extract x and y coordinates of each point in the whole cable route
        x = [point[0] for point in self.all_cables]
        y = [point[1] for point in self.all_cables]

        self.ax.plot(
            x, y, marker='o', 
            linestyle='None', 
            color='black', 
            markersize=3
        )

        colors = ['orange', 'purple', 'grey', 'red', 'green']
        
        # Plot each battery with its assigned houses in a different color
        for i, battery in enumerate(self.district.batteries):
            houses = self.district.battery_houses_connections[battery]
            
            # Extract x and y coordinates of each point in the cluster
            x = [house.pos_x for house in houses]
            y = [house.pos_y for house in houses]

            chosen_color = colors[i]

            # Plot the house cluster as points on a grid with the assigned color
            self.ax.plot(
                x, y, 
                color=chosen_color, 
                marker='o', 
                linestyle='None', 
                markersize=6
            )

            # Plot the batteries in color corresponding to houses
            self.ax.plot(
                battery.pos_x, 
                battery.pos_y, 
                color=chosen_color, 
                marker='s', 
                markersize=15)

        plt.show()


    def collect_network_cables(self):
        """Collects all cables that belong to the current battery (network)."""
        for cable_route in self.layed_cables[self.current_battery].values():
            self.cable_networks[self.current_battery].update(cable_route)


    def find_shortest_connections_between_clusters(self):
        """
        Finds shortest connection to other cluster for each cluster.
        """
        # Store clusters in variable for cleaner code
        clusters = self.clusters[self.current_battery]

        # For each cluster, calculate the shortest connection to another cluster
        for cluster in clusters:
            shortest_connection = float("inf")
            for other_cluster in clusters:
                if cluster != other_cluster:
                    for point1 in cluster:
                        for point2 in other_cluster:
                            manhattan_distance = self.manhattan_distance(point1, point2)
                            if manhattan_distance < shortest_connection:
                                shortest_connection = manhattan_distance
                                begin_point = point1
                                end_point = point2

            # For each cluster add shortest connection to dictionary
            if shortest_connection != float("inf"):
                self.connections = {}
                self.connections[(begin_point, end_point)] = shortest_connection
            else:
                break


    def manhattan_distance(self, point1, point2):
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

                    distance = self.manhattan_distance(point1, point2)
            
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
    

    def choose_x_y_lines(self, cable, route_direction):
        """Determine what will be the y-line and x-line of cable route between points.
        These are the outer lines of the manhatten distance domain between the points.
        Its value is either the x or y coordinate of the begin or end point."""
        
        begin_point = cable[0]
        end_point = cable[1]

        if route_direction is None:
            # Choose random direction
            y_line = random.choice((begin_point[1], end_point[1]))
        
        if route_direction == "beginpoint_y_route": # The cable uses the y coordinate of the begin point for one of the cable segments
            y_line = begin_point[1]
        elif route_direction == "endpoint_y_route":
            y_line = end_point[1]
        
        # After the y_line is choosen, the x_line is always the other coordinate
        if y_line == begin_point[1]:
            x_line = end_point[0]
        else:
            x_line = begin_point[0]
        
        return y_line, x_line


    def lay_cable_connection(self, connection, route_direction=None):
        """Lays cable route between two points."""
        begin_point = connection[0]
        end_point = connection[1]

        y_line, x_line = self.choose_x_y_lines(connection, route_direction)
        
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
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    hill_climber = HillClimber(district2)
    hill_climber.run()