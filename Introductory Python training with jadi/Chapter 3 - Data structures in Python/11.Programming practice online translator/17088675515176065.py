n = int(input())
dictionary = {}
for i in range(n):
    key, value = input().split()
    dictionary[key] = value
sentence = input().split()
for item in sentence:
    if item in dictionary.keys():
        print(dictionary[item], end=' ')
    else:
        print(item, end=' ')

