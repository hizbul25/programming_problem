'''
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains space-separated integers describing an array of numbers .

Output Format

You must print the following lines:

    A decimal representing of the fraction of positive numbers in the array.
    A decimal representing of the fraction of negative numbers in the array.
    A decimal representing of the fraction of zeroes in the array.

Sample Input

6
-4 3 -9 0 4 1

Sample Output

0.500000
0.333333
0.166667

Explanation

There are positive numbers, negative numbers, and zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are , and , respectively.
'''
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

zero, pos, neg = 0, 0, 0
for i in arr:
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    else:
        zero += 1

pos = pos / n
neg = neg / n
zero = zero / n

print("%0.6f" % pos)
print("%0.6f" % neg)
print("%0.6f" % zero)