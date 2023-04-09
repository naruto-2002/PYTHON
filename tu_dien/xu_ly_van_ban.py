import re

s = ''
while True:
    try:
        s += input()
        if(s[len(s)-1] != '.' and s[len(s)-1] != '!' and s[len(s)-1] != '?'):
            s += '.'
    except EOFError:
        break
while '  ' in s:
    s = s.replace('  ', ' ')
s = s.lower()
ss = re.findall(r'[\w\s,:]+', s)
sss = re.findall(r'[.!?]', s)
cnt = 0
for val in ss:
    val = val.strip()
    val = val[0:1].upper() + val[1:] + sss[cnt]
    cnt += 1
    print(val)