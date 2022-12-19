my_file = open('jet_pattern.txt', 'r')
jet_pattern = my_file.read()
floor = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
number_of_jets = len(jet_pattern)

def starting_positions_horizontal(highest_y):
    return [(3, highest_y+4), (4, highest_y+4), (5, highest_y+4), (6, highest_y+4)]

def starting_positions_plus(highest_y):
    return [(4, highest_y+4), (4, highest_y+5), (4, highest_y+6), (3, highest_y+5), (5, (highest_y+5))]

def starting_positions_l(highest_y):
    return [(3, highest_y+4), (4, highest_y+4), (5, highest_y+4), (5, highest_y+5), (5, highest_y + 6)]

def starting_positions_vertical(highest_y):
    return [(3, highest_y+4), (3, highest_y+5), (3, highest_y+6), (3, highest_y+7)]

def starting_positions_square(highest_y):
    return [(3, highest_y+4), (3, highest_y+5), (4, highest_y+4), (4, highest_y+5)]

def sideways_movement(block, direction, stack):
    blocked_on_left = False
    blocked_on_right = False
    for point in block:
        if point[0] == 1 or (point[0]-1, point[1]) in stack:
            blocked_on_left = True
        if point[0] == 7 or (point[0]+1, point[1]) in stack:
            blocked_on_right = True
        
    if direction == '<':
        if blocked_on_left:
            return block
        else:
            new_block = [(point[0]-1, point[1]) for point in block]
            return new_block
    elif direction == '>':
        if blocked_on_right:
            return block
        else:
            new_block = [(point[0]+1, point[1]) for point in block]
            return new_block

def downwards_movement(block, stack, floor):
    is_below = False
    new_block = [(point[0], point[1]-1) for point in block]
    for point in block:
        if (point[0], point[1]-1) in stack or (point[0], point[1]-1) in floor:
            is_below = True
            new_block = block
    return (is_below, new_block)

stack = floor
sideways_count = 0
for i in range(1000000000000):
    highest_y = max(point[1] for point in stack)
    is_below = False
    block = []
    if i % 5 == 0:
        block = starting_positions_horizontal(highest_y)
    elif i % 5 == 1:
        block = starting_positions_plus(highest_y)
    elif i % 5 == 2:
        block = starting_positions_l(highest_y)
    elif i % 5 == 3:
        block = starting_positions_vertical(highest_y)
    elif i % 5 == 4:
        block = starting_positions_square(highest_y)
    while not is_below:
        pattern_idx = sideways_count % number_of_jets
        direction = jet_pattern[pattern_idx]
        block = sideways_movement(block, direction, stack)
        (is_below, block) = downwards_movement(block, stack, floor)
        sideways_count+=1

highest_point = max([point[1] for point in stack])
print(highest_point)


