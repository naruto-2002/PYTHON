import math

def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

def check(number):
    sum = 0
    for val in number:
        sum += int(val)
    if(isPrime(sum)):
        return True
    else:
        return False



t = int(input())
while(t > 0):
    t -= 1
    number = input()
    if(check(number)):
        print('YES')
    else:
        print('NO')