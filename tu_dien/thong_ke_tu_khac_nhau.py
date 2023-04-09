import re
res = {}
a = []
for t in range(int(input())):
    t -= 1
    s = input().lower()
    x = re.findall(r'[a-z]+', s)
    for ss in x:
        if ss not in a:
            res[ss] = 1
            a.append(ss)
        else:
            res[ss] += 1
       

a.sort()
a.sort(key=lambda x: -res[x])

for val in a:
    print(val, res[val])
