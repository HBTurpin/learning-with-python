
with open('day2-input') as file:
    entries = [line.rstrip() for line in file]



#Part 1
valid_passwords = 0
for entry in entries:
    minimum = entry.split(" ")[0].split("-")[0]
    maximum = entry.split(" ")[0].split("-")[1]
    letter = entry.split(" ")[1][0]
    password = entry.split(" ")[2]
    if password.count(letter) >= int(minimum) and password.count(letter) <= int(maximum):
        valid_passwords += 1
print(valid_passwords)

#Part 2
valid_passwords = 0
for entry in entries:
    first = entry.split(" ")[0].split("-")[0]
    second = entry.split(" ")[0].split("-")[1]
    letter = entry.split(" ")[1][0]
    password = entry.split(" ")[2]
    if (password[int(first)-1] == letter) != (password[int(second)-1] == letter):
        valid_passwords += 1
print(valid_passwords)