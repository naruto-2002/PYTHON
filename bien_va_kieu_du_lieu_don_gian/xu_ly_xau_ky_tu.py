s1 = input().lower()
s2 = input().lower()

ss1 = s1.split(' ')
ss2 = s2.split(' ')

hop = list(set(ss1)|set(ss2))
hop.sort()

giao = list(set(ss1)&set(ss2))
giao.sort()

print(' '.join(hop))
print(' '.join(giao))