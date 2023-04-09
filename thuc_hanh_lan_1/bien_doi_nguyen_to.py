import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

ma = 0
mi = 0
for i in range(n):
    if not is_prime(a[i]):
        steps1 = 0
        steps2 = 0
        x = y = a[i]
        while not is_prime(x):
            x -= 1
            steps1 += 1
        while not is_prime(y):
            y += 1
            steps2 += 1
        mi = min(steps1, steps2)
    if(mi != 10**6):
        ma = max(mi, ma)

print(ma)
