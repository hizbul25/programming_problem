#URL: https://www.hackerrank.com/challenges/finding-the-percentage


n = int(input().strip())
students = {}
mark_sheet = []
for _ in range(n):
    mark_sheet = [c_temp for c_temp in input().strip().split(' ')]
    students[mark_sheet[0]] = sum((float(i) for i in mark_sheet[1:]))/3

find_name = input().strip()
print('{0:.2f}'.format(students[find_name]))
