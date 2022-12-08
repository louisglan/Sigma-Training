def calculate_move_score(opponent_move, victory_status):
    opponent_score = opponent_scores[opponent_move]
    if victory_status == 'X': 
        if opponent_score == 1:
             my_score = opponent_score+2
        else:
            my_score = opponent_score-1
    elif victory_status == 'Y':
        my_score = opponent_score
    else:
        if opponent_score == 3:
             my_score = opponent_score-2
        else:
            my_score = opponent_score+1
    return my_score

my_file =  open('rock_paper_scissors.txt', 'r')
data = my_file.read()
moves = data.split('\n')
victory_scores  = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
opponent_scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

points = [calculate_move_score(el[0], el[2])+victory_scores[el[2]] for el in moves]
total_points = sum(points)
print(total_points)