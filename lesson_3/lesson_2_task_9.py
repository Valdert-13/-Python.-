# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
M = 10
N = 5
L = 99 # Верхняя граница максимального числа в матрице
a = []
c = []
for i in range(N):    # заполняем матрицу
    b = []
    for j in range(M):
        n = int(random()*L)
        b.append(n)
    a.append(b)

for row in a:
    print(' '.join([str(elem) for elem in row]))

print
mx = -1
for j in range(M):  # ищем минимальное значение в каждом сталбце
    mn = L
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    c.append(mn)   #массив в принцепе не нужен просто чтобы было нагляднее
    if mn > mx:  # Ищем максимальное число из минимальных значений
        mx = mn
print ()
print (c)
print ()
print("Максимальный среди минимальных: ", mx)