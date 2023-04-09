t = int(input())

for i in range(t):
    n = int(input())
    left, right, s, cnt = 1, 1, 0, 0
    while left <= n and right <= n:
        if s < n:
            s += right
            right += 1
        elif s > n:
            s -= left
            left += 1
        else:
            cnt += 1
            s -= left
            left += 1
    print(cnt)