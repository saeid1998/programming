word = input()
counter_hello = 0
for i in range(len(word)):
    if word[i] == 'h' and counter_hello == 0:
        counter_hello += 1
    elif word[i] == 'e' and counter_hello == 1:
        counter_hello += 1
    elif word[i] == 'l' and counter_hello == 2:
        counter_hello += 1
    elif word[i] == 'l' and counter_hello == 3:
        counter_hello += 1
    elif word[i] == 'o' and counter_hello == 4:
        counter_hello += 1
if counter_hello == 5:
    print("YES")
else:
    print("NO")