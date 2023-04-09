
m, n = map(int, input().split())
a = [int(val) for val in input().split()]

b = []

for i in range(1, n + 1):
    if(a.count(i) > 0):
        b.append([i, a.count(i)])

b.sort(key=lambda x: x[1], reverse = True)

ok = False

res = 0

for i in range(len(b)-1):
    if(b[i][1] != b[i+1][1]):
        ok = True
        res = b[i+1][0]
        break

if(ok):
    print(res)
else:
    print('NONE')