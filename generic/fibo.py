def fibo(n):
	a, b = 0, 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		while b <= n:
			print(b)
			print("\t")
			a, b = b, a+b
		print(" ")

fibo(100)