
with open('day10-input') as file:
    numbers = [int(number.rstrip()) for number in file]
numbers.sort()
numbers.insert(0,0)
numbers.insert(len(numbers),numbers[len(numbers)-1]+3)


#Part 1
differences = [0,0,0]
for i in range(0,len(numbers)-1,1):
    diff = numbers[i+1] - numbers[i]
    if diff in [1,2,3]:
        differences[diff-1] += 1

print(differences)
print(differences[0]*differences[2])



#Part 2 - need to rethink this one
total_lists = 0
def branch(index, list): #Issue with upper tier list getting branched to the lower tier branches
    global total_lists
    current_number = numbers[index]
    list.insert(len(list),current_number)
    found = False
    for n in range(1,3,1):
        if index+n >= len(numbers)-1:
            break
        next_number = numbers[index+n]
        difference = next_number - current_number
        if difference <= 3:
            branch(index+n,list)
            found = True

    if found == False:
        total_lists += 1

branch(0,[])
print(total_lists)