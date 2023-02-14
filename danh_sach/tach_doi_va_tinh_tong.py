def totalNumber(nub):
    l = len(nub)
    l1 = l//2
    res = ''
    s1 = ''
    s2 = ''
    if(l%2 == 0):
        for i in range(0, l1): s1 += nub[i]
        for i in range(l1, l): s2 += nub[i]
        res = str(int(s1) + int(s2))
    else:
        for i in range(0, l1): s1 += nub[i]
        for i in range(l1, l): s2 += nub[i]
        res = str(int(s1) + int(s2))
    return res

s = input()
while(len(s) > 1):
    s = totalNumber(s)
    print(s)