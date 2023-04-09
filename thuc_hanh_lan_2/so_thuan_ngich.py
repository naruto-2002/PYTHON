def is_palindrome_in_base(num, base):
    digits = []
    while num:
        digits.append(num % base)
        num //= base
    for i in range(len(digits)//2):
        if digits[i] != digits[-(i+1)]:
            return False
    return True
def count_palindromes_in_range(start, end, base_max):
    count = 0
    for i in range(start, end+1):
        is_palindrome = True
        for base in range(2, base_max+1):
            if not is_palindrome_in_base(i, base):
                is_palindrome = False
                break
        if is_palindrome:
            count += 1
    return count
a, b, m = map(int, input().split())
print(count_palindromes_in_range(a, b, m))