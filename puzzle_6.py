# Part I

with open('input_puzzle_6.txt', 'r') as file:
    data = file.read().rstrip()

for s in range(0,len(data)):
    check_set = set(data[s:s+4])
    if(len(check_set) == 4):
        break

# Part 2
for c in range(0,len(data)):
    check_set_b = set(data[c:c+14])
    if(len(check_set_b) == 14):
        break

print("Part 1" ,data[s:s+4], s + 4)
print("Part 2" ,data[c:c+14], c + 14)



