
f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
while(t > 0):
    t -= 1
    nub, k = map(int, input().split())
    res = ''
    while(nub/k != 0):
        x = nub%k
        res = f[x] + res
        nub //= k
    print(res)
