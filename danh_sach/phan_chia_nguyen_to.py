import math

def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

n = int(input())
a = [int(val) for val in input().split()]
b = []
for val in a:
    if(val not in b):
        b.append(val)
m = len(b)
ok = 0
for i in range(m):
    if(isPrime(sum(b[0:i+1])) and isPrime(sum(b[i+1:m]))):
        ok = 1
        print(i)
        break
if(ok == 0):
    print('NOT FOUND')
