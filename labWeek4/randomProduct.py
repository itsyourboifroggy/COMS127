# Jack Byboth 2/6/24 section 2

import random

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))

def randomProduct(a, b, c):
    num = 1
    while a > 0:
        num *= random.randrange(b, c + 1)
        a -= 1
        
    return num

rand = randomProduct(num1, num2, num3)
print(rand)
