

def reverse(n):
    return n[::-1]

def gith(n):
    if(n == 0 or n == 1):
        return 1
    return n*gith(n-1)

