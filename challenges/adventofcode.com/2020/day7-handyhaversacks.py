
with open('day7-input') as file:
    rules = [rule.rstrip() for rule in file]


#Part 1
bags = ["shiny gold"]
found = True
while found:
    found = False
    for rule in rules:
        for bag in bags:
            if bag in str(' '.join(map(str, rule.split()[4:]))):
                parent = ' '.join(map(str, rule.split()[:2]))
                if parent not in bags:
                    bags.insert(0,parent)
                    found = True

print(len(bags)-1)

#Part 2
total_bags = 0
def go_deeper(bag):
    global total_bags
    total_bags += 1
    for rule in rules:
        if bag == ' '.join(map(str, rule.split()[:2])):
            read = rule.split()[4:]
            for i in range(0, len(read), 4):
                if read[i] == "no":
                    break
                for b in range(0,int(read[i]),1):
                    go_deeper(' '.join(map(str, read[i+1:i+3])))


go_deeper("shiny gold")
print(total_bags-1)