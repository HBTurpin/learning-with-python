oneList = ["Cat", 75, "Bob", 10, "Ben", 55, "Summer", 99, "Tomasz", 40]
oneList = ["a", 10, "b", 1, "c", 60, "d", 88, "e", 100]
print("The original list looked like this: ", oneList)

newList = []
for i in range(int(len(oneList) / 2)):
    name = oneList[(i * 2)]
    score = oneList[(i * 2) + 1]
    if score > 45:
        newList.insert(len(newList), name + "-" + str(score))

print("The new list looks like this: ", newList)
