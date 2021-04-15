list = [3,3,3,3,3,3,3]
number = input("What number do we want to check: ")

if list == []:
    print("The list is empty.")
else:
    result = True
    for value in list:
        if value != int(number):
            result = False
    print(result)
