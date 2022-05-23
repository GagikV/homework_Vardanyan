# While true


def divide(a, b):
    try:
        a, b = int(a), int(b)
        div = a / b
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    return div


print(divide(input("Введите первое значение: "), input("Введите второе значение: ")))
