n = int(input())
a, b = map(int, input().split())
arr = [int(val) for val in input().split()]
# res = arr[0:a] + arr[a:b][::-1] + arr[b:]
arr[a-1:b] = arr[a-1:b][::-1]
print(arr)