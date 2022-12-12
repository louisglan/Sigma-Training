import math

def monkey0(item):
    worry = item * 17
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 3 == 0:
        new_monkey = 4
    else:
        new_monkey = 2
    return worry, new_monkey

def monkey1(item):
    worry = item * 11
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 5 == 0:
        new_monkey = 3
    else:
        new_monkey = 5
    return worry, new_monkey

def monkey2(item):
    worry = item + 4
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 2 == 0:
        new_monkey = 6
    else:
        new_monkey = 4
    return worry, new_monkey

def monkey3(item):
    worry = item * item
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 13 == 0:
        new_monkey = 0
    else:
        new_monkey = 5
    return worry, new_monkey

def monkey4(item):
    worry = item + 7
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry %11 == 0:
        new_monkey = 7
    else:
        new_monkey = 6
    return worry, new_monkey

def monkey5(item):
    worry = item + 8
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry %17 == 0:
        new_monkey = 0
    else:
        new_monkey = 2
    return worry, new_monkey

def monkey6(item):
    worry = item + 5
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 19 == 0:
        new_monkey = 7
    else:
        new_monkey = 1
    return worry, new_monkey

def monkey7(item):
    worry = item + 3
    worry = math.floor(worry/3)
    new_monkey = 0
    if worry % 7 == 0:
        new_monkey = 1
    else:
        new_monkey = 3
    return worry, new_monkey

monkey_functions = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
monkey_items = [[99, 67, 92, 61, 83, 64, 98], [78, 74, 88, 89, 50], [98, 91], [59, 72, 94, 91, 79, 88, 94, 51], [95, 72, 78], [76], [69, 60, 53, 89, 71, 88], [72, 54, 63, 80]]
total_times_inspected = [0]*8
for j in range(20):
    for (i, monkey) in enumerate(monkey_items):
        if len(monkey) == 0:
            continue
        else:
            for k in range(len(monkey)):
                (new_worry, new_monkey) = monkey_functions[i](monkey[k])
                monkey_items[new_monkey].append(new_worry)
                total_times_inspected[i]+=1
            monkey_items[i] = []
total_times_inspected.sort(reverse=True)
monkey_business = total_times_inspected[0]*total_times_inspected[1]
print(monkey_business)
