name = input("Type some string: ")
list1 = []

for i in range(len(name)):
    list1.append([i, name[i]])
print(list1)


scores = [["ben", 667, 22, 1, 44, 5, 0], ["may", 10, 12, 14], ["zeke", 99, 888], ["bob", 55, 66, 44, 56, 77, 88]]
highestScore = 0
highestPlayer = ""
for playerScores in scores:
    currentScore = 0
    for playerScore in range(1, len(playerScores), 1):
        currentScore += playerScores[playerScore]
    print("Player ", playerScores[0], " got a total of : ", currentScore)

    if currentScore > highestScore:
        highestScore = currentScore
        highestPlayer = playerScores[0]

print("Here is the best player name and their score: ", highestPlayer, highestScore)

