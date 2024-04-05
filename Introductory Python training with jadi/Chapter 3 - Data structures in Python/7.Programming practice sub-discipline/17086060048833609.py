word = input()
is_ab = False
is_ba = False
i = 0
while i < len(word)-1:
    if word[i] == 'A' and word[i+1] == 'B':
        is_ab = True
        i += 2
    elif word[i] == 'B' and word[i+1] == 'A':
        is_ba = True
        i += 2
    else:
        i += 1
if is_ab and is_ba:
    print("YES")
else:
    print("NO")

