t = int(input())
while(t > 0):
    t -= 1
    s = input()
    l = len(s)
    ss = s[l-2:l]
    if(ss == '86'):
        print('YES')
    else:
        print('NO')
