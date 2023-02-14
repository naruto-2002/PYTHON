import math
def check(n):
    n = str(n)
    if(n == n[::-1] and len(n) > 1):
        return True
    return False

row, column = map(int, input().split())
a = []
b = []
for i in range(row):
    c = [int(val) for val in input().split()]
    a.append(c)
    b = b + c
ma = -1
for val in b:
    if(val > ma and check(val)):
        ma = val
if(ma == -1):
    print('NOT FOUND')
else:
    print(ma)
    for i in range(row):
        for j in range(column):
            if(a[i][j] == ma):
                print(f'Vi tri [{i}][{j}]')

