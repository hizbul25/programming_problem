# URL: https://www.hackerrank.com/challenges/palindrome-index

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    if s == s[::-1]:
        print(-1)
    else:
        for i in range(int(len(s) / 2)):
            if s[i] != s[len(s) - 1 - i]:
                print(i if ((s[:i] + s[i + 1:]) == (s[:i] + s[i + 1:])[::-1]) else len(s) - 1 - i)
                break

