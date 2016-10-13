"""selection sort"""
def selectionsort(a):
	for i in range(len(a)):
		min = i
		for j in range(i, len(a)):
			if a[j] < a[min]:
				min = j
		a[i], a[min] = a[min], a[i]

	return a

print(selectionsort([3, 7, 4, 9, 5, 2, 6, 1, 27]))