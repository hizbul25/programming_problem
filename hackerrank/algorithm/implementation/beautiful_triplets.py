#URL: https://www.hackerrank.com/challenges/beautiful-triplets


n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
a = [int(s_temp) for s_temp in input().strip().split(' ')]
cnt = 0

for i in range(n):
    if a[i]+d in a and a[i]+2*d in a:
        cnt += 1
print(cnt)
