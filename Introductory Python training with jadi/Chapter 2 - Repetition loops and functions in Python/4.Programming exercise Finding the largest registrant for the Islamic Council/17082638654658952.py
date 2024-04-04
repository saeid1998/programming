age = 0
while True:
    input_num = int(input())
    if input_num == -1:
        break
    else:
        if input_num > age:
            age = input_num
print(age)
