#URL: https://www.hackerrank.com/challenges/capitalize

s = input().strip()
words = s.split(' ')
for word in words:
    print(word.capitalize(), end=' ')