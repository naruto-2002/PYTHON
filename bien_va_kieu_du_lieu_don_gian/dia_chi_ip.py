
def check(a):
    if(len(a) < 4):
        return 0
    for val in a:
        if(val.isdigit()):
            if int(val) < 0 or int(val) > 255:
                return 0
        else:
            return 0
    return 1

t = int(input())
while(t > 0):
    t -= 1
    ip = input()
    a = ip.split('.')
    if(check(a) == 1):
        print('YES')
    else:
        print('NO')