number = input()

seven = 0
four = 0
for val in number:
    if(val == '7'):
        seven += 1
    if(val == '4'):
        four += 1
total = seven + four
if(total == 4 or total == 7): print('YES')
else: print('NO')
