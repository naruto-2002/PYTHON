n = int(input())
list = [int(val) for val in input().split()]
res = []
for val in list:
    res.append(val)
    while(len(res) > 1 and (res[len(res) - 2] + res[len(res) - 1])%2 == 0):
        res.pop()
        res.pop()
print(len(res))
# 