def decrement_number():
    for i in range(1000, 0, -1):
        if i and i % 5 == 0:
            print("\n")
        print(i)
        print("\t")


decrement_number()