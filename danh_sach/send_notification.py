t = int(input())
while(t > 0):
    t -= 1
    s = input()
    if(len(s) > 100):
        dem = 100
        while(s[dem] != ' ' and s[dem] != 'null'):
            dem -= 1
        print(s[:dem])

    else:
        print(s)
