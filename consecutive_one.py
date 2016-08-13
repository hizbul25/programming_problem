# Count Consecutive one in a binary list.


from itertools import groupby


def len_iter(items):
    return sum(1 for _ in items)


def consecutive_one(data):
    return max(len_iter(run) for val, run in groupby(data) if val)

if __name__ == '__main__':
    data = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    print(data)
    print(consecutive_one(data))
