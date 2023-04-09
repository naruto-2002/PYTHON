def generate_partitions(n):
    def backtrack(start, sum_, path):
        if sum_ == n:
            res.append(path)
            return
        for i in range(start, n - sum_ + 1):
            backtrack(i, sum_ + i, path + [i])

    res = []
    backtrack(1, 0, [])
    return res

t = int(input())
for i in range(t):
    n = int(input())
    partitions = generate_partitions(n)
    for val in partitions:
        val.sort(key=lambda x: x, reverse=True)
    partitions.sort()
    print(len(partitions))
    res = []
    for partition in partitions:
        res.append('(' + " ".join(str(x) for x in partition) + ')')
    for i in range(len(res)-1, -1, -1):
        print(res[i], end=" ")
    print()
