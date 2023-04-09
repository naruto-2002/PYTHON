arr1 = [int(val) for val in input().split()]
arr2 = [int(val) for val in input().split()]

hop = list(set(arr1) | set(arr2))
giao = list(set(arr1) & set(arr2))

print('hop cua hai mang: ',hop)
print('giao cua hai mang: ',giao)




