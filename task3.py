# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3

import random

a = []
N = int(input())
for i in range(N):
    b = random.randint(0, 100)
    a.append(b)
print(a)

g1 = []
g2 = []

fr = False

for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            if i not in g1 and j not in g2:
                print(f'значение: {a[i]} индексы {i} и {j}')
                g1.append(j)
                g2.append(i)
                fr = True

if fr == False:
    print('Нет')
