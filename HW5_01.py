with open('newtextfile.txt', 'w', encoding='utf-8') as i:
    while True:
        inf = input('осуществите ввод строки для записи, пустая строка для окончания: ')
        if not inf:
            break
        print(inf, file=i)

# требуется закрыть файл
