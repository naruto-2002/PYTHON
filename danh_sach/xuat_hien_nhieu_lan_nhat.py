t = int(input())

while(t > 0):
    t -= 1
    n = int(input())
    a = input().split()
    a = sorted(a)
    l = len(a)
    m = {}

    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    s = 0
    p = 0
    for i in a:
        if(m[i] > s):
            s = m[i]
            p = i
    if s > l/2:
        print(p)
    else:
        print('NO')
    