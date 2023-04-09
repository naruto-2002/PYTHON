res = []

for t in range(int(input())):
    res.append(input())

dem = 0
s = res[0]

for i in range(len(res)):
    dem += 1
    if(res[i] == ''):
        print(f'{s}: {dem-2}')
        s = res[i+1]
        dem = 0

print(f'{s}: {dem-1}')