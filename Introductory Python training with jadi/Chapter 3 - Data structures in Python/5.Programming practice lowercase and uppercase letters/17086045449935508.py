word = input()
upper_case = 0
lower_case = 0
for i in range(len(word)):
    if word[i] == word[i].lower():
        lower_case += 1
    elif word[i] == word[i].upper():
        upper_case += 1
if upper_case > lower_case:
    print(word.upper())
else:
    print(word.lower())
