#URL: https://www.hackerrank.com/challenges/maximum-perimeter-triangle

n = int(input())
ar = sorted([int(i) for i in input().strip().split()])
triangle = 0
perimeter = 0
if n > 2:
    for i in range(len(ar)):
        if i <= len(ar) - 3:
            if ar[i] < ar[i+1] + ar[i+2] and ar[i+1] < ar[i] + ar[i+2] and ar[i+2] < ar[i+1] + ar[i]:
                if ar[i] + ar[i + 1] + ar[i + 2] > perimeter:
                    triangle = (ar[i], ar[i+1], ar[i+2])
                    perimeter = ar[i] + ar[i + 1] + ar[i + 2]


if perimeter == 0:
    print('-1')
else:
    for i in sorted(triangle):
        print(i, end=' ')

