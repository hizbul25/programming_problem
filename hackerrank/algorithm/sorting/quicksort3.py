#URL: https://www.hackerrank.com/challenges/quicksort3


def qsort(ar, start, end):
    if end - start <= 0:
        return ar
    pivot = ar[end]

    ind = start

    for i in range(start, end):
        if ar[i] <= pivot:
            ar[ind], ar[i] = ar[i], ar[ind]
            ind += 1
        else:
            pass
    ar[ind], ar[end] = ar[end], ar[ind]
    print(' '.join(map(str, ar)))

    ar = qsort(ar, start, ind-1)
    ar = qsort(ar, ind+1, end)

    return ar


if __name__ == '__main__':
    n = int(input())
    ar = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    qsort(ar, 0, n-1)