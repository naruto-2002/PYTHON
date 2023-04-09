n = 6
arr = [1, 2, 3, 4, 5, 6]
arr.sort()
arr1 = arr[::-1]
a = 0
b = 0
for i in range(len(arr)):
    if(i%2 != 0):
        print(arr[a], end=' ')
        a += 1
    else:
        print(arr1[b], end = ' ')
        b += 1