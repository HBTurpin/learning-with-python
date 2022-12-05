import math

def part_1():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day3-input.txt') as file:
        lines = [line.rstrip() for line in file]

    score = 0
    scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for line in lines:
        split_index = int(math.floor(len(line)/2))
        compartments = [line[0:split_index], line[split_index:]]
        for item in compartments[0]:
            if item in compartments[1]:
                # print(compartments)
                # print(item, scores.find(item) + 1)
                score += scores.find(item) + 1
                break
    print(score)

                
part_1()


def part_2():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day3-input.txt') as file:
        lines = [line.rstrip() for line in file]

    score = 0
    scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(0, len(lines), 3):

        rucksacks = lines[i:i+3]
        print(rucksacks, "\n")
        for item in rucksacks[0]:
            if item in rucksacks[1] and item in rucksacks[2]:
                score += scores.find(item) + 1
                break
    print(score)

                
part_2()