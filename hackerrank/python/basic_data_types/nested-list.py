#URL: https://www.hackerrank.com/challenges/nested-list


n = int(input().strip())
students = [[input().strip(), float(input().strip())] for _ in range(n)]
mark = sorted(set([m for n, m in students]))[1]
print('\n'.join(sorted([n for n, m in students if m == mark])))
