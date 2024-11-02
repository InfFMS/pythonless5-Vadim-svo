# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]

import random

N = int(input())
a = []
for i in range (N):
    b = random.randint(10, 100)
    a.append(b)
a.append(10)
a.append(10)
print(a)

c = a

for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            c.remove(a[i])

print(c)