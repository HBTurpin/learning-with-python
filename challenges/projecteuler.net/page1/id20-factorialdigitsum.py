

def factorial(num):
    result = num
    for i in range(num,1,-1):
        result *= i
    return result

def sum_digits(num):
    result = 0
    string_num = str(num)
    for i in range(len(str(num))):
        print(string_num[i])
        result += int(string_num[i])
    return result

print(sum_digits(factorial(100)))
