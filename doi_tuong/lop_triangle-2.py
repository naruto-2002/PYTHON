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
        if(c1+c2<=c3 or c1+c3<=c2 or c2+c3<=c1):
            return False
        return True
    
    def output(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        if(self.check()):
            #  d = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            # print('{:.2f}'.format(d))
            dt = math.sqrt((c1+c2+c3)*(c1+c2-c3)*(c1-c2+c3)*(-c1+c2+c3))/4
            print('{:.2f}'.format(dt))
        else:
            print('INVALID')

a = []
t1 = int(input())
for t in range(t1):
    x = [float(val) for val in input().split()]
    a += x 

i = 0
for t in range(t1):
    tam_giac = Triangle(a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5])
    tam_giac.output()
    i += 6



