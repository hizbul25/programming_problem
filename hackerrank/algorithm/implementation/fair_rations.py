#URL: https://www.hackerrank.com/challenges/fair-rations

n = int(input().strip())
b = [int(B_temp) for B_temp in input().strip().split(' ')]

total = 0
carry = False
for x in b:
    carry = (carry + x) % 2
    total += carry * 2

if carry:
    print("NO")
else:
    print(total)