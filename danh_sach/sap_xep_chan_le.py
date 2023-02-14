a = []
n = int(input())
while(True):
    b = [int(val) for val in input().split()]
    a += b
    if(len(a) == n):
        break
evenPos = []
oddPos = []
evens = []
odds = []

for i in range(len(a)):
    if a[i]%2 == 0:
        evenPos.append(i)
        evens.append(a[i])
    else:
        oddPos.append(i)
        odds.append(a[i])

evens = sorted(evens)
odds = sorted(odds)[::-1]

for i in range(len(evenPos)):
    a[evenPos[i]] = evens[i]

for i in range(len(oddPos)):
    a[oddPos[i]] = odds[i]

for val in a:
    print(val, end=' ')


