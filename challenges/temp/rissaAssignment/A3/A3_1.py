numAccesses = 0
dataFile = open(str(input("Enter the name of the file to read from: ")+".txt"), "r") #Read only mode
outputFile = open("res.txt", "w") #Writing mode


for line in dataFile.readlines(): #For every line in the input_file
    lastName = line.split(" ")[0]
    emailAddress = line.split(" ")[1]
    numberAccesses = int(line.split(" ")[2])
    if numberAccesses < 15: #If they have less than 15 blackboard accesses add them to the new list.
        outputFile.write(emailAddress+",")
        numAccesses += 1

print("you will need to check in with "+str(numAccesses)+" people, their emails are in res.txt")

dataFile.close()
outputFile.close()



