#URL: https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs

from collections import Counter

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()

    counter = Counter(b)

    if counter.get('_') is None and len(counter) > 1:
        happy, diff = True, 0
        for i in range(n - 1):
            if b[i] != b[i+1]:
                happy = False
                diff += 1
            elif diff > 1:
                happy = False
                break
            else:
                happy = True

        print('YES' if happy else 'NO')

    else:
        del counter['_']
        if len(counter) == 0:
            print('YES')
        elif 1 in counter.values():
            print('NO')
        else:
            print('YES')

