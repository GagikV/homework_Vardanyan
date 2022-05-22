from itertools import count
from itertools import cycle

c = 0
for i in cycle("ABC"):
    if c > 10:
        break
    print(i)
    c += 1


for i in count(3):
    if i > 10:
        break
    else:
        print(i)
