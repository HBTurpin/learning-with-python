def is_prime(number):
    if number == 1:
        return False
    for j in range (2,number,1):
        if number % j == 0:
            return False
    return True



#Could defo be optimised by not not incrementing through every number...
def get_prime_number(position):
    prime_count = 0
    prime_check = 2
    while prime_count <= position:
        if is_prime(prime_check):
            prime_count += 1
            print(str(prime_count)+":"+str(prime_check))
        if prime_count == position:
            return prime_check
        prime_check += 1


print(get_prime_number(10001))







