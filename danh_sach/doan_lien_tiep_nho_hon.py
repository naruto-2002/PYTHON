t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    a = [int(val) for val in input().split()]
    l = len(a)
    st = []
    for i in range(l):
        while(len(st) > 0 and a[st[-1]] <= a[i]):
            st.pop()
        if(len(st) == 0):
            print(i + 1, end=' ')
        else:
            print(i - st[-1], end=' ')
        st.append(i)
    print()