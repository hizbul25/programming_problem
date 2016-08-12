# Count Consecutive one in a binary list.


def consecutive_one(data):
    one_list = []
    size = 0
    for num in data:
        if num == 1:
            one_list.append(num)
        elif num == 0 and size < len(one_list):
            size = len(one_list)
            one_list = []

    return size

if __name__ == '__main__':
    data = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
    print(consecutive_one(data))
