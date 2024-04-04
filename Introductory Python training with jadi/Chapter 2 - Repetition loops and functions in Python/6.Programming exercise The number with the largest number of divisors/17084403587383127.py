def divisor(number):
    number_of_divisor = 2
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            number_of_divisor += 1
    return number_of_divisor


greatest_divisor = 0
number = 0
for i in range(20):
    entered_number = int(input())
    if divisor(entered_number) > greatest_divisor:
        greatest_divisor = divisor(entered_number)
        number = entered_number
    elif divisor(entered_number) == greatest_divisor and entered_number > number:
        number = entered_number
print(number, greatest_divisor)

