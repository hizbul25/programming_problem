#URl: https://www.hackerrank.com/challenges/find-a-string

s = input().strip()
ss = input().strip()

count = 0
for i in range(len(s)):
    if s[i:i+len(ss)] == ss:
        count += 1
print(count)
