import re
s = input()
numbers = re.findall(r'\d', s)
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
if(a + b == c): print('YES')
else: print('NO')