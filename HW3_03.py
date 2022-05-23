a=()
b=()
c=()


def func(a, b, c):
    a = int(input("введите значение первой переменной: "))
    b = int(input("введите значение второй переменной: "))
    c = int(input("введите значение второй переменной: "))
    mylist = [a, b, c]
    try:
        mylist.remove(min(mylist))
        return sum(mylist)
    except TypeError:
        return "можно вносить только числа"


print(func(a, b, c))