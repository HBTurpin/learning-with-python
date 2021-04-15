file_name = str(input("Enter the name of the file to read from: ")+".txt") #Read only mode
file = open(file_name, "r")
print("Reading student ids and scores from file:", file_name)

lastId = ""
scoresList = []
for line in file.readlines(): #For every line in the input_file
    pId = line[:line.find(" ")] #Splice to get everything before the found space.
    score = int(line[line.find(" ")+1:]) #Splice to get everything after the found space.

    if pId != lastId:
        if lastId != "": #Do not print anything for the initial change of ID.
            print(lastId, "completed", len(scoresList), "quizzes and got these scores:", scoresList)
        lastId = pId
        scoresList = [] #New ID so empty the score list.

    scoresList.append(score)

print(lastId, "completed", len(scoresList), "quizzes and got these scores:", scoresList) #Deal with last student
file.close()


