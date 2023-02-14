m, n = map(int, input().split())
a = []
b = []
for i in range(m):
    c = [int(val) for val in input().split()]
    a.append(c)
    b = b + c
ma = max(b)
mi = min(b)
distance = ma - mi
ok = False
for i in range(m):
    for j in range(n):
        if(a[i][j] == distance):
            ok = True
            break
    if(ok):
        break
if(ok):
    print(distance)
    for i in range(m):
        for j in range(n):
            if(a[i][j] == distance):
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')
