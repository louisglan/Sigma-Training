my_file =  open('trees.txt', 'r')
data = my_file.read()

def check_left(i, j, trees_grid):
    values_to_compare = trees_grid[i][0:j]
    if trees_grid[i][j] > max(values_to_compare):
        return True
    else: 
        return False

def check_right(i, j, trees_grid):
    values_to_compare = trees_grid[i][j+1:]
    if trees_grid[i][j] > max(values_to_compare):
        return True
    else: 
        return False

def check_above(i, j, trees_grid):
    values_to_compare = [trees_grid[n][j] for n in range(len(trees_grid)) if n < i]
    if trees_grid[i][j] > max(values_to_compare):
        return True
    else: 
        return False

def check_below(i, j, trees_grid):
    values_to_compare = [trees_grid[n][j] for n in range(len(trees_grid)) if n > i]
    if trees_grid[i][j] > max(values_to_compare):
        return True
    else: 
        return False

tree_rows = data.split('\n')
side_length = len(tree_rows)
counter = 0
trees_grid = [[int(el) for el in list(tree_row)] for tree_row in tree_rows]
for (i, tree_row) in enumerate(trees_grid):
    for (j, tree_column) in enumerate(trees_grid):
        if i==0 or i == side_length-1 or j == 0 or j == side_length-1:
            counter+=1
        else:
            if check_left(i, j, trees_grid) or check_right(i, j, trees_grid) or check_above(i, j, trees_grid) or check_below(i, j, trees_grid):
                counter+=1
print(counter)
