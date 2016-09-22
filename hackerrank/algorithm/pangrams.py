#URL: https://www.hackerrank.com/challenges/pangrams

from collections import Counter

print('pangram' if len(Counter(input().lower())) == 27 else 'not pangram')
