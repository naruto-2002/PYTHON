def check(nub):
    l = len(nub)
    numbers = []
    for val in nub:
        if(numbers.count(val) <= 0):
            numbers.append(val)
    if(len(numbers) != 2):
        return False
    for i in range(l - 2):
        if(nub[i] != nub[i + 2]):
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
