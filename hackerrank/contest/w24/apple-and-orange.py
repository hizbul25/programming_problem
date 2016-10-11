#URL: https://www.hackerrank.com/contests/w24/challenges/apple-and-orange


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]

print(sum([1 if s <= a+int(apple) <= t else 0 for apple in input().strip().split(' ')]))
print(sum([1 if s <= b+int(orange) <= t else 0 for orange in input().strip().split(' ')]))