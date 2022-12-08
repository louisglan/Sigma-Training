my_file =  open('trees.txt', 'r')
data = my_file.read()

def check_left(i, j, trees_grid):
    if j==0:
        return 0
    values_to_compare = trees_grid[i][0:j][::-1]
    counter = 0
    for value in values_to_compare:
        if trees_grid[i][j]>value:
            counter+=1
        else:
            return counter+1
    return counter

def check_right(i, j, trees_grid):
    if j==side_length-1:
        return 0
    values_to_compare = trees_grid[i][j+1:]
    counter = 0
    for value in values_to_compare:
        if trees_grid[i][j]>value:
            counter+=1
        else:
            return counter+1
    return counter

def check_above(i, j, trees_grid):
    if i==0:
        return 0
    values_to_compare = [trees_grid[n][j] for n in range(len(trees_grid)) if n < i][::-1]
    counter = 0
    for value in values_to_compare:
        if trees_grid[i][j]>value:
            counter+=1
        else:
            return counter+1
    return counter

def check_below(i, j, trees_grid):
    if i==side_length-1:
        return 0
    values_to_compare = [trees_grid[n][j] for n in range(len(trees_grid)) if n > i]
    counter = 0
    for value in values_to_compare:
        if trees_grid[i][j]>value:
            counter+=1
        else:
            return counter+1
    return counter

tree_rows = data.split('\n')
side_length = len(tree_rows)
trees_grid = [[int(el) for el in list(tree_row)] for tree_row in tree_rows]
scenic_scores = []
for i in range(len(trees_grid)):
    for j in range(len(trees_grid)):
        print(check_left(i, j, trees_grid), check_right(i, j, trees_grid), check_above(i, j, trees_grid), check_below(i, j, trees_grid))
        scenic_scores.append(check_left(i, j, trees_grid) * check_right(i, j, trees_grid) * check_above(i, j, trees_grid) * check_below(i, j, trees_grid))
highest_score = max(scenic_scores)
print(highest_score)
