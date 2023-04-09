def check(n):
    for val in n:
        if(val != '0' and val != '1' and val != '2'):
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
    