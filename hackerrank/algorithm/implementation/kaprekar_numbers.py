#URL: https://www.hackerrank.com/challenges/kaprekar-numbers


def iskaprekar(num):
    if num < 0 or 2 <= num <= 3:
        return False
    if 0 <= num <= 1:
        return True
    square = str(num * num)
    L = len(str(num))
    return int(square[:-L]) + int(square[-L:]) == num

p, q = int(input()), int(input())
kaprekar_nums = [i for i in range(p, q + 1) if iskaprekar(i)]

if kaprekar_nums:
    print(*kaprekar_nums)
else:
    print('INVALID RANGE')