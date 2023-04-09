def get_char(n, k):
    if n == 1:
        return 'A'
    len_prev = 2 ** (n - 1) - 1
    mid = len_prev + 1
    if k == mid:
        return chr(ord('A') + n - 1)
    elif k < mid:
        return get_char(n - 1, k)
    else:
        return get_char(n - 1, k - mid)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(get_char(n, k))
