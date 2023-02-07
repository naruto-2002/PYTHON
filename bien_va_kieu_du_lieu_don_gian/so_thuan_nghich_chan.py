def check(n):
    l = len(n)
    if(l%2 != 0):
        return False
    if(n != n[::-1]):
        return False
    for i in range(l):
        if(int(n[i])%2 != 0):
            return False
    return True
    
t = int(input())
while(t > 0):
    t -= 1
    n = input()
    for i in range(2, int(n), 2):
        if(check(str(i))):
            print(i, end=' ')
    print()
