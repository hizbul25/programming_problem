#URL: https://www.hackerrank.com/challenges/gem-stones

n = int(input())
all_elem = set(input())
for g in range(n - 1):
    all_elem &= set(input())
print(len(all_elem))
