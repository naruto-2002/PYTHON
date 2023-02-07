import re
t = int(input())
while(t > 0):
    t -= 1
    s = input()
    s += '@'
    res = ''
    dem = 1
    l = len(s)
    for i in range(l - 1):
        if(s[i] == s[i + 1]):
            dem += 1
        else:
            res += str(dem) + s[i]
            dem = 1
    print(res)