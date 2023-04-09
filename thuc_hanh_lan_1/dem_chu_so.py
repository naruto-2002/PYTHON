nub = [0] * 11
def Load(n, arr):
    if n == 0:
        return
    s = str(n)
    l = len(s)
    for i in range(10):
        arr[i] += nub[l - 1]
    for i in range(l - 1):
        arr[0] -= pow(10, i)
    for i in range(l):
        j = 0
        p = 0
        if i == 0:
            p = 1
            j = 1
            arr[0] += nub[l - 1 - i] * (ord(s[i]) - 48 - p)
        sum = nub[l - 1 - i]  * (ord(s[i]) - 48 - p)
        while j < ord(s[i]) - 48:
            arr[j] += pow(10, l - i - 1) + sum
            j += 1
		
        arr[j] += n % (pow(10, l - i - 1)) + sum + 1
        for k in range (j + 1, 10):
            arr[k] += sum
            
t = int(input())
for i in range(10):
    nub[i] = int(i * pow(10, i - 1))
    
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    arr1 = [0] * 20
    arr2 = [0] * 20
    Load(n - 1, arr1)
    Load(m, arr2)
    for i in range (10):
        print(arr2[i] - arr1[i], end = ' ')
    print()