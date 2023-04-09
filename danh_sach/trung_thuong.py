
t = int(input())

while(t > 0):
    t -= 1
    n = int(input())
    a = []
    while(n > 0):
        n -= 1
        a.append(int(input()))
    a = sorted(a)
    m = {}
    for val in a:
        if val in m:
            m[val] += 1
        else:
            m[val] = 1
    s = 0
    p = 0

    for val in a:
        if(m[val] > s):
            s = m[val]
            p = val
    
    print(p)