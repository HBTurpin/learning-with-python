
with open('day9-input') as file:
    numbers = [number.rstrip() for number in file]

#Part 1
def is_summable(list_of_numbers, result):
    for i1, n1 in enumerate(list_of_numbers):
        for i2, n2 in enumerate(list_of_numbers):
            if i1 != i2:
                print(n1, "+", n2, "=", int(n1) + int(n2))
                if int(n1) + int(n2) == int(result):
                    return True
    return False

invalid_number = 0
for i in range(25,len(numbers),1):
    if not is_summable(numbers[i-25:i],numbers[i]):
        invalid_number = numbers[i]
        break

print(invalid_number)

#Part 2
for i1 in range(0,len(numbers),1):
    for i2 in range(i1,len(numbers),1):
        if i1 != i2:
            total = sum(map(int,numbers[i1:i2+1]))
            if total > int(invalid_number):
                break
            if int(invalid_number) == total:
                print(max(map(int,numbers[i1:i2+1]))+min(map(int,numbers[i1:i2+1])))
