import math

n = int(input())
numbers = []
for i in range(n):
    num = float(input())
    numbers.append(math.sqrt(num))

for i in range(n):
    str_num = str(numbers[i])
    index_num = str_num.index('.')
    if str_num[index_num + 1] == '0' or str_num[index_num + 2] or str_num[index_num + 3] or str_num[index_num + 4]:
        str_num += '0000'
    print(str_num[0:index_num + 5])


