import copy
my_file =  open('directory-commands.txt', 'r')
data = my_file.read()
commands = data.split('\n')

def makeTree(commands):
    device = {'/': {}}
    dir_instructions = []
    current_directory = device
    for i in range(len(commands)):
        if '$ cd' in commands[i]:
            if commands[i] == '$ cd /':
                current_directory=device['/']
                dir_instructions = []
            elif commands[i] == '$ cd ..':
                current_directory = device['/']
                for command in dir_instructions[0:-1]:
                    current_directory = current_directory[command]
                dir_instructions.pop()
            else:
                current_directory = current_directory[f'dir {commands[i][5:]}']
                dir_instructions.append(f'dir {commands[i][5:]}')
        if commands[i] == '$ ls':
            j = 1
            while '$' not in commands[i+j]:
                if 'dir' in commands[i+j]:
                    current_directory[commands[i+j]]={}
                else:
                    [size, name] = commands[i+j].split(' ')
                    current_directory[f'file {name}'] = int(size)
                if i+j==len(commands)-1:
                    break
                else:
                    j=j+1
    return device

def getDirSizes(device):
    dir_vols = []
    current_dir = device['/']
    dir_instructions = ['/']
    counter = 0

    while len([key for key in dict.keys(device['/']) if 'file' in key])!=6:
        print(dir_instructions)
        print(current_dir)
        files_and_dirs = dict.keys(current_dir)
        num_of_dirs = len([file for file in files_and_dirs if 'dir' in file])
        is_all_files = num_of_dirs == 0
        if is_all_files:
            total_for_dir = sum(current_dir.values())
            if total_for_dir <= 100000:
                dir_vols.append(total_for_dir)
            current_dir = device
            for command in dir_instructions[0:-1]:
                current_dir = current_dir[command]
            dir_instructions.pop()
            files_and_dirs = dict.keys(current_dir)
            dir_keys = [key for key in files_and_dirs if 'dir' in key]
            del current_dir[dir_keys[0]]
            current_dir[f'file {counter}']= total_for_dir
            counter += 1
            
        else:
            dir_keys = [key for key in files_and_dirs if 'dir' in key]
            dir_instructions.append(dir_keys[0])
            current_dir = current_dir[dir_keys[0]]
    return dir_vols

device = makeTree(commands)
dirSizes = getDirSizes(copy.copy(device))
total = sum(dirSizes)
print(total)