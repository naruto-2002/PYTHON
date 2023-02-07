
def check(nub):
    sum = 0
    for val in nub:
        sum += int(val)
    if(sum%10 != 0):
        return False
    for i in range(len(nub) - 1):
        if(abs(int(nub[i]) - int(nub[i + 1])) != 2):
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