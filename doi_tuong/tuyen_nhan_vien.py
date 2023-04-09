import re
dem = 1
class Staff:

    mnv = 'TS0'
    name = ''
    tb = 0
    rank = ''

    def __init__(self, name, lth, th):
        global dem
        self.mnv += str(dem)
        dem += 1

        self.name = name
        tb = (lth+th)/2
        self.tb = tb
        
        rank = ''
        if(tb < 5):
            rank = 'TRUOT'
        elif(tb < 8):
            rank = 'CAN NHAC'
        elif(tb <= 9.5):
            rank = 'DAT'
        else:
            rank = 'XUAT SAC'
        self.rank = rank

    def output(self):
        print(self.mnv, self.name, format(self.tb, '.2f'), self.rank)

lnv = []
for t in range(int(input())):
    s = input()
    lth = float(input())
    if lth > 10:
        lth /= 10
    th = float(input())
    if th > 10:
        th /= 10
    lnv.append(Staff(s, lth, th))

lnv.sort(key=lambda x: -x.tb)

for nv in lnv:
    nv.output()

        


