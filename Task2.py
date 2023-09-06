# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)

from random import randint


def index_elements(list_1, minn, maxx):
    list_2 = []
    for i in range(len(list_1)):
        if minn <= list_1[i] <= maxx:
            list_2.append(i)
    return list_2


list_1 = [randint(-10, 10) for i in range(int(input('Введите кол-во эл-тов: ')))]
print(list_1)
minn = int(input('Введите минимальную границу диапазона: '))
maxx = int(input('Введите максимальную границу диапазона: '))
print(index_elements(list_1, minn,maxx))

