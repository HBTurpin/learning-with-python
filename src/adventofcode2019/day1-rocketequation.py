import math


with open('day1-input') as file:
    entries = [line.rstrip() for line in file]


#Part 1
fuel_required = 0
for entry in entries:
    fuel_required += math.floor(int(entry)/3)-2
print(fuel_required)




#Part 2
def recursion_calculation(mass):
    fuel = math.floor(int(mass)/3)-2
    if fuel > 0:
        return fuel + recursion_calculation(fuel)
    return max(fuel,0)

fuel_required = 0
for entry in entries:
    fuel_required += recursion_calculation(int(entry))
print(fuel_required)
