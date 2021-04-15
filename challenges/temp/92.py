def checker(list1,minScore):
    valid = []
    for item in list1:
        if item[1] >= minScore:
            valid.append(item[0])
    return valid



#first call to the function
myList1 = [ ["P12",20], ["P11",2], ["P4",22], ["P5",12], ["P13",2] ]
value = int(input("Enter the min score threshold: "))
res = checker(myList1, value)
print("Participants with score above the threshold includes: ", res)

#second call to the function
myList1 = [ ["P2",5], ["P113",22] ]
value = int(input("Enter the min score threshold: "))
res = checker(myList1, value)
print("Participants with score above the threshold includes: ", res)
