#URL: https://www.hackerrank.com/challenges/icecream-parlor


t = int(input().strip())

for _ in range(t):
    m = int(input().strip())
    n = int(input().strip())
    cost = [int(cost_temp) for cost_temp in input().strip().split(' ')]

    for i, c in enumerate(cost[:-1]):
        for j in range(i+1, len(cost)):
            if cost[j] == m - c:
                print("{} {}".format(i+1, j+1))
                break
