'''

You are given an array of integers, , and a positive integer, . Find and print the number of pairs where and + is evenly divisible by .

Input Format

The first line contains space-separated integers, and , respectively.
The second line contains space-separated integers describing the respective values of .

Constraints

Output Format

Print the number of pairs where and + is evenly divisible by .

Sample Input

6 3
1 3 2 6 1 2

Sample Output

 5
'''

import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
pairs = 0
for i in range(n):
    for j in range(i+1, n):
        if (a[j] + a[i]) % k == 0:
            pairs += 1


print(pairs)