import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


n = int(input())
a = [int(val) for val in input().split()]

primePos = []
primes = []

for i in range(len(a)):
    if(isPrime(a[i])):
        primePos.append(i)
        primes.append(a[i])
primes.sort()

for i in range(len(primes)):
    a[primePos[i]] = primes[i]

res = ' '.join(list(map(str, a)))
print(res)