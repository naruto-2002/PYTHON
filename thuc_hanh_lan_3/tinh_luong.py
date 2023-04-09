

class Department:
    def __init__(self, maPB, tenPB):
        self.maPB = maPB
        self.tenPB = tenPB

class Staff:
    def __init__(self, maNV, tenNV, tenPB, Lcb, Sngc):
        self.maNV = maNV
        self.tenNV = tenNV
        self.tenPB = tenPB
        self.Lcb = Lcb
        self.Sngc = Sngc

        a = maNV[0:1]
        b = int(maNV[1:3])

        self.Lthang = HS(a, b)*Lcb*Sngc*1000

    def output(self):
        print(self.maNV, self.tenNV, self.tenPB, self.Lthang, sep=' ')


def HS(a, b):
    if(a == 'A'):
        if(b >= 1 and b <= 3):
            return 10
        elif(b >= 4 and b <= 8):
            return 12
        elif(b >= 9 and b <= 15):
            return 14
        elif(b >= 16):
            return 20
    elif(a == 'B'):
        if(b >= 1 and b <= 3):
            return 10
        elif(b >= 4 and b <= 8):
            return 11
        elif(b >= 9 and b <= 15):
            return 13
        elif(b >= 16):
            return 16
    elif(a == 'C'):
        if(b >= 1 and b <= 3):
            return 9
        elif(b >= 4 and b <= 8):
            return 10
        elif(b >= 9 and b <= 15):
            return 12
        elif(b >= 16):
            return 14
    elif(a == 'D'):
        if(b >= 1 and b <= 3):
            return 8
        elif(b >= 4 and b <= 8):
            return 9
        elif(b >= 9 and b <= 15):
            return 11
        elif(b >= 16):
            return 13

t1 = int(input())
lpb = []
while(t1 > 0):
    t1 -= 1
    s = input()
    ss = s.split(' ')
    a = ss[0]
    b = ''
    for i in range(1, len(ss)):
        b += ss[i] + ' '
    pb = Department(a, b.strip())
    lpb.append(pb)

t2 = int(input())
lnv = []
while(t2 > 0):
    t2 -= 1
    tmp = ''
    maNV = input()
    tenNV = input()
    tenPB = ''
    maPB = maNV[len(maNV)-2:]
    for pb in lpb:
        if(pb.maPB == maPB):
            tenPB += pb.tenPB
            break
    Lcb = int(input())
    Sngc = int(input())
    nv = Staff(maNV, tenNV, tenPB, Lcb, Sngc)
    lnv.append(nv)

for nv in lnv:
    nv.output()
