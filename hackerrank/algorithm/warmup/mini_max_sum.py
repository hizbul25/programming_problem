'''
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    print("{} {}".format(sum(arr) - max(arr), sum(arr) - min(arr)))