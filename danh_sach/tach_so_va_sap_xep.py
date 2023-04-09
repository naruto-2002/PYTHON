import re
t = int(input())
a = []
while(t > 0):
    t -= 1
    s = input()
    x = re.findall(r'\d+', s)
    a += x
a = [int(val) for val in a]
a.sort()
for val in a:
    print(val)
