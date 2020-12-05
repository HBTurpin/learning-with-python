import string

with open('day4-input') as file:
    lines = [line.rstrip() for line in file]

#Part 1
valid_passports = 0
passport = ""
matches = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
for line in lines: #Slight issue with this method as it won't count the last passport unless there is two leading blank lines.
    if len(line.strip()) == 0:
        if all(i in passport for i in matches):
            valid_passports += 1
        passport = ""
    else:
        passport += line + " "

print(valid_passports)



#Part 2
valid_passports = 0
passport = ""
for line in lines:
    if len(line.strip()) == 0:
        valid_passport = 1
        fields = passport.split(" ")
        for field in fields:

            if len(field.strip()) == 0:
                continue

            id = field.split(":")[0]
            data = field.split(":")[1]
            if id == "byr":
                if not (1920 <= int(data) <= 2002):
                    valid_passport = 0
            elif id == "iyr":
                if not (2010 <= int(data) <= 2020):
                    valid_passport = 0
            elif id == "eyr":
                if not (2020 <= int(data) <= 2030):
                    valid_passport = 0
            elif id == "hgt":
                number = int(''.join([i for i in data if i.isdigit()]))
                if "cm" in data:
                    if not(150 <= number <= 193):
                        valid_passport = 0
                elif "in" in data:
                    if not(59 <= number <= 76):
                        valid_passport = 0
                else:
                    valid_passport = 0
            elif id == "hcl":
                if not data[0] == "#" or not len(data[1:]) == 6 or not(all(i in string.hexdigits for i in data[1:])):
                    valid_passport = 0
            elif id == "ecl":
                if not(any(i in data for i in ["amb","blu","brn","gry","grn","hzl","oth"])):
                    valid_passport = 0
            elif id == "pid":
                if len(data) != 9 or not(all(i in string.digits for i in data)):
                    valid_passport = 0

        valid_passports += valid_passport
        passport = ""
    else:
        passport += line + " "

print(valid_passports)
