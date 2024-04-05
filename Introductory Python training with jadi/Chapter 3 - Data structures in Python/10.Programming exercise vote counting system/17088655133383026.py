n = int(input())
dictionary = {}
for i in range(n):
    string = input()
    if string in dictionary:
        dictionary[string] += 1
    else:
        dictionary[string] = 1

for key, value in sorted(dictionary.items()):
    print(key, value)
