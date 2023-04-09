
t = int(input())
while(t > 0):
    t -= 1
    number = input()
    number = number.replace('0', '1')
    sum_multiple = 1
    for val in number:
        sum_multiple *= int(val)
    print(sum_multiple)