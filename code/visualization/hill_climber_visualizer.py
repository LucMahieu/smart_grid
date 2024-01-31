from code.algorithms.hill_climber import HillClimber
import matplotlib.pyplot as plt

def setup_plot(max_x_value, max_y_value):
        """
        Initialise the plot out of loop so plot gets updated.
        """
        plt.figure(figsize=(6, 6))
        ax = plt.gca()

        # Create grid lines with 5 interval spacing
        ax.set_xticks(range(0, max_x_value + 1, 5)) # major
        ax.set_xticks(range(0, max_x_value + 1, 5)) # major

        # Create gridlines with 1 interval spacing
        ax.set_xticks(range(0, max_x_value + 1), minor=True)
        ax.set_yticks(range(0, max_y_value + 1), minor=True)
        ax.grid(True)
        
        # Adjust transparancy of gridlines with alpha
        ax.grid(which='major', alpha=0.5) # the gridlines with interval of 5
        ax.grid(which='minor', alpha=0.2)

        return ax
    

def plot_network(district, result):
    """
    Plots end result of the algorithm including all cables, houses, and 
    batteries on the grid.
    """
    ax = setup_plot(50, 50)

    # Extract x and y coordinates of each point in the whole cable route
    x = [point[0] for point in result.all_cables]
    y = [point[1] for point in result.all_cables]

    ax.plot(
        x, y, marker='o', 
        linestyle='None', 
        color='black', 
        markersize=3
    )

    colors = ['orange', 'purple', 'grey', 'red', 'green']
    
    # Plot each battery with its assigned houses in a different color
    for i, battery in enumerate(district.batteries):
        houses = district.battery_houses_connections[battery]
        
        # Extract x and y coordinates of each point in the cluster
        x = [house.pos_x for house in houses]
        y = [house.pos_y for house in houses]

        chosen_color = colors[i]

        # Plot the house cluster as points on a grid with the assigned color
        ax.plot(
            x, y, 
            color=chosen_color, 
            marker='o', 
            linestyle='None', 
            markersize=6
        )

        # Plot the batteries in color corresponding to houses
        ax.plot(
            battery.pos_x, 
            battery.pos_y, 
            color=chosen_color, 
            marker='s', 
            markersize=15)

    plt.show()