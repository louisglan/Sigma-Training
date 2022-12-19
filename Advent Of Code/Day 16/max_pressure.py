import itertools

my_file =  open('scan.txt', 'r')
data = my_file.read()
split_data = data.split('\n')

def generate_valves(split_data):
    valve_strings = []
    for valve in split_data:
        valve = valve.replace('; tunnels lead to valves ', ';')
        valve = valve.replace('; tunnel leads to valve ', ';')
        valve = valve.replace(' has flow rate=', ';')
        split_string = valve[6:].split(';')
        split_string[1] = int(split_string[1])
        split_string[2] = split_string[2].split(', ')
        valve_strings.append(split_string)
    return valve_strings

def operate_on_valve(starting_node, current_node, adjacent_node, visited, stack):
    if path_lengths[starting_node][adjacent_node] > path_lengths[starting_node][current_node] + 1:
        path_lengths[starting_node][adjacent_node] = path_lengths[starting_node][current_node] + 1
    if adjacent_node not in visited and adjacent_node not in stack:
        stack.append(adjacent_node)
    return stack

def BFS(starting_node):
    stack = []
    visited = []
    stack.append(starting_node)
    visited.append(starting_node)
    path_lengths[starting_node][starting_node] = 0
    while len(stack) > 0:
        current_node = stack[0]
        visited.append(current_node)
        stack.pop(0)
        for valve in adjacent_valves[current_node]:
            stack = operate_on_valve(starting_node, current_node, valve, visited, stack)
    return path_lengths

def traverse_tunnels(valves_with_pressure, pressure_rates, path_lengths):
    starting_valve = 'AA'
    def pressure_size(e):
        return pressure_rates[e]
    valves_with_pressure.sort(reverse=True, key=pressure_size)
    print(valves_with_pressure)
    order_permutations = list(itertools.permutations(valves_with_pressure, 6))
    max_pressure = 0
    for permutation in order_permutations:
        i = 0
        time_left = 30
        current_valve = starting_valve
        total_pressure = 0
        while i < len(permutation) and time_left > 1:
            next_valve=permutation[i]
            distance_to_next_valve = path_lengths[current_valve][next_valve]
            time_left -= distance_to_next_valve+1
            if time_left>=0:
                total_pressure+=time_left*pressure_rates[next_valve]
            current_valve=next_valve
            i+=1
        if total_pressure > max_pressure:
            max_pressure = total_pressure
    print(max_pressure)
    
    

valve_strings = generate_valves(split_data)
valves = [valve_string[0] for valve_string in valve_strings]
path_lengths={v: {v: float('inf') for v in valves} for v in valves}
pressure_rates = {v[0]: v[1] for v in valve_strings}
valves_with_pressure = [valve for valve in valves if pressure_rates[valve] > 0]
adjacent_valves = {valve[0]: {adjacent_valve: 1 for adjacent_valve in valve[2]} for valve in valve_strings}
for i in range(len(valves)):
    BFS(valves[i])


traverse_tunnels(valves_with_pressure, pressure_rates, path_lengths)
