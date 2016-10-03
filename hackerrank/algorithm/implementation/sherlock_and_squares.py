#URL: https://www.hackerrank.com/challenges/sherlock-and-squares

from math import sqrt, floor, ceil
t = int(input().strip())


for _ in range(t):
    f, l = input().strip().split(' ')
    f, l = [int(f), int(l)]
    print((floor(sqrt(l)) - ceil(sqrt(f)))+1)

