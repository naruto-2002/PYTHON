n = int(input())
list = []
for index in range(n):
    s = input()
    if list.count(s) == 0:
        list.append(s)
print(len(list))




