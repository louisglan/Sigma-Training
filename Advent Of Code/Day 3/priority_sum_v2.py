def calculate_priority(group):
    first_rucksack = group[0]
    second_rucksack = group[1]
    third_rucksack = group[2]
    common_letters = [el for el in first_rucksack if el in second_rucksack and el in third_rucksack]
    points = new_dict[common_letters[0]]
    return points

starting_order1 = ord('a')
starting_order2 = ord('A')
new_dict = {}
for i in range(26):
    current_order1 = starting_order1+i
    current_order2 = starting_order2+i
    char1 = chr(current_order1)
    char2 = chr(current_order2)
    new_dict[char1]=i+1
    new_dict[char2]=i+27

my_file =  open('rucksack-items.txt', 'r')
data = my_file.read()
rucksacks = data.split('\n')
groups = []
for i in range(len(rucksacks)//3):
    groups.append([rucksacks[3*i], rucksacks[3*i+1], rucksacks[3*i+2]])

priorities = [calculate_priority(group) for group in groups]
total_priorities = sum(priorities)
print(total_priorities)
