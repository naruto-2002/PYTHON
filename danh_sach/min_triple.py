t = int(input())
while(t > 0): 
    t -= 1
    n = int(input())
    arr = [int(val) for val in input().split()]
    min1 = min(arr)
    arr.remove(min1)
    min2 = min(arr)
    arr.remove(min2)
    min3 = min(arr)
    print(min1 + min2 + min3)

