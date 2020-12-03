def collatz_chain_length(start):
    number = start
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = (number*3)+1
        length += 1
    return length


def find_longest_chain(min,max):
    longest_chain = 0
    longest_start = 0
    for i in range(min,max+1,1):
        length = collatz_chain_length(i)
        if length > longest_chain:
            longest_start = i
            longest_chain = length
    return longest_start



print(find_longest_chain(13,1000000))
