def calculate_score(opponent_move, my_move):
    point_diff = choice_scores[my_move] - opponent_scores[opponent_move]
    if point_diff == 1 or point_diff == -2:
        return 6
    elif point_diff == 0:
        return 3
    else:
        return 0

my_file =  open('rock_paper_scissors.txt', 'r')
data = my_file.read()
moves = data.split('\n')
choice_scores  = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
opponent_scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

points = [calculate_score(el[0], el[2])+choice_scores[el[2]] for el in moves]
total_points = sum(points)
print(total_points)