#URL: https://www.hackerrank.com/challenges/the-love-letter-mystery

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    l, r = 0, len(s) - 1
    count = 0
    while l < r:
        count += abs(ord(s[l]) - ord(s[r]))
        l += 1
        r -= 1
    print(count)
