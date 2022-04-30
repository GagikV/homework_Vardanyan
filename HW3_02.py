def cust_inf(**kwargs):
    return ' '.join(kwargs.values())


print(cust_inf(name=input("Введите ваше имя: ").capitalize(), last_name=input("Введите вашу Фамилию имя: ").capitalize(),
               birth=input("Введите ваш год рождения: "), city=input("Введите ваш город: "),
               e_mail=input("Введите вашу электронную почту: "),
               mob=input("Введите ваш телефонный номер: ")))