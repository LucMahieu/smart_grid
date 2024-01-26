import csv
from classes.cable import Cable
from classes.battery import Battery
from classes.house import House


class District():
    def __init__(self, name, battery_file, house_file, grid_size=50):
        self.name = name
        self.houses = []
        self.batteries = []
        self.add_houses(house_file)
        self.add_batteries(battery_file)
        self.district_cost_seperate = 0
        self.district_cost_shared = 0
        self.cable_price = 9 
        self.battery_houses_connections = {battery: [] for battery in self.batteries}
        self.invalid = 0

    def add_houses(self, house_file):
        """
        This function reads the given file, and adds the house attributes to the list of houses.
        """
        with open(house_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            # Add coordinates and output house
            for row in csv_reader:
                pos_x, pos_y, max_output = row
                self.houses.append(House(int(pos_x), int(pos_y), float(max_output)))
        
    def add_batteries(self, battery_file):
        """
        This function reads the given file, and adds the battery attributes to the list of battries.
        """        
        with open(battery_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            # Add coordinates and capacity battery
            for row in csv_reader:
                capacity = row[1]
                pos_x, pos_y = row[0].split(",")
                self.batteries.append(Battery(int(pos_x), int(pos_y), float(capacity)))
    
    def shared_costs(self):
        '''
        Calculates cost when cables are shared.
        '''
        count = 0
        for battery in self.battery_houses_connections:
            cablecoordinates_list = []

            for house in self.battery_houses_connections[battery]:
                count +=1
                if house.battery is None:
                    self.invalid += 1
                    return None  # Break immediately if any house is not connected

                for cable in house.cables:
                    cablecoordinates_list.append(cable)

            # Calculate shared cablesegments per battery by removing duplicate segments from count
            cablesegment_list = [tuple(cablecoordinates_list[i] + cablecoordinates_list[i+1]) for i in range(len(cablecoordinates_list)-1)]
            cablesegment_counter = len(set(cablesegment_list))
            self.district_cost_shared += cablesegment_counter * self.cable_price 
        
        self.district_cost_shared += len(self.batteries) * self.batteries[0].price
        print(count)
        return self.district_cost_shared

    def reset_state(self):
        print("Resetting district state")
        for house in self.houses:
            house.reset()

        for battery in self.batteries:
            battery.reset_capacity()

        # Reinitialize shared cost and battery-house connections
        self.district_cost_shared = 0
        self.battery_houses_connections = {battery: [] for battery in self.batteries}

        # Reset invalid solution flag
        self.invalid = 0