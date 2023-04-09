import math
a = [0]*2*10**6
a[0] = a[1] = 1
for i in range(2, 2*10**3):
    if(a[i] == 0):
        for j in range(i*i, 2*10**6, i):
            a[j] = 1

sum=0
for t in range(int(input())):
    n = int(input())
    m = n
    
    while(n%2 == 0):
        sum += 2
        n //= 2
    arr = []
    for i in range(3, int(math.sqrt(n))+1,2):
        while n%i==0 and a[i]==0:
            sum+=i
            n//=i
            if a[n//i]==0 and n%(n//i)==0:
                sum+=n//i
                n//(n//i)
    if n!=1:
        sum+=n
print(sum)
    
                

            


