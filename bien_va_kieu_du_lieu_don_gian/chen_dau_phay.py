s = input()
s = s[::-1]
res = ''
dem = 0
for i in range(len(s)):
    dem += 1
    res += s[i]
    if(dem == 3):
        res += '*'
        dem = 0
res = res.strip('*')
res = res.replace('*', ',')
print(res[::-1])

   
