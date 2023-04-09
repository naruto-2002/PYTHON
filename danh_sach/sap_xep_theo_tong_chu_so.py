def totalNumb(n):
    sum = 0
    for val in n:
        sum += int(val)
    return sum

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


    