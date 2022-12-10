my_file =  open('program-instructions.txt', 'r')
data = my_file.read()
instructions = data.split('\n')
sum = 1
cycle = 1
output_sum = 0

def increment_output(cycle, output_sum, sum):
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    if cycle % 20 == 0 and cycle in relevant_cycles:
        output_sum+=sum * cycle
    return output_sum

def follow_instructions(cycle, sum, output_sum):
    for instruction in instructions:
        if instruction == 'noop':
            output_sum = increment_output(cycle, output_sum, sum)
            cycle+=1
            continue
        else:
            increment_value = int(instruction.split(' ')[1])
            output_sum = increment_output(cycle, output_sum, sum)
            cycle+=1
            output_sum = increment_output(cycle, output_sum, sum)
            cycle+=1
            sum+=increment_value
    return output_sum

print(follow_instructions(cycle, sum, output_sum))