# Part I
data_file = open("input_puzzle_5.txt", "r")

all_crates = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}

for line in data_file.readlines()[0:8]:
    all_crates["1"].append(line[1])
    all_crates["2"].append(line[5])
    all_crates["3"].append(line[9])
    all_crates["4"].append(line[13])
    all_crates["5"].append(line[17])
    all_crates["6"].append(line[21])
    all_crates["7"].append(line[25])
    all_crates["8"].append(line[29])
    all_crates["9"].append(line[33])

for i in all_crates:
    while " " in all_crates[i]:
        all_crates[i].remove(" ")

for c in all_crates:
        all_crates[c].reverse()


data_file = open("input_puzzle_5.txt", "r")
for line in data_file.readlines()[10:513]:
    instruction = line.split()
    move_number = int(instruction[1])
    crate_a = instruction[3]
    crate_b = instruction[5]
    list_to_take = all_crates[crate_a]
    cut = len(list_to_take) - move_number
    movers = list_to_take[cut:len(list_to_take)]
    rev_movers = movers.reverse()
    all_crates[crate_b] = all_crates[crate_b] + movers
    all_crates[crate_a] = all_crates[crate_a][0:cut]

for c in all_crates:
        crates_answer = all_crates[c]
        print(crates_answer[len(crates_answer)-1])

# Part II

data_file = open("input_puzzle_5.txt", "r")

all_crates = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}

for line in data_file.readlines()[0:8]:
    all_crates["1"].append(line[1])
    all_crates["2"].append(line[5])
    all_crates["3"].append(line[9])
    all_crates["4"].append(line[13])
    all_crates["5"].append(line[17])
    all_crates["6"].append(line[21])
    all_crates["7"].append(line[25])
    all_crates["8"].append(line[29])
    all_crates["9"].append(line[33])

for i in all_crates:
    while " " in all_crates[i]:
        all_crates[i].remove(" ")

for c in all_crates:
        all_crates[c].reverse()


data_file = open("input_puzzle_5.txt", "r")
for line in data_file.readlines()[10:513]:
    instruction = line.split()
    move_number = int(instruction[1])
    crate_a = instruction[3]
    crate_b = instruction[5]
    list_to_take = all_crates[crate_a]
    cut = len(list_to_take) - move_number
    movers = list_to_take[cut:len(list_to_take)]
    all_crates[crate_b] = all_crates[crate_b] + movers
    all_crates[crate_a] = all_crates[crate_a][0:cut]

for c in all_crates:
        crates_answer = all_crates[c]
        print(crates_answer[len(crates_answer)-1])