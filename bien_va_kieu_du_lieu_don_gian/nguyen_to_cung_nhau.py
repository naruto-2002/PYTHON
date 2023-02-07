import math
n, k = map(int, input().split())
dem = 0
for i in range(10**k + 1):
    
    if(len(str(i)) == k and math.gcd(i, n) == 1):
        print(i, end=' ')
        dem += 1
    if(dem == 10):
        print()
        dem = 0