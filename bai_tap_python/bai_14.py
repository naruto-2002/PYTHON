s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s2 = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
text = "LOVE"
def mh(text):
    res = ''
    for i in range(len(text)):
        res += chr((ord(text[i]) - ord('A') + 3)%26 + ord('A'))
    return res
def gm(text):
    res = ''
    for i in range(len(text)):
        res += chr((ord(text[i]) - ord('A') - 3)%26 + ord('A'))
    return res
kqmh = mh(text)
kqgm = gm(kqmh)
print(kqmh)
print(kqgm)
            



