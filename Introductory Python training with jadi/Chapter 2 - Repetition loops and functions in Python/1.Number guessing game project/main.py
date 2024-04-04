import random
start = 1
end = 99
while True:
    number = random.randint(start, end)
    print(number)
    user_input = input()
    if user_input == 'k':
        end = number - 1
    elif user_input == 'b':
        start = number + 1
    elif user_input == 'd':
        break


