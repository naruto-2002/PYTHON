import math
a, k, n = map(int, input().split())
ok = 0
c = k*math.gcd(a, k)
for i in range(c, n + 1, k):
    if(i - a > 0):
        ok = 1
        print(i-a, end=' ')
if(ok == 0):
    print(-1)