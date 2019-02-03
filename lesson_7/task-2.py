# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


list = []

for i in range(44):
    list.append(random.randint(0, 50))
print(list)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

mergeSort(list)
print(list)