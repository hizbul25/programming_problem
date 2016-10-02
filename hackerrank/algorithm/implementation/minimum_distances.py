#URL: https://www.hackerrank.com/challenges/minimum-distances

from collections import Counter


def diff(arr):
    for i in range(len(arr) - 1):
        return abs(arr[i] - arr[i+1])


def min_distance(arr):
    c = Counter(arr)
    dups = [i for i in c if c[i] != 1]
    result = []
    for item in dups:
        result.append(diff([i for i, j in enumerate(arr) if j == item]))
    return result


if __name__ == '__main__':
    n = int(input().strip())
    A = [int(A_temp) for A_temp in input().strip().split(' ')]
    distance = min_distance(A)
    if not distance:
        print('-1')
    else:
        print(min(distance))