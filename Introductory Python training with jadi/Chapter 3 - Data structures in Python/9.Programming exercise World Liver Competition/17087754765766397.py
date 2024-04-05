n = int(input())
arr = input().split()
allowed_number = 0
number_of_teams = 0
for i in range(n):
    if int(arr[i]) == 0 or int(arr[i]) == 1 or int(arr[i]) == 2:
        allowed_number += 1
while allowed_number > 2:
    allowed_number -= 3
    number_of_teams += 1
print(number_of_teams)

