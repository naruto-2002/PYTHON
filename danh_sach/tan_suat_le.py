t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(val) for val in input().split()]
    b = list(set(a))
    for val in b:
        if(a.count(val)%2 != 0):
            print(val)
            break
        