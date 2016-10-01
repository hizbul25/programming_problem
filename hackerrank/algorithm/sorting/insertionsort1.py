#URL: https://www.hackerrank.com/challenges/insertionsort1


def print_list(arr):
    print(" ".join(map(str, arr)))


def insertion_sort(arr):
    if len(arr) == 1:
        print_list(arr)
        return arr
    else:
        x = arr[-1]
        for i in reversed(range(len(arr) - 1)):
            if x < arr[i]:
                arr[i+1] = arr[i]
                print_list(arr)

                if i == 0:
                    arr[0] = x
                    print_list(arr)
                    break
            else:
                arr[i+1] = x
                print_list(arr)
                break
    return arr


if __name__ == '__main__':
    size = int(input())
    ar = [int(i) for i in input().strip().split()]
    insertion_sort(ar)