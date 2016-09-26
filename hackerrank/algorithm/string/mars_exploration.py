#URL: https://www.hackerrank.com/challenges/mars-exploration

S = input().strip()

res = 0
sos = 'SOS'
for i in range(0, len(S), 3):
    for j in range(3):
        if S[i+j] != sos[j]:
            res += 1
print(res)