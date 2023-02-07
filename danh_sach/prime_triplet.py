arr = [0]*1000001
arr[0] = arr[1] = 1
for i in range(2, 1000):
    if(arr[i] == 0):
        for j in range(i*i, 1000001, i):
            arr[j] = 1

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    res = 0
    for i in range(6, n):
        if(arr[i] == 0 and arr[i - 6] == 0 and  (arr[i - 2] == 0 or arr[i - 4] == 0)):
            res += 1
    print(res)
