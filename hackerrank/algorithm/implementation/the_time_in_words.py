#URL: https://www.hackerrank.com/challenges/the-time-in-words


h = int(input().strip())
m = int(input().strip())
hrs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
mins= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",  "fourteen",  "fifteen", "sixteen",  "seventeen",  "eighteen",  "ninteen",  "twenty", "twenty one",  "twenty two",  "twenty three",  "twenty four",  "twenty five",  "twenty six",  "twenty seven",  "twenty eight",  "twenty nine"]

if m == 0:
    print("{} o' clock".format(hrs[h-1]))
elif m == 15:
    print("quarter past {}".format(hrs[h-1]))
elif (m > 0 and m < 15) or (m>15 and m<30):
    print("{} minutes past {}".format(mins[m-1], hrs[h-1]))
elif m == 30:
    print("half past %s"%(hrs[h-1]))
elif m > 30 and m < 60:
    m = 60-m
    h += 1
    if m == 15:
        mn = "quarter"
    else:
        mn = mins[m-1]+" minutes"
    print("{} to {}".format(mn, hrs[h-1]))