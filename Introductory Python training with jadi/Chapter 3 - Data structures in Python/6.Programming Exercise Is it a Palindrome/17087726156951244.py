word = input().lower()
is_palindrome = True
for i in range(len(word)//2):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = False
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")
