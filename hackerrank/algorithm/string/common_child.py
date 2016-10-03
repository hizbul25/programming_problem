#URL: https://www.hackerrank.com/challenges/common-child


def common_child(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])

    return lengths[-1][-1]

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(common_child(s1, s2))