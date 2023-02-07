import re
t = int(input())
while(t > 0):
    t -= 1
    nub = input()
    flag = re.fullmatch(r'[47]+',nub)
    if(flag): print('YES')
    else: print('NO')