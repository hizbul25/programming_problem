#URL: https://www.hackerrank.com/challenges/lisa-workbook

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
p = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
offset = 1
for chapter in p:
    pages = (chapter + k - 1)//k
    for idx in range(pages):
        if offset >= (idx * k)+1 and offset <= min((idx+1)*k, chapter):
            count += 1
        offset += 1

print(count)