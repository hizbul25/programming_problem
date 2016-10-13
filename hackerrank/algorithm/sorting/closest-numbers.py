def difference(a):
    a.sort()
    smallest_dif = max(a)
    smallest_pair = []
    for i in range(len(a)-1):
            _difference = a[i+1]-a[i]
            if _difference < smallest_dif:
                smallest_dif = _difference
                smallest_pair = [(a[i], a[i+1])]
            elif _difference == smallest_dif:
                smallest_pair.append((a[i], a[i+1]))
    for i in smallest_pair:
        print("{} {}".format(i[0], i[1]), end=' ')


n = int(input().strip())
arr = [int(temp_arr) for temp_arr in input().strip().split(' ')]
difference(arr)
