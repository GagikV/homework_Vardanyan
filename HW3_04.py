a = int(input("Введите значение числа: "))
b = int(input("Введите значение степени: "))


def stepen(a, b):
    res1 = a ** b
    return res1


print(f"Результат возведения: {stepen(a, b)}")


def stepen2(a, b):
    try:
        a, b = int(a), int(b)
        if a <= 0 or b >=0:
            return "не выполнено условие: \n a > 0 \n b <0"
        else:
            res2 = 1
            for i in range(abs(b)):
                res2 /= a
            return f'Результат возведения: {round(res2, 3)}'
    except ValueError:
        return "можно вносить только числа"



print(stepen2(a, b))