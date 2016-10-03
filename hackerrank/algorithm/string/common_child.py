#URL: https://www.hackerrank.com/challenges/common-child


def common_child(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0:
                lengths[i][j] = 0
            elif a[i-1] == b[j-1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    return lengths[len(a)][len(b)]

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(common_child(s1, s2))