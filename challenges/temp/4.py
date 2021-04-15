

file_name = input("Input a name for the file to be written to: ")
file = open(str(file_name+".txt"), "w")

for i in range (0,20,1):
  file.write(str(i)+"\n") #Write the numbers

file.close()





file_name = input("Input a name for the file to be read: ")
file = open(str(file_name+".txt"))
lines = file.readlines()
total = 0
for line in lines:
  total += int(line)

print(total)
file.close()




name = input("Please enter your first name and last name seperated by a space: ")
first_name = name.split(" ")[0]
print(first_name)
last_name = name.split(" ")[1]
print(last_name)