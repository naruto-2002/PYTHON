def check(n):
    sum = 0
    for val in n:
        sum += int(val)
    s = str(sum)
    if(s == s[::-1] and len(s) > 1):
        return True
    return False

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if(check(n)):
        print('YES')
    else:
        print('NO')