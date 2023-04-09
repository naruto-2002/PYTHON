
n = int(input())
a = [int(val) for val in input().split()]
a.sort(reverse=True)
multiply = [a[0]*a[1], a[0]*a[1]*a[2], a[-1]*a[-2], a[-1]*a[-2]*a[-3], a[0]*a[-1]*a[-2]]
ma = max(multiply)
print(ma)