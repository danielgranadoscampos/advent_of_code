#Advent of code solution day 3

# Part I
data_file = open("input_puzzle_3.txt", "r")
total_priorities = 0
for line in data_file:
    rucksack = line.strip()
    total_item_number = int(len(rucksack))
    compartment_number = int(total_item_number/2)

    first_bag = rucksack[0:compartment_number]
    second_bag = rucksack[(compartment_number ): total_item_number]

    for letter in first_bag:
        if (letter in second_bag and letter.isupper() == True):
            points = ord(letter) - 38
        elif (letter in second_bag and letter.islower() == True):
            points = ord(letter) - 96


    total_priorities = total_priorities + points

print(total_priorities)


# PART II

file = open("input_puzzle_3.txt", "r")
data_file = file.read().split()
total_priorities = 0
line_index = 0
while line_index < len(data_file):
    for letter in data_file[line_index]:
        if(letter in data_file[line_index + 1] and letter in data_file[line_index + 2] and letter.isupper() == True):
            points = ord(letter) - 38
        elif(letter in data_file[line_index + 1] and letter in data_file[line_index + 2] and letter.islower() == True):
            points = ord(letter) - 96
        
    total_priorities = total_priorities + points
    
    line_index = line_index + 3
    print(line_index)

print(total_priorities)

