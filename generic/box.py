def create_box():
    with open('input_files/box.txt', 'r') as lines:
        num_list = []
        for num in lines:
            num_list.append(int(num.strip()))
        num_list.pop(0)

    for n in num_list:
        print(n * ("*" * n + "\n"))


create_box()