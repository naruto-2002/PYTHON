
n = int(input())
a = [float(val) for val in input().split()]
ma = max(a)
mi = min(a)
b = [val for val in a if val != ma and val != mi]
medium = sum(b)/len(b)
print(format(medium, '.2f'))
