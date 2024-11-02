# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

import random

N = int(input())
a = []
Fin = []
s = 0
for i in range (N):
    b = random.randint(10, 100)
    a.append(b)
a.append(777)
print(a)

for i in range (len(a)):
    k = len(str(a[i]))
    Tr = 0
    c = []
    for j in range(k):
        c.append(a[i]%10)
        a[i] -= (a[i]%10)
        a[i] //= 10
    for h in range(len(c)-1):
        if c[h] != c[h+1]:
            Tr += 1
    if Tr == 0:
        Fin.append((str(c)[1:-1]).replace(', ', ''))

print(Fin)