import math

def max_power_of_p(N, p):
    x = 0
    while N > 0:
        N //= p
        x += N
    return x

# Đọc số lượng test case
T = int(input())

# Xử lý từng test case
for i in range(T):
    N, p = map(int, input().split())
    x = max_power_of_p(N, p)
    print(x)
