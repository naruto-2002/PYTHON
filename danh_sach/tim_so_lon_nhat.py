import re
t = int(input())
while(t > 0):
    t -= 1
    s = str(input())
    numbers = re.findall(r'\d+', s)
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    if(len(numbers) != 0):
        print(int(max(numbers)))

