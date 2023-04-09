t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(val) for val in input().split()]
    a = list(set(sorted(a)))
    l = len(a)
    res = (a[l-1]-a[0]+1)-l
    print(res)