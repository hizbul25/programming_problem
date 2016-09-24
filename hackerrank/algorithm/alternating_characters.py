#URL: https://www.hackerrank.com/challenges/alternating-characters

t = int(input())

for p in range(t):
    s = input()
    char = None
    count = 0
    for i in range(len(s)):
        if char is None:
            char = s[i]
        elif char == s[i]:
            count += 1
        else:
            char = s[i]
    print(count)
