fibonacci_list = [1, 2]

max_number = 0
while max_number <= 4000000:
    max_number = fibonacci_list[len(fibonacci_list) - 2] + fibonacci_list[len(fibonacci_list) - 1]
    fibonacci_list.insert(len(fibonacci_list), max_number)

answer = 0
for n in fibonacci_list:
    if n % 2 == 0:
        answer += n

print(answer)
