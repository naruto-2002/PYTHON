import math
import re
def check1(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
def check2(n):
    s = str(n)
    numbers = re.findall(r'\d', s)
    for value in numbers:
        if check1(int(value)) == False:
            return False
    return True
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    if(check1(n) == True and check2(n) == True):
        print('Yes')
    else:
        print('No')