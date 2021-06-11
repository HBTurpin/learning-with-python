
def get_divisors(num):
    list_of_divisors = []
    for i in range(1,int(num/2)+1,1):
        if (num / (i)) % 1 == 0:
            list_of_divisors.append(i)
    return list_of_divisors

def sum_list(list):
    result = 0
    for i in range(len(list)):
        result += list[i]
    return result
    
def is_amicable(num):
    num_divisors_sum = sum_list(get_divisors(num))
    result_divisors_sum = sum_list(get_divisors(num_divisors_sum))
    if result_divisors_sum == num and num_divisors_sum != num:
        print(num_divisors_sum, result_divisors_sum)
        return True
    return False

def total_amicable_numbers(num):
    result = 0
    for i in range(num):
        result += i if is_amicable(i) else 0
    return result


total_amicable_numbers(10000)
