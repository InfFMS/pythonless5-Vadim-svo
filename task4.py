# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
import random

N = int(input())
a = []
m = []
for i in range (N):
    b = random.randint(0, 1000)
    a.append(b)

s = 0
for i in range(len(a)):
    s += a[i]

sred = s // len(a)

for i in range(len(a)-1):
    if a[i] < sred+sred//3 and a[i]> sred-sred // 3:
        m.append(a[i])
print(a)
print(sred)
print(m)