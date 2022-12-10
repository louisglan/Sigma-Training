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
    return [head_x, head_y]

def tail_movement(lead_x, lead_y, tail_x, tail_y):
    if abs(lead_x-tail_x) <= 1 and abs(lead_y-tail_y) <= 1:
        return [tail_x, tail_y]
    if lead_x > tail_x:
        tail_x +=1
    if lead_y > tail_y:
        tail_y +=1 
    if lead_x < tail_x:
        tail_x-=1
    if lead_y < tail_y:
        tail_y-=1
    return [tail_x, tail_y]

def position_comparison(x, y, positions):
    no_match = True
    for position in positions:
        if position[0] == x and position[1] == y:
            no_match = False
    if no_match:
        positions.append([x, y])
    return positions

n = 9
positions_visited = [[0, 0]]
(start_x, start_y) = (0, 0)
(head_x, head_y) = (0, 0)
tails = [[0, 0]]*9
for move in moves:
    for jumps in range(move[1]):
        (head_x, head_y) = head_movement(head_x, head_y, move[0])
        tails[0] = tail_movement(head_x, head_y, tails[0][0], tails[0][1])
        for (i, tail) in enumerate(tails):
            if i == 0:
                tail = tail_movement(head_x, head_y, tail[0], tail[1])
            else:
                tails[i] = tail_movement(tails[i-1][0], tails[i-1][1], tail[0], tail[1])
            positions_visited = position_comparison(tails[-1][0], tails[-1][1], positions_visited)
        # print([head_x, head_y], [tail_x, tail_y])
num_positions = len(positions_visited)
print(num_positions)