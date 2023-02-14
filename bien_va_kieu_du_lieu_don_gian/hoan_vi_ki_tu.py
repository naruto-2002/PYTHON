import itertools

s = input()
res = itertools.permutations(s, len(s))
for ans in res:
    print(''.join(ans))