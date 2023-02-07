import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

def check(n):
    l = len(n)
    sum = 0
    for i in range(l):
        sum += int(n[i])
        if(i%2 == 0 and int(n[i])%2 != 0 or i%2 != 0 and int(n[i])%2 == 0):
            return False
    if(not isPrime(sum)):
        return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if(check(n)):
        print('YES')
    else:
        print('NO')