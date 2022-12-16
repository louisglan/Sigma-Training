my_file =  open('closest-beacons.txt', 'r')
data = my_file.read()
split_data = data.split('\n')
closest_beacons = [[[int(coordinate) for coordinate in coordinates.split(', y=')] for coordinates in instructions[12:].split(': closest beacon is at x=')] for instructions in split_data]

def combining_lists(range_lower1, range_upper1, range_lower2, range_upper2):
    new_range_lower = None
    new_range_upper = None
    if range_lower2 <= range_upper1+1 and range_upper2+1 >= range_lower1:
        if range_lower2 < range_lower1:
            new_range_lower = range_lower2
        else:
            new_range_lower = range_lower1
        if range_upper2 > range_upper1:
            new_range_upper = range_upper2
        else:
            new_range_upper = range_upper1
    return (new_range_lower, new_range_upper)

final_coordinates = [0, 0]
sensor_ranges = []
for sensor, beacon in closest_beacons:
    distance_to_beacon = (abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1]))
    sensor_ranges.append(distance_to_beacon)
for k in range(1,4000001):
    occupied_positions = []
    for j in range(len(closest_beacons)):
        distance_to_row = abs(k-closest_beacons[j][0][1])
        distance_difference = sensor_ranges[j] - distance_to_row
        if distance_difference < 0:
            continue
        else:
            lower_x_position = closest_beacons[j][0][0]-distance_difference
            higher_x_position = closest_beacons[j][0][0]+distance_difference
            occupied_positions.append((lower_x_position, higher_x_position))
    num_iterations = len(occupied_positions)
    for j in range(num_iterations-1):
        for i in range(num_iterations-1-j):
            (new_range_lower, new_range_upper) = combining_lists(occupied_positions[-1][0], occupied_positions[-1][1], occupied_positions[-i-2][0], occupied_positions[-i-2][1])
            if new_range_lower is None:
                continue
            else:
                occupied_positions[-i-2] = (new_range_lower, new_range_upper)
                occupied_positions.pop()
                break
    if len(occupied_positions) > 1:
        print(occupied_positions, i)
        final_coordinates[1]=k
        row_with_missing_value = [occupied_positions[0][0], occupied_positions[0][1], occupied_positions[1][0], occupied_positions[1][1]]
        final_coordinates[0] = (sorted(row_with_missing_value))[1]+1
        break
final_answer = final_coordinates[1] + final_coordinates[0]*4000000
print(final_answer)
