t = int(input())
dem, a, res = 0, [], []
while(t > 0):
    t -= 1
    s = input().split()
    if(len(a) == 0 and len(s) == 6): res.append(1)
    a.append(s)
    if(len(a) > 1 and len(s) == 6 and len(a[-2]) == 7): res.append(1)
    if(len(s) == 7): dem += 1
    if(dem == 4):
        res.append(2)
        dem = 0
print(len(res))
for val in res:
    print(val)

