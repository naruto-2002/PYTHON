import itertools

n, k = map(int, input().split())

arr = [int(val) for val in input().split()]

arr = set(arr)

arr = sorted(arr)

res = itertools.combinations(list(arr), k)
for ans in res:
    for val in ans:
        print(val, end=' ')
    print()
