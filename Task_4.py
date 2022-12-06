# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input('Введите число N: '))
myList = [n]
for i in range(n):
    myList.append(random.randrange(-n, n))
print(myList)

with open('file.txt') as file:
    for item in file:
        if int(item) < len(myList):
            print(f'Элемент с позицией {int(item)}: {myList[int(item)]}')
        else:
            print(f'В списке не существует элемента с позицией {int(item)}')