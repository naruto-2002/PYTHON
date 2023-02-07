import re
s = input()
l = 0
u = 0
for val in s:
    if val.islower(): 
        l += 1
    else: 
        u += 1
if(l >= u): 
    print(s.lower())
else: 
    print(s.upper())