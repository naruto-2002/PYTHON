import itertools

n, k = map(int, input().split())

s = list(set(input().split(' ')))

res = itertools.combinations(s, k)

names = []

for val in res:
    names.append(' '.join(sorted(list(val))))

names.sort()

for val in names:
    print(val)