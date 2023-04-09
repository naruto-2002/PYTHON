s = input()
l = len(s)
if(l%2 != 0):
    l -= 1
a = []
for i in range(0, l, 2):
    number = s[i] + s[i+1]
    if(number not in a):
        a.append(number)
a = ' '.join(list(map(str, a)))
print(a)