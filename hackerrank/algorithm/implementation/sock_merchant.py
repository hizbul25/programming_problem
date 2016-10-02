#URL: https://www.hackerrank.com/challenges/sock-merchant

from collections import Counter

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
pairs = 0
socks = Counter(c)

for i in socks.values():
    if i >= 2:
        if i % 2:
            pairs += (i-1)//2
        else:
            pairs += i // 2

print(pairs)
