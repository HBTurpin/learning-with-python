digits = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]



def get_less_99(number):
    text = ""
    if number <= 0:
        return text
    if number <= 19:
        text += digits[number-1]
    else:
        text += tens[(number//10)-1]
        if number%10 >= 1:
            text += digits[(number%10)-1]

    return text



def get_text_number(number):
    text = ""
    if number // 1000 >= 1:
        text += get_less_99(number//1000) + "thousand"
    if (number // 100) % 10 >= 1:
        text += get_less_99((number // 100) % 10) + "hundred"
    if number%100 >= 1 and number >= 100:
        text += "and"
    text += get_less_99(number%100)
    print(text)
    return text

def get_sum_text(min,max):
    length = 0
    for i in range(min,max+1,1):
        length += len(get_text_number(i))
    return length




print(get_sum_text(1,1000))

