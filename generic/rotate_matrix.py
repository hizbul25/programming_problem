original = [
    [1, 2, 3, 4],
    [9, 8, 5, 6],
    [6, 5, 3, 7],
    [9, 2, 6, 8],
]
print(list(zip(*original[::-1])))
