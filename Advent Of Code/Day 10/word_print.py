my_file =  open('program-instructions.txt', 'r')
data = my_file.read()
instructions = data.split('\n')

def increment_row(cycle, output, sprite_position):
    if cycle-1 in [sprite_position-1, sprite_position, sprite_position + 1]:
        output+='#'
    else:
        output+= '.'
    if cycle %40 == 0:
        output +='\n'
        cycle-=40
    return output, cycle

def follow_instructions():
    sprite_position = 1
    cycle = 1
    output = ''
    for instruction in instructions:
        if instruction == 'noop':
            (output, cycle) = increment_row(cycle, output, sprite_position)
            cycle+=1
            continue
        else:
            increment_value = int(instruction.split(' ')[1])
            (output, cycle) = increment_row(cycle, output, sprite_position)
            cycle+=1
            (output, cycle) = increment_row(cycle, output, sprite_position)
            cycle+=1
            sprite_position+=increment_value
        
        print(cycle, sprite_position)
    return output

print(follow_instructions())