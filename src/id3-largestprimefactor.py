answer = 600851475143
i = 2

while i * i < answer:
    if answer % i == 0:
        answer = answer / i
    else:
        i += 1

print(answer)


