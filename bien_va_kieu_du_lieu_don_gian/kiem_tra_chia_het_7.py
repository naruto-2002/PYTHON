def slove(n, dem):
    a = int(n)
    b = int(n[::-1])
    c = a + b
    if(c%7 == 0):
        print(c)
        return
    if(dem > 1000):
        print(-1)
        return
    slove(str(c), dem+1)

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if(int(n)%7 == 0):
        print(n)
    else:
        dem = 0
        slove(n, dem)