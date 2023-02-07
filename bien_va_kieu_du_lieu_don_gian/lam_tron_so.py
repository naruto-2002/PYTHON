t = int(input())
while(t > 0):
    t -= 1
    m = int(input())
    n = 10
    while(m/n >= 1):
        m = round(m/n + 0.0001)*n
        n *= 10
    print(m)