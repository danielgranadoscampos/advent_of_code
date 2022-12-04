# Part I
data_file = open("input_puzzle_4.txt", "r")
fully_contain = 0
overlap_number = 0

for line in data_file:
    sections = line.replace(",", "-").strip().split("-")
    
    range_a = range(int(sections[0]), int(sections[1]) + 1)
    range_b = range(int(sections[2]), int(sections[3]) + 1)

    if set(list(range_a)).issubset(range_b) or set(list(range_b)).issubset(range_a):
        fully_contain +=1 
    
    ## Part II
    for i in list(range_a):
        if (i in list(range_b)):
            overlap_number = overlap_number + 1 
            break
   

print(fully_contain)
print(overlap_number)

