"""Insertion sort"""

def insertionsort(a):
	for i in range(len(a)):
		x = a[i]
		j = i - 1

		while j >= 0 and a[j] > x:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = x

	return a

print(insertionsort([3, 7, 4, 9, 5, 2, 6, 1]))