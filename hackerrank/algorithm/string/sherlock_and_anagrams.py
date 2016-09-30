#URL: https://www.hackerrank.com/challenges/sherlock-and-anagrams

from collections import Counter

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    substrings = (''.join(sorted(s[j: j + i])) for i in range(1, len(s)) for j in range(len(s) - i + 1))
    substrings = Counter(substrings)

    print(sum(v * (v - 1) // 2 for v in substrings.values()))