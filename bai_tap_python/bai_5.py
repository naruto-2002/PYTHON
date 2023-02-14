

a = [1, 2, 3, 4, 5]
b = [2, 3, 4]

stra = strb = ''

for val in a:
    stra += str(val)
for val in b:
    strb += str(val)

if(strb in stra):
    print('yes')
else:
    print('no')




