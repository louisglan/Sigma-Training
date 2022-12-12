import math

my_file =  open('height-map.txt', 'r')
data = my_file.read()
rows = data.split('\n')
grid = [[*row] for row in rows]

def convert_letters_to_heights(grid):
    starting_order1 = ord('a')
    letter_height_dict = {}
    for i in range(26):
        current_order1 = starting_order1+i
        char1 = chr(current_order1)
        letter_height_dict[char1]=i+1
    letter_height_dict['S'] = 1
    letter_height_dict['E'] = 26
    number_grid = [[letter_height_dict[el]for el in row] for row in grid]
    return number_grid

def generate_nodes(grid):
    nodes = {}
    shortest_distance_to_nodes = {}
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            nodes[(i, j)] = grid[j][i]
            shortest_distance_to_nodes[(i, j)] = math.inf
    return nodes, shortest_distance_to_nodes

def operate_on_node(current_node, adjacent_node, visited, stack):
    if nodes[adjacent_node] <= nodes[current_node] + 1:
        if shortest_distance_to_nodes[adjacent_node] > shortest_distance_to_nodes[current_node] + 1:
            shortest_distance_to_nodes[adjacent_node] = shortest_distance_to_nodes[current_node] + 1
        if adjacent_node not in visited and adjacent_node not in stack:
            stack.append(adjacent_node)
    return stack

def BFS():
    stack = []
    visited = []
    stack.append(starting_node)
    visited.append(starting_node)
    shortest_distance_to_nodes[starting_node] = 0
    while len(stack) > 0:
        current_node = stack[0]
        visited.append(current_node)
        stack.pop(0)
        above_node = None
        right_node = None
        below_node = None
        left_node = None
        if current_node[1] < grid_height-1:
            above_node = (current_node[0], current_node[1]+1)
            stack = operate_on_node(current_node, above_node, visited, stack)
        if current_node[0] < grid_width-1:
            right_node = (current_node[0]+1, current_node[1])
            stack = operate_on_node(current_node, right_node, visited, stack)
        if current_node[1] > 0:
            below_node = (current_node[0], current_node[1]-1)
            stack = operate_on_node(current_node, below_node, visited, stack)
        if current_node[0] > 0:
            left_node = (current_node[0]-1, current_node[1])
            stack = operate_on_node(current_node, left_node, visited, stack)
    return shortest_distance_to_nodes

number_grid = convert_letters_to_heights(grid)
grid_height = len(number_grid)
grid_width = len(number_grid[0])
grid_area = grid_height * grid_width
(nodes, shortest_distance_to_nodes) = generate_nodes(number_grid)
starting_node = (0, 20)
end_node = (148, 20)

BFS()
print(shortest_distance_to_nodes[end_node])


# Each node will have a shortest distance to that node. If you can get to a node from the current node, 
# compare current distance to your node +1 to current shortest distance to that node and if it is smaller, 
# set that node's shortest distance to the new shortest distance.
# To do a breadth-first-search, add the starting node to the stack. Then look at the starting node and add
# all its nearest neighbours to the stack (top, right, bottom). Whilst doing so, change the shortest distance to that
# neighbour. Then look at the bottom of the stack (top). Look at all the adjacent nodes of top (top, right, bottom) and
# add them to the stack if they haven't been visited, modifying the shortest distance if they have and it needs changing. 
# Then take the next item and rinse and repeat. This algorithm should end when all nodes have been looked at.