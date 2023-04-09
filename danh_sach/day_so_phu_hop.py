
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(val) for val in input().split()]
    b = [int(val) for val in input().split()]

    a = sorted(a)
    b = sorted(b)

    check = True
    for i in range(n):
        if(a[i] > b[i]):
            check = False
            break

    if(check):
        print('YES')
    else:
        print('NO')

