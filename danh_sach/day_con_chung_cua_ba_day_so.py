t = int(input())
while(t > 0):
    t -= 1
    m, n, k = map(int, input().split())
    p1 = p2 = p3 = ok = 0
    a = [int(val) for val in input().split()]
    b = [int(val) for val in input().split()]
    c = [int(val) for val in input().split()]

    while p1 < m and p2 < n and p3 < k:
        if(a[p1] == b[p2] and b[p2] == c[p3]):
            print(a[p1], end=' ')
            ok = 1
            p1 += 1
            p2 += 1
            p3 += 1
        elif a[p1] < b[p2]: p1 += 1
        elif b[p2] < c[p3]: p2 += 1
        elif c[p3] < a[p1]: p3 += 1
    
    if(ok == 0):
        print('NO')
    else:
        print()
   
    
