'''
Given a time in AM/PM format, convert it to military (-hour) time.

Note: Midnight is on a -hour clock, and on a -hour clock. Noon is on a -hour clock, and on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.: or ), where .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM

Sample Output

19:05:45
'''

#!/bin/python3

import sys


def time_convert(t):
    converted_time = ''
    if t[8] == 'P' and int(t[:2]) <= 12:
        if t[:2] == '12':
            converted_time += t[:8]
        else:
            converted_time += (str(12 + int(t[:2])) + t[2:8])
    else:
        if t[:2] == '12':
            converted_time += ('00' + t[2:8])
        else:
            converted_time += t[:8]

    return converted_time

time = input().strip()
print(time_convert(time))
