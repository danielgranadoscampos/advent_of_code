#Advent of code solution day 2.
data_file = open("input_puzzle_2.txt", "r")
pick_points = 0
result = 0
real_result = 0
for line in data_file:
    game = line.strip().split()
    if (game[1] == 'X'):
        pick_points = pick_points + 1
    elif (game[1] == 'Y'):
        pick_points = pick_points + 2
    elif (game[1] == 'Z'):
        pick_points = pick_points + 3

    if (game == ['A', 'X']):
        result = result + 3
    elif (game == ['A', 'Y']):
        result = result + 6
    elif (game == ['A', 'Z']):
        result = result + 0
    elif (game == ['B', 'X']):
        result = result + 0
    elif (game == ['B', 'Y']):
        result = result + 3
    elif (game == ['B', 'Z']):
        result = result + 6
    elif (game == ['C', 'X']):
        result = result + 6
    elif (game == ['C', 'Y']):
        result = result + 0
    elif (game == ['C', 'Z']):
        result = result + 3
# Part two changes the scores
    if (game == ['A', 'X']):
        real_result = real_result + 3
    elif (game == ['A', 'Y']):
        real_result = real_result + 4
    elif (game == ['A', 'Z']):
        real_result = real_result + 8
    elif (game == ['B', 'X']):
        real_result = real_result + 1
    elif (game == ['B', 'Y']):
        real_result = real_result + 5
    elif (game == ['B', 'Z']):
        real_result = real_result + 9
    elif (game == ['C', 'X']):
        real_result = real_result + 2
    elif (game == ['C', 'Y']):
        real_result = real_result + 6
    elif (game == ['C', 'Z']):
        real_result = real_result + 7
    
# Answers part I 
print(result + pick_points)
#Answers part II
print(real_result)


## Notes ## ------- 
# Rather than using IF statements another option was to use a dictionary mapping the weapon choices with the result.
# The for each game we would look it up in the dictionary to get the correspondent value and keep adding it up 

# For example for Part I 



outcomes = {('AX'): 4,('AY'): 8,('AZ'): 3,
            ('BX'): 1, ('BY'): 5, ('BZ'): 9,
            ('CX'): 7, ('CY'): 2, ('CZ'): 6,
            }
print(outcomes)

data_file = open("input_puzzle_2.txt", "r")
score = 0
for line in data_file:
    game = line.replace(" ", "").strip()
    print(game)
    score += outcomes[game]
print(score)