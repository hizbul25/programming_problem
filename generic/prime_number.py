# show a list of prime number until n


def prime_number(n):
    prime = []
    if n <= 1:
        return 1
    for i in range(1, n, 2):
        print(i)

prime_number(10)
