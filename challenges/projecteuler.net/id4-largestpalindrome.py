import math

def find_largest_palindrome(digits):
    largest_number = 0
    for a in range ((10**digits)-1,10**(digits-1),-1):
        for b in range ((10**digits)-1,10**(digits-1),-1):
            number = str(a*b)
            # Loop through each index of the number to see if it matches the opposite side.
            palindrome = 1
            for i in range(math.ceil(len(number)/2)):
                if number[i] != number[-i-1]:
                     palindrome = 0
            #If palindrome check if larger number
            if palindrome:
                if int(number) > largest_number:
                    largest_number = int(number)
    #Need to loop through all of them as its possible the number might not be the first one.
    return largest_number


def find_largest_palindrome_simplified(digits):
    largest_number = 0
    for a in range ((10**digits)-1,10**(digits-1),-1):
        for b in range ((10**digits)-1,10**(digits-1),-1):
            number = a*b
            if str(number) == str(number)[::-1]:
                if int(number) > largest_number:
                    largest_number = int(number)
    return largest_number

print(find_largest_palindrome_simplified(3))







