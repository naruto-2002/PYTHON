nubs = [8,7,6,5,4,3,2,1]
str = 'SACKGAUL'
key = [[1, 4], [2, 8], [3, 1], [4, 5], [5, 7], [6, 2], [7, 6], [8, 3]]

dir = {}

cnt = 0
for i in range(8, 0, -1):
    dir[i] = str[cnt]
    cnt += 1

for val in key:
    dir[val[0]] = str[8 - val[1]]

print(dir)
