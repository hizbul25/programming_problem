#URL: https://www.hackerrank.com/challenges/countingsort1


n = int(input())
ar = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(' '.join(map(str, [ar.count(i) for i in range(100)])))