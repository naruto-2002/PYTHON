t = int(input())
while(t > 0):
    t -= 1
    m, n = map(int, input().split())
    a = [int(val) for val in input().split()]
    ma = max(a)
    negative = []
    plus = []
    for val in a:
        if(val >= 0):
            plus.append(val)
        else:
            negative.append(val)
    
    arr = negative + plus

    id = 0
    for i in range(len(arr)):
        if(arr[i] == ma):
            print(n, arr[i], end=' ')
            id = i
            break
        else:
            print(arr[i], end=' ')
    for i in range(id+1, len(arr)):
        print(arr[i], end=' ')
    print()

    


