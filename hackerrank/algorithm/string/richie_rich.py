#URL: https://www.hackerrank.com/challenges/richie-rich

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
number = list(input().strip())

change = 0
for i in range(n//2):
    if number[i] != number[n-1-i]:
        change += 1
if change > k:
    print(-1)
else:
    change = 0
    cpos = []
    for i in range(n//2):
        if number[i] != number[n-1-i]:
            cpos.append(i)
            if int(number[i]) > int(number[n-1-i]):
                number[n-1-i] = number[i]
            else:
                number[i] = number[n-1-i]
            change += 1

    i = 0
    while(k - change) > 0:
        if i <= n/2:
            if number[i] != '9':
                number[i] = '9'
                number[n-1-i] = '9'
                if i in cpos:
                    change += 1
                else:
                    change += 2
            i += 1
        else:
            break
    if n % 2 == 1 and k-change > 0:
        number[n/2+1] = '9'
        change += 1
    print("".join(str(e) for e in number))