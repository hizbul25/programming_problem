#URL: https://www.hackerrank.com/challenges/repeated-string


s = input().strip()
n = int(input().strip())

a = s.count('a')
x = n//len(s)
print(x*a+s[:n % len(s)].count('a'))
