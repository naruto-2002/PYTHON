import math
def isPrime(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0): return False
    return True
n = int(input())
a = [int(val) for val in input().split()]
res = []
for val in a:
    if(isPrime(val) and (val not in res)):
        res.append(val)
for val in res:
    print(val, a.count(val))