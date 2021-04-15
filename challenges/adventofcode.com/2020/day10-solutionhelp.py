with open('day10-input') as file:
    adapters = [int(number.rstrip()) for number in file]

def part_1():
    c = 0
    v = 0
    differences = {1: 0, 2: 0, 3: 1}
    difference_list = []
    while len(adapters) > c:
        adapter = adapters[c]
        diff = adapter - v
        difference_list.append(diff)
        differences[diff] += 1
        v = adapter
        c += 1
    print(differences[1] * differences[3])
    return difference_list


part_1()


def part_2():
    diffs = part_1()
    import operator
    import functools
    combinations = functools.reduce(operator.mul, [z if z != 8 else 7 for z in [2**(y.count('1') - 1) for y in " ".join([str(diff) for diff in diffs]).split("3 ") if y]], 1)
    print("combinations", combinations)


part_2()
