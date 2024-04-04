num = int(input())
inverse_num = 0
inverse_num += (num % 10) * 100
num //= 10
inverse_num += (num % 10) * 10
num //= 10
inverse_num += num % 10
print(inverse_num * 2)