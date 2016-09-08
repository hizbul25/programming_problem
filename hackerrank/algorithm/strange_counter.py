'''
Problem URL: https://www.hackerrank.com/challenges/strange-code
'''

t = int(input().strip())
total = 0
n = 3
while total < t:
    total += n
    n *= 2
n /= 2
print(int(total - n + (n-t)+1))
