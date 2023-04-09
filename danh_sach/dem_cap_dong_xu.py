import math
n = int(input())
a = []
for i in range(n):
    a.append(input())
res = 0
for i in range(n):
    row = 0
    for j in range(n):
        if(a[i][j] == 'C'):
            row += 1
    res += math.comb(row, 2)
        
for j in range(n):
    column = 0
    for i in range(n):
        if(a[i][j] == 'C'):
            column += 1
    res += math.comb(column, 2)

print(res)

