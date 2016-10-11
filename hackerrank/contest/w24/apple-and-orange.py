#URL: https://www.hackerrank.com/contests/w24/challenges/apple-and-orange


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]

print(sum([1 if a+int(apple) >= s and a+int(apple) <= t else 0 for apple in input().strip().split(' ')]))
print(sum([1 if b+int(orange) >= s and b+int(orange) <= t else 0 for orange in input().strip().split(' ')]))