#URL: https://www.hackerrank.com/challenges/tutorial-intro

v = int(input())
n = int(input())
vec = [int(c_temp) for c_temp in input().strip().split(' ')]
for i in range(0, n):
    if vec[i] == v:
        print(i)