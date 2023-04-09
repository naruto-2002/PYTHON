import math
from decimal import Decimal

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(slef, p):
        x0 = slef.x - p.x
        y0 = slef.y - p.y
        res = math.sqrt(x0**2 + y0**2)
        return format(res, '.4f')
        
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1