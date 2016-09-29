#URL: https://www.hackerrank.com/challenges/making-anagrams

from collections import Counter

A = input().strip()
B = input().strip()

a = Counter(A)
b = Counter(B)

length = sum(min(a[c], b[c]) for c in(set(A) & set(B)))

print((len(A) - length) + (len(B) - length))