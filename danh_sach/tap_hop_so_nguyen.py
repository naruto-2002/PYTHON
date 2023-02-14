m, n = map(int, input().split())
a = [int(val) for val in input().split()]
b = [int(val) for val in input().split()]

giao = list(set(a)&set(b))
hieu_AB = list(set(a)-set(b))
hieu_BA = list(set(b)-set(a))

giao.sort()
hieu_AB.sort()
hieu_BA.sort()

giao = ' '.join(list(map(str, giao)))
hieu_AB = ' '.join(list(map(str, hieu_AB)))
hieu_BA = ' '.join(list(map(str, hieu_BA)))

print(giao, hieu_AB, hieu_BA, sep='\n')