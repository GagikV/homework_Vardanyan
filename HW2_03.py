my_dict = {"1":"зима", "2":"зима", "3":"весна", "4":"весна", "5":"весна", "6":"лето", "7":"лето", "8":"лето", "9":"осень", "10":"осень", "11":"осень", "12":"зима"}
my_list = ["зима", "зима", "весна","весна","весна", "лето","лето","лето", "осень","осень","осень", "зима"]
month = input("введите номер месяца: ")
print(my_dict.get(month))
month = int(month)-1
print(my_list[month])