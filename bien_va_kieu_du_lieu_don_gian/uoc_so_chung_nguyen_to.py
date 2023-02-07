import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

def totalNumber(number):
    number = str(number)
    sum = 0
    for val in number:
        sum += int(val)
    return sum
t = int(input())
for tt in range(t):
    a, b = map(int, input().split())
    if(isPrime(totalNumber(math.gcd(a, b)))):
        print('YES')
    else:
        print('NO')
