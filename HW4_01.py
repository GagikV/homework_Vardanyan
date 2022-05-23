from sys import argv


def sallary():
    try:
        sall_1, time_2, bonus_3 = map(float, argv[1:])
        print(f"Ставка = {sall_1} руб/час\nКоличество часов = {time_2} часов\nПремия = {bonus_3} руб\nЗарплата сотрудника = {sall_1 * time_2 + bonus_3} руб")
    except ValueError:
        print("Введите все три значения переменных для ставки, количества часов работы и бонуса")


sallary()
