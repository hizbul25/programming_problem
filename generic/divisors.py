def divisors():
    with open('input_files/divisors.txt', 'r') as lines:
        num_list = []
        for num in lines:
            num_list.append(num.strip())
    size = num_list.pop(0)

    for item in num_list:
        for i in range(1, int(item) + 1):
            if int(item) % i == 0:
                print(i)
        print("\n")

divisors()