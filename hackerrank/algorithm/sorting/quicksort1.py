#URL: https://www.hackerrank.com/challenges/quicksort1


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

p = arr[0]
left, eq, right = [], [], []

for a in arr:
    if a < p:
        left.append(a)
    elif a > p:
        right.append(a)
    else:
        eq.append(a)

new_list = left + eq + right
print(' '.join(map(str, new_list)))