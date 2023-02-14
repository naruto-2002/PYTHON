
arr = [0,1,1]
def fibonacci(n):
    if n==93: return
    arr.append(arr[n-1]+arr[n-2])
    fibonacci(n+1)

fibonacci(3)
t = int(input())
while(t > 0):
    t -= 1
    a, b = map(int, input().split())
    res = arr[a:b+1]
    for val in res:
        print(val, end=' ')
    print()    
    
    



