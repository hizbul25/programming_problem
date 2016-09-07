#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
T = [0]*n
T[1] = 1
for i in range(2, n):
    if c[i] != 1:
        T[i] = min(T[i-1]+1, T[i-2]+1)
    else:
        T[i] = 999
print(T[n-1])
