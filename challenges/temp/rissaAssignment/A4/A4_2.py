myList = ["Kat: 10,20,3", "Bob: 3", "Mary: 44,33,55,66", "Jack: 2,1,5,6,7", "Lori: 99"]

for i in range(len(myList)):
    string = myList[i]
    name = string[:string.find(": ")]
    numbers = string[string.find(" ")+1:]
    myList[i] = [name, numbers]

print("Revised list: ", myList)
print("Part 2: Here is the output formatted nicer:")

for item in myList:
    print(item[0], "had these scores:", item[1])