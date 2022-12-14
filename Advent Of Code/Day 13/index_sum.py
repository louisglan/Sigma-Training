import ast

my_file =  open('lists.txt', 'r')
data = my_file.read()
lists = data.split('\n\n')

def list_comparison(left, right, index):
    if type(left) is int and type(right) is list:
        left = [left]
    elif type(right) is int and type(left) is list:
        right = [right]
    elif type(left) is int and type(right) is int:
        if left < right:
            if index not in indices:
                indices.append(index)
            return True
        elif left > right:
            return True
    if type(left) is list and type(right) is list:
        left_length = len(left)
        right_length = len(right)
        max_length = max(left_length, right_length)
        for i in range(max_length):
            if i > left_length-1 and i <= right_length-1:
                if index not in indices:
                    indices.append(index)
                return True
            elif i > len(right)-1 and i <= len(left)-1:
                return True
            comparison = list_comparison(left[i], right[i], index)
            if comparison:
                return True

indices = []
for (i, list_pair) in enumerate(lists):
    left_list = ast.literal_eval(list_pair.split('\n')[0])
    right_list = ast.literal_eval(list_pair.split('\n')[1])
    list_comparison(left_list, right_list, i+1)
index_sum = sum(indices)

print(index_sum)