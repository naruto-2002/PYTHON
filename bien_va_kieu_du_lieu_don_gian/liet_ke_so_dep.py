
def check1(n):
    if(len(n) == 1):
        return False
    if(int(n) != int(n[::-1])):
        return False
    return True

arr = [0,2,4,6,8]

def check2(n):
    for c in n:
        if(arr.count(int(c)) <= 0):
            return False
    if(len(n)%2 != 0):
        return False
    return True

t = int(input())
for tt in range(t):
    n = int(input())
    for i in range(n):
        if(check1(str(i)) and check2(str(i))):
            print(i, end=' ')
    print()
