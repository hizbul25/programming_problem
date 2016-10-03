#URL: https://www.hackerrank.com/challenges/utopian-tree


t = int(input().strip())

for a0 in range(t):
    height = 1
    n = int(input().strip())
    for i in range(1, n+1):
        if i % 2 != 0:
            height *= 2
        elif i % 2 == 0:
            height += 1

    print(height)