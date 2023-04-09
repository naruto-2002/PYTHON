import itertools
arr = [int(val) for val in input().split()]
l = len(arr)
permus = itertools.permutations(arr, l)
for permu in permus:
    print(permu)