import re
t = int(input())
while(t > 0):
    t -= 1
    s = input()
    chars = re.findall(r'[A-Z]+', s)
    numbers = re.findall(r'\d+', s)
    res = ''
    l = len(chars)
    for i in range(l):
        tt = int(numbers[i])
        while(tt > 0):
            tt -= 1
            res += chars[i]
    print(res)
