#Problem URL: https://www.hackerrank.com/challenges/save-the-prisoner

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]

    while m > 0:
        m -= 1
        s = n if s > n else s + 1

    s = n if s < 1 else s - 1
    print(s)


