

number = input()
k = int(input())

numbers = []
l = len(number)
if(l%2 != 0): l -= 2

a = []
b = []
for i in range(0,l,2):
    nub = int(number[i] + number[i+1])
    if(nub not in a):
        a.append(nub)
        numbers.append([nub])
    b.append(nub)

for val in numbers:
    val.extend([b.count(val[0])])

numbers.sort(key=lambda x: x[0])

ok = 0
for val in numbers:
    if val[1] >= k:
        ok = 1
        print(val[0], val[1])
if(ok == 0):
    print('NOT FOUND')