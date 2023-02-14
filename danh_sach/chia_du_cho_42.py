t = 0
b = [0]*42
while True: 
    a = [int(val) for val in input().split()]
    for val in a:
        b[val%42] = 1
    t += len(a)
    if(t == 10):
        break

res = 0
for val in b:
    if(val == 1):
        res += 1

print(res)