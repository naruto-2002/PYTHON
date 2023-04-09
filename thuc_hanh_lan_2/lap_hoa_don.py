class HoaDon:
    def __init__(self, maMH, tenMH, soLM, donG, tienCK):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soLM = soLM
        self.donG = donG
        self.tienCk = tienCK
        self.total = donG*soLM-tienCK

    def output(self):
        print(self.maMH, self.tenMH, self.soLM, self.donG, self.tienCk, self.total, sep=' ')

t = int(input())
lhd = []
while(t > 0):
    t -= 1
    hd = HoaDon(input(), input(), int(input()), int(input()), int(input()))
    lhd.append(hd)
lhd.sort(key = lambda x: x.total, reverse=True)
for hd in lhd:
    hd.output()