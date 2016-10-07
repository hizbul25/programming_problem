#URL: https://www.hackerrank.com/challenges/caesar-cipher-1


n = int(input().strip())
s = input().strip()
k = int(input().strip())

cipher = ''
for c in s:
    if ord(c) >=97 and ord(c) <= 122:
        cipher += chr((ord(c) - 97 + k) % 26 + 97)
    elif ord(c) >= 65 and ord(c) <= 90:
        cipher += chr((ord(c) - 65 + k) % 26 + 65)
    else:
        cipher += c
print(cipher)