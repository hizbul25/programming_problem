import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
pair = []
for i in list(a):
    for j in list(a):
        if a[i] < a[j] and (a[i] + a[j] % k == 0):
            pair.append((i, j))

print(pair)