# import math
# import re
# def isPrime(n):
#     if(n < 2):
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if(n%i == 0):
#             return False
#     return True

# def isPangram(s):
#     s = s.lower()
#     ss = re.findall(r'[a-z]', s)
#     ss = list(set(ss))
#     if(len(ss) >= 26):
#         return True
#     return False

import string
x = "the quick brown fox jumped over the lazy dog"
if(set(x) >= set(string.ascii_lowercase)):
    print("ok")