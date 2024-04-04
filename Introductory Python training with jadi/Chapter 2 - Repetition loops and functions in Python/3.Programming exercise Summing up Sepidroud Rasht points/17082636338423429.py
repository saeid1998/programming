total_points = 0
number_of_wins = 0
for i in range(30):
    enter_num = int(input())
    total_points += enter_num
    if enter_num == 3:
        number_of_wins += 1
print(total_points, number_of_wins)

