import math
def bandScore(n):
    if(n < 3): return 0
    elif(n < 5): return 2.5
    elif(n < 7): return 3.0
    elif(n < 10): return 3.5
    elif(n < 13): return 4.0
    elif(n < 16): return 4.5
    elif(n < 20): return 5.0
    elif(n < 23): return 5.5
    elif(n < 27): return 6.0
    elif(n < 30): return 6.5
    elif(n < 33): return 7.0
    elif(n < 35): return 7.5
    elif(n < 37): return 8.0
    elif(n < 39): return 8.5
    elif(n < 41): return 9.0

t = int(input())
while(t > 0):
    t -= 1
    a, b, c, d = map(float, input().split())
    res = bandScore(a) + bandScore(b) + c + d
    res /= 4
    e = res - int(res)
    if(e < 0.25):
        e = 0
    elif(e < 0.75):
        e = 0.5
    else:
        e = 1
    res = int(res) + e
    print(format(res, '.1f'))


