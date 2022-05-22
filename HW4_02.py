import random
my_list = [random.randint (1, 250) for n in range(15)]
print(my_list)
new_list = []
new_list2 = []

for i in range(len(my_list)-1):
  if my_list[i] < my_list[i+1]:
    new_list.append(my_list[i+1])

my_list2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list2 = [my_list[i+1] for i in range(len(my_list)-1) if my_list[i] < my_list[i+1]]

print(new_list)
print(new_list2)