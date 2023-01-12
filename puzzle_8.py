with open("input_puzzle_8.txt") as file:
    data = [row.strip() for row in file.readlines()]


n_rows = len(data)
n_columns = len(data[1])

inside_visible = 0

for r in range(1, (n_rows-1)):
    for c in range(1, (n_columns-1)):
        current_tree = int(data[r][c])
        left_trees= [int(d) for d in str(data[r][0:c])]
        right_trees = [int(d) for d in str(data[r][c:(n_columns)])]
        top_trees = [data[r-i][c] for i in range(1, r+1)]
        top_trees_numbered = [int(d) for d in top_trees]
        bottom_trees = [data[r+i][c] for i in range(1, n_rows-r)]
        bottom_trees_numbered = [int(d) for d in bottom_trees]

        if max(left_trees)<current_tree or max(right_trees)<current_tree or max(top_trees_numbered)<current_tree or max(bottom_trees_numbered)<current_tree:
            inside_visible += 1


outside_visible = (n_rows*2) + ((n_columns-2)*2)
total = outside_visible + inside_visible
print(total)











