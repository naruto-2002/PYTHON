import math

def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True


n, x = map(int, input().split())

primes = []

for i in range(2, 10000):
    if(isPrime(i)):
        primes.append(i)
    if(len(primes) == n):
        break

res = [x]

for val in primes:
    l = len(res) - 1
    res.append(res[l] + val)

for val in res:
    print(val, end=' ')
