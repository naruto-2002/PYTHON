import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

def reverseNumber(n):
    return int(n[::-1])

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    res = []
    for i in range(13, n):
        b = reverseNumber(str(i))
        if(isPrime(i) and isPrime(b) and i != b and b < n):
            if(not res.count(i) or not res.count(b)):
                res.append(i)
                res.append(b)
    for val in res:
        print(val, end=' ')
    print()
    



