#URL: https://www.hackerrank.com/challenges/find-digits


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum((n % int(i) == 0 if int(i) > 0 else False for i in str(n))))
