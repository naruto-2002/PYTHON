a = [0]*1000001
a[0] = a[1] = 1
for i in range(2, 1001):
    if(a[i] == 0):
        for j in range(i*i, 1000001, i):
            a[j] = 1


t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    res = '1'
    for i in range(2, n + 1):
        if(a[i] == 0):
            count = 0
            m = n
            while(m%i == 0):
                count += 1
                m /= i
            if(count > 0):
                res += ' * ' + str(i) + '^' + str(count)
    print(res)

