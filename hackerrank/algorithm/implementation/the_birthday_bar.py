'''
https://www.hackerrank.com/challenges/the-birthday-bar/problem
'''

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]

print(sum([1 for i in range(n-m+1) if sum(s[i:i+m]) == d]))
