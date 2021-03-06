# URL: https://www.hackerrank.com/challenges/reduced-string

s = input()
stack = []

for i in range(len(s)):
    if not stack or s[i] != stack[-1]:
        stack += [s[i]]
    else:
        stack.pop()

if stack:
    print(''.join(stack))
else:
    print('Empty String')