# https://www.hackerrank.com/challenges/string-construction

n = int(input().strip())
for a0 in range(n):
    p = []
    count = 0
    s = input().strip()
    for i in range(len(s)):
        if s[i] not in p:
            p.append(s[i])
            count += 1
    print(count)