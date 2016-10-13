def bin2dec(n):
	dec = 0
	for i in str(n):
		dec = dec * 2 + int(i)
	print dec


bin2dec(11001)