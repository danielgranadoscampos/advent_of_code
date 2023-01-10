# Read files and lines
file = open("input_puzzle_7.txt")
line = file.readline().rstrip('\n')

# Variable to save directories
dirs_step = {"/home":0}
# Variable to keep track of path
current_path = "/home"


for line in file:
    #Select all commands
    if line[0]== "$":
        if line[2:4] == "ls":
            pass
        elif line[2:4]== "cd":
            if line[5:6] == "/":
                current_path = "/home"
            #return to the previous line where "/" was found.    
            elif line[5:7] == "..":
                current_path = current_path[0:current_path.rfind("/")]
            else:
                dir_name = line[5:]
                current_path = current_path + "/" + dir_name
                dirs_step.update({current_path:0})

    elif line[0:3]=="dir":
        pass
    else:
        size = int(line[:line.find(" ")])
        dir = current_path
        for i in range(current_path.count("/")):
            dirs_step[dir] += size
            dir = dir[:dir.rfind("/")]

total = 0
disk_space = 30000000 - (70000000 - dirs_step["/home"])
valid_dirs = []

for dir in dirs_step:
    
    #1
    if dirs_step[dir] < 100000:
        total += dirs_step[dir]
    #2
    if disk_space <= dirs_step[dir]:
        valid_dirs.append(dirs_step[dir])

smallest = min(valid_dirs)

print("Part 1: ", total)
print("Part 2: ", smallest)


# Answer help at https://www.youtube.com/watch?v=FXQWIWHaFBE&t=1215s