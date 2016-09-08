def find_sub_array(arr):
    summ, max_size, start_index, end_index = 0, -1, 0, 0
    for i in range(len(arr) - 1):
        if arr[i] == 0:
            summ = -1
        else:
            summ = 1

        for j in range(i+1, len(arr)):
            if arr[j] == 0:
                summ += -1
            else:
                summ += 1

            if summ == 0 and max_size < j - i + 1:
                max_size = j - i + 1
                start_index = i

    end_index = start_index + max_size - 1
    if max_size == -1:
        return 'No such subset'
    else:
        return start_index, end_index

print(find_sub_array([1, 0, 1, 1, 1, 0, 0]))