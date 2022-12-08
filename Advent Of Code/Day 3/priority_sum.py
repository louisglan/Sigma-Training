def calculate_priority(rucksack):
    first_half = rucksack[0:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    common_letters = [el for el in first_half if el in second_half]
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
priorities = [calculate_priority(rucksack) for rucksack in rucksacks]
total_priorities = sum(priorities)
print(total_priorities)
