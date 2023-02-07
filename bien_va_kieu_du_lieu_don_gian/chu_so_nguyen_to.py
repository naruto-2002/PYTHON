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
    if(not isPrime(l)):
        return False
    not_Prime = 0
    is_Prime = 0
    for val in n:
        if(isPrime(int(val))):
            is_Prime += 1
        else:
            not_Prime += 1
    if(is_Prime <= not_Prime):
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