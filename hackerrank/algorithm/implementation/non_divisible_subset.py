'''

'''

#!/bin/python3

import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]

L = [0]*k

for x in arr:
    L[x % k] += 1
res = 0
for i in range(k//2+1):
    if i == 0 or k == i*2:
        res += bool(L[i])
    else:
        res += max(L[i], L[k-i])

print(res)
