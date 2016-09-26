#URL: https://www.hackerrank.com/challenges/camelcase


s = input().strip()
UppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count = 1
for i in s:
    if i in UppercaseLetters:
        count += 1

print(count)