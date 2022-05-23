from random import randint

my_list = [randint(0, 10) for i in range (20)]
uniq_list = [i for i in my_list if my_list.count(i) == 1]
print(f"Исходный список {my_list}\nСписок без повторений {uniq_list}")