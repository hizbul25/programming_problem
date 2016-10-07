#URL: https://www.hackerrank.com/challenges/countingsort3


n = int(input().strip())
L = []
count = 0
for _ in range(n):
    info = input().split()
    L.append(int(info[0]))
for i in range(100):
    count += L.count(i)
    print(count, end=' ')