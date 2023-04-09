import math
l, r = map(int, input().split())
for a in range(l, r + 1 - 2):
    for b in range(a + 1, r + 1 - 1):
        for c in range(b + 1, r + 1):
            if(a < b and b < c and math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1):
                print('(' + str(a) + ', ' + str(b) + ', ' + str(c) + ')')

