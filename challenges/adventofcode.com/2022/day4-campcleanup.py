import math

def part_1():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day4-input.txt') as file:
        pairs = [line.rstrip() for line in file]
    count = 0
    for pair in pairs:
        elf = [areas.split("-") for areas in pair.split(",")]

        elf1 = list(range(int(elf[0][0]), int(elf[0][1])+1))
        elf2 = list(range(int(elf[1][0]), int(elf[1][1])+1))

        if (int(elf[0][0]) in elf2 and int(elf[0][1]) in elf2) or (int(elf[1][0]) in elf1 and int(elf[1][1]) in elf1):
            count += 1
    print(count)



                
part_1()


def part_2():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day4-input.txt') as file:
        pairs = [line.rstrip() for line in file]

    count = 0
    for pair in pairs:
        elf = [areas.split("-") for areas in pair.split(",")]

        elf1 = list(range(int(elf[0][0]), int(elf[0][1])+1))
        elf2 = list(range(int(elf[1][0]), int(elf[1][1])+1))

        if (int(elf[0][0]) in elf2 or int(elf[0][1]) in elf2) or (int(elf[1][0]) in elf1 or int(elf[1][1]) in elf1):
            count += 1
    print(count)
       
part_2()