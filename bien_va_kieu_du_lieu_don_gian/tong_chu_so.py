# import re
# nub = input()
# arr = re.findall(r'\d', nub)
# arr = list(map(int, arr))
# if(nub[0] == '-'):
#     arr[0] *= -1
# dem = 0
# while(len(arr) != 1):
#     dem += 1
#     total = sum(arr)
#     nub = str(total)
#     arr = re.findall(r'\d', nub)
#     arr = list(map(int, arr))
#     if(nub[0] == '-'):
#         arr[0] *= -1
# print(dem)


def trans(s):
    n = 0
    for i in s:
        n += ord(i) - ord('0')
    return str(n)

s = input()
dem = 0
while(len(s) > 1):
    s = trans(s)
    dem += 1
print(dem)
