
with open('day8-input') as file:
    instructions = [instruction.rstrip() for instruction in file]


#Part 1
accumulator  = 0
visited = []
address = 0
while address not in visited:
    operation = instructions[address].split()[0]
    argument = instructions[address].split()[1]
    visited.insert(0, address)
    if operation == "nop":
        address += 1
    elif operation == "acc":
        accumulator += int(argument)
        address += 1
    elif operation == "jmp":
        address += int(argument)

print(accumulator)

#Part 2
accumulator  = 0
visited = []
address = 0
while address not in visited and address != len(instructions):
    operation = instructions[address].split()[0]
    argument = instructions[address].split()[1]
    visited.insert(0, address)
    movement = 0
    if operation == "nop":
        movement = 1
    elif operation == "acc":
        accumulator += int(argument)
        movement = 1
    elif operation == "jmp":
        movement = int(argument)

    #It's not necessarily the address before the infinite loop. This is wrong...
    if address+movement in visited:
        #print("stopped repeat address:",address+movement)
        if operation == "nop":
            movement = int(argument)
        elif operation == "jmp":
            movement = 1



    address += movement
    #print(operation,argument)
    #print(address)



print(accumulator)