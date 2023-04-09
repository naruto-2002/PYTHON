n = int(input())
a = []
while True:
    x = [int(val) for val in input().split()]
    a += x
    if len(a) == n:
        break
ma = max(a)
ok = 1
for i in range(1, ma + 1):
    if i not in a:
        ok = 0
        print(i)
if ok == 1:
    print('Excellent!')