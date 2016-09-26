#URL: https://www.hackerrank.com/challenges/merge-the-tools

s = input().strip()
k = int(input())
l = len(s) // k
for i in range(l):
    t = ''
    for c in s[i * k:i * k + k]:
        if c not in t:
            t += c
    print(t)