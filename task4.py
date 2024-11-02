# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка

import random

N = int(input())
k = []
a = []
s = 0
for i in range (N):
    b = random.randint(0, 1000)
    a.append(b)
print(a)

for i in range (len(a)):
    s += a[i]

sred = s / N
print(sred)

m = sred / 100 * 30
print(m)
for i in range (len(a)):
    if abs(sred - a[i]) > m:
        k.append(a[i])

b = [a for a in a if a not in k]
print(b)