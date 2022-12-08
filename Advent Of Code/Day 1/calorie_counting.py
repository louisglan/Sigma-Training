
my_file = open("Calories.txt", "r")
data = my_file.read()
my_file.close()
data_into_list = data.split("\n")
joined_data = ', '.join(data_into_list)
split_data = joined_data.split(', , ')
calories_strings = [data.split(', ') for data in split_data]
calories_totals = [sum([int(el) for el in arr]) for arr in calories_strings]
maximum_total = max(calories_totals)
calories_totals.sort()
print(sum(calories_totals[-1:-4:-1]))