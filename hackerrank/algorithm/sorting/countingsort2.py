#URL: https://www.hackerrank.com/challenges/countingsort2

from collections import Counter

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
counter = Counter(arr)
for i in range(100):
    for j in range(counter[i]):
        print(i, end=' ')
