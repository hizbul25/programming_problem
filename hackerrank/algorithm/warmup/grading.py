'''
https://www.hackerrank.com/challenges/grading/problem
'''


n = int(input().strip())
grades = []
grades_i = 0
for _ in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

for grade in grades:
    remainder = grade % 5
    diff = 5 - remainder
    if grade >= 38 and diff < 3:
        print(grade + diff, sep='\n')
    else:
        print(grade, sep='\n')
