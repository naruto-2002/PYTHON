okk = 1
while okk != 0:
    a = [int(val) for val in input().split()]
    dem = 0
    while True:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            okk = 0
            break
        elif a[0] == a[1] and a[1] == a[2] and a[2] == a[3] :
            print(dem)
            break
        dem += 1
        a0 = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - a0)
   
