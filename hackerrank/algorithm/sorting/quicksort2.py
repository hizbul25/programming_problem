#URL: https://www.hackerrank.com/challenges/quicksort2


def print_list(arr):
    print(' '.join(map(str, arr)))


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = quicksort([i for i in arr if i < arr[0]])
        right = quicksort([i for i in arr if i > arr[0]])

        print_list(left + [arr[0]] + right)
        return left + [arr[0]] + right


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    quicksort(arr)


