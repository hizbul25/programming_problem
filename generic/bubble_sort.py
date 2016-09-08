data = [3, 7, 4, 9, 5, 2, 6, 1]
for i in range(0, len(data)):
    for j in range(0, len(data) - 1):
        if data[j+1] < data[j]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
print(data)