numbers = [65,23,1,5,45,23,4]
print("The original list is: ", numbers)
for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2
print("The new list is: ", numbers)


letters = ["a","c","d","z","f","x"]
print("The original list is: ", letters)
for i in range(len(letters)):
  letters[i] = letters[i] + letters[i]
print("The new list is: ", letters)



numbers = [65,23,1,5,45,23,4]
newlist = []
print("The original list is: ", numbers)
for i in range(len(numbers)):
  newlist.insert(len(newlist),numbers[i])
  newlist.insert(len(newlist), numbers[i])
print("The new list is: ", newlist)



letters = ["a","c","d","z","f","x"]
print("The original list is: ", letters)
for i in range(len(letters)):
  if i % 2 == 0:
    letters[i] = letters[i] + letters[i]
print("The new list is: ", letters)


letters = ["a","c","d"]
newlist = []
print("The original list is: ", letters)
for i in range(len(letters)):
    newlist.insert(len(newlist),letters[i])
    newlist.insert(len(newlist), i)
print("The new list is: ", newlist)
