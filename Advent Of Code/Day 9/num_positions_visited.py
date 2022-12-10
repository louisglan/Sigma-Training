my_file =  open('rope-moves.txt', 'r')
data = my_file.read()
split_data = data.split('\n')
moves = [[el.split(' ')[0], int(el.split(' ')[1])] for el in split_data]

def head_movement(head_x, head_y, direction):
    if direction == 'U':
        head_y+=1
    elif direction == 'D':
        head_y-=1
    elif direction == 'L':
        head_x-=1
    elif direction == 'R':
        head_x+=1
    return (head_x, head_y)

def tail_movement(head_x, head_y, tail_x, tail_y):
    if abs(head_x-tail_x) <= 1 and abs(head_y-tail_y) <= 1:
        return (tail_x, tail_y)
    if head_x > tail_x:
        tail_x +=1
    if head_y > tail_y:
        tail_y +=1 
    if head_x < tail_x:
        tail_x-=1
    if head_y < tail_y:
        tail_y-=1
    return (tail_x, tail_y)

def position_comparison(x, y, positions):
    no_match = True
    for position in positions:
        if position[0] == x and position[1] == y:
            no_match = False
    if no_match:
        positions.append([x, y])
    return positions

positions_visited = [[0, 0]]
(start_x, start_y) = (0, 0)
(head_x, head_y) = (0, 0)
(tail_x, tail_y) = (0, 0)
for move in moves:
    for jumps in range(move[1]):
        (head_x, head_y) = head_movement(head_x, head_y, move[0])
        (tail_x, tail_y) = tail_movement(head_x, head_y, tail_x, tail_y)
        positions_visited = position_comparison(tail_x, tail_y, positions_visited)
        # print([head_x, head_y], [tail_x, tail_y])
num_positions = len(positions_visited)
print(num_positions)