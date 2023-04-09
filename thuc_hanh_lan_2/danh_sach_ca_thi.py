import functools
cnt = 1
class CaThi:
    def __init__(self, ngayT, gioT, phongT):
        global cnt
        self.maCT = 'C' + format(cnt, '03d')
        cnt += 1
        self.ngayT = ngayT
        self.gioT = gioT
        self.phongT = phongT

    def output(self):
        print(self.maCT, self.ngayT, self.gioT, self.phongT, sep=' ')
def slove(s1, s2):
    if(s1 > s2): return 1
    return -1

def cmp(a, b):
    date1 = ''.join(a.ngayT.split('/')[::-1])
    time1 = a.gioT
    date2 = ''.join(b.ngayT.split('/')[::-1])
    time2 = b.gioT
    if(date1 == date2):
        if(time1 == time2):
            return slove(a.maCT, b.maCT)
        else:
            return slove(time1, time2)
    return slove(date1, date2)


# f1 = open('D:/Documents/nam_3_ki_2/lap_trinh_phython/thuc_hanh_lan_2/test.txt')
f1 = open('CATHI.in')
input = []
for val in f1:
    input.append(val.rstrip())
dem = 0
t = int(input[dem])
dem += 1
lct = []
while(t > 0):
    t -= 1
    ngayT = input[dem]
    dem += 1
    gioT = input[dem]
    dem += 1
    phongT = input[dem]
    dem += 1
    ct = CaThi(ngayT, gioT, phongT)
    lct.append(ct)
lct.sort(key = functools.cmp_to_key(cmp))
for ct in lct:
    ct.output()



