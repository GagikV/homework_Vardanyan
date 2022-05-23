from random import randint

with open('text5.txt', mode='w+', encoding='utf-8') as file:
    file.write(" ".join([str(randint(1, 200)) for _ in range(100)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))
