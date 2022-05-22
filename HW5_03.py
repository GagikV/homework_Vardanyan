with open('text3.txt', 'r', encoding='utf-8') as f:
    employees = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Средняя зарплата = {round(sum(employees.values()) / len(employees), 3)}\n"f"Работники с зарплатой больше 20000 руб. "
          f"{[i[0] for i in employees.items() if i[1] < 20000]}")
