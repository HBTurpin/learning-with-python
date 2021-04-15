
def find_num( word ):
    total = 0
    for letter in word:
        if letter == "a":
            total += 1
    return total

word = input("Enter a word or sentence: ")
char = "a"
res = find_num( word )
print("The letter " + char + " showed up " + str(res) + " times in what you entered.")