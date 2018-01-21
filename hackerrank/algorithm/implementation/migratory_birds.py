'''
https://www.hackerrank.com/challenges/migratory-birds/problem
'''
from collections import Counter

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
counter = Counter(ar)
print(counter.most_common()[0][0])
