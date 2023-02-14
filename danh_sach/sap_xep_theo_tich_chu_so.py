def totalNumb(n):
    multiple = 1
    for val in n:
        multiple *= int(val)
    return multiple

t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(val) for val in input().split()]
    a = sorted(a)
    a = sorted(a, key = lambda x: totalNumb(str(x)))
    b = list(map(str, a))
    res = ' '.join(b)
    print(res)


    