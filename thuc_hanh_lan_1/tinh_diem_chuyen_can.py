
class student:
    def __init__(self, msv, ht, lop, diemCC):
        self.msv = msv
        self.ht = ht
        self.lop = lop
        self.diemCC = diemCC
        self.ghi_chu = ''

    def output(self):
        print(self.msv, self.ht, self.lop, self.diemCC, self.ghi_chu, sep=' ')


t = int(input())
n = m = t
lsv = []
while(n > 0):
    n -= 1
    sv = student(input(), input(), input(), 0)
    lsv.append(sv)
while( m > 0):
    m -= 1
    msv, data = map(str, input().split())

    diemCC = 10
    for val in data:
        if(val == 'v'):
            diemCC -= 2
        elif(val == 'm'):
            diemCC -= 1
        if(diemCC <= 0):
            diemCC = 0
            break

    for sv in lsv:
        if(sv.msv == msv):
            sv.diemCC = diemCC
            if(diemCC == 0):
                sv.ghi_chu = 'KDDK'

for sv in lsv:
    sv.output()

