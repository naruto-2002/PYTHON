n = 5
arr = ['abcdfdfdf', 'abcdfdfdf', 'fkdfjabcd', 'turitriabcd', 'abcd']
arr.sort(key=lambda x: len(x))
temp = arr[0]
res = ''
for ss in temp:
    res += ss
    ok = 1
    for i in range(1, len(arr)):
        if(res not in arr[i]):
            ok = 0
            break
    if(ok == 0):
        break

print(len(res))
    
