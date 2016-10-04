#URL: https://www.hackerrank.com/challenges/almost-sorted


def isSorted(a):
    for i in range(n-1):
        if a[i] > a[i+1]:
            return False
    return True


def swap(a, left, right):
    temp = a[left]
    a[left] = a[right]
    a[right] = temp


n = int(input())
a = [int(temp) for temp in input().strip().split()]

if isSorted(a):
    print("yes")
else:

    left, right = -1, -1
    for i in range(n-1):
        if a[i] > a[i+1]:
            left = i
            break
    for i in range(n-1, left, -1):
        if a[i] < a[i-1]:
            right = i
            break
    i, j = left, right
    swap(a, left, right)

    if isSorted(a):
        print("yes")
        print("swap {} {}".format(left+1, right+1))
    else:
        swap(a, left, right)
        a[left: right+1] = reversed(a[left: right+1])
        if isSorted(a):
            print("yes")
            print("reverse {} {}".format(left+1, right+1))
        else:
            print("no")