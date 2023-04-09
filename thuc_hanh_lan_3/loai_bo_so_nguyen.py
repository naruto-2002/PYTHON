import re
pth = "D:/Documents/nam_3_ki_2/lap_trinh_phython/thuc_hanh_lan_3/data.txt"
f1 = open('DATA.in')
arr = []
for line in f1:
    line = line.replace('\n', '')
    while(line.find('  ') == True):
        line = line.replace('  ', ' ')
    arr += line.split(' ')

res = []
regex1 = '[a-zA-Z]+'
regex2 = '[0-9]{10}'
for val in arr:
    if(re.match(regex1, val) or re.match(regex2, val)):
        res.append(val)
res.sort()
print(' '.join(res))

