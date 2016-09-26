# Problem URL: https://www.hackerrank.com/challenges/bonetrousle

firstLine = int(input())

for a in range(0, firstLine):
    nums = input()
    numsArr = list(map(int, nums.split(" ")))
    n = numsArr[0]
    k = numsArr[1]
    b = numsArr[2]

    num1 = 0
    rem = 0

    answer = True
    remAdded = False
    count = 0
    boxArr = []
    for i in range(1, b+1):
        count += i
        boxArr.append(i)

    num1 = (n - count)//b
    rem = (n - count) % b

    for j in range(0, len(boxArr)):
        boxArr[j] += num1
        if boxArr[j] > k:
            answer = False

    if rem == 0:
        remAdded = True
    elif boxArr[-1] + 1 > k:
        remAdded = False
    elif answer is not False:
        l = len(boxArr) - 1
        for r in range(l, l - rem, -1):
            boxArr[r] += 1
        remAdded = True

    if answer is False or remAdded is False:
        print(-1)
    elif 0 in boxArr:
        print(-1)
    else:
        for z in range(0, len(boxArr)):
            if z != len(boxArr) - 1:
                print(boxArr[z], end=" ")
            else:
                print(boxArr[z])