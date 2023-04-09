def count_pivots(arr):
    n = len(arr)
    max_left = [0] * n
    min_right = [0] * n
    max_left[0] = arr[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], arr[i])
    min_right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        min_right[i] = min(min_right[i+1], arr[i])
    count = 0
    for i in range(n):
        if i == 0 and arr[i] < min_right[i+1]:
            count += 1
        elif i == n-1 and arr[i] > max_left[i-1]:
            count += 1
        elif arr[i] > max_left[i-1] and arr[i] < min_right[i+1]:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if count_pivots(arr) == 0:
        print(1)
    else:
        print(count_pivots(arr))
    
