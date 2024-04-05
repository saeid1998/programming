number = input()
number = sorted(number)
number = number[(len(number)//2):]
for i in range(len(number)-1):
    print(f'{number[i]}+', end='')
print(number[-1])
