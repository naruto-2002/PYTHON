
n = int(input())
a = []
for i in range(n):
    a.append([int(val) for val in input().split()])

sum_up = 0
sum_down = 0

for i in range(n):
    for j in range(n):
        if(j < n - i - 1):
            sum_up += a[i][j]
        elif(j > n - i - 1):
            sum_down += a[i][j]

distance = abs(sum_up - sum_down)
k = int(input())
if(distance <= k):
    print('YES')
else:
    print('NO')
print(distance)
