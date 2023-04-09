def check(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if(l1 != l2):
        return False
    for char in s1:
        if(s1.count(char) != s2.count(char)):
            return False
    return True

t = int(input())
for i in range(1, t + 1):
    s1 = input()
    s2 = input()
    if(check(s1, s2)):
        print('Test ' + str(i) + ': ' + 'YES')
    else:
        print('Test ' + str(i) + ': ' + 'NO')
