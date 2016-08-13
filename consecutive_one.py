# Count Consecutive one in a binary list.


def consecutive_one(data):
    longest = 0
    current = 0
    for num in data:
        if num == 1:
            current += 1
        elif longest < current:
            longest = current
            current = 0
    return max(current, longest)

if __name__ == '__main__':
    data = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    print(consecutive_one(data))
