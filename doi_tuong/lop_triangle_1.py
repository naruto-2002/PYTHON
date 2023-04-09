import math

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.c1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        self.c2 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
        self.c3 = math.sqrt((x2-x3)**2 + (y2-y3)**2)

    def check(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        if(c1+c2 <= c3 or c1+c3 <= c2 or c2+c3 <= c1):
            return False
        else:
            return True

    def output(self):
        if(self.check()):
            cv = self.c1 + self.c2 + self.c3
            print(round(cv, 3))
        else:
            print('INVALID')

t = int(input())
tt = t
a = []
while(t > 0):
    t -= 1
    x = [float(val) for val in input().split()]
    a += x
i = 0
while(tt > 0):
    tt -= 1
    tam_giac = Triangle(a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5])
    tam_giac.output()
    i += 6

