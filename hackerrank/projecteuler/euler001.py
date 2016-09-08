def sum_multiples(n):
    max3 = range(0, n, 3)[-1]
    max5 = range(0, n, 5)[-1]
    max15 = range(0, n, 15)[-1]

    sum3 = (max3 + 3) * max3 // 3 // 2
    sum5 = (max5 + 5) * max5 // 5 // 2
    sum15 = (max15 + 15) * max15 // 15 // 2

    return sum3 + sum5 - sum15

n = int(input())
for i in range(n):
    a = int(input())
    print(sum_multiples(a))