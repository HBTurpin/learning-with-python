
with open('day3-input') as file:
    entries = [line.rstrip() for line in file]

#Part 1
total_trees = 0
for y in range(0, len(entries), 1):
    x = (y * 3) % len(entries[0])
    if entries[y][x] == "#":
        total_trees += 1
print(total_trees)

#Part 2
paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for path in paths:
    total_trees = 0
    step = 0
    while (step * path[1]) < len(entries):
        y = (step * path[1])
        x = (step * path[0]) % len(entries[y])
        if entries[y][x] == "#":
            total_trees += 1
        step += 1
    result *= total_trees
print(result)



