#URL: https://www.hackerrank.com/challenges/new-year-chaos


def checkIfChao(arr):
    for i in range(0, len(arr)):
        original = arr[i] - 1
        if original > i + 2:
            return True
    return False


def countIS(arr):
    n = len(arr)
    if n == 1:
        return 0

    middle = n//2

    left = arr[0:middle]
    right = arr[middle:]
    count_left = countIS(left)
    count_right = countIS(right)
    count_inter = 0
    l = 0
    r = 0

    for i in range(0, n):
        if r == len(right) or (l != len(left) and left[l] < right[r]):
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            count_inter += len(left) - l
            r += 1
    return count_left + count_right + count_inter


if __name__ == '__main__':
    T = int(input().strip())

    for a0 in range(T):
        n = int(input().strip())
        ar = [int(q_temp) for q_temp in input().strip().split(' ')]
        if checkIfChao(ar):
            print('Too chaotic')
        else:
            print(countIS(ar))

