#URL: https://www.hackerrank.com/challenges/py-set-add


n = int(input())
countries = []
for __ in range(n):
    countries.append(input().strip())
print(len(set(countries)))