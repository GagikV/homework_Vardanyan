def sum():
    a = 0
    while True:
        list = input("Ввести значения чисел, для выхода ввести 'q':  ").split()
        for num in list:
            if num.lower() == "q":
                return a
            else:
                try:
                    a += int(num)
                except ValueError:
                    print("Чтобы выйти из программы, введите 'q'.")
        print(f"Сумма значений равна: {a}")


print(sum())