n, m = map(int, input().split())
a = list(map(int, input().split()))

# Hàm tính giá trị của biểu thức
def evaluate_expression(exp):
    stack = []
    for token in exp:
        if token.isdigit():
            stack.append(int(token))
        elif(len(stack) > 1):
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            else:
                stack.append(op1 * op2)
    return stack[0]

# Tìm tất cả các biểu thức có thể tạo ra từ dãy số và các phép toán
def find_expressions():
    expressions = []
    # Duyệt tất cả các phép toán
    for op1 in ['+', '-', '*']:
        for op2 in ['+', '-', '*']:
            for op3 in ['+', '-', '*']:
                # Duyệt tất cả các trường hợp sử dụng hoặc không sử dụng một phép toán ở mỗi vị trí
                for i in range(2 ** (n - 1)):
                    exp = []
                    for j in range(n - 1):
                        exp.append(str(a[j]))
                        if i & (1 << j):
                            exp.append(op1)
                        else:
                            exp.append(op2)
                    exp.append(str(a[-1]))

                    # Thử tính giá trị của biểu thức
                    try:
                        if evaluate_expression(exp) == m:
                            # Kết quả đúng, thêm vào danh sách các biểu thức tìm được
                            expressions.append(''.join(exp).replace('*', 'x'))
                    except ZeroDivisionError:
                        pass

    # In ra tất cả các biểu thức tìm được hoặc IMPOSSIBLE nếu không tìm thấy
    if expressions:
        for exp in expressions:
            print(exp + '=' + str(m))
    else:
        print('IMPOSSIBLE')

find_expressions()
