#URL: https://www.hackerrank.com/challenges/absolute-permutation

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    if k == 0:
        i = 1
        while i < n+1:
            print(i, end=' '),
            i += 1
        print(" ")
    elif n % 2 != 0 or k > n/2 or n % k != 0:
        print(-1)
    elif (n/k) % 2 != 0:
        print(-1)
    else:
        p = n//k
        for t in range(p):
            if t % 2 == 0:
                for i in range((k*t)+1, k*(t+1)+1):
                    print(i+k, end=' '),
            else:
                for i in range((k*t)+1, k*(t+1)+1):
                    print(i-k, end=' '),
        print(" ")