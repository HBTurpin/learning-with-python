
with open('day5-input') as file:
    seats = [line.rstrip() for line in file]

#Part 1
highest_id = 0
for seat in seats:
    row = int(seat[0:7].replace("F","0").replace("B","1"),2)
    column = int(seat[7:10].replace("L","0").replace("R","1"),2)
    id = row*8+column
    highest_id = (id if id > highest_id else highest_id)
print(highest_id)



#Part 2
ids = []
for seat in seats:
    row = int(seat[0:7].replace("F","0").replace("B","1"),2)
    column = int(seat[7:10].replace("L","0").replace("R","1"),2)
    id = row*8+column
    ids += [id]


ids.sort()
prev_id = ids[0]-1
for id in ids:
    if id-1 != prev_id:
        print(id-1)
    prev_id = id





