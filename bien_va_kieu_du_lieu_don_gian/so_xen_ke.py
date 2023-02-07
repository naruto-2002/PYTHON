def check(n):
    l = len(n)
    if(l%2 == 0 or n[0] == n[1]):
        return False
    for i in range(0, l - 1, 2):
        if(n[i] != n[i+2]):
            return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if(check(n)):
        print('YES')
    else:
        print('NO')
