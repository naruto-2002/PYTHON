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
    is_prime = 0
    not_prime = 0
    for val in n:
        if(isPrime(int(val))):
            is_prime += 1
        else:
            not_prime += 1
    if(is_prime <= not_prime):
        return False
    return True
t = int(input())
while(t > 0):
    t -= 1
    number = input()
    if(check(number)):
        print('YES')
    else:
        print('NO')