class Rectangle:

    def __init__(self,length, width, color):
        self.length = length
        self.width = width
        self.color = color[:1].upper() + color[1:].lower()

    def check(self):
        if self.length <= 0 or self.width <= 0:
            return 0
        return 1

    def output(self):
        if(self.check() == 1):
            print((self.length + self.width)*2, self.length*self.width, self.color, sep = ' ')
        else:
            print('INVALID')
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
r.output()
    