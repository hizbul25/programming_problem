#URL: https://www.hackerrank.com/challenges/insertionsort2


def print_list(arr):
    print(" ".join(map(str, arr)))


def insertion_sort(ar):
    if len(ar) == 1:
        print_list(ar)
        return ar
    else:
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                else:
                    break

            print_list(ar)

        return ar

if __name__ == '__main__':
    size = int(input())
    ar = [int(i) for i in input().strip().split()]
    insertion_sort(ar)