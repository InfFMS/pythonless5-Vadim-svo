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

N = int(input())
a = []
c = 0
g2 = 1001
for i in range (N):
    b = random.randint(0, 100)
    a.append(b)
print(a)

for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j] and j != g2:
            print(f'значение:{a[i]} индексы {i} и {j}')
            g2 = i
            c+=1
if c ==0:
    print('нет')