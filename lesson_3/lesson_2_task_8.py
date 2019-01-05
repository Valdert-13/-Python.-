# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.


import random


matrix = [[] for _ in range(4)]

for line in matrix:
    line_sum = 0
    for i in range(4):
        # num = int(input('Введите значение: '))  # для работы руками
        num = random.randint(9, 99) # Нужно для теста что все работает
        print (f'Вы велли число: { num }')
        line.append(num)
        line_sum += num
    line.append(line_sum)

print ()

for row in matrix:
    print(' '.join([str(elem) for elem in row]))