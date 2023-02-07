P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def slove(k, s):
    res = ''
    for i in s:
        x = 0
        for j in P:
            if(i == j):
                break
            x += 1
        x = (x + k)%28
        res = P[x] + res
    return res

while(True):
    Input = input()
    arr = Input.split(' ')
    k = arr[0]
    if(len(arr) == 2):
        s = arr[1]
        print(slove(int(k), s))

    if(k == '0'):
        break
