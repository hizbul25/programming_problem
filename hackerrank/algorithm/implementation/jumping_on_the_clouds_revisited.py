#URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')][::k]
print(100 - len(c) - c.count(1) * 2)
