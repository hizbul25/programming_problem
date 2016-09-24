#URL: https://www.hackerrank.com/challenges/beautiful-binary-string

n = int(input().strip())
b = [int(i) for i in input().strip()]

count = 0
for i in range(2, n):
    if b[i-2] == 0 and b[i-1] == 1 and b[i] == 0:
        b[i] = 1
        count += 1
print(count)