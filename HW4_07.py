def factorial(num):
    f_num = 1
    for i in range(num + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1


for i in factorial(int(input("Укажите число для расчета его факториала: "))):
    print(i)


