s = input()
l = len(s)
if(l%2 != 0):
    l -= 1
a = []
b = []
for i in range(0, l, 2):
    number = s[i] + s[i+1]
    b.append(number)
    if(number not in a):
        a.append(number)
for val in a:
    print(val, b.count(val))