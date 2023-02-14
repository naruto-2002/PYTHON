def check(nub):
    for val in nub:
        if(val != '6' and val != '8'):
            return False
    if('888' in nub):
        return False
    return True

nub = input()
if(check(nub)):
    print('YES')
else:
    print('NO')