

n = int(input())
binary = [int(val) for val in input().split()]
res = 0
for i in range(0, len(binary) - 1):
    if(binary[i] != binary[i + 1]):
        res += 1
print(res)

    