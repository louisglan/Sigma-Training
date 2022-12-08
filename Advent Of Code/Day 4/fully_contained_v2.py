def calculate_fully_contained(elf1, elf2):
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')
    one_contains_two = int(elf1_start)<=int(elf2_start) and int(elf1_end) >= int(elf2_end)
    two_contains_one = int(elf2_start)<=int(elf1_start) and int(elf2_end) >= int(elf1_end)
    one_below_two = int(elf1_start)<=int(elf2_start) and int(elf1_end) >= int(elf2_start)
    one_above_two = int(elf1_end)>=int(elf2_end) and int(elf1_start) <= int(elf2_end)
    if (one_contains_two or two_contains_one or one_below_two or one_above_two):
        return True
    else:
        return False


my_file =  open('assignment-pairs.txt', 'r')
data = my_file.read()
pairs = data.split('\n')
split_pairs = [pair.split(',') for pair in pairs]
priorities = [calculate_fully_contained(pair[0], pair[1]) for pair in split_pairs if calculate_fully_contained(pair[0], pair[1])]
total_priorities = len(priorities)
print(total_priorities)
