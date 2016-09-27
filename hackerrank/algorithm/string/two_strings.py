#URL: https://www.hackerrank.com/challenges/two-strings


p = int(input().strip())

for _ in range(p):
    a = set(input().strip())
    b = set(input().strip())

    if set.intersection(a, b):
        print('YES')
    else:
        print('NO')
