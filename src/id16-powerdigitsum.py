def sum_power_digits(number,power):
    sum = 0
    to_sum = str(number**power)
    for i in range(len(to_sum)):
        sum += int(to_sum[i])
    return sum

print(sum_power_digits(2,1000))
