my_file =  open('closest-beacons.txt', 'r')
data = my_file.read()
split_data = data.split('\n')
closest_beacons = [[[int(coordinate) for coordinate in coordinates.split(', y=')] for coordinates in instructions[12:].split(': closest beacon is at x=')] for instructions in split_data]

occupied_x_positions = []
beacon_x_positions = []
row_y_coordinate = 2000000
for sensor, beacon in closest_beacons:
    if beacon[1] == row_y_coordinate:
        beacon_x_positions.append(beacon[0])
    distance_to_beacon = (abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1]))
    distance_to_row = abs(row_y_coordinate-sensor[1])
    distance_difference = distance_to_beacon - distance_to_row
    if distance_difference < 0:
        continue
    else:
        x_range=range(sensor[0]-distance_difference, sensor[0]+distance_difference+1)
        occupied_x_positions+=x_range
no_duplicate_list = set(occupied_x_positions)
final_list = []
for position in no_duplicate_list:
    if position in beacon_x_positions:
        continue
    else:
        final_list.append(position)

num_positions = len(final_list)
print(num_positions)
