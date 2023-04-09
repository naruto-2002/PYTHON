import math
# A = P x (1 + r)^n
t = int(input())
while(t > 0):
    t -= 1
    P, r, A = map(float, input().split())
    n = math.log(A/P, 1+r*0.01)
    print(math.ceil(n))

