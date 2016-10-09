#URL: https://www.hackerrank.com/challenges/bon-appetit


n, k = list(map(int, input().split()))
ba = list(map(int, input().split()))
print(int(input())-(sum(ba)-ba[k])//2 or 'Bon Appetit')