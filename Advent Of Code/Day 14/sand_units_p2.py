my_file =  open('rocks.txt', 'r')
data = my_file.read()
rocks = data.split('\n')
rock_instructions = [[[int(coordinate) for coordinate in point.split(',')] for point in rock.split(' -> ')] for rock in rocks]

all_points = []
def construct_points(all_points, instructions):
    for instruction in instructions:
        for i in range(len(instruction)-1):
            x1 = instruction[i][0]
            x2 = instruction[i+1][0]
            y1 = instruction[i][1]
            y2 = instruction[i+1][1]
            if instruction[i][0] != instruction[i+1][0]:
                for x in range(abs(x2-x1)+1):
                    if x2 > x1:
                        if (x1 + x, y1) not in all_points:
                            all_points.append((x1 + x, y1))
                    else:
                        if (x1 - x, y1) not in all_points:
                            all_points.append((x1 - x, y1))
            else:
                for y in range(abs(y2-y1)+1):
                    if y2 > y1:
                        if (x1, y1 + y) not in all_points:
                            all_points.append((x1, y1 + y))
                    else:
                        if (x1, y1 - y) not in all_points:
                            all_points.append((x1, y1 - y))
    return all_points

def sand_movement(occupied_points, max_y):
    starting_position = (500,0)
    previous_position = None
    current_position = starting_position
    while previous_position != current_position:
        previous_position = current_position
        x=current_position[0]
        y=current_position[1]
        lower_position = (x, y+1)
        lower_left_position = (x-1, y+1)
        lower_right_position = (x+1, y+1)
        reached_floor = lower_position[1] == max_y
        if reached_floor:
            occupied_points.append(current_position)
        elif lower_position not in occupied_points:
            current_position = lower_position
        elif lower_left_position not in occupied_points:
            current_position = lower_left_position
        elif lower_right_position not in occupied_points:
            current_position = lower_right_position
        else:
            occupied_points.append(current_position)
            print(current_position)
    if current_position == starting_position:
        return (occupied_points, True)
    else:
        return (occupied_points, False)

occupied_points = construct_points(all_points, rock_instructions)
occupied_points.sort()
initial_space = len(occupied_points)
y_coordinates = [coordinate[1] for coordinate in occupied_points]
floor_y = max(y_coordinates)+2
print(floor_y)

free_falling = False
while not free_falling:
    (occupied_points, free_falling) = sand_movement(occupied_points, floor_y)
    final_space = len(occupied_points)
    # print(final_space-initial_space)
final_space = len(occupied_points)
num_of_units = final_space-initial_space
print(num_of_units)