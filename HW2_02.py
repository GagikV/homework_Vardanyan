my_list = []
a = "NONE"
n = 0
while n != a:
  n = input(f"Введите любое значение (введите 'NONE' для остановки ввода): ").upper()
  if n == a:
    break
  else:
    my_list.append(n)
    x = len(my_list)
    print(my_list)
    print(x)
print(my_list)
for i in range(1, len(my_list), 2):
  my_list[i-1], my_list[i]=my_list[i], my_list[i-1]
  print(my_list)
