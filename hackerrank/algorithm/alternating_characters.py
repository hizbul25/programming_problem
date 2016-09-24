#URL: https://www.hackerrank.com/challenges/alternating-characters

t = int(input())

for p in range(t):
    s = input()
    stack = []
    count = 0
    for i in range(len(s)):
        if not stack:
            stack = s[i]
        elif s[i] in stack:
            count += 1
        else:
            stack = []
            stack = s[i]
    print(count)
