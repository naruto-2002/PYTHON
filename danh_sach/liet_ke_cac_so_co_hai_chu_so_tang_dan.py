a = input()
l = len(a)
if(l%2 != 0):
    l -= 1
b = []
for i in range(0, l, 2):
    number = a[i] + a[i+1]
    if(number not in b):
        b.append(number)
b.sort()
b = ' '.join(b)
print(b)