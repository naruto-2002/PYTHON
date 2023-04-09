

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    sum = 0
    multiply = 1
    l = len(n)
    ok = 0
    for i in range(l):
        if(i%2 == 0):
            if(n[i] != '0'):
                ok = 1
                multiply *= int(n[i])
        else:
            sum += int(n[i])
    if(ok == 0):
        multiply = 0
    print(multiply, sum)