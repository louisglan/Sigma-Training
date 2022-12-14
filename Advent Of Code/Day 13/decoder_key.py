import ast

my_file =  open('lists.txt', 'r')
data = my_file.read()
list_pairs = data.split('\n\n')
lists = []
for list_pair in list_pairs:
    left_list = ast.literal_eval(list_pair.split('\n')[0])
    right_list = ast.literal_eval(list_pair.split('\n')[1])
    lists.append(left_list)
    lists.append(right_list)
lists.append([[2]])
lists.append([[6]])

def list_comparison(left, right, index):
    if type(left) is int and type(right) is list:
        left = [left]
    elif type(right) is int and type(left) is list:
        right = [right]
    elif type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left > right:
            if index not in indices:
                indices.append(index)
            return True
    if type(left) is list and type(right) is list:
        left_length = len(left)
        right_length = len(right)
        max_length = max(left_length, right_length)
        for i in range(max_length):
            if i > left_length-1 and i <= right_length-1:
                return True
            elif i > len(right)-1 and i <= len(left)-1:
                if index not in indices:
                    indices.append(index)
                return True
            comparison = list_comparison(left[i], right[i], index)
            if comparison:
                return True

indices = []
changes = True
while changes:
    indices = []
    for i in range(len(lists)-1):
        list_comparison(lists[i], lists[i+1], i+1)
    if len(indices) == 0:
        changes = False
    else:
        for index in indices:
            lower_switch = lists[index-1]
            upper_switch = lists[index]
            lists[index-1] = upper_switch
            lists[index] = lower_switch

lower_packet_idx = lists.index([[2]])+1
upper_packet_idx = lists.index([[6]])+1
decoder_key = lower_packet_idx * upper_packet_idx
print(decoder_key)