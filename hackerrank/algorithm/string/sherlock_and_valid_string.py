#URL: https://www.hackerrank.com/challenges/sherlock-and-valid-string

from collections import Counter


def is_valid(s):
    char_map = Counter(s)
    char_occurence_map = Counter(char_map.values())
    if len(char_occurence_map) == 1:
        return True
    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return True
    return False

if __name__ == '__main__':
    s = input().strip()
    if is_valid(s):
        print('YES')
    else:
        print('NO')
