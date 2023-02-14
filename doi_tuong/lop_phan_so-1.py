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
    
    def output(self):
        print(self.tu, self.mau, sep = '/')

a, b = map(int, input().split())
ps = fraction(a, b)
ps.shorten()
ps.output()


