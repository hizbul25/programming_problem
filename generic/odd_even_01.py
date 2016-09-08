def odd_even_one():
    num = int(input())
    for i in range(0, num):
        input_num = int(input())
        if input_num % 2 == 0:
            print("even\n")
        else:
            print("odd\n")

if __name__ == "__main__":
    odd_even_one()