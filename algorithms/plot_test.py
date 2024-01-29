# import matplotlib.pyplot as plt

# # Jouw dictionary met kabelsegmenten
# cable_segments = {'2, 3': '2, 4',
#  '2, 5': '3, 5',
#  '4, 5': '4, 6',
#  '4, 6': '5, 6',
#  '5, 6': '5, 7',
#  '5, 7': '6, 7',
#  '6, 7': '6, 8',
#  '7, 8': '7, 9',
#  '7, 9': '8, 9',
#  '8, 9': '8, 10',
#  '8, 10': '9, 10',
#  '9, 10': '9, 11',
#  '9, 11': '10, 11',
#  '10, 11': '10, 12',
#  '10, 12': '11, 12',
#  '11, 12': '11, 13',
#  '12, 13': '12, 14',
#  '12, 14': '13, 14',
#  '13, 14': '13, 15',
#  '13, 15': '14, 15',
#  '14, 15': '14, 16',
#  '15, 16': '15, 17',
#  '15, 17': '16, 17',
#  '16, 17': '16, 18',
#  '16, 18': '17, 18',
#  '17, 18': '17, 19',
#  '17, 19': '18, 19',
#  '18, 19': '18, 20',
#  '18, 20': '19, 20',
#  '22, 23': '22, 24',
#  '22, 24': '23, 24',
#  '23, 24': '23, 25',
#  '24, 25': '24, 26',
#  '24, 26': '25, 26',
#  '25, 26': '25, 27',
#  '25, 27': '26, 27',
#  '26, 27': '26, 28',
#  '26, 28': '27, 28',
#  '27, 28': '27, 29',
#  '27, 29': '28, 29',
#  '28, 29': '28, 30',
#  '28, 30': '29, 30',
#  '29, 30': '29, 29',
#  '29, 29': '30, 29',
#  '30, 29': '30, 30'}

# # Functie om de string coördinaten om te zetten naar integers
# def parse_coordinates(coord_str):
#     x, y = coord_str.split(', ')
#     return int(x), int(y)

# # Initialiseren van de plot
# plt.figure(figsize=(10, 10))
# ax = plt.gca()

# # Het grid instellen
# ax.set_xticks(range(21))
# ax.set_yticks(range(21))
# ax.grid(True)

# # Elk segment plotten
# for start, end in cable_segments.items():
#     x1, y1 = parse_coordinates(start)
#     x2, y2 = parse_coordinates(end)
#     ax.plot([x1, x2], [y1, y2], marker='o', color='black')

# # De plot tonen
# plt.show()


import matplotlib.pyplot as plt

# Jouw uitgebreide dictionary met kabelsegmenten
extended_cable_segments = {
    '2, 3': '2, 4',
    '2, 5': '3, 5',
    # Voeg hier alle andere segmenten toe...
    '29, 29': '30, 29',
    '30, 29': '30, 30'
}

# Coördinaten van huizen en de batterij
house_coordinates = [(5, 5), (10, 10), (15, 15)]  # Vervang dit met je eigen coördinaten
battery_coordinate = (30, 30)  # Vervang dit met de coördinaat van de batterij

# Functie om de string coördinaten om te zetten naar integers
def parse_coordinates(coord_str):
    x, y = coord_str.split(', ')
    return int(x), int(y)

# Initialiseren van de plot
plt.figure(figsize=(8, 8))
ax = plt.gca()

# Het grid instellen
ax.set_xticks(range(32))
ax.set_yticks(range(32))
ax.grid(True)

# Elk segment plotten
for start, end in extended_cable_segments.items():
    x1, y1 = parse_coordinates(start)
    x2, y2 = parse_coordinates(end)
    ax.plot([x1, x2], [y1, y2], color='black')

# Huizen plotten
for x, y in house_coordinates:
    ax.plot(x, y, marker='o', color='green', markersize=10)

# Batterij plotten
pastel_red = "#fa4242"
ax.plot(*battery_coordinate, marker='s', color=pastel_red, markersize=12)

# De plot tonen
plt.show()