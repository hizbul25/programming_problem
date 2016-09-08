'''
Problem URL: https://www.hackerrank.com/challenges/circular-array-rotation
'''

n, k, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
k %= n
arr = arr[-k:] + arr[:-k]
for i in range(m):
    print(arr[int(input().strip())])