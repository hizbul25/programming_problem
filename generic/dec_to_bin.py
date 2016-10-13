def dec2bin(n):
	bin = []
	while 1 <= n:
		rem = n % 2
		n = n // 2
		bin.append(rem)

	return bin[::-1]

print(dec2bin(25))
