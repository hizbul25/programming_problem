'''
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''


def birthday_cake_candles(n, ar):
    return ar.count(max(ar))


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = birthday_cake_candles(n, ar)
    print(result)