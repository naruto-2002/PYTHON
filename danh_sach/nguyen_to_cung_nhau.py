import math
n = int(input())
a = [int(val) for val in input().split()]
a = sorted(a)
res = []
for i in range(n - 1):
    for j in range(i+1, n):
        if(math.gcd(a[i], a[j]) == 1):
            res.append([a[i], a[j]])
res = sorted(res, key = lambda x:x[0])
for val in res:
    print(val[0], val[1])