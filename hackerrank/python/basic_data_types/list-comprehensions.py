#URL: https://www.hackerrank.com/challenges/list-comprehensions


x, y, z, n = [int(input().strip()) for i in range(4)]
print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])