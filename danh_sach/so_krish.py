import re

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n - 1)

def check(n):
    m = str(n)
    numbers = re.findall(r'\d', m)
    sum = 0
    for val in numbers:
        sum += factorial(int(val))
    if(n == sum):
        return True
    else:
        return False

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    if(check(n) == True):
        print('Yes')
    else:
        print('No')