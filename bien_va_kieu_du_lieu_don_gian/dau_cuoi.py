t  = int(input())
while(t > 0):
    t -= 1
    a = input()
    l = len(a)
    if(a[0] == a[l-2] and a[1] == a[l - 1]):
        print('YES')
    else:
        print('NO')
