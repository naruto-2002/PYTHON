
n = int(input())
arr = [int(val) for val in input().split()]
res = 0
for i in range(0, len(arr) - 1):
    for j in range(i+1, len(arr)):
        if(i < j and arr[i] > arr[j]):
            res += 1
print(res)
    
