# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random


list = []
for i in range(44):
    list.append(random.randint(-100, 100))
print(list)


def buble(list):
    n = 1
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        n += 1


buble(list)
print(list)
