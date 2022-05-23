my_list = [8, 7, 4, 3, 2]
num = ""
while num != "q":
    i = 0
    num = input("Введите натуральное значение:  ")
    if num.isdigit():
        for n in my_list:
            if int(num) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(num))
    print(my_list)
