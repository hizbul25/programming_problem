data = [3, 7, 4, 9, 5, 2, 6, 1]
for i in range(0, len(data)):
    x = data[i]
    j = i - 1

    while j >= 0 and data[j] > x:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = x

print(data)
