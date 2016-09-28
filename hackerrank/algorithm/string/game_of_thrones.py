#URL: https://www.hackerrank.com/challenges/game-of-thrones

from collections import Counter

s = input().strip()
c = Counter(s)
parity = (v % 2 for v in c.values())
parity_count = Counter(parity)
if 1 in parity_count:
    print('NO' if parity_count[1] > 1 else 'YES')
else:
    print('YES')