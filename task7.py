# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]

import random

N = int(input())
a = []
k = []
for i in range (N):
    b = random.randint(-100, 100)
    a.append(b)

a.append(0)
print(a)

for i in range(len(a)):
    if a[i] > 0:
        k.insert(0, a[i])
    elif a[i] < 0:
        k.insert(-1, a[i])

for i in range(len(a)):
    if a[i] == 0:
        k.insert(-1, 0)

if k[-1] > 0:
    c = k.pop(-1)
    k.insert(0, c)
elif k[-1] < 0:
    c = k.pop(-1)
    for i in range(len(k)):
        if k[i] < 0:
            k.insert(i, c)
            break


print(k)