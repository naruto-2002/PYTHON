class student:
    def __init__(self, name, birth, point1, point2, point3):
        self.name = name
        self.birth = birth
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def totalPoint(self):
        return self.point1 + self.point2 + self.point3
    
    def output(self):
        print(self.name, self.birth, format(self.totalPoint(), '.1f'), sep=' ')

sv = student(input(), input(), float(input()), float(input()), float(input()))
sv.output()
