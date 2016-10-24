#URL: https://www.hackerrank.com/challenges/py-introduction-to-sets

n = int(input())
plants = [int(temp_p) for temp_p in input().strip().split(' ')]

distinct_plant = set(plants)
avg_height = sum(distinct_plant)/len(distinct_plant)
print(avg_height)