from collections import OrderedDict

months = OrderedDict( [("January",31),("February", 28),("March",31),
                       ("April", 30), ("May", 31), ("June", 30),
                       ("July", 31), ("August", 31), ("September", 30),
                       ("October", 31), ("November", 30), ("December", 31)] )

days = ['Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']



def is_leap(year): #https://en.wikipedia.org/wiki/Leap_year#Algorithm
    leap = True
    if year % 4 != 0:
        leap = False
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    return leap



def get_sundays(syear,eyear):
    day = 0
    sunday_count = 0
    for year in range(syear,eyear):
        leap = is_leap(year)
        for m in months:
            dayName = days[day%7]
            if dayName == "Sunday":
                sunday_count += 1
            day += months[m]
            if leap == True and m == "February":
                day += 1

    return sunday_count



print(get_sundays(1901,2001))

