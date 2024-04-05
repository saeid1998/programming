x1, x2, x3 = [int(x) for x in input().split()]
x1 = abs(x1)
x2 = abs(x2)
x3 = abs(x3)
distance = 0
if x2 <= x1 <= x3 or x3 <= x1 <= x2:
    distance = abs(x1 - x2) + abs(x1 - x3)
elif x1 <= x2 <= x3 or x3 <= x2 <= x1:
    distance = abs(x2 - x1) + abs(x2 - x3)
elif x1 <= x3 <= x2 or x2 <= x3 <= x1:
    distance = abs(x3 - x1) + abs(x3 - x2)

print(distance)
