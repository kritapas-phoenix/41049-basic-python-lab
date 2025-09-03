import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

number = 1

while number > 0:
    number = int(input("Enter your number: "))
    if is_prime(number):
        print(f"{number} prime")
    else:
        print(f"{number} not prime")