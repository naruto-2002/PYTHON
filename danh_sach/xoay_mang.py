t = int(input())
while(t > 0):
    t -= 1
    n, m = map(int, input().split())
    arr = [int(val) for val in input().split()]
    while(m > 0):
        m -= 1
        arr.append(arr.pop(0))
    for val in arr:
        print(val, end=' ')
    print()
        
