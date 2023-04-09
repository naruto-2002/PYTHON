dc1 = {'a': 1, 'b': 1, 'e': 3,'c': 3, 'd': 3, 'h': 4}
dc2={}
a = []
l = len(dc1)
for k,v in dc1.items():
    if(v not in a):
        a.append(v)
        dc2[k] = v
print(dc2)

