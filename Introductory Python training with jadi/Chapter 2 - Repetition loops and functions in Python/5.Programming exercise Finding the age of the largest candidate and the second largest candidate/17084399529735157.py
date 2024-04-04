one_oldest_age = 0
second_oldest_age = 0
while True:
    input_num = int(input())
    if input_num == -1:
        break
    else:
        if input_num > one_oldest_age:
            second_oldest_age = one_oldest_age
            one_oldest_age = input_num
        elif input_num > second_oldest_age:
            second_oldest_age = input_num
print(one_oldest_age, second_oldest_age)
