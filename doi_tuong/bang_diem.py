dem = 1
class Student:
    
    def __init__(self, name, points):
        global dem
        self.msv = 'HS' + format(dem, '02d')
        dem += 1
        
        self.name = name
        self.tb = 2*(points[0]+points[1])
        for i in range(2, 10):
            self.tb += points[i]
        self.tb /= 12
        
    def rank(self):
        tb = self.tb
        if(tb >= 9):
            return 'XUAT SAC'
        elif(tb >= 8):
            return 'GIOI'
        elif(tb >= 7):
            return 'KHA'
        elif(tb >= 5):
            return 'TB'
        return 'YEU'

    def output(self):
        tb = self.tb
        print(self.msv, self.name, round((tb*100+1)/100, 1), self.rank())

lsv = []
for t in range(int(input())):
    s = input()
    x = [float(val) for val in input().split()]
    lsv.append(Student(s, x))

lsv.sort(key=lambda x: (-x.tb, x.msv))

for sv in lsv:
    sv.output()

    
