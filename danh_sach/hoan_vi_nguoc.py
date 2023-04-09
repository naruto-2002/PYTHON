import itertools

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    m = ''
    for i in range(1, n+1):
        m += str(i)
    hoan_vi = itertools.permutations(m, n)
    hoan_vi = list(hoan_vi)
    hoan_vi = hoan_vi[::-1]
    print(len(hoan_vi))
    for val in hoan_vi:
        print(''.join(val), end=' ')
    print()
    