def residue(number):
    l = len(number)
    sum = 0
    for i in range(l):
        sum += int(number[i])
        if(i == l - 1):
            sum = (sum%3)
        else:
            sum = (sum%3)*10
    return sum
    


t = int(input())
while(t > 0):
    t -= 1
    number = input()
    if(residue(number) == 0):
        print('YES')
    else:
        print('NO')