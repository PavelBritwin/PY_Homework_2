# Реализуйте алгоритм перемешивания списка.

import random

list = []
for i in range(7):
    list.append(random.randrange(-99, 99))
print(list)

for j in range(len(list)):
    rnd = random.randrange(0, len(list))
    list[j], list[rnd] = list[rnd], list[j]
print(list)