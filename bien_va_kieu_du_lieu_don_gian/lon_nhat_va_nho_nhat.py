
while True:
    n = int(input())
    if(n == 0):
        break
    m = n
    a = []
    while(m > 0):
        m -= 1
        a.append(int(input()))
    mi = min(a)
    ma = max(a)
    if(mi == ma):
        print('BANG NHAU')
    else:
        print(mi, ma)