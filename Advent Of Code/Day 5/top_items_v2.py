boxes = {
    1: ['Z', 'J', 'N', 'W', 'P', 'S'],
    2: ['G', 'S', 'T'],
    3: ['V', 'Q', 'R', 'L', 'H'],
    4: ['V', 'S', 'T', 'D'],
    5: ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
    6: ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
    7: ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
    8: ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'],
    9: ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
}

def take_move(move):
    num_els = move[0]
    start_box = move[1]
    end_box = move[2]
    boxes[end_box] += (boxes[start_box][-num_els:])
    del boxes[start_box][len(boxes[start_box])-num_els:]

my_file =  open('instructions.txt', 'r')
data = my_file.read()
moves = data.split('\n')[10:]
replaced_moves = [move[5:].replace(' to ', ' from ') for move in moves]
split_moves = [move.split(' from ') for move in replaced_moves]
int_moves = [[int(string) for string in move] for move in split_moves]
for move in int_moves:
    take_move(move)
final_string = ''
for box in boxes:
    final_string += boxes[box][-1]
print(final_string)