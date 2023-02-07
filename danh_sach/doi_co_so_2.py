import re
import math

def sloveBinary(a, binarys):
    res = ''
    for value in binarys:
        ans = 0
        for i in range(a):
            ans += value[i]*(2**(a - i - 1))
        swicher = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        res += swicher.get(ans, str(ans))
    return res

t = int(input())
while(t > 0):
    t -= 1

    n = int(input())
    a = int(math.log(n, 2))

    s = input()
    b = a - (len(s))%a
   
    while(b > 0 and b < a):
        b -= 1
        s = '0' + s

    binary = re.findall(r'\d', s)
    for i in range(len(binary)):
        binary[i] = int(binary[i])
    
    tmp = 0
    binarys = []
    for i in range(a, len(binary) + 1, a):
        binarys.append(binary[tmp:i])
        tmp = i
    print(sloveBinary(a, binarys))




    
    