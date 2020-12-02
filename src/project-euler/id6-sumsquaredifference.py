def sum_square_difference(min,max):
    answer = 0
    sum = 0
    for i in range(min,max+1):
        answer += i*i
        sum += i
    answer -= sum*sum
    return abs(answer)



print(sum_square_difference(1,100))







