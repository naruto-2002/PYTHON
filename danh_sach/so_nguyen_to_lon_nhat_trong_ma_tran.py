import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i==0):
            return False
    return True

row, column = map(int, input().split())
a = []
b = []
for i in range(row):
    c = [int(val) for val in input().split()]
    a.append(c)
    b = b + c
ma = -1
for val in b:
    if(val > ma and isPrime(val)):
        ma = val

if(ma == -1):
    print('NOT FOUND')
else:
    print(ma)
    for i in range(row):
        for j in range(column):
            if(a[i][j] == ma):
                print(f'Vi tri [{i}][{j}]')

