#URL: https://www.hackerrank.com/challenges/funny-string

t = int(input())

is_funny = False
for _ in range(t):
    s = input()
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == abs(ord(r[i]) - ord(r[i-1])):
            is_funny = True
        else:
            is_funny = False
            break
    if is_funny:
        print('Funny')
    else:
        print('Not Funny')

