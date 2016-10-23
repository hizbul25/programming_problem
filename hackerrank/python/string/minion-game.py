#URL: https://www.hackerrank.com/challenges/the-minion-game

s, v = input(), 'AEIOU'
stuart, kevin = 0, 0
for i in range(len(s)):
    if s[i] in v:
        kevin += len(s) - i
    else:
        stuart += len(s) - i

if kevin > stuart:
    print('Kevin {}'.format(kevin))
elif stuart > kevin:
    print('Stuart {}'.format(stuart))
else:
    print('Draw')