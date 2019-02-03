#Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random
import statistics

list = []

for i in range(44):
    list.append(random.randint(0, 50) * 2 + 1)
print(list)
static = statistics.median(list)
listmin = []
listmax = []

for i in list:
    if i < static:
        listmin.append(i)
    else:
        listmax.append(i)

print(listmin)
print(listmax)