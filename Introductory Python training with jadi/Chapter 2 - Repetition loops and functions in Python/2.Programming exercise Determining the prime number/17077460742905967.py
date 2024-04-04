def is_prime(number):
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True


user_number = int(input())
if is_prime(user_number):
    print("prime")
else:
    print("not prime")
