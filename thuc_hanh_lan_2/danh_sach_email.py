f1 = open('CONTACT.in')
res = []
for line in f1:
    line = line.rstrip().lower()
    if(line not in res):
        res.append(line)
res.sort()
for val in res:
    print(val)