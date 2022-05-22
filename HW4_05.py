from functools import reduce


def my_func(first, last):
    return first*last


a = [i for i in range(100, 1001) if i % 2 == 0]
print(a)
print(reduce(my_func, a))

