#URL: https://www.hackerrank.com/challenges/larrys-array

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    small_num = []
    cnt = 0
    for i in range(n-1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                cnt += 1
    small_num.append(cnt)

    if sum(small_num) % 2:
        print("NO")
    else:
        print("YES")