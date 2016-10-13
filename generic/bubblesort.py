"""Bubble Sort"""

def bubblesort(a):
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i] < a[j]:
				a[i], a[j] = a[j], a[i]
	return a

print(bubblesort([3, 7, 4, 9, 5, 2, 6, 1, 27]))