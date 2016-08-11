def matching_number():
    with open('input_files/matching_number.txt', 'r') as lines:
        for line in lines:
            data = line.split(" ")
            if len(data) > 1:
                if data[0][0] in data[1] and data[0][1] in data[1]:
                    print(sorted(data[0]))
                elif data[0][0] in data[1]:
                    print(data[0][0])
                elif data[0][1] in data[1]:
                    print(data[0][1])
                else:
                    print('N')

matching_number()