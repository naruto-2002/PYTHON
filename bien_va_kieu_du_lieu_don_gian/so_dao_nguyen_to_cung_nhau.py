import math
t = int(input())
while( t > 0):
    t -= 1
    n = input()
    a = int(n)
    b = int(n[::-1])
    if(math.gcd(a, b) == 1):
        print('YES')
    else:
        print('NO')