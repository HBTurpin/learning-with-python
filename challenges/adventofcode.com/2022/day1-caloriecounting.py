import math



def part_1():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day1-input.txt') as file:
        lines = [line.rstrip() for line in file]
    
    elf_list = []
    elf_count = 0
    elf_largest = [1, 0]
    elf_index = 1
    for line in lines:
        if line == "":
            elf_list.append(elf_count)
            if elf_count > elf_largest[1]:
                elf_largest = [elf_index, elf_count]
            elf_count = 0
            elf_index += 1
        else:
            elf_count += float(line)
    print(elf_largest)
        




def part_2():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day1-input.txt') as file:
        lines = [line.rstrip() for line in file]
    
    elf_list = []
    elf_count = 0
    for line in lines:
        if line == "":
            elf_list.append(elf_count)
            elf_count = 0
        else:
            elf_count += float(line)
    elf_list.sort(reverse=True)
    print(sum(elf_list[0:3]))

part_2()