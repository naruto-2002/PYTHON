def check(nub):
    l = len(nub)
    if(l < 3):
        return False
    a = -1
    b = -2
    for i in range(l-1):
        if(int(nub[i]) == int(nub[i+1])):
            return False
        if(int(nub[i]) > int(nub[i+1])):
            a = i
            break
    for i in range(l-1, 0, -1):
        if(int(nub[i]) == int(nub[i-1])):
            return False
        if(int(nub[i]) > int(nub[i-1])):
            b = i
            break
    if(a != b):
        return False
    return True
t = int(input())
while(t > 0):
    t -= 1
    nub = input()
    if(check(nub)):
        print('YES')
    else:
        print('NO')