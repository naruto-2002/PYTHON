dem = 1
class HoaDon:

    def __init__(self, name, old_nub, new_nub):
        global dem
        self.mkh = 'KH' + format(dem, '02d')
        dem += 1
        self.name = name
        total = new_nub - old_nub
        if(total <= 50):
            total = total*100
            total += total*0.02
        elif(total <= 100):
            total = 50*100 + (total-50)*150
            total += total*0.03
        else:
            a = total - 100
            b = (total - a) - 50
            total = 50*100 + b*150 + a*200
            total += total*0.05
        self.total = total
        

    def output(self):
        print(self.mkh, self.name, round(self.total))
        

lhd = []
for t in range(int(input())):
    s = input()
    a = int(input())
    b = int(input())
    lhd.append(HoaDon(s, a, b))

lhd.sort(key=lambda x: -x.total)

for hd in lhd:
    hd.output()

