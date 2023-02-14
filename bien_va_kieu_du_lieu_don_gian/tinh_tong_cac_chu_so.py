import re
t = int(input())
while(t > 0):
    s = input()
    chars = re.findall(r'[a-zA-Z]', s)
    chars = sorted(chars)
    numbers = re.findall(r'\d', s)
    numbers = list(map(int, numbers))
    print(''.join(chars),sum(numbers), sep = '')

    t-= 1