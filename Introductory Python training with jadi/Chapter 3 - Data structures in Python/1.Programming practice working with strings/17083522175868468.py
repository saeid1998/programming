string = input()
string = string.lower()
new_string = ''
for letter in string:
    if not (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        new_string += letter

for letter in new_string:
    print(f'.{letter}', end='')
