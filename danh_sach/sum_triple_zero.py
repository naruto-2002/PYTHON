
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    arr = sorted([int(val) for val in input().split()])
    res = 0
    for i in range(0, len(arr) - 2):
        l = i + 1
        r = len(arr) - 1
        x = arr[i]
        while(l < r):
            if(x + arr[l] + arr[r] == 0):
                res += 1
                l += 1
            elif(x + arr[l] + arr[r] < 0):
                l += 1
            else:
                r -= 1
    print(res)

