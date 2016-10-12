#URL: https://www.hackerrank.com/challenges/find-the-median


n = int(input().strip())
arr = sorted([int(temp_arr) for temp_arr in input().strip().split(' ')])
half = n // 2
print(arr[half])
