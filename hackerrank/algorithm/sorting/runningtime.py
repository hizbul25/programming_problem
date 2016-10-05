#URL: https://www.hackerrank.com/challenges/runningtime


def insertion_sort(ar):
    count = 0
    if len(ar) == 1:
        count = 1
    else:
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                    count += 1
                else:
                    break
    print(count)
if __name__ == '__main__':
    size = int(input())
    ar = [int(i) for i in input().strip().split()]
    insertion_sort(ar)