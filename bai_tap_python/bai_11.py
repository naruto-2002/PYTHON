import bai_10

n = int(input())
s = input()

if(bai_10.isPrime(n)):
    print(f'{n} la so nguyen to')
else:
    print(f'{n} khong phai la so nguyen to')

if(bai_10.isPangram(s)):
    print(f'\"{s}|" la mot pangram')
else:
    print(f'\"{s}\" khong phai la mot pangram')