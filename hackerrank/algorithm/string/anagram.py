#URL: https://www.hackerrank.com/challenges/anagram

from collections import Counter

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    if len(s) % 2:
        print(-1)
    else:
        l = len(s) // 2
        s1, s2 = s[:l], s[l:]
        c2 = Counter(s2)
        replacements = len(s1)

        for c in s1:
            if c in c2 and c2[c] > 0:
                replacements -= 1
                c2[c] -= 1
        print(replacements)
