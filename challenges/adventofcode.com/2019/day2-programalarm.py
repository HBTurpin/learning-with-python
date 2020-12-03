
with open('day2-input') as file:
    list = file.readline().split(",")



#Part 1
list[1] = 12
list[2] = 2

for opcode in range(0,len(list)-1,4):
    v1 = list[int(list[opcode+1])]
    v2 = list[int(list[opcode+2])]
    resultpos = int(list[opcode+3])

    if list[opcode] == "1":
        list[resultpos] = int(v1) + int(v2)
    elif list[opcode] == "2":
        list[resultpos] = int(v1) * int(v2)
    elif list[opcode] == "99":
        break

print(list[0])



#Part 2