#URL: https://www.hackerrank.com/challenges/manasa-and-stones


t = int(input().strip())

for _ in range(t):
    n, a, b = int(input().strip()), int(input().strip()), int(input().strip())
    print(*sorted(set(a*(n-1-j) + b*j for j in range(n))))