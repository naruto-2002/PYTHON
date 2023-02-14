import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append([int(val) for val in input().split()]) 
    for j in range(n):
        if(isPrime(a[i][j])):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
