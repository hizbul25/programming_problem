#URL: https://www.hackerrank.com/challenges/chocolate-feast


t = int(input().strip())

for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]
    chocolate, wrappers = n // c, n // c

    while wrappers >= m:
        chocolate += 1
        wrappers -= m
        wrappers += 1
    print(chocolate)