import math

class fraction:

    def  __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def shorten(self):
        ucln = math.gcd(self.tu, self.mau)
        a = self.tu
        b = self.mau
        self.tu = int(a/ucln)
        self.mau = int(b/ucln)

    def totalFraction(self, ps):
        a = self.tu
        b = self.mau
        c = ps.tu
        d = ps.mau
        self.tu = a*d + c*b
        self.mau = b*d
        return self
    
    def output(self):
        print(self.tu, self.mau, sep = '/')

a, b, c, d = map(int, input().split())
ps_1 = fraction(a, b)
ps_2 = fraction(c, d)
res = ps_1.totalFraction(ps_2)
res.shorten()
res.output()




