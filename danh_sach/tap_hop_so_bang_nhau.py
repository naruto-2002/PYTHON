m, n = map(int, input().split())
a = [int(val) for val in input().split()]
b = [int(val) for val in input().split()]

a = list(set(a))
b = list(set(b))

a = list(map(str, a))
b = list(map(str, b))

a = ''.join(a)
b = ''.join(b)

if(a == b):
    print('YES')
else:
    print('NO')