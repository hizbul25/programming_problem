 #https://www.hackerrank.com/contests/projecteuler/challenges/euler003


def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2

    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num /= i

    if num > 2:
        factors.append(int(num))

    return max(factors)

n = int(input())
for i in range(n):
    a = int(input())
    print(prime_factors(a))
