import math

my_file = open('encrypted-file.txt', 'r')
data = my_file.read()
encryption = [int(number) for number in data.split('\n')]
number_count = len(encryption)
original_indexes = {i: value*811589153 for (i, value) in enumerate(encryption)}
current_positions = [i for i in range(number_count)]
for k in range(10):
    print([original_indexes[i] for i in current_positions])
    for i in range(number_count):
        current_index = current_positions.index(i)
        new_index_temp = current_index + original_indexes[i]
        if new_index_temp <= 0:
            new_index_temp -= math.ceil(new_index_temp / number_count)
        elif new_index_temp >= number_count-1:
            new_index_temp += math.ceil(new_index_temp / number_count-1)
        new_index = new_index_temp % number_count
        if new_index > current_index:
            for j in range(new_index-current_index):
                current_positions[current_index + j] = current_positions[current_index + j + 1]
            current_positions[new_index] = i
        elif new_index < current_index:
            for j in range(current_index-new_index):
                current_positions[current_index - j] = current_positions[current_index - j - 1]
            current_positions[new_index] = i

decryption = [original_indexes[i] for i in current_positions]
zero_index = decryption.index(0)
first_number = decryption[(1000+zero_index) % number_count]
second_number = decryption[(2000+zero_index) % number_count]
third_number = decryption[(3000+zero_index) % number_count]
coordinate_sum = first_number + second_number + third_number
print(coordinate_sum)