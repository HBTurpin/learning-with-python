
with open('day1-input') as file:
    entries = [line.rstrip() for line in file]



#Part 1
for entry1 in entries:
    for entry2 in entries:
        if int(entry1) + int(entry2) == 2020:
            print(int(entry1) * int(entry2))
            break


#Part 2
for entry1 in entries:
    for entry2 in entries:
        for entry3 in entries:
            if int(entry1) + int(entry2) + int(entry3) == 2020:
                print(int(entry1) * int(entry2) * int(entry3))
                break
