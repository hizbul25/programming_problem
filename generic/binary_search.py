"""Binary Search"""

def binary_search(arr, x):
	exist = False
	lo = 0
	hi = len(arr) - 1

	while lo < hi:
		mid = (lo + hi)// 2

		if arr[mid] == x:
			exist =True
			break
		elif x < arr[mid]:
			hi = mid

		elif x > arr[mid]:
			lo = mid + 1

	return exist

print(binary_search(sorted([3, 7, 4, 9, 5, 2, 6, 1, 27]), 90))