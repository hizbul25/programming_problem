#https://www.hackerrank.com/contests/projecteuler/challenges/euler002


def sum_fibo(n):
    temp = n
    sum = 0
    a, b = 0, 1
    while n > 0 and a < temp:
        a, b = b, a + b
        n -= 1
        if a % 2 == 0 and a <= temp:
            sum += a
    return sum

n = int(input())
for i in range(n):
    a = int(input())
    print(sum_fibo(a))
