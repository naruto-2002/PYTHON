import functools

dem = 1
class Student:

    def __init__(self, ten, diem, dtoc, kv):
        global dem
        self.ma = 'TS' + format(dem, '02d')
        dem += 1
        self.ten = handleTen(ten)
        self.dtoc = (dtoc.strip()).lower()
        self.kv = kv
        self.diem = diem + handleDiemUT(kv, self.dtoc)
        TT = 'Truot'
        if(self.diem >= 20.5): TT = 'Do'
        self.state = TT

    def output(self):
        print(self.ma, self.ten, format(self.diem, '.1f'), self.state, sep=' ')


def handleTen(s):
        s = s.lower()
        Str = s.split(' ')
        res = ''
        for val in Str:
            if(val != ''):
                res += val[0:1].upper() + val[1:] + ' '
        return res.strip()

def handleDiemUT(a, s):
     diem = 0
     if(a == 1): diem += 1.5
     elif(a == 2): diem += 1
     if(s != 'kinh'): diem += 1.5
     return diem

def slove(s1, s2):
    if(s1 > s2): return 1
    return -1

def cmp(a, b):
     if(a.diem == b.diem):
          return slove(a.ma, b.ma)
     return b.diem - a.diem

t = int(input())
lsv = []
while(t > 0):
    t -= 1
    sv = Student(input(), float(input()), input(), float(input()))
    lsv.append(sv)

lsv.sort(key = functools.cmp_to_key(cmp))

for sv in lsv:
    sv.output()
