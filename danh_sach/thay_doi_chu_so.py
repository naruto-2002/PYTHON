def total_min(a, b, number1, number2):
    number1 = number1.replace(b, a)
    number2 = number2.replace(b, a)
    return int(number1) + int(number2)

def total_max(a, b, number1, number2):
    number1 = number1.replace(a, b)
    number2 = number2.replace(a, b)
    return int(number1) + int(number2)


t = int(input())
while(t > 0):
    t -= 1
    p, q = map(int, input().split())
    number1 = ''
    number2 = ''
    try:
        number1 = input()
        number2 = input()
    except EOFError as e:
        list = number1.split(' ')
        number1 = list[0]
        number2 = list[1]
    a = str(min(p, q))
    b = str(max(p, q))
    
    print(total_min(a, b, number1, number2),total_max(a, b, number1, number2))

